console.log("ajax conectado");



function manejarError(evt) {
    console.log('ocurrio un error.');
}




let objXMLHTTP= new XMLHttpRequest();

let idActividad = document.getElementById("flashRolP").textContent +"/";
let urlParaConsultaActividad = "http://127.0.0.1:5000/api/notasEstudiante/";
urlParaConsultaActividad += idActividad;


objXMLHTTP.open("GET", urlParaConsultaActividad);
objXMLHTTP.addEventListener('load', completadoActividad);
objXMLHTTP.addEventListener('error', manejarError);
objXMLHTTP.send();


function completadoActividad(evt) {
    
    let dataActividad = JSON.parse(this.response);

    for (let i=0; i < dataActividad.materias.length; i++) {
        document.getElementById("listaParallenarDeMaterias").innerHTML += "<li>" + dataActividad.materias[i].nombre+ "</li>";
        document.getElementById("listaParaLlenarNotasMateria").innerHTML += "<li>" + dataActividad.materias[i].nota+ "</li>";

    }

    for (let i=0; i< dataActividad.actividades.length; i++) {
        document.getElementById("listaParallenarDeActividadesMaterias").innerHTML += "<li>" + dataActividad.actividades[i].materia+ "</li>";
        document.getElementById("listaParallenarDeActividades").innerHTML += "<li>" + dataActividad.actividades[i].nombre+ "</li>";
        document.getElementById("listaParallenarDeNotasActividades").innerHTML += "<li>" + dataActividad.actividades[i].nota+ "</li>";
        document.getElementById("listaParallenarDeRetroActividades").innerHTML += "<li>" + dataActividad.actividades[i].retroalimentacion+ "</li>";
    }

    document.getElementById("promedioFinal").innerHTML = dataActividad.promedioFinal;

}