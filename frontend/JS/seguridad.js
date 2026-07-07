const rol = localStorage.getItem("rol");
const pagina = window.location.pathname;



const permisos = {
    
    ADMINISTRADOR: {
        "/index": true,
        "/registro_paciente": true,
        "/agendamientoDeCitas": true,
        "/confirmacionDeCitas": true,
        "/Medico": true,
        "/laboratorio": true,
        "/resultados": true,
        "/consulta_pacientes": true
    },

    RECEPCIONISTA: {
        "/index": true,
        "/registro_paciente": true,
        "/agendamientoDeCitas": true,
        "/confirmacionDeCitas": true,
        "/consulta_pacientes": true
    },

    MEDICO: {
        "/index": true,
        "/Medico": true,
        "/resultados": true
    },

    LABORATORIO: {
        "/index": true,
        "/laboratorio": true,
        "/resultados": true
    },

    PACIENTE: {
        "/index": true,
        "/confirmacionDeCitas": true
    }
};

const paginaInicio = {
    ADMINISTRADOR: "/index",
    RECEPCIONISTA: "/registro_paciente",
    MEDICO: "/Medico",
    LABORATORIO: "/laboratorio",
    PACIENTE: "/confirmacionDeCitas"
};

if (!rol) {
    alert("Debe iniciar sesión.")
    window.location.href = "/";
}

else if (!permisos[rol] || !permisos[rol][pagina]) {
    alert("No tiene permiso para acceder a esta página.")
    
    
    if (document.referrer) {
        window.history.back();
    }
    else {
        window.location.href = paginaInicio[rol];
    }

        
}

