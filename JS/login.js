const roles = document.querySelectorAll(".rol");
const roleText = document.getElementById("roleText");
const roleIcon = document.getElementById("roleIcon");
const loginButton = document.getElementById("loginButton");
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
    else{
        alert("Selecciona un rol antes de ingresar");
    }
});