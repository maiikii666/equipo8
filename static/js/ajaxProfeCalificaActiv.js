console.log("ajax conectado");



function manejarError(evt) {
    console.log('ocurrio un error.');
}




let objXMLHTTP= new XMLHttpRequest();

let idActividad = document.getElementById("flashRolP").textContent +"/";
let urlParaConsultaActividad = "http://127.0.0.1:5000/api/actividad/";
urlParaConsultaActividad += idActividad;


objXMLHTTP.open("GET", urlParaConsultaActividad);
objXMLHTTP.addEventListener('load', completadoActividad);
objXMLHTTP.addEventListener('error', manejarError);
objXMLHTTP.send();


function completadoActividad(evt) {
    
    let dataActividad = JSON.parse(this.response);

    document.getElementById("nombreActividad").innerHTML = dataActividad["nombre"];
    document.getElementById("materiaActividad").innerHTML = dataActividad["materia"];
    document.getElementById("descripcionActividad").innerHTML = dataActividad["descripcion"];

    for (let i=0; i < dataActividad.estudiantes.length; i++) {
        document.getElementById("listaParaLlenarEstudiantesProfe").innerHTML += "<li>" +"Codigo: "+ dataActividad.estudiantes[i].codigo + " Nota: " + dataActividad.estudiantes[i].nota + "</li>";

    }

}