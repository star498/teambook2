import React from 'react';
 
const JugadoresList = (props) => {
  return (
    <div>
      {
        props.jugadores.map((p) => {
          return (
               <table >
               <tr>
                <td ROWSPAN="4">
                {p.id}
                </td>
                <td>
                {p.nombre} {p.apellido}
                </td>
                </tr>
                <tr>
                <td>
                {p.celular}
                </td>
                </tr>
               <tr>
                <td>
                {p.nivel}
                </td>
              </tr>
               <tr>
                <td>
               {p.email}
                </td>
              </tr>
                
              </table> 

          )
        })
      }
    </div>
  )
};
export default JugadoresList;