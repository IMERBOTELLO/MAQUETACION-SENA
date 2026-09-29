const tabla = document.getElementById("tablapacientes");
const buscador = document.getElementById("buscador");

buscador.addEventListener("input", () => {
    const filtro = buscador.value.toLowerCase();
    const filas = tabla.querySelectorAll("tr");

    filas.forEach(fila => {
        const celdas = fila.querySelectorAll("td");
        let coincidencia = false;

        celdas.forEach(celda => {
            if (celda.textContent.toLowerCase().includes(filtro)) {
                coincidencia = true;
            }
        });

        fila.style.display = coincidencia ? "" : "none";
    });
});

fetch("/pacientes/")
.then(async response => {

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.detail);
    }

    return data;

})
.then(pacientes => {
    tabla.innerHTML = "";

    pacientes.forEach(paciente => {

        tabla.innerHTML += `
            <tr>

                <td>${paciente.nombres_paciente}</td>
                <td>${paciente.apellidos_pacientes}</td>
                <td>${paciente.numero_documento}</td>
                <td>${paciente.correo}</td>
                <td>${paciente.telefono}</td>
                <td>${paciente.fecha_registro}</td>
                <td>${paciente.fecha_nacimiento}</td>
                

                <td class="text-center">

                    <button 
                        class="btn btn-warning btn-sm me-1 editar"
                        data-id="${paciente.id_paciente}">
                        <i class="bi bi-pencil"></i>
                    </button>

                    <button 
                        class="btn btn-danger btn-sm eliminar"
                        data-id="${paciente.id_paciente}">
                        <i class="bi bi-trash"></i>
                    </button>

                </td>

            </tr>
        `;
    });
})

.catch(error => {
    alert(error.message);
});

document.addEventListener("click", function(event) {

    if (event.target.closest(".eliminar")) {

        const dataId = event.target.closest(".eliminar").dataset.id;

        if (confirm("¿Está seguro de que desea eliminar este paciente?")) {
            
            fetch("/paciente/" + dataId, {

                method: "DELETE",

             })

            .then(response => response.json())

            .then(data => {
                alert("paciente eliminado");

                location.reload();
            })
            
            .catch(error => {
                console.log(error);
            });
        }
    }

});

document.addEventListener("click", function(event) {

    const botonEditar = event.target.closest(".editar");

    if (!botonEditar) {
        return;
    }

    const idPaciente = botonEditar.dataset.id;

    window.location.href = `/registro_paciente?id=${idPaciente}`;
});