import styled, {css} from "styled-components";
import {popUpBubbleCloseButtonBgColor, popUpBubbleTxtColor, offWcfefe_txt, green_bg} from "../../theme/colors";

const headerHeight = '70px';

export const HeaderStyled = styled.div`
  background-color: ${offWcfefe_txt};
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: space-between;
  padding: 15px 20px;
  max-height: ${headerHeight};
  overflow: hidden;
`;

export const ContentContainerStyled = styled.div`
  height: calc(100vh - ${headerHeight});
  min-height: 450px;
`;

export const LogoImgStyled = styled.img`
  max-height: 40px;
`;

export const MapToggleButtonStyled = styled.button`
    height: 40px;
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