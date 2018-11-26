import React from 'react';
 
const AddJugador = (props) => {
  return (

              <form>
              <h3><strong>Crear una cuenta</strong></h3>
                
                  <div class="form-group">
                  <input id="nombre" type="text" class="form-control" name="nombre" placeholder="Nombre " required/>
                  </div>
                 <div class="form-group">
                  <input id="apellido" type="text" class="form-control" name="apellido" placeholder="Apellido" required/>
                 </div>
                 <div class="form-group">
                  <input id="email" type="email" class="form-control" name="email" placeholder="Correo electronico" required/>
                 </div>
                 <div class="form-group">
                  <div class="input-group">
                   <span class="input-group-addon"><i class="glyphicon glyphicon-phone"></i></span>
                  <input id="celular" type="text" class="form-control" name="celular" placeholder="Numero" maxlength="9" required/>
                 </div>
                 </div>

                 <div class="form-group">
                    <div class="input-group">
                   <span class="input-group-addon"><i class="glyphicon glyphicon-calendar"></i></span>
                  <input id="fnacimiento" type="Date" class="form-control" name="fnacimiento" placeholder="Nacimiento" required/>
                 </div>
                 </div>
                <div class="form-group">
                  <div class="input-group">
                  <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
                  <input id="usuario" type="text" class="form-control" name="usuario" placeholder="Usuario" required/>
                </div>
                </div>
                
                <div class="form-group">
                   <div class="input-group">
                  <span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
                  <input id="clave" type="password" class="form-control" name="clave" placeholder="Contraseña" required/>
                </div>
                </div>
                <div class="form-group">
                   <div class="input-group" >
                  <input type="radio" id="femenino"
                     name="sexo" value="1" checked/>
                    <label  for="femenino">Mujer</label>

                    <input type="radio" id="masculino"
                     name="sexo" value="2"/>
                    <label for="masculino">Hombre</label>
                </div>
                </div>
               
                <div class="form-group">
                 <input  type="submit" value="registrar" name="submit" class="btn btn-success"/> 
                </div>
              </form>

  )
};
export default AddJugador;
