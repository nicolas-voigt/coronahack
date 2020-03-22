import React from "react";
import {CoronaMarker} from "./CoronaMarker";
import {Markers} from "./MarkersData";

const CoronaMarkers = Markers.map((marker, index) => (
    <CoronaMarker
        key={index}
        lat={marker.latitude}
        lng={marker.longitude}
        factor={marker.factor}
        link={marker.Url}
        text={marker.Title}
    />
));

export default CoronaMarkers;
