console.log("probando")

const productos = [
    {nombre: 'planta' , precio: 500},
    {nombre: 'flor' , precio: 1000},
]



const formulario = document.querySelector('#formulario');
const boton = document.querySelector('#boton');
const resultado = document.querySelector('#resultado')

const filtrar = ()=>{
    //console.log(formulario.value);
    const texto = formulario.value.toLowerCase();
    for (let producto of productos){
        let nombre = producto.nombre.toLocaleLowerCase();
        if(nombre.indexOf(texto) !== -1){
            resultado.innerHTML += `b
             <li>${producto.nombre}
            `

        }
    }
}

boton.addEventListener('click', filtrar)

