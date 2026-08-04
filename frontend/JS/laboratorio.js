const formulario = document.getElementById('formlaboratorio');
formulario.addEventListener('submit', guardarLaboratorio);

const documento = document.getElementById("documento");
documento.addEventListener("blur", buscarPaciente);

async function buscarPaciente() {
    const numero_documento = documento.value.trim();

    if (numero_documento === "") {
        return;
    }

    try {
        const respuesta = await fetch(
            `http://127.0.0.1:8000/atenciones_medicas/laboratorio/${numero_documento}`
        );

        if (!respuesta.ok) {
            throw new Error("No se encontro una atencion Medica para este documento");
        }

        const datos = await respuesta.json();

        console.log("datos recibidos", datos);

        // mostrar nombre

        document.getElementById("nombre").value = 
            datos.nombre_paciente;

        // bloquear el campo

        document.getElementById("nombre").disabled = true;

    } catch (error) {

        console.error(error);

        document.getElementById("nombre").value = "";
        document.getElementById("nombre").disabled = false;
    }
}


// guardar laboratorio

async function guardarLaboratorio(event) {
    event.preventDefault();
    const datos = {
        nombre_paciente: document.getElementById("nombre").value,
        numero_documento: document.getElementById("documento").value,
        tipo_examen: document.getElementById("tipoExamen").value,
        fecha: document.getElementById("fecha").value,
        resultado: document.getElementById("resultado").value
    };


    console.log(datos);


    const respuesta = await fetch(
        "http://127.0.0.1:8000/laboratorios/",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify(datos),
        }
    );


    if (respuesta.ok) {
        alert("Laboratorio registrado correctamente");

        formulario.reset();

    } else {

        const error = await respuesta.json();
        alert(error.detail);
    }

}


(() => {
'use strict'
const forms = document.querySelectorAll('.needs-validation')

forms.forEach(form => {
    form.addEventListener('submit', event => {
    if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
    }
    form.classList.add('was-validated')
    }, false)
})
})()