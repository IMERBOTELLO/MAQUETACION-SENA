document.getElementById("guardarBtn").addEventListener("click", function() {
    let diagnostico = document.querySelector("textarea").value;

    if (diagnostico.trim() === "") {
        alert("Debes ingresar un diagnóstico");
    } else {
        document.getElementById("resultadoMedico").innerHTML = `
            <div class="alert alert-success">
                <strong>Diagnóstico guardado:</strong> ${diagnostico}
            </div>
        `;
    }
});

document.getElementById("ordenBtn").addEventListener("click", function() {
    let examenes = document.querySelector("select").selectedOptions;

    if (examenes.length === 0) {
        alert("Debes seleccionar al menos un examen");
    } else {
        let lista = [];
        for (let i = 0; i < examenes.length; i++) {
            lista.push(examenes[i].text);
        }

        document.getElementById("resultadoMedico").innerHTML += `
            <div class="alert alert-warning">
                <strong>Orden generada:</strong> ${lista.join(", ")}
            </div>
        `;
    }
});