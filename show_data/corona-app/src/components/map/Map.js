import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

const AnyReactComponent = ({ text }) => <div>{text}</div>;

class Map extends Component {
  static defaultProps = {
    center: {
      lat: 52.5200,
      lng: 13.4050
    },
    zoom: 11
  };

  render() {
    return (
      // Important! Always set the container height explicitly
      <div style={{ height: '100vh', width: '100%' }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: "AIzaSyDcm7GzeP8Y67_tT6f6hPe3DsHFDygu-IQ" }}
          defaultCenter={this.props.center}
          defaultZoom={this.props.zoom}
        >
          <AnyReactComponent
            lat={52.5200}
            lng={13.4050}
            text="My Marker"
          />
        </GoogleMapReact>
      </div>
    );
  }
}

export default Map;