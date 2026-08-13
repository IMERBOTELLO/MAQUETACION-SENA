// Estructura de datos - SIN DATOS PREDETERMINADOS
let resultadosPendientes = [];
let resultadosValidados = [];
let resultadosRechazados = [];
let entregasRealizadas = [];
let nextId = 1;

// Función para registrar resultado (RF06)
async function registrarResultado() {

    const documento = document.getElementById("docPaciente").value;
    const nombre = document.getElementById("nombrePaciente").value;
    const examen = document.getElementById("tipoExamen").value;
    const fecha = document.getElementById("fechaResultado").value;
    const valores = document.getElementById("valoresExamen").value;
    const archivo = document.getElementById("archivoPDF").files[0];

    if(!archivo) {
        alert('❌ Error: Debe seleccionar un archivo para subir');
        return;
    }

    const pdfBase64 = await convertFileToBase64(archivo);

    const respuestaLaboratorio = await fetch(
        `http://127.0.0.1:8000/laboratorios/documento/${documento}`
    );

    if (!respuestaLaboratorio.ok) {
        alert('❌ Error: No se pudo obtener el laboratorio para este paciente');
        return;
    }

    const laboratorio = await respuestaLaboratorio.json();

    const respuestaAtencion = await fetch(
        `http://127.0.0.1:8000/atenciones_medicas/documento/${documento}`
    );

    if (!respuestaAtencion.ok) {
        alert('❌ Error: No se pudo obtener la atención para este paciente');
        return;
    }

    const atencion = await respuestaAtencion.json();

    const datos = {
        id_lab: laboratorio.id_lab,
        documento_paciente: documento,
        nombre_paciente: nombre,
        examen_medico: examen,
        fecha_resultado: fecha,
        info_examen: valores,
        pdf: pdfBase64,
        id_examen: atencion.id_atencion
    };

    const respuesta = await fetch(
        `http://127.0.0.1:8000/resultados/`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(datos)
        }
    );

    if (!respuesta.ok) {

        const error = await respuesta.json();
        alert(`❌ Error: ${error.detail}`);
        return;
    }

    alert('✅ Resultado registrado exitosamente');

    // Validación de campos obligatorios
    if(!documento || !nombre || !examen || !fecha) {
        alert('❌ Error: Debe completar todos los campos obligatorios (Documento, Nombre, Examen, Fecha)');
        return;
    }
    
    alert('✅ Resultado registrado exitosamente');
    
    limpiarFormularioResultado();

    await cargarResultadosDesdeBD();
}

// cargar datos del paciente

async function cargarDatosLaboratorio() {

    const documento = document.getElementById('docPaciente').value;

    if (!documento) {
        return;
    }

    try {

        const respuesta = await fetch(
            `http://127.0.0.1:8000/laboratorios/documento/${documento}`
        );

        if (!respuesta.ok) {
            alert('❌ Error: No se pudo obtener el laboratorio para este documento');

            document.getElementById('nombrePaciente').value = '';
            document.getElementById('tipoExamen').value = '';
            document.getElementById('fechaResultado').value = '';
            document.getElementById('valoresExamen').value = '';

            return;
        }

        const laboratorio = await respuesta.json();

        document.getElementById('nombrePaciente').value = laboratorio.nombre_paciente;
        document.getElementById('tipoExamen').value = laboratorio.tipo_examen;
        document.getElementById('fechaResultado').value = laboratorio.fecha;
        document.getElementById('valoresExamen').value = laboratorio.resultado;

    } catch (error) {

        console.error(error);
        alert("Error al consultar el laboratorio");
    }
}

