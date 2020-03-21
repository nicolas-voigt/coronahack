import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import APIKeys from '../../APIKeys.ignore';


const CoronaMarker = ({ lat, lng,factor, link, text }) =>
  <div>
    <div>{text}</div>
  </div>;

const Markers = [
  {
    lat:52.5200,
    lng:13.4050,
    factor:1,
    link:"https://www.worldometers.info/coronavirus/",
    text:"Berlin",
  },
  {
    lat:53.5584,
    lng:9.7877,
    factor:2,
    link:"https://www.worldometers.info/coronavirus/",
    text:"Hamburg",
  },
  {
    lat:50.1211,
    lng:8.4964,
    factor:3,
    link:"https://www.worldometers.info/coronavirus/",
    text:"Frankfurt",
  },
];

const CoronaMarkers = Markers.map((marker, index) =>(
  <CoronaMarker
    lat={marker.lat}
    lng={marker.lng}
    factor={marker.factor}
    link={marker.link}
    text={marker.text}
  />
));


class Map extends Component {
  static defaultProps = {
    zoom: 9
  };

  render() {
    const { lat, lng, zoom } = this.props
    return (
      <div style={{ height: '100vh', width: '100%' }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: APIKeys.getGoogleMapsKey() }}
          defaultCenter={{
            lat: lat || 52.5200,
            lng: lng || 13.4050
          }}
          defaultZoom={zoom}
        >
          {CoronaMarkers}
        </GoogleMapReact>
      </div>
    );
  }
}

export default Map;