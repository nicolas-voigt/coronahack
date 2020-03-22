import styled, {css} from "styled-components";
import {popUpBubbleCloseButtonBgColor, popUpBubbleTxtColor, offWcfefe_txt} from "../../theme/colors";

export const HeaderStyled = styled.div`
  background-color: ${offWcfefe_txt};
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: space-between;
  padding: 15px 20px;
  max-height: 70px;
  overflow: hidden;
`;

export const LogoImgStyled = styled.img`
  max-height: 40px;
`;

export const MapToggleButtonStyled = styled.button`
    height: 40px;
    display: inline-block;
    border-radius: 8px;
    background-color: ${popUpBubbleCloseButtonBgColor};
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
            opacity: 1;
            margin-left: 0;
        }
    }
`;