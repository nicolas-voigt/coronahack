import React from 'react';
import { geolocated } from "react-geolocated";
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
    const { isGeolocationAvailable, coords } = this.props
    return (
      <nav>
        <div><Button variant="primary" onClick={this.toggleMap}>Karte anzeigen</Button></div>
        <Form>
          <Form.Control type="text" placeholder="PLZ tippen" /><Button variant="secondary" onClick={this.toggleZip}>Postleitzahl angeben</Button>
        </Form>
        {this.state.toggleMap &&
            <Map
            lat={(isGeolocationAvailable && coords) && coords.latitude}
            lng={(isGeolocationAvailable && coords) && coords.longitude}
        />}
        {this.state.toggleMap && <Zip />}
      </nav>
    );
  }
}

export default geolocated({
    positionOptions: {
        enableHighAccuracy: false,
    },
    userDecisionTimeout: 5000,
})(Dashboard);