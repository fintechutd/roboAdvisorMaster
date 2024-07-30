import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Login from './components/Login'
import Logo from './components/Logo'
import './index.css'
import Questionnaire from './components/Questionnaire/Questionnaire'

function App() {

  return (
    <Router>
      <Routes>
        
        <Route path='/' element={<Questionnaire/>}></Route>
      </Routes>
    </Router>
  )
}

export default App
