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
        contraseña: inputContraseña.value
    };

    fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(datosLogin)
    })
    .then(response => {

        if (!response.ok) {
            throw new Error("Credenciales incorrectas");
        }

        return response.json();

    })
    .then(data => {

        console.log(data);

        if (data.rol === "administrador") {
            window.location.href = "index.html";
        }

        else if (data.rol === "recepcionista") {
            window.location.href = "registro_paciente.html";
        }

        else if (data.rol === "medico") {
            window.location.href = "Medico.html";
        }

        else if (data.rol === "laboratorio") {
            window.location.href = "laboratorio.html";
        }

        else if (data.rol === "paciente") {
            window.location.href = "confirmacionDeCitas.html";
        }
    

    })
    .catch(error => {

        alert(error.message);

    });
});

