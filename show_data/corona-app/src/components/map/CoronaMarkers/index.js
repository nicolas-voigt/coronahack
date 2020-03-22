import React from "react";
import {CoronaMarker} from "./CoronaMarker";
//import {Markers} from "./MarkersData";
import RestService from './services/RestService.js';

let api = new RestService();
export default api.retrieveArticlesFromCity('Herne').then((results) => {
  results.map((marker, index) => (
    <CoronaMarker
        key={index}
        lat={marker.lat}
        lng={marker.lng}
        factor={marker.factor}
        link={marker.link}
        text={marker.text}
    />
  ))
})
