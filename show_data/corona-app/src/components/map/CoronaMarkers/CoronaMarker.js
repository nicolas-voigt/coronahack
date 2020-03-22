import React, {useState} from "react";
import {
    CoronaMarkerContainer,
    FaMapMarkerAltStyled,
    CloseButtonStyled,
    CoronaMarkerStyled,
    MarkerTitleStyled,
    MarkerAnchorContainerStyled,
    MarkerAnchorStyled
} from "./MarkerStyled"

export const CoronaMarker = ({factor, link, text}) => {
    const [popUpIsOn, setPopUpIsOn] = useState(false);

    return (
        <CoronaMarkerContainer>
            <FaMapMarkerAltStyled popUpIsOn={popUpIsOn} onClick={() => {setPopUpIsOn(!popUpIsOn)}}/>
            <CoronaMarkerStyled popUpIsOn={popUpIsOn} factor={factor} className={"hallo marker"}>
                <CloseButtonStyled onClick={() => {setPopUpIsOn(false)}} />
                <MarkerTitleStyled>{text}</MarkerTitleStyled>
                <MarkerAnchorContainerStyled>
                    <MarkerAnchorStyled href={link} title={text}
                                        target="_blank">{link}</MarkerAnchorStyled>
                </MarkerAnchorContainerStyled>
            </CoronaMarkerStyled>
        </CoronaMarkerContainer>
    )
};
