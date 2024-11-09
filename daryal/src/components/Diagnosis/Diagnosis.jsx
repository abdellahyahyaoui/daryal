import React from 'react';
import './Diagnosis.scss';

function Diagnosis({ diagnosis }) {
  const [diagnostico, ...soluciones] = diagnosis.split('\n');

  return (
    <div className="diagnosis">
      <h2>Diagnóstico Avanzado</h2>
      <p>{diagnostico}</p>
      <h3>Soluciones Recomendadas</h3>
      <ul>
        {soluciones.map((solucion, index) => (
          <li key={index}>{solucion}</li>
        ))}
      </ul>
    </div>
  );
}

export default Diagnosis;