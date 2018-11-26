import React from 'react';
 
const AddJugador = (props) => {
  return (
          
              <form onSubmit={(event) => props.addJugador(event)}>
              <h3><strong>Crear una cuenta</strong></h3>
                
                  <div class="form-group">
                  <input id="nombre" type="text" class="form-control" name="nombre"      value={props.nombre}  onChange={props.handleChange}  placeholder="Nombre " required/>
                  </div>
                 <div class="form-group">
                  <input id="apellido" type="text" class="form-control" name="apellido"     value={props.apellido}  onChange={props.handleChange}  placeholder="Apellido" required/>
                 </div>
                 <div class="form-group">
                  <input id="email" type="email" class="form-control" name="email" placeholder="Correo electronico"    onChange={props.handleChange}   value={props.email}  required/>
                 </div>
                 <div class="form-group">
                  <div class="input-group">
                   <span class="input-group-addon"><i class="glyphicon glyphicon-phone"></i></span>
                  <input id="celular" type="text" class="form-control" onChange={props.handleChange}  name="celular"      value={props.celular} placeholder="Numero" maxlength="9" required/>
                 </div>
                 </div>

                 <div class="form-group">
                    <div class="input-group">
                   <span class="input-group-addon"><i class="glyphicon glyphicon-calendar"></i></span>
                  <input id="fechanacimiento" type="Date" class="form-control" name="fechanacimiento" onChange={props.handleChange}   value={props.fechanacimiento} placeholder="Nacimiento" required/>
                 </div>
                 </div>
                <div class="form-group">
                  <div class="input-group">
                  <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
                  <input id="usuario" type="text" class="form-control" name="usuario" placeholder="Usuario" required onChange={props.handleChange}   value={props.usuario} />
                </div>
                </div>
                
                <div class="form-group">
                   <div class="input-group">
                  <span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
                  <input id="clave" type="password" class="form-control" name="clave" placeholder="Contraseña" required onChange={props.handleChange}   value={props.clave} />
                </div>
                </div>
               
                <div class="form-group">
                 <input  type="submit" value="registrar" name="submit" class="btn btn-success"/> 
                </div>
              </form>
            

  )
};
export default AddJugador;