// RF09: Generar entrega de resultados
function generarEntregaResultados() {
    const documento = document.getElementById('entregaDocumento').value;
    const formato = document.getElementById('formatoEntrega').value;
    const correo = document.getElementById('correoEntrega').value;
    const diagnostico = document.getElementById('diagnosticoFinal').value;
    const incluirResultados = document.getElementById('incluirResultados').checked;
    
    if(!documento) {
        alert('Por favor ingrese el documento del paciente');
        return;
    }
    
    if(formato === 'digital' && !correo) {
        alert('Para entrega en formato digital, debe proporcionar un correo electrónico');
        return;
    }
    
    // Buscar resultados del paciente
    const resultadosPaciente = [...resultadosValidados, ...resultadosPendientes].filter(r => r.documento === documento);
    const paciente = resultadosPaciente[0];
    
    if(!paciente && !document.getElementById('entregaNombre').value) {
        alert('No se encontraron resultados para este paciente. Primero registre los resultados.');
        return;
    }
    
    const nombrePaciente = document.getElementById('entregaNombre').value || paciente?.nombre || 'Paciente';
    
    // Crear registro de entrega
    const nuevaEntrega = {
        id: Date.now(),
        fecha: new Date().toISOString().split('T')[0],
        paciente: nombrePaciente,
        documento: documento,
        formato: formato === 'digital' ? 'Digital (PDF)' : formato === 'impreso' ? 'Impreso físico' : 'Ambos formatos',
        estado: 'Entregado',
        diagnostico: diagnostico || 'Sin diagnóstico registrado'
    };
    
    entregasRealizadas.unshift(nuevaEntrega);
    renderizarHistorialEntregas();
    
    // Mensaje de éxito
    let mensaje = `✅ ${formato === 'digital' ? 'RESUMEN DIGITAL GENERADO' : formato === 'impreso' ? 'RESUMEN IMPRESO' : 'AMBOS FORMATOS GENERADOS'}\n\n`;
    mensaje += `Paciente: ${nombrePaciente}\n`;
    mensaje += `Documento: ${documento}\n`;
    if(formato === 'digital' || formato === 'ambos') mensaje += `Enviado a: ${correo}\n`;
    mensaje += `Diagnóstico: ${diagnostico || 'No especificado'}\n`;
    if(incluirResultados && resultadosPaciente.length > 0) {
        mensaje += `\nResultados incluidos:\n`;
        resultadosPaciente.forEach(r => {
            mensaje += `- ${r.examen}: ${r.valores || 'Valores disponibles en el PDF'}\n`;
        });
    }
    mensaje += `\n📄 Documento PDF generado exitosamente.`;
    
    const alertDiv = document.getElementById('mensajeEntrega');
    alertDiv.className = 'alert alert-success mt-3';
    alertDiv.innerHTML = `<i class="bi bi-check-circle-fill me-2"></i>${mensaje.replace(/\n/g, '<br>')}`;
    alertDiv.classList.remove('d-none');
    
    setTimeout(() => {
        alertDiv.classList.add('d-none');
    }, 8000);
    
    // Limpiar campos
    document.getElementById('entregaDocumento').value = '';
    document.getElementById('entregaNombre').value = '';
    document.getElementById('correoEntrega').value = '';
    document.getElementById('diagnosticoFinal').value = '';
    document.getElementById('incluirResultados').checked = false;
}

function cargarDatosPaciente() {
    const documento = document.getElementById('entregaDocumento').value;
    const todosResultados = [...resultadosValidados, ...resultadosPendientes];
    const paciente = todosResultados.find(r => r.documento === documento);
    
    if(paciente) {
        document.getElementById('entregaNombre').value = paciente.nombre;
        if(!document.getElementById('diagnosticoFinal').value) {
            document.getElementById('diagnosticoFinal').placeholder = `Ej: Resultados de ${paciente.examen} - Pendiente de interpretación médica`;
        }
    } else {
        alert('No se encontraron resultados para este documento. Registre primero los resultados.');
    }
}

function previsualizarResumen() {
    const documento = document.getElementById('entregaDocumento').value;
    const nombre = document.getElementById('entregaNombre').value;
    const diagnostico = document.getElementById('diagnosticoFinal').value;
    const incluirResultados = document.getElementById('incluirResultados').checked;
    
    if(!documento) {
        alert('Ingrese documento del paciente primero');
        return;
    }
    
    const resultadosPaciente = [...resultadosValidados, ...resultadosPendientes].filter(r => r.documento === documento);
    
    let contenido = `<h6>Paciente: ${nombre || 'No especificado'}</h6>`;
    contenido += `<p><strong>Documento:</strong> ${documento}</p>`;
    contenido += `<p><strong>Diagnóstico Final:</strong> ${diagnostico || 'Pendiente de actualización'}</p>`;
    
    if(incluirResultados && resultadosPaciente.length > 0) {
        contenido += `<hr><h6>Resultados de Laboratorio:</h6>`;
        resultadosPaciente.forEach(r => {
            contenido += `<div class="mb-2"><strong>${r.examen} (${r.fecha}):</strong><br>${r.valores || 'Resultados disponibles en PDF adjunto'}</div>`;
        });
    } else if(incluirResultados && resultadosPaciente.length === 0) {
        contenido += `<p class="text-warning">No hay resultados registrados para este paciente.</p>`;
    }
    
    contenido += `<hr><small class="text-muted">Documento generado por HOSPISOFT - Sistema de Gestión Hospitalaria</small>`;
    
    document.getElementById('vistaPreviaContenido').innerHTML = contenido;
    document.getElementById('vistaPrevia').classList.remove('d-none');
    
    setTimeout(() => {
        document.getElementById('vistaPrevia').scrollIntoView({ behavior: 'smooth' });
    }, 100);
}

