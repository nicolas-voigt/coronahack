import React, { Component } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';


class Dashboard extends Component {

  render() {
    return (
      <nav>
        <div><Button variant="primary">Karte anzeigen</Button></div>
        <Form>
          <Form.Control type="text" placeholder="PLZ tippen" /><Button variant="secondary">Postleitzahl angeben</Button>
        </Form>
      </nav>
    );
  }
}

export default Dashboard;
