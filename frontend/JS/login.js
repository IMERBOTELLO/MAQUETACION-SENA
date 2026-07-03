const roles = document.querySelectorAll(".rol");
const roleText = document.getElementById("roleText");
const roleIcon = document.getElementById("roleIcon");
const loginButton = document.getElementById("loginButton");

const inputUsuario = document.getElementById("Usuario")
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

    
    if (inputUsuario.value.trim() === "") {
        alert("El campo de usuario es obligatorio.");
        inputUsuario.focus();
        return; 
    }

    
    if (inputContraseña.value.trim() === "") {
        alert("El campo de contraseña es obligatorio.");
        inputContraseña.focus();
        return; 
    }

    if(currentRole === "recepcionista"){
        window.location.href = "registro_paciente.html";
    }
    else if(currentRole === "medico"){
        window.location.href = "Medico.html";
    }
    else if(currentRole === "laboratorio"){
        window.location.href = "laboratorio.html";
    }
    else if(currentRole === "paciente"){
        window.location.href = "confirmacionDeCitas.html";
    }
    else if(currentRole === "administrador"){
        window.location.href = "index.html";
    }
});