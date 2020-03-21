import React, { Component } from 'react';
import Map from '../map/Map.js';
import Zip from '../zip/Zip.js';
import Menu from '../menu/Menu.js'
import 'bootstrap/dist/css/bootstrap.min.css';

class Dashboard extends Component {

  render() {
    return (
      <div style={{ width: '100%' }}>
          <Menu />
      </div>
    );
  }
}

export default Dashboard;
