import styled from 'styled-components';

export const ProfilesContainerStyled = styled.div`
`;

const cardHeight = 60;
export const ProfileStyled = styled.div`
display: inline-block;
  width: 200px;
  height: ${cardHeight}px;
  overflow: hidden;
  text-overflow: ellipsis;
  vertical-align: top;
  background-color: white;
  color: #1b1e21;
  margin: 10px;
`;

export const PicContainerStyled = styled.div`
display: inline-block;
  width: 60px;
  height: ${cardHeight}px;
  overflow: hidden;
  position: relative;
  
  img {
    width: 100%;  
    max-width: 100%;  
  }
`;
export const ContentContainerStyled = styled.div`
vertical-align: top;
  display: inline-block;
  padding-left: 8px;
`;

export const NameStyled = styled.h4`
  font-size: 12px;
  margin: 0 0 4px;
`;

export const RoleStyled = styled.span`
  font-size: 10px;
`;

export const LinkContainer = styled.div`
  display: flex;
  flex-direction: row;
  
`;
export const LinkStyled = styled.a`
  font-size: 15px;
`;
