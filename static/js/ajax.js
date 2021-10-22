const rol = document.getElementById("rolPagina").textContent
const usuario = document.getElementById("flashRolP").textContent

console.log(rol, usuario)

let objXMLHTTP= new XMLHttpRequest();

let urlParaConsulta = "http://127.0.0.1:5000/api/informacion/"

urlParaConsulta += rol+ "/"+usuario;

console.log(urlParaConsulta)

objXMLHTTP.open("GET", urlParaConsulta);
objXMLHTTP.addEventListener('load', completado);
objXMLHTTP.addEventListener('error', manejarError);
objXMLHTTP.send();

function manejarError(evt) {
    console.log('ocurrio un error.');
}

function completado(evt) {
    let data = JSON.parse(this.response);
    console.log(data);
    document.getElementById("campoNombreInfo").textContent =data.nombre;
    document.getElementById("campoApellidoInfo").textContent = data.apellido;
    document.getElementById("codigoEnInfo").textContent = data.codigo;
    document.getElementById("campoTelefonoInfo").value = data.telefono;
    document.getElementById("campoCorreoInfo").value = data.correo;
}

function alerta() {
    window.alert("usuario actualizado");
}