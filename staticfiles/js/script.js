/* Restar Producto */
document.getElementById("btnMenos").addEventListener("click", function() {
    let cantidadInput = document.getElementById("cantidadInput");
    cantidadInput.value = Math.max(parseInt(cantidadInput.value) - 1, 1);
    let totalProductos = document.getElementById("totalProductos");
    totalProductos.innerHTML = `Productos (${cantidadInput.value})`;
});
/* Agragar Producto */
document.getElementById("btnMas").addEventListener("click", function() {    
    let cantidadInput = document.getElementById("cantidadInput");
    cantidadInput.value = parseInt(cantidadInput.value) + 1;
    let totalProductos = document.getElementById("totalProductos");
    totalProductos.innerHTML = `Productos (${cantidadInput.value})`;
});
// /* Mensaje Producto */
// function añadidoCarrito() {
//     var titulo = "Producto añadido al carrito";
//     var mensaje = "¡El producto ha sido añadido con éxito!";
//     alert(titulo + "\n\n" + mensaje);
// }
window.addEventListener('scroll', function () {
    const supermanIcon = document.getElementById('scroll-top-icon');
    if (window.scrollY > 30) {
        supermanIcon.style.display = 'block';
    } else {
        supermanIcon.style.display = 'none';
    }
});