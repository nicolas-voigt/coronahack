import React from 'react';
import styled from 'styled-components'

const CoronaMarkerStyled = styled.div`
  background: #ffffff;
  display: block;
`;

export const CoronaMarker = ({lat, lng, factor, link, text}) => {
    return (
        <CoronaMarkerStyled className={'hallo marker'}>
            {text}
            {lat}<br/>
            {lng}<br/>
            {factor}<br/>
            {link}<br/>
        </CoronaMarkerStyled>
    )
};