function cerrarPrevisualizacion() {
    document.getElementById('vistaPrevia').classList.add('d-none');
    document.getElementById('vistaPreviaContenido').innerHTML = '';
}

function renderizarTodo() {
    renderizarPendientes();
    renderizarValidados();
}

async function cargarResultadosDesdeBD() {

    try {
        // Obtener resultados pendientes

        const respuestaPendientes = await fetch(
            `http://127.0.0.1:8000/laboratorios/pendiente-resultados`
        );

        if (!respuestaPendientes.ok) {
            throw new Error('Error al obtener resultados pendientes');
        }

        const pendientes = await respuestaPendientes.json();

        // Obtener resultados validados

        const respuestaValidados = await fetch(
            `http://127.0.0.1:8000/resultados/registrados`
        );

        if (!respuestaValidados.ok) {
            throw new Error('Error al obtener resultados validados');
        }

        const validados = await respuestaValidados.json();

        // guardar los datos

        resultadosPendientes = pendientes.map(laboratorio => ({
            id: laboratorio.id_lab,
            documento: laboratorio.numero_documento,
            nombre: laboratorio.nombre_paciente,
            examen: laboratorio.tipo_examen,
            fecha: laboratorio.fecha,
            valores: laboratorio.resultado
        }));

        resultadosValidados = validados.map(resultado => ({
            id: resultado.id_resultado,
            documento: resultado.documento_paciente,
            nombre: resultado.nombre_paciente,
            examen: resultado.examen_medico,
            fecha: resultado.fecha_resultado,
            valores: resultado.info_examen
        }));

    

    // mostrar en la interfaz

    renderizarPendientes();
    renderizarValidados();

    } catch (error) {

        console.error('Error cargando resultados:', error);
    }
}

function renderizarPendientes() {

    const tbody = document.getElementById('pendientesBody');

    if(resultadosPendientes.length === 0) {

        tbody.innerHTML = `
            <tr>
                <td colspan="6" class="text-center text-muted">
                    No hay resultados pendientes
                </td>
            </tr>
        `;

        return;
    }

    tbody.innerHTML = '';

    resultadosPendientes.forEach(r => {

        tbody.innerHTML += `
            <tr>
                <td>
                    <i class="bi bi-person-circle me-2 text-primary"></i>
                    ${r.nombre}
                </td>

                <td>${r.documento}</td>

                <td>${r.examen}</td>

                <td>${r.fecha}</td>

                <td>
                    <span class="badge bg-warning text-dark">
                        Pendiente
                    </span>
                </td>

                <td>
                    <span class="text-muted">
                        Pendiente de registrar resultado
                    </span>
                </td>
            </tr>
        `;

    });
}

function renderizarValidados() {

    const tbody = document.getElementById('validadosBody');

    if(resultadosValidados.length === 0) {

        tbody.innerHTML = `
            <tr>
                <td colspan="4" class="text-center text-muted">
                    No hay resultados validados
                </td>
            </tr>
        `;

        return;
    }

    tbody.innerHTML = '';

    resultadosValidados.forEach(r => {

        tbody.innerHTML += `
            <tr>
                <td>
                    ${r.nombre}
                </td>

                <td>
                    ${r.examen}
                </td>

                <td>
                    Registro de resultado
                </td>

                <td>
                    <span class="badge bg-success">
                        Validado
                    </span>
                </td>

                </tr>
        `;

    });
}

