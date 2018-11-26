import React, { Component } from 'react';  // nuevo
import ReactDOM from 'react-dom';
import axios from 'axios';
import JugadoresList from './components/JugadoresList';
import AddJugador from './components/AddJugador';


class App extends Component {
  constructor() {
    super();
	this.state ={
	    jugadores: []
	 };

  }

  componentDidMount() {
  this.getJugadores();
  };

  // nuevo
  getJugadores() {
   axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/jugadores`)  // nuevo
 .then((res) =>{ this.setState({ jugadores: res.data.data.jugadores }); })
 .catch((err) =>{ console.log(err); });
};

  render() {
    return (
  <section >
    <div class="container cabecera">
      <h1><strong>Teambook</strong></h1>
    </div>
    <div class="container">
        <div class="row">
          <div class="col-sm-6">
            <br/>
            <AddJugador/>
            <hr/><br/>
          </div>
          <div class="col-sm-6">
            <br/>
            <h5 class="title">Amigos que tiene Teambook</h5>
            <br/> <JugadoresList jugadores={this.state.jugadores}/>
            <hr/><br/>
             </div>
        </div>
    </div>
    </section>
    )
 }
};

ReactDOM.render(
  <App />,
  document.getElementById('root')
);

