import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';
 
import AddJugador from '../AddJugador';
 
test('AddJugador renders properly', () => {
  const wrapper = shallow(<AddJugador/>);
  const element = wrapper.find('form');
  expect(element.find('input').length).toBe(10);
  expect(element.find('input').get(0).props.name).toBe('nombre');
  expect(element.find('input').get(1).props.name).toBe('apellido');
  expect(element.find('input').get(2).props.name).toBe('email');
  expect(element.find('input').get(3).props.name).toBe('celular');
  expect(element.find('input').get(4).props.name).toBe('fnacimiento');
  expect(element.find('input').get(5).props.name).toBe('usuario');
  expect(element.find('input').get(6).props.name).toBe('clave');
  expect(element.find('input').get(7).props.value).toBe('1');
  expect(element.find('input').get(8).props.value).toBe('2');
  expect(element.find('input').get(9).props.type).toBe('submit');
});


test('AddJugador renders a snapshot properly', () => {
  const tree = renderer.create(<AddJugador/>).toJSON();
  expect(tree).toMatchSnapshot();
});