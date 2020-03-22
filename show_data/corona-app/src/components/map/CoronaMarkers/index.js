import React from "react";
import {CoronaMarker} from "./CoronaMarker";
import {Markers} from "./MarkersData";
import RestService from '../../../services/RestService.js';

let api = new RestService();
let CoronaMarkers = () => {
  api.retrieveArticlesFromCity('Herne').then((results) => {
    results.map((marker, index) => (
      <CoronaMarker
          key={index}
          lat={52.5200}
          lng={13.4050}
          factor={marker.factor}
          link={marker.link}
          text={marker.text}
      />
    ))
});
}

export default CoronaMarkers;
