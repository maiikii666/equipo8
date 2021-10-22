console.log("ajax conectado");

let objXMLHTTP= new XMLHttpRequest();

let urlParaConsultaEstudiantes = "http://127.0.0.1:5000/api/listaEstudiantes/"

objXMLHTTP.open("GET", urlParaConsultaEstudiantes);
objXMLHTTP.addEventListener('load', completadoConsultaEstudiantes);
objXMLHTTP.addEventListener('error', manejarError);
objXMLHTTP.send();

function manejarError(evt) {
    console.log('ocurrio un error.');
}

function completadoConsultaEstudiantes(evt) {
    let dataConsultaEstudiantes = JSON.parse(this.response);
    for (let i=0; i < dataConsultaEstudiantes.length; i++) {
        document.getElementById("listaParaLlenarEstudiantes").innerHTML += "<li>" + dataConsultaEstudiantes[i].codigo + " " + dataConsultaEstudiantes[i].nombreYApellido + "</li>";
        console.log(dataConsultaEstudiantes[i])

    }
}



let objXMLHTTP2= new XMLHttpRequest();

let urlParaConsultaTodasMaterias = "http://127.0.0.1:5000/api/materias/"

objXMLHTTP2.open("GET", urlParaConsultaTodasMaterias);
objXMLHTTP2.addEventListener('load', completadoMaterias);
objXMLHTTP2.addEventListener('error', manejarError);
objXMLHTTP2.send();


function completadoMaterias(evt) {
    let dataTodasMaterias = JSON.parse(this.response);
    for (let i=0; i < dataTodasMaterias.length; i++) {
        let materiaAConsultar=dataTodasMaterias[i].nombre
        document.getElementById("listaMaterias").innerHTML += "<button"+" onclick="+"cargarNuevaMateria('"+materiaAConsultar+"')"+"><li>"+ dataTodasMaterias[i].nombre +"</li></button><br>";
        console.log(dataTodasMaterias[i]); /*PONER MAS BONITO EL BOTON*/

    }
}


function cargarNuevaMateria(materia) {
    let objXMLHTTP3= new XMLHttpRequest();
    let urlParaConsultaUnicaMateria = "http://127.0.0.1:5000/api/materias/" + materia +"/";
    console.log(urlParaConsultaUnicaMateria)
    objXMLHTTP3.open("GET", urlParaConsultaUnicaMateria);
    objXMLHTTP3.addEventListener('load', completadoMateriaSeleccionada);
    objXMLHTTP3.addEventListener('error', manejarError);
    objXMLHTTP3.send();

    function completadoMateriaSeleccionada() {
        let dataUnicaMateria = JSON.parse(this.response);
        
        document.getElementById("nombreMateriaAdministrarMateria").value = dataUnicaMateria.nombre;
        document.getElementById("nombreMateriaAdministrarMateria2").value = dataUnicaMateria.nombre;
        document.getElementById("nombreProfeConsultarMateria").textContent = dataUnicaMateria.nombreProfe;
        document.getElementById("listaParaLlenarEstudiantes").innerHTML = dataUnicaMateria.estudiantes;
    }

}


