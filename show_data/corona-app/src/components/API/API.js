import React, {Component} from 'react';
import { AxiosProvider, Request, Get, Delete, Head, Post, Put, Patch, withAxios } from 'react-axios';
import CoronaMarkers from '../map/CoronaMarkers';

class Markers extends Component {
    render() {
      return (
        <Post url="localhost:8000/get_data" params={{city: "Herne"}}>
          {(error, response, isLoading, makeRequest, axios) => {
            if(response !== null) {
              return response.city.map((marker, index) => {
                return (<CoronaMarkers
                key={index}
                lat={52.5200}
                lng={13.4050}
                factor={marker.factor}
                link={marker.url}
                text={marker.text}
                />)
              });
            } else {
              return null;
            }
          }}
        </Post>
    )
  }
}

export default Markers;
