const parametros = new URLSearchParams(window.location.search);
const idPaciente = parametros.get("id");

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

    let url = "http://127.0.0.1:8000/pacientes/";
    let metodo = "POST";

    // Si viene un id, significa que estamos editando
    if (idPaciente) {
        url = `http://127.0.0.1:8000/pacientes/${idPaciente}`;
        metodo = "PUT";
    }

    fetch(url, {

        method: metodo,

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

        if (idPaciente) {
            alert("Paciente actualizado correctamente.");
            window.location.href = "/consulta_pacientes";

        }
        else {
            alert("Paciente creado correctamente.");
            formulario.reset();
        }

        

    })

    .catch(error => {

        alert(error.message);

    });

});

const nombres = document.getElementById("nombres");
const apellidos = document.getElementById("apellidos");
const numero_documento = document.getElementById("numero_documento");
const correo = document.getElementById("correo");
const fecha_registro = document.getElementById("fecha_registro");
const fecha_nacimiento = document.getElementById("fecha_nacimiento");
const telefono = document.getElementById("telefono");

if (idPaciente) {

    fetch(`http://127.0.0.1:8000/pacientes/${idPaciente}`)

    .then(async response => {

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail);
        }

        return data;

    })

    .then(paciente => {

        nombres.value = paciente.nombres_paciente;
        apellidos.value = paciente.apellidos_pacientes;
        numero_documento.value = paciente.numero_documento;
        correo.value = paciente.correo;
        fecha_registro.value = paciente.fecha_registro;
        fecha_nacimiento.value = paciente.fecha_nacimiento;
        telefono.value = paciente.telefono;

    })

    .catch(error => {

        alert(error.message);

    });

}