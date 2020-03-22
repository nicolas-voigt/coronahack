import React from "react";
import {CoronaMarker} from "./CoronaMarker";
import {Markers} from "./MarkersData";

const CoronaMarkers = Markers.map((marker, index) => (
    <CoronaMarker
        key={index}
        lat={marker.Longitude}
        lng={marker.Latitude}
        link={marker.Url}
        text={marker.Title}
    />
));

export default CoronaMarkers;
