document.addEventListener('DOMContentLoaded', function() {

    const selectPais = document.getElementById('pais');
    selectPais.innerHTML = '<option value="">Seleccione un país</option>';
    fetch('pais/')
    .then(response => response.json())
    .then(data => {
        data.forEach(pais => {
            const option = document.createElement('option');
            option.value = pais.id_pais;
            option.textContent = pais.nombre_pais;
            selectPais.appendChild(option);
        });
    });
   
    const selectRegion = document.getElementById('region');
    selectRegion.innerHTML = '<option value="">Seleccione una región</option>';
    const selectComuna = document.getElementById('comuna');
    selectComuna.innerHTML = '<option value="">Seleccione una comuna</option>';

    var registroExitoso = document.getElementById('registro-exitoso-indicador');
if (registroExitoso && registroExitoso.value === 'true') {
    var successModal = new bootstrap.Modal(document.getElementById('successModal'), {
        keyboard: false // Permite cerrar el modal con la tecla Escape
    });
    successModal.show();

    document.getElementById('successModal').addEventListener('hidden.bs.modal', function () {
        window.location.href = '/login';
    });
};

});

document.getElementById('pais').addEventListener('change', function() {

    const paisId = this.value;
    const selectRegion = document.getElementById('region');
    selectRegion.removeAttribute('disabled');
    selectRegion.innerHTML = '<option value="">Seleccione una región</option>'; // Limpiar regiones
    if (paisId) {
        fetch(`region/${paisId}/`)
        .then(response => response.json())
        .then(data => {
            data.forEach(region => {
                const option = document.createElement('option');
                option.value = region.id_region;
                option.textContent = region.nombre_region;
                selectRegion.appendChild(option);
            });
        });
    }
});

document.getElementById('region').addEventListener('change', function() {
    
        const regionId = this.value;
        const selectComuna = document.getElementById('comuna');
        selectComuna.removeAttribute('disabled');
        selectComuna.innerHTML = '<option value="">Seleccione una comuna</option>'; // Limpiar comunas
        if (regionId && regionId !== 'undefined') { // Asegurarse de que regionId tenga un valor válido
            fetch(`comuna/${regionId}/`) // Ajustar la URL correctamente
            .then(response => response.json())
            .then(data => {
                data.forEach(comuna => {
                    const option = document.createElement('option');
                    option.value = comuna.id_comuna;
                    option.textContent = comuna.nombre_comuna;
                    selectComuna.appendChild(option);
                });
            })
            .catch(error => console.error('Error:', error));
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


$(document).ready(function() {
    $('#successModal').modal('show');
    $('#successModal').on('hidden.bs.modal', function (e) {
        window.location.href = "{% url 'login' %}";
    })
});

