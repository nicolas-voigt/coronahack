import React, { Component } from 'react';
import Map from '../map/Map.js';
import Zip from '../zip/Zip.js';

class Dashboard extends Component {

  render() {
    return (
      <div style={{ width: '100%' }}>
          <Map />
          <Zip />
      </div>
    );
  }
}

export default Dashboard;