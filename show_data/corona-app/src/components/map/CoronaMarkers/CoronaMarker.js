import React from "react";
import styled from "styled-components";
import {
    FaMapMarkerAlt,
    FaWindowClose
} from "react-icons/fa";
import {
    popUpBubbleBgColor,
    popUpBubbleTxtColor,
    popUpBubbleCloseButtonBgColor
} from "../../../theme/colors";
import { MdClose } from "react-icons/md";

const CoronaMarkerContainer = styled.div`
  position: absolute;
`;

const FaMapMarkerAltStyled = styled(FaMapMarkerAlt)`
  color: red;
`;

const CloseButtonStyled = styled(MdClose)`
  background: ${popUpBubbleCloseButtonBgColor};
  color: ${popUpBubbleTxtColor};
  position: absolute;
  top:0;
  right:0;
  width:15px;
  height:15px;
  opacity: 0.7;
  transition: opacity .15s linear;
  
  &:hover {
    opacity: 1;
  }
`;


const CoronaMarkerStyled = styled.div`
    background-color: ${popUpBubbleBgColor}cc;
    color: ${popUpBubbleTxtColor};
    display: block;
    border: 1px solid ${popUpBubbleTxtColor};
    position: absolute;
    box-sizing: border-box;
    overflow: hidden;
    top: 0;
    left: 0;
    transform: translate(-50%, 20px);
    border-radius: 8px 0 8px 8px;
    padding: 12px;
    box-shadow: 0 2px 8px 1px rgba(0,0,0,0.3);
    cursor: pointer;
    text-align: left;
    transition: background-color .15s linear;
  
      &:hover {
         background-color: ${popUpBubbleBgColor};
      }
`;

const MarkerTitleStyled = styled.h3`
  margin: 0 0 8px;
`;

const MarkerAnchorStyled = styled.a`
  
`;



export const CoronaMarker = ({factor, link, text}) => {
    return (
        <CoronaMarkerContainer>
            <FaMapMarkerAltStyled/>
            <CoronaMarkerStyled factor={factor} className={"hallo marker"}>
                <CloseButtonStyled />
                <MarkerTitleStyled>{text}</MarkerTitleStyled>
                <MarkerAnchorStyled href={link} title={`Info für ${text}`} target="_blank">{link}</MarkerAnchorStyled>
            </CoronaMarkerStyled>
        </CoronaMarkerContainer>
    )
};
