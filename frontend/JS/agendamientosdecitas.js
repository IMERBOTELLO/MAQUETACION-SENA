window.addEventListener("DOMContentLoaded", cargarMedicos);

async function cargarMedicos() {

  try {

    const respuesta = await fetch("http://127.0.0.1:8000/medicos/");

    if (!respuesta.ok) {
      throw new Error("No se puediron cargar los medicos");
    }

    const medicos = await respuesta.json();

    const select = document.getElementById("profesional");
    
    medicos.forEach(medico => {
      const opcion = document.createElement("option");
      opcion.value = medico.id_medico;

      opcion.textContent =
        "Dr." + 
        medico.nombre_medico +
        " - " +
        medico.especialidad;
      
      select.appendChild(opcion);
    });
  
  } catch (error) {
    console.error(error);
  }

}


const inputDocumento = document.getElementById("NUMERO_CEDULA");
inputDocumento.addEventListener("blur", buscarPaciente);

async function buscarPaciente() {
  const documento = document.getElementById("NUMERO_CEDULA").value;

  if (documento.trim() === "") {
    return;
  }

  try {

    const respuesta = await fetch (
      `http://127.0.0.1:8000/pacientes/documento/${documento}`
    );

    if (!respuesta.ok) {
      throw new Error ("Paciente no encontrado");
    }

    const paciente = await respuesta.json();

    document.getElementById("nombre").value =
      paciente.nombres_paciente + " " + paciente.apellidos_pacientes;
  
  } catch (error) {

    document.getElementById("nombre").value = "";

    alert("Paciente no encontrado");

  }

}

document.getElementById("formCita").addEventListener("submit", async function(e) {

  e.preventDefault();
  
  const nombre = document.getElementById("nombre").value;
  const numero_documento = document.getElementById("NUMERO_CEDULA").value;
  const profesional = document.getElementById("profesional").value;
  const fecha = document.getElementById("fecha").value;
  const hora = document.getElementById("time").value;
  const servicio = document.getElementById("servicio").value;



  const datos = {

    nombre_paciente: nombre,
    numero_documento_paciente: numero_documento,
    id_medico: parseInt(profesional),
    fecha: fecha,
    hora: hora,
    servicio: servicio

  };

  try {
    const respuesta = await fetch(
      "http://127.0.0.1:8000/citas/",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(datos)
      }
    );

    if (!respuesta.ok) {
      throw new Error ("No se pudo crear la cita");
    }

    const cita = await respuesta.json();

    alert("Cita creada con éxito");

    location.reload();

  } catch (error) {

    alert(error.message);

  }

  

});
