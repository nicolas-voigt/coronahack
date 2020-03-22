import React, {useState} from "react";
import {CoronaMarker} from "./CoronaMarker";
import RestService from '../../../services/RestService.js';

let api = new RestService();
let CoronaMarkers = () => {

    const [currentResults, setCurrentResults] = useState([]);

    api.retrieveArticlesFromCity('Herne').then((results) => {
        setCurrentResults(results)
    });

    return <>
        {console.log(currentResults)}
        {currentResults & currentResults.map((marker, index) => (
            <CoronaMarker
                key={index}
                lat={52.5200}
                lng={13.4050}
                factor={marker.factor}
                link={marker.link}
                text={marker.text}
            />
        ))}
    </>
}

export default CoronaMarkers;
