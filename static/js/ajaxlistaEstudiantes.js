console.log("ajax conectado");

let objXMLHTTP= new XMLHttpRequest();

let urlParaConsulta = "http://127.0.0.1:5000/api/listaEstudiantes/"

objXMLHTTP.open("GET", urlParaConsulta);
objXMLHTTP.addEventListener('load', completado);
objXMLHTTP.addEventListener('error', manejarError);
objXMLHTTP.send();

function manejarError(evt) {
    console.log('ocurrio un error.');
}

function completado(evt) {
    let data = JSON.parse(this.response);
    for (let i=0; i < data.length; i++) {
        document.getElementById("listaParaLlenarEstudiantes").innerHTML += "<li>" + data[i].codigo + " " + data[i].nombreYApellido + "</li>";
        console.log(data[i])

    }
}


