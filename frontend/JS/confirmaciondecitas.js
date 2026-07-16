// Variables de estado
let pagoRealizado = false;
let datosCita = {};

// Inicializar Calendario
flatpickr("#fecha", {
    minDate: "today",
    dateFormat: "Y-m-d",
    onChange: function(selectedDates, dateStr) {
        cargarHorarios();
    }
});

function cargarHorarios() {
    const horas = ["08:00", "09:30", "11:00", "14:00", "15:30"];
    const select = document.getElementById("hora");
    select.innerHTML = '<option value="">Selecciona hora</option>';
    horas.forEach(h => {
        let opt = document.createElement("option");
        opt.value = h;
        opt.textContent = h;
        select.appendChild(opt);
    });
}

function simularPago() {
    pagoRealizado = true;
    document.getElementById("estadoPago").classList.remove("d-none");
}

// Manejo del Formulario
document.getElementById("formCita").addEventListener("submit", function(e) {
    e.preventDefault();

    if (!pagoRealizado) {
        alert("Por favor, valide el pago antes de continuar.");
        return;
    }

    // Capturar datos
    datosCita = {
        nombre: document.getElementById("nombre").value,
        cedula: document.getElementById("cedula").value,
        medico: document.getElementById("profesional").value,
        servicio: document.getElementById("servicio").value,
        fecha: document.getElementById("fecha").value,
        hora: document.getElementById("hora").value
    };

    // Llenar vista de confirmación
    document.getElementById("res-nombre").textContent = datosCita.nombre;
    document.getElementById("res-cedula").textContent = datosCita.cedula;
    document.getElementById("res-medico").textContent = datosCita.medico;
    document.getElementById("res-servicio").textContent = datosCita.servicio;
    document.getElementById("res-fecha").textContent = datosCita.fecha;
    document.getElementById("res-hora").textContent = datosCita.hora;

    // Intercambiar vistas
    document.getElementById("contenedorFormulario").classList.add("d-none");
    document.getElementById("seccionConfirmacion").classList.remove("d-none");
});

function finalizarProceso(accion) {
    if (accion === 'Confirmar') {
        const msj = `CITA CONFIRMADA - HOSPISOFT\nPaciente: ${datosCita.nombre}\nMédico: ${datosCita.medico}\nFecha: ${datosCita.fecha} ${datosCita.hora}`;
        alert("Cita confirmada con éxito. Se enviará la notificación.");
        // Aquí podrías usar window.open(`https://wa.me/TUNUMERO?text=${encodeURIComponent(msj)}`);
        location.reload();
    } else {
        if(confirm("¿Seguro que desea cancelar? Se perderán los datos ingresados.")) {
            location.reload();
        }
    }
}