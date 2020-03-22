import styled, {css} from "styled-components";
import {popUpBubbleCloseButtonBgColor, popUpBubbleTxtColor, offWcfefe_txt, green_bg} from "../../theme/colors";

const headerHeight = '70px';

export const HeaderStyled = styled.div`
  background-color: ${offWcfefe_txt};
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: space-between;
  max-height: ${headerHeight};
    padding: 10px;
  
  @media (min-width: 768px){
    padding: 15px 20px;
    height: 70px;
  }
  
`;

export const ContentContainerStyled = styled.div`
  height: calc(100vh - ${headerHeight});
  min-height: 450px;
`;

export const LogoImgStyled = styled.img`
  max-height: 40px;
`;

const inputHeight = 40;
const buttonDefaults = css`
height: ${inputHeight}px;
    display: inline-block;
    border-radius: 8px;
    background-color: ${props => !props.mapIsOn? green_bg : popUpBubbleCloseButtonBgColor};
    border: none;
    color: ${popUpBubbleTxtColor};
    text-align: left;
    font-size: 14px;
    padding: 8px 32px;
    transition: all 0.5s;
    cursor: pointer;
    outline: none;
    box-shadow: none;
    
    &:focus {
        outline: none;
        box-shadow: none;
    }
`;

export const MapToggleButtonStyled = styled.button`
    ${buttonDefaults}
    
    span {
        cursor: pointer;
        display: inline-block;
        position: relative;
        transition: all 0.5s;
    }
    
    svg {
        color: ${popUpBubbleCloseButtonBgColor};
        opacity: 0;
        margin-left: -14px;
        transition: all 0.5s;
        vertical-align: top;
    }
    
    &:hover {
        padding: 8px 20px;
        
        span {
            margin-right: 8px;
        }
        
        svg {
           
          color: ${popUpBubbleTxtColor};
          opacity: ${props => props.mapIsOn? `0.5` : `1`};
            
            margin-left: 0;
        }
    }
`;


export const LabelStyled = styled.label`
  display: none;
`;

export const InputStyled = styled.input`
  border: 1px solid ${green_bg};
  border-radius: 8px 0 0 8px;
  height: ${inputHeight - 2}px;
  padding: 0 10px;
    
    &:focus {
        outline: none;
        box-shadow: none;
    }
`;

export const CitySearchButtonStyled = styled.button`
  ${buttonDefaults};
  
  padding: 8px 12px;
  border-radius: 0 8px 8px 0;
`;


