import React from 'react';
 
const JugadoresList = (props) => {
  return (
    <div>
      {
        props.jugadores.map((p) => {
          return (
               <div class="row">
                   <div class="col-sm-6">
                     <img src="images/perfil.png"  width="80" height="80" alt="author"/>
                   </div>
                   <div class="col-sm-6">
                     <a  key={p.id}>{ p.nombre}</a>
                     <div > <strong>{ p.email }</strong></div>
                   </div>
                   
                 </div>

          )
        })
      }
    </div>
  )
};
export default JugadoresList;