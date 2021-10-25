console.log("ajax conectado");



function manejarError(evt) {
    console.log('ocurrio un error.');
}




let objXMLHTTP2= new XMLHttpRequest();

let idProfesor = document.getElementById("flashRolP").textContent +"/";
let urlParaConsultaMateriasProfe = "http://127.0.0.1:5000/api/materiasPorProfe/";
urlParaConsultaMateriasProfe += idProfesor;


objXMLHTTP2.open("GET", urlParaConsultaMateriasProfe);
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
        
        document.getElementById("nombreMateriaAdministrarMateria").textContent = dataUnicaMateria.nombre;
        document.getElementById("listaParaLlenarEstudiantesProfe").innerHTML ="";

        for (let i=0; i < dataUnicaMateria.estudiantes.length; i++) {
            document.getElementById("listaParaLlenarEstudiantesProfe").innerHTML += "<li>" +"Codigo: "+ dataUnicaMateria.estudiantes[i].codigo + " Nombre: " + dataUnicaMateria.estudiantes[i].nombre + " " + dataUnicaMateria.estudiantes[i].apellido + " Nota Final: " + dataUnicaMateria.estudiantes[i].nota + "</li>";
            console.log(dataUnicaMateria.estudiantes[i])
    
        }
    }

}


