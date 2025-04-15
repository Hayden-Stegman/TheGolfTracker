import './App.css'
import { ThemeProvider } from 'styled-components';
import { theme } from './themes/theme';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <div>HELLO</div>
    </ThemeProvider>
  )
}

export default App
