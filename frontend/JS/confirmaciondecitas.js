console.log("confirmaciondecitas.js cargado correctamente");

document.addEventListener("DOMContentLoaded", () => {

    const cedula = document.getElementById("cedula");
    const nombre = document.getElementById("nombre");
    const profesional = document.getElementById("profesional");
    const fecha = document.getElementById("fecha");
    const hora = document.getElementById("hora");
    const servicio = document.getElementById("servicio");

    // Cuando el usuario salga del campo de cédula
    cedula.addEventListener("blur", buscarCita);


    async function buscarCita() {

        const documento = cedula.value.trim();

        // Si no escribió documento, no hacemos nada
        if (documento === "") {
            return;
        }

        try {

            // ==========================================
            // 1. BUSCAR LA CITA POR DOCUMENTO
            // ==========================================

            const respuesta = await fetch(
                `http://127.0.0.1:8000/citas/${documento}/documento`
            );

            if (!respuesta.ok) {
                throw new Error("No se encontró una cita para este documento");
            }

            const cita = await respuesta.json();

            console.log("Cita encontrada:", cita);


            // ==========================================
            // 2. LLENAR LOS DATOS DE LA CITA
            // ==========================================

            nombre.value = cita.nombre_paciente;

            fecha.value = cita.fecha;

            hora.innerHTML = `
                <option value="${cita.hora}" selected>
                    ${cita.hora}
                </option>
            `;

            servicio.innerHTML = `
                <option value="${cita.servicio}" selected>
                    ${cita.servicio}
                </option>
            `;


            // ==========================================
            // 3. BUSCAR LOS MÉDICOS
            // ==========================================

            const respuestaMedico = await fetch(
                "http://127.0.0.1:8000/medicos/"
            );

            if (!respuestaMedico.ok) {
                throw new Error("No se pudieron cargar los médicos");
            }

            const medicos = await respuestaMedico.json();

            console.log("Médicos encontrados:", medicos);


            // ==========================================
            // 4. BUSCAR EL MÉDICO DE ESTA CITA
            // ==========================================

            // IMPORTANTE:
            // El JSON de la cita tiene "id_medico"
            // NO tiene "medico"

            const medico = medicos.find(
                medico => medico.id_medico === cita.id_medico
            );


            if (!medico) {
                throw new Error(
                    "No se encontró el médico asociado a esta cita"
                );
            }

            console.log("Médico encontrado:", medico);


            // ==========================================
            // 5. MOSTRAR EL ESPECIALISTA
            // ==========================================

            profesional.innerHTML = `
                <option value="${medico.id_medico}" selected>
                    Dr. ${medico.nombre_medico} - ${medico.especialidad}
                </option>
            `;


            // ==========================================
            // 6. BLOQUEAR LOS CAMPOS
            // ==========================================

            nombre.disabled = true;
            fecha.disabled = true;

            profesional.disabled = true;
            hora.disabled = true;
            servicio.disabled = true;


            console.log("Todos los datos de la cita fueron cargados correctamente");


        } catch (error) {

            console.error("Error:", error);


            // ==========================================
            // LIMPIAR LOS CAMPOS
            // ==========================================

            nombre.value = "";
            fecha.value = "";

            profesional.innerHTML = `
                <option value="">
                    Seleccione un médico
                </option>
            `;

            hora.innerHTML = `
                <option value="">
                    Seleccione hora
                </option>
            `;

            servicio.innerHTML = `
                <option value="">
                    Seleccione un servicio
                </option>
            `;


            // ==========================================
            // VOLVER A HABILITAR LOS CAMPOS
            // ==========================================

            nombre.disabled = false;
            fecha.disabled = false;

            profesional.disabled = false;
            hora.disabled = false;
            servicio.disabled = false;


            alert(error.message);
        }
    }

});

document.getElementById("formCita").addEventListener("submit", async (e) => {

    e.preventDefault();

    document.getElementById("res-nombre").textContent =
        document.getElementById("nombre").value;

    document.getElementById("res-cedula").textContent =
        document.getElementById("cedula").value;

    document.getElementById("res-medico").textContent =
        document.getElementById("profesional").options[
            document.getElementById("profesional").selectedIndex
        ].text;

    document.getElementById("res-servicio").textContent =
        document.getElementById("servicio").value;
    
    document.getElementById("res-fecha").textContent =
        document.getElementById("fecha").value;
    
    document.getElementById("res-hora").textContent =
        document.getElementById("hora").value;

    // ocultar formulario

    document.getElementById("contenedorFormulario")
        .classList.add("d-none");

    // mostrar confirmacion

    document.getElementById("seccionConfirmacion")
        .classList.remove("d-none");
});

// ==========================================
// CONFIRMAR / CANCELAR CITA
// ==========================================

async function finalizarProceso(accion) {

    if (accion === "Cancelar") {
        alert("Cita cancelada");
        location.reload();
        return;
    }

    const datos = {
        documento: document.getElementById("cedula").value,
        nombre_paciente: document.getElementById("nombre").value,
        especialista: document.getElementById("profesional").options[
            document.getElementById("profesional").selectedIndex
        ].text,
        
        fecha: document.getElementById("fecha").value,
        hora: document.getElementById("hora").value,
        servicio: document.getElementById("servicio").value,
    };

    try {
        const respuesta = await fetch(
            "http://127.0.0.1:8000/citas_programadas/",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(datos),
            }
        );
        
        if (!respuesta.ok) {
            throw new Error("No se pudo confirmar la cita");
        }

        const resultado = await respuesta.json();

        console.log(resultado);

        alert("Cita confirmada");

        location.reload();

    } catch (error) {
        console.error(error);
        alert(error.message);
    }
}