function renderizarHistorialEntregas() {
    const tbody = document.getElementById('historialEntregas');
    if(entregasRealizadas.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" class="text-center text-muted">No hay entregas registradas</td></tr>';
        return;
    }
    tbody.innerHTML = '';
    entregasRealizadas.forEach(e => {
        tbody.innerHTML += `
            <tr>
                <td>${e.fecha}</td>
                <td>${e.paciente}</td>
                <td>${e.documento}</td>
                <td>${e.formato}</td>
                <td><span class="badge bg-success">${e.estado}</span></td>
                <td><button class="btn btn-sm btn-info rounded-pill" onclick="imprimirYEliminar(${e.id}, '${e.paciente}', '${e.documento}')"><i class="bi bi-printer"></i> Imprimir</button></td>
            </tr>
        `;
    });
}

function imprimirYEliminar(id, paciente, documento) {
    alert(`🖨️ IMPRIMIENDO RESULTADOS\n\nPaciente: ${paciente}\nDocumento: ${documento}\n\nSe está generando el documento para impresión...`);
    
    entregasRealizadas = entregasRealizadas.filter(e => e.id !== id);
    renderizarHistorialEntregas();
    alert('✅ Registro eliminado del historial después de imprimir.');
}

function reintentarRegistro(id) {
    const resultado = resultadosRechazados.find(r => r.id === id);
    if(resultado) {
        document.getElementById('docPaciente').value = resultado.documento;
        document.getElementById('nombrePaciente').value = resultado.nombre;
        document.getElementById('tipoExamen').value = resultado.examen;
        
        resultadosRechazados = resultadosRechazados.filter(r => r.id !== id);
        renderizarTodo();
        
        document.getElementById('formRegistroResultado').scrollIntoView({ behavior: 'smooth' });
        alert(`Complete los valores del examen para ${resultado.nombre} y vuelva a registrar el resultado.`);
    }
}

function limpiarFormularioResultado() {
    document.getElementById('docPaciente').value = '';
    document.getElementById('nombrePaciente').value = '';
    document.getElementById('tipoExamen').value = '';
    document.getElementById('fechaResultado').value = '';
    document.getElementById('valoresExamen').value = '';
    document.getElementById('archivoPDF').value = '';
}

function buscarPaciente() {
    const termino = document.getElementById('searchGlobal').value.toLowerCase();
    if(!termino) {
        renderizarTodo();
        return;
    }
    
    const pendientesFiltrados = resultadosPendientes.filter(r => r.documento.includes(termino) || r.nombre.toLowerCase().includes(termino));
    const validadosFiltrados = resultadosValidados.filter(r => r.documento.includes(termino) || r.nombre.toLowerCase().includes(termino));
    
    const pendientesBody = document.getElementById('pendientesBody');
    if(pendientesFiltrados.length === 0 && validadosFiltrados.length === 0) {
        pendientesBody.innerHTML = '<tr><td colspan="6" class="text-center text-muted">No se encontraron resultados</td>;</tr>';
    } else {
        pendientesBody.innerHTML = '';
        pendientesFiltrados.forEach(r => {
            pendientesBody.innerHTML += `
                <tr>
                    <td><i class="bi bi-person-circle me-2 text-primary"></i>${r.nombre}</td>
                    <td>${r.documento}</td>
                    <td>${r.examen}</td>
                    <td>${r.fecha}</td>
                    <td><span class="badge-status badge-pendiente">Pendiente</span></td>
                    <td><button class="btn btn-sm btn-primary rounded-pill" onclick="completarValidacion(${r.id})"><i class="bi bi-pencil-square"></i> Completar valores</button></td>
                </tr>
            `;
        });
    }
}

function mostrarModal(titulo, mensaje) {
    document.getElementById('modalMensaje').innerHTML = `<strong>${titulo}</strong><br><br>${mensaje}`;
    const modal = new bootstrap.Modal(document.getElementById('confirmacionModal'));
    modal.show();
}


function convertFileToBase64(archivo) {
    return new Promise((resolve, reject) => {
        const lector = new FileReader();

        lector.onload = () => {

            const base64 = lector.result.split(",")[1];
            resolve(base64);
        };

        lector.onerror = error => reject(error);

        lector.readAsDataURL(archivo);
    });

}

document.addEventListener('DOMContentLoaded', function() {

    cargarResultadosDesdeBD();

});
