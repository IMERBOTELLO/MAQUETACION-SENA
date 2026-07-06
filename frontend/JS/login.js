const roles = document.querySelectorAll(".rol");
const roleText = document.getElementById("roleText");
const roleIcon = document.getElementById("roleIcon");
const loginButton = document.getElementById("loginButton");

const inputCorreo = document.getElementById("correo")
const inputContraseña = document.getElementById("contraseña")

let currentRole = "";

roles.forEach(role => {
    role.addEventListener("click", () => {
        const selectedRole = role.dataset.role;
        const selectedIcon = role.dataset.icon;
        currentRole = selectedRole;
        roleText.textContent = selectedRole;
        roleIcon.className = `bi ${selectedIcon}`;
    });
});

loginButton.addEventListener("click", () => {

    if (!currentRole) {
        alert("Por favor, selecciona un rol en el panel izquierdo antes de continuar.");
        return;
    }

    
    if (inputCorreo.value.trim() === "") {
        alert("El campo de correo es obligatorio.");
        inputCorreo.focus();
        return; 
    }

    
    if (inputContraseña.value.trim() === "") {
        alert("El campo de contraseña es obligatorio.");
        inputContraseña.focus();
        return; 
    }

    const datosLogin = {
        correo: inputCorreo.value,
        contraseña: inputContraseña.value,
        rol: currentRole.toUpperCase()
    };

    fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(datosLogin)
    })
    .then(async response => {

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail);
        }

        return data;

    })
    .then(data => {
        localStorage.setItem("rol", data.rol);

        if (data.rol === "ADMINISTRADOR") {
            window.location.href = "/index";
        }

        else if (data.rol === "RECEPCIONISTA") {
            window.location.href = "/registro_paciente";
        }

        else if (data.rol === "MEDICO") {
            window.location.href = "/Medico";
        }

        else if (data.rol === "LABORATORIO") {
            window.location.href = "/laboratorio";
        }

        else if (data.rol === "PACIENTE") {
            window.location.href = "/confirmacionDeCitas";
        }
    
    })
    .catch(error => {

        alert(error.message);

    });
});

