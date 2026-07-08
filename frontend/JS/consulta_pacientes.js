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

fetch("http://127.0.0.1:8000/pacientes/")
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

                    <button class="btn btn-warning btn-sm me-1">
                        <i class="bi bi-pencil"></i>
                    </button>

                    <button class="btn btn-danger btn-sm">
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