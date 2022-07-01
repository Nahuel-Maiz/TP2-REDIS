import React from 'react'
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
import CargarPersonaje from "./Componentes/CargarPersonaje";
import logo from './logo.svg';
import './App.css';

function App() {
  return (

    <BrowserRouter>
    <Routes>
        <Route exac path="/cargarPersonaje" element={<CargarPersonaje />} />
    </Routes>
    </BrowserRouter>
  );
}

export default App;
