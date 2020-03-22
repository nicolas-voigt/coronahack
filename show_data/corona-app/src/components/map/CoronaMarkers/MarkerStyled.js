import styled from "styled-components";
import {
    popUpBubbleBgColor,
    popUpBubbleCloseButtonBgColor,
    popUpBubbleTxtColor,
    green_bg
} from "../../../theme/colors";
import {FaMapMarkerAlt} from "react-icons/fa";
import {MdClose} from "react-icons/md";


export const CoronaMarkerContainer = styled.div`
  position: absolute;
`;

const MapMarkerSize = 30;
export const FaMapMarkerAltStyled = styled(FaMapMarkerAlt)`
    color: ${props => props.popUpIsOn? green_bg : popUpBubbleCloseButtonBgColor};
    width: ${MapMarkerSize}px;
    height: ${MapMarkerSize}px;    
    transform: translate(-50%, -${MapMarkerSize + 10}px);
}
`;

export const CloseButtonStyled = styled(MdClose)`
  background: ${popUpBubbleCloseButtonBgColor};
  color: ${popUpBubbleTxtColor};
  position: absolute;
  top:0;
  right:0;
  width:16px;
  height:16px;
  opacity: 0.7;
  transition: opacity .15s linear;
  
  &:hover {
    opacity: 1;
  }
`;

export const CoronaMarkerStyled = styled.div`
    opacity: ${props => props.popUpIsOn? `1` : `0`};
    background-color: ${popUpBubbleBgColor}e6; /*TODO Geldi: replace with rgba*/
    color: ${popUpBubbleTxtColor};
    display: block;
    border: 1px solid ${popUpBubbleTxtColor};
    position: absolute;
    box-sizing: border-box;
    overflow: hidden;
    max-width: 250px;
    top: 0;
    left: 0;
    transform: translate(-50%, 20px);
    border-radius: 8px 0 8px 8px;
    padding: 16px;
    box-shadow: 0 2px 8px 1px rgba(0,0,0,0.3);
    cursor: pointer;
    text-align: left;
    transition: all .15s linear;
  
  &:hover {
     background-color: ${popUpBubbleBgColor};
  }
`;

export const MarkerTitleStyled = styled.h3`
  margin: 0 0 8px;
  font-size: 18px;
`;

export const MarkerAnchorContainerStyled = styled.div`
  max-width: 220px;
  overflow: hidden;
   text-overflow: ellipsis;
`;

export const MarkerAnchorStyled = styled.a`
  color: #fff;
  text-decoration: none;
  
  &:hover {
    text-decoration: underline;
  }
`;