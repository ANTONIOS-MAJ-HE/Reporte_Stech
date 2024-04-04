import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './styles/App.css';

function App() {
  const [ventas, setVentas] = useState([]);
  const [filtroCanal, setFiltroCanal] = useState('');
  const [filtroNumeroOrden, setFiltroNumeroOrden] = useState('');
  const [filtroNombreCliente, setFiltroNombreCliente] = useState('');
  const [filtroFechaDesde, setFiltroFechaDesde] = useState('');
  const [filtroFechaHasta, setFiltroFechaHasta] = useState('');

  useEffect(() => {
    const authToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyOTE0MTg2LCJpYXQiOjE3MTEzNzgxODYsImp0aSI6IjNjODMxMDM1MWFiZTRiZDA5OTIzODE4ODg4NzFjMWNjIiwidXNlcl9pZCI6MX0.3c7Hn9YZvW7GXy0CmgZyMKZWwpyypuZs773cKoLFg8s";

    const fetchData = async () => {
      try {
        let url = 'http://localhost:8000/consulta/';
        let parametros = [];

        if (filtroCanal) {
          parametros.push(`canal/${filtroCanal}/`);
        }
        if (filtroNumeroOrden) {
          parametros.push(`numero-orden/${filtroNumeroOrden}/`);
        }
        if (filtroNombreCliente) {
          parametros.push(`nombre-cliente/${filtroNombreCliente}/`);
        }
        if (filtroFechaDesde) {
          // Convertir la fecha desde el formato de entrada al formato de fecha ISO
          const fechaDesdeISO = new Date(filtroFechaDesde).toISOString().split('T')[0];
          parametros.push(`fecha_desde/${fechaDesdeISO}/`);
        }
        if (filtroFechaHasta) {
          // Convertir la fecha desde el formato de entrada al formato de fecha ISO
          const fechaHastaISO = new Date(filtroFechaHasta).toISOString().split('T')[0];
          parametros.push(`fecha_hasta/${fechaHastaISO}/`);
        }

        if (parametros.length > 0) {
          url += parametros.join('');
        }

        const response = await axios.get(url, {
          headers: {
            Authorization: `Bearer ${authToken}`,
          }
        });
        setVentas(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    // Realizar la primera solicitud al montar el componente
    fetchData();

    // Establecer un temporizador para realizar solicitudes periódicas cada 5 segundos
    const intervalId = setInterval(fetchData, 5000);

    // Limpiar el temporizador cuando el componente se desmonte para evitar fugas de memoria
    return () => clearInterval(intervalId);
  }, [filtroCanal, filtroNumeroOrden, filtroNombreCliente, filtroFechaDesde,  filtroFechaHasta]);

  return (
    <div className="App">
      <h1>Reporte de Ventas</h1>
      <div className="filtros">
        <input type="text" placeholder="Canal" value={filtroCanal} onChange={(e) => setFiltroCanal(e.target.value)} />
        <input type="text" placeholder="Número de Orden" value={filtroNumeroOrden} onChange={(e) => setFiltroNumeroOrden(e.target.value)} />
        <input type="text" placeholder="Nombre del Cliente" value={filtroNombreCliente} onChange={(e) => setFiltroNombreCliente(e.target.value)} />
        <input type="date" placeholder="Fecha Desde" value={filtroFechaDesde} onChange={(e) => setFiltroFechaDesde(e.target.value)} />
        <input type="date" placeholder="Fecha Hasta" value={filtroFechaHasta} onChange={(e) => setFiltroFechaHasta(e.target.value)} />
      </div>
      <table>
        <thead>
          <tr>
            <th>Canal</th>
            <th>Número de Orden</th>
            <th>Nombre del Cliente</th>
            <th>Producto</th>
            <th>Cantidad</th>
            <th>Precio (S/IGV)</th>
            <th>Total (S/IGV)</th>
            <th>Fecha de Orden</th>
            <th>Fecha de Proceso</th>
          </tr>
        </thead>
        <tbody>
          {ventas.map((venta, index) => (
            <tr key={index}>
              <td>{venta.canal}</td>
              <td>{venta.numero_orden}</td>
              <td>{venta.nombre_cliente}</td>
              <td>{venta.nombre_producto}</td>
              <td>{venta.cantidad}</td>
              <td>{venta.precio_s_igv}</td>
              <td>{venta.total_s_igv}</td>
              <td>{venta.fecha_orden}</td>
              <td>{venta.fecha_proceso}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
