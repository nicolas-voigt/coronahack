import styled, { createGlobalStyle  } from 'styled-components'

export const InjectGlobal = createGlobalStyle `
  @import url('https://fonts.googleapis.com/css?family=Lato:300,400,700&display=swap');
  
  body {
    background-color: #009688;
    font-family: 'Lato', sans-serif;
    width: 100vW;
    height: 100vh;
  }
  
  p {
    line-height: 1.7;
  }
`;