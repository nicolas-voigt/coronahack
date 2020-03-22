import React from "react";
import {CoronaMarker} from "./CoronaMarker";
import {Markers} from "./MarkersData";

const CoronaMarkers = Markers.map((marker, index) => (
    <CoronaMarker
        key={index}
        lat={marker.lat}
        lng={marker.lng}
        factor={marker.factor}
        link={marker.link}
        text={marker.text}
    />
));

export default CoronaMarkers;
