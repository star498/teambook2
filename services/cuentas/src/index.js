import React, { Component } from 'react';  // nuevo
import ReactDOM from 'react-dom';
import axios from 'axios';
import JugadoresList from './components/JugadoresList';
import AddJugador from './components/AddJugador';


class App  extends Component{
  constructor() {
    super();
      this.state ={
      jugadores: [],
       nombre: '',
       barrientos: '',
       email: '',
       celular: '',
       fechanacimiento: '',
       usuario:'',
       clave:''
   };
  this.addJugador = this.addJugador.bind(this);  // new
  this.handleChange = this.handleChange.bind(this);
  };
   componentDidMount() {
  this.getJugadores();
  };
 

 // nuevo
  getJugadores() {
   axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users/jugadores`)  // nuevo
  .then((res) =>{ this.setState({ jugadores: res.data.data.jugadores }); })
  .catch((err) =>{ console.log(err); });
  };


  addJugador(event) {
    event.preventDefault();
    const data = {
    nombre: this.state.nombre,
    apellido: this.state.apellido,
    email: this.state.email,
    celular: this.state.celular,
    fechanacimiento: this.state.fechanacimiento,
    usuario: this.state.usuario,
    clave: this.state.clave
    };

  axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users/crearjugador`, data)
  .then((res) => { 
  this.getJugadores();
  this.setState({ nombre: '', apellido: '', email: '', celular:'' ,fechanacimiento: '',  usuario: '', clave:''  });  
  })
  .catch((err) => { console.log(err); });
  };

handleChange(event) {
  const obj = {};
  obj[event.target.name] = event.target.value;
  this.setState(obj);
};


  render() {
    return (

           <section className="section">
                <div className="container">
                <div class="row">
                <div class="col-sm-6">
                   <br/>
                      <AddJugador 
                      nombre={this.state.nombre}
                      apellido={this.state.apellido}
                      email={this.state.email}
                      celular= {this.state.celular}
                      fechanacimiento={this.state.fechanacimiento}
                      usuario={this.state.usuario}
                      clave={this.state.clave}
                      addJugador={this.addJugador}
                      handleChange={this.handleChange} 
                      />
                </div>
                <div class="col-sm-6">
                 <br/>
                   <h5 class="title">Amigos que tiene Teambook</h5>
                    <hr/><br/>
                   <JugadoresList jugadores={this.state.jugadores}/>
                </div>
              </div>
             </div>
          </section>
           )
   };
};

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
class Header  extends Component{
  constructor() {
    super();
  };

  render() {
    return (
           <section className="section" id="cabecera" >
                <div className="container header">
                    <h1><strong>Teambook</strong></h1> 
                </div>
              </section>
           )
   };
};
ReactDOM.render(
  <Header />,
  document.getElementById('header')
);




