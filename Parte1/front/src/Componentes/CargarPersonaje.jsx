import React from 'react'
import {useState} from 'react';
import '../hojas-de-estilo/CargarPersonaje.css'

function CargarPersonaje() {

    const [personaje, setPersonaje] = useState({
        episodio: '',
        personaje : ''
    });

    const handleChange = (e) =>{
        setPersonaje({ ...personaje, [e.target.name]: e.target.value });
    }

    console.log(personaje);

    const cargarPersonaje = async (e) =>{
        const res = await fetch("http://localhost:3030/cargar",
        {
        method: 'POST',
        body: JSON.stringify(personaje),
        headers: {"Content-Type": "application/json"}
        })
        const data = await res.json();
    }

    return (
        <>
            <div className='todo-cargar'>
                <h1>Ingrese los datos para cargar</h1>

            <div>
                

            </div>


            </div>
        </>
    )
}

export default CargarPersonaje;