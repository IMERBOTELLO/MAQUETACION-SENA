// Calendario
flatpickr("#fecha", {
  minDate: "today",
  dateFormat: "Y-m-d",
  onChange: function(selectedDates, dateStr) {
    cargarHorarios(dateStr);
  }
});

// Horarios simulados
function cargarHorarios(fecha) {
  const horas = ["09:00", "10:00", "11:00", "14:00", "15:00"];
  const select = document.getElementById("hora");
  select.innerHTML = '<option value="">Selecciona hora</option>';

  horas.forEach(h => {
    const option = document.createElement("option");
    option.value = h;
    option.textContent = h;
    select.appendChild(option);
  });
}

// Simulación de pago
let pagoRealizado = false;

function simularPago() {
  pagoRealizado = true;
  document.getElementById("estadoPago").classList.remove("d-none");
}

// Enviar a WhatsApp
document.getElementById("formCita").addEventListener("submit", function(e) {
  e.preventDefault();

  if (!pagoRealizado) {
    alert("Debes realizar el pago primero");
    return;
  }

  const nombre = document.getElementById("nombre").value;
  const telefono = document.getElementById("telefono").value;
  const profesional = document.getElementById("profesional").value;
  const fecha = document.getElementById("fecha").value;
  const hora = document.getElementById("hora").value;
  const servicio = document.getElementById("servicio").value;

  const mensaje = `Hola, quiero confirmar mi cita:
Nombre: ${nombre}
Profesional: ${profesional}
Fecha: ${fecha}
Hora: ${hora}
Servicio: ${servicio}`;

  const url = `https://wa.me/${telefono}?text=${encodeURIComponent(mensaje)}`;
  window.open(url, "_blank");
});