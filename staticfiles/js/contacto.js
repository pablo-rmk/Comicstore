let enviar = document.getElementById('enviar');
enviar.addEventListener('click', () => {

    let titulo = document.getElementById('tituloInput').value;
    let email = document.getElementById('emailInput').value;
    let texto = document.getElementById('textArea1').value;

    if (titulo == '' || email == '' || texto == '') {
        alert('Por favor complete todos los campos antes de enviar.')
    } else {
        
        var successModal = new bootstrap.Modal(document.getElementById('successModal'), {
            keyboard: false 
        });
        successModal.show();

    }
});

window.addEventListener('scroll', function () {
    const supermanIcon = document.getElementById('scroll-top-icon');
    if (window.scrollY > 30) {
        supermanIcon.style.display = 'block';
    } else {
        supermanIcon.style.display = 'none';
    }
});