import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Container, Row, Col} from 'reactstrap';
import GymmeNavbar from './components/navbar';

const App = () => {
  return (
    <div className="App">
      <GymmeNavbar></GymmeNavbar>
      <Container>
        <Row>
          <Col md="2">
          </Col>
          <Col md="5">
          </Col>
          <Col md="3">
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;
