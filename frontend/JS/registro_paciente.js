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

const formulario = document.getElementById("formpaciente");

formulario.addEventListener("submit", function (event) {

    event.preventDefault();

    const paciente = {

        nombres_paciente: document.getElementById("nombres").value,
        apellidos_pacientes: document.getElementById("apellidos").value,
        numero_documento: document.getElementById("numero_documento").value,
        correo: document.getElementById("correo").value,
        fecha_registro: document.getElementById("fecha_registro").value,
        fecha_nacimiento: document.getElementById("fecha_nacimiento").value,
        telefono: document.getElementById("telefono").value

    };

    fetch("http://127.0.0.1:8000/pacientes/", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(paciente)

    })

    .then(async response => {

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail);
        }

        return data;

    })

    .then(data => {

        alert("Paciente registrado correctamente.");
        formulario.reset();

    })

    .catch(error => {

        alert(error.message);

    });

});