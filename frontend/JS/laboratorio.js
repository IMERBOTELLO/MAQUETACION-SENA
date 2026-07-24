const formulario = document.getElementById('formlaboratorio');
formulario.addEventListener('submit', guardarLaboratorio);

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