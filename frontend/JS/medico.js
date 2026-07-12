document.getElementById("guardarBtn").addEventListener("click", async function () {

    const numero_documento = document.getElementById("numero_documento").value;
    const diagnostico = document.getElementById("diagnostico").value;
    const observaciones = document.getElementById("observaciones").value;

    const examenesSeleccionados = document.getElementById("examenes").selectedOptions;
    let listaExamenes = [];

    for (let i = 0; i < examenesSeleccionados.length; i++) {
        listaExamenes.push(examenesSeleccionados[i].text);
    }

    if (
        numero_documento.trim() === "" ||
        diagnostico.trim() === "" ||
        observaciones.trim() === "" ||
        listaExamenes.length === 0
    ) {
        alert("Todos los campos son obligatorios.");
        return;
    }

    const datos = {
        numero_documento: numero_documento,
        diagnostico: diagnostico,
        observaciones: observaciones,
        fecha_atencion: new Date().toISOString().split("T")[0],
        examenes: listaExamenes.join(", ")
    };

    try {

        const respuesta = await fetch("http://127.0.0.1:8000/atenciones_medicas/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(datos)
        });

        if (!respuesta.ok) {
            throw new Error("No se pudo guardar la atención médica.");
        }

        const resultado = await respuesta.json();

        document.getElementById("resultadoMedico").innerHTML = `
            <div class="alert alert-success">
                Diagnóstico guardado correctamente. ID: ${resultado.id_atencion}
            </div>
        `;

    } catch (error) {
        alert(error.message);
    }

});


document.getElementById("ordenBtn").addEventListener("click", function () {

    const examenes = document.getElementById("examenes").selectedOptions;

    if (examenes.length === 0) {
        alert("Debes seleccionar al menos un examen");
        return;
    }

    let lista = [];

    for (let i = 0; i < examenes.length; i++) {
        lista.push(examenes[i].text);
    }

    document.getElementById("resultadoMedico").innerHTML += `
        <div class="alert alert-warning">
            <strong>Orden generada:</strong> ${lista.join(", ")}
        </div>
    `;
});