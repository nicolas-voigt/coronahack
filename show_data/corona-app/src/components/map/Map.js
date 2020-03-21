import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import APIKeys from '../../APIKeys.ignore';

const AnyReactComponent = ({ text }) => <div>{text}</div>;

class Map extends Component {
  static defaultProps = {
    zoom: 9
  };

  render() {
    const { lat, lng, zoom } = this.props
    return (
      // Important! Always set the container height explicitly
      <div style={{ height: '100vh', width: '100%' }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: APIKeys.getGoogleMapsKey() }}
          defaultCenter={{
            lat: lat || 52.5200,
            lng: lng || 13.4050
          }}
          defaultZoom={zoom}
        >
          <AnyReactComponent
            lat={lat || 52.5200}
            lng={lng || 13.4050}
            text="My Marker"
          />
        </GoogleMapReact>
      </div>
    );
  }
}

export default Map;
