import React, {Component} from 'react';
import GoogleMapReact from 'google-map-react';
import APIKeys from '../../APIKeys.ignore';
import CoronaMarkers from './CoronaMarkers'

class Map extends Component {
    static defaultProps = {
        zoom: 9
    };

    render() {
        const {lat, lng, zoom} = this.props;
        return (
            <div style={{height: '100vh', width: '100%'}}>
                <GoogleMapReact
                    bootstrapURLKeys={{key: APIKeys.getGoogleMapsKey()}}
                    defaultCenter={{
                        lat: lat || 52.5200,
                        lng: lng || 13.4050
                    }}
                    defaultZoom={zoom}
                    distanceToMouse={() => {
                    }}
                >
                    {CoronaMarkers}
                </GoogleMapReact>
            </div>
        );
    }
}

export default Map;