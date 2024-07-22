function obtenerDatos() {

    let user = document.getElementById('user').value;
    let pass = document.getElementById('pass').value;

    if (user == '' || pass == '') {

        alert('Los campos Correo Electrónico y Contraseña no pueden estar vacíos.');

    } else {
        const usuario = {
            user: document.getElementById('user').value,
            pass: document.getElementById('pass').value
        }

        console.log(usuario)
        console.log(usuario.user);
        console.log(usuario.pass);

        alert(`¡Bienvenido ${usuario.user}!`)
    };
};


const validarCliente = (usuario) => {
    
};

window.addEventListener('scroll', function () {
    const supermanIcon = document.getElementById('scroll-top-icon');
    if (window.scrollY > 30) {
        supermanIcon.style.display = 'block';
    } else {
        supermanIcon.style.display = 'none';
    }
});