import React from 'react';

const data = [
  { name: 'Player 1', score: 100 },
  { name: 'Player 2', score: 90 },
];

export default function TableScores() {
  return (
    <div className="w-full max-w-md mx-auto">
      <table className="table-auto w-full">
        <caption className="text-lg font-medium text-gray-900 mb-2">Tabla de Puntuaciones</caption>
        <thead>
          <tr className="bg-light-purple">
            <th className="px-4 py-2 text-left text-white">Nombre</th>
            <th className="px-4 py-2 text-left text-white">Puntuación</th>
          </tr>
        </thead>
        <tbody>
          {data.map((player, index) => (
            <tr key={index} className={index % 2 === 0 ? "bg-gray-100" : "bg-white"}>
              <td className="border px-4 py-2">{player.name}</td>
              <td className="border px-4 py-2">{player.score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}