import React from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Map from '../map/Map.js';
import Zip from '../zip/Zip.js';

export class Dashboard extends React.Component {

  constructor (props) {
    super(props)
    this.state = {
      toggleMap: false,
      toggleZip: false,
    }
    this.toggleMap = this.toggleMap.bind(this);
    this.toggleZip = this.toggleZip.bind(this);
  }

  toggleMap(){
    this.setState({ toggleMap: !this.state.toggleMap });
  }

  toggleZip(){
    this.setState({ toggleZip: !this.state.toggleZip });
  }

  render() {

    return (
      <nav>
        <div><Button variant="primary" onClick={this.toggleMap}>Karte anzeigen</Button></div>
        <Form>
          <Form.Control type="text" placeholder="PLZ tippen" /><Button variant="secondary" onClick={this.toggleZip}>Postleitzahl angeben</Button>
        </Form>
        {this.state.toggleMap && <Map />}
        {this.state.toggleMap && <Zip />}
      </nav>
    );
  }
}

export default Dashboard;