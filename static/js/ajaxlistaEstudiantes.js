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
    const data = JSON.parse(this.response);
    for (let i=0; i < data.length; i++) {
        document.getElementById("listaParaLlenarEstudiantes").innerHTML += "<li>" + data[i].codigo + " " + data[i].nombreYApellido + "</li>";
        console.log(data[i])

    }
}



let objXMLHTTP2= new XMLHttpRequest();

let urlParaConsulta2 = "http://127.0.0.1:5000/api/materias/"

objXMLHTTP2.open("GET", urlParaConsulta2);
objXMLHTTP2.addEventListener('load', completadoMaterias);
objXMLHTTP2.addEventListener('error', manejarError);
objXMLHTTP2.send();


function completadoMaterias(evt) {
    let data2 = JSON.parse(this.response);
    for (let i=0; i < data2.length; i++) {
        
        document.getElementById("listaMaterias").innerHTML += "<button"+" onclick="+"cargarNuevaMateria("+data2[i].nombre+")"+"><li>"+ data2[i].nombre +"</li></button><br>";
        console.log(data2[i]); /*PONER MAS BONITO EL BOTON*/

    }
}

function cargarNuevaMateria(materia) {
    let objXMLHTTP3= new XMLHttpRequest();
    let urlParaConsulta3 = "http://127.0.0.1:5000/api/materias/" + materia +"/";
    objXMLHTTP3.open("GET", urlParaConsulta3);
    objXMLHTTP3.addEventListener('load', completadoMateriaSeleccionada);
    objXMLHTTP3.addEventListener('error', manejarError);
    objXMLHTTP3.send();

    function completadoMateriaSeleccionada() {
        let data3 = JSON.parse(this.response);
        
        document.getElementById("NombreMateriaAdministrarMateria").textContent = data3.nombre;
        document.getElementById("nombreProfeConsultarMateria").textContent = data3.profesor;
        document.getElementById("listaParaLlenarEstudiantes").innerHTML = data3.estudiantes;
    }

}


