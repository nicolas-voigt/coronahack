import { createGlobalStyle  } from 'styled-components'

export const InjectGlobal = createGlobalStyle `
  @import url('https://fonts.googleapis.com/css?family=Lato:300,400,700&display=swap');
  
  body {
    background-color: #009688;
    font-family: 'Lato', sans-serif;
  }
  
  p {
  line-height: 1.7;
  }
`;