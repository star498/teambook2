import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';
 
import JugadoresList from '../JugadoresList';
 
const jugadores = [
  {
    'nombre': 'estrella',
    'email': 'strella@gmail.com',
    'apellido': 'barrientos',
    'celular': '4356565',
    'nivel': 0,
    'fechanacimiento': '12-15-48',
    'sexo' : 1,
    'id': 1,
    'estado': true
  },
  {
    'nombre': 'estrella',
    'email': 'strella@gmail.com',
    'apellido': 'barrientos',
    'celular': '4356565',
    'nivel': 0,
    'fechanacimiento': '12-15-48',
    'sexo' : 1,
    'id': 2,
    'estado': true
  },
];
 
test('JugadoresList renders properly', () => {
  const wrapper = shallow(<JugadoresList jugadores={jugadores}/>);
  const element = wrapper.find('h4');
  expect(element.length).toBe(2);
  expect(element.get(0).props.children).toBe('estrella');
});
test('JugadoresList renders a snapshot properly', () => {
  const tree = renderer.create(<JugadoresList jugadores={jugadores}/>).toJSON();
  expect(tree).toMatchSnapshot();
});


 
