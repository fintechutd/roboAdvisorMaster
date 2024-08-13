import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Login from './components/Login'
import Logo from './components/Logo'
import './index.css'
import Questionnaire from './components/Questionnaire/Questionnaire'
import Dashboard from './components/Dashboard/Dashboard';

function App() {

  return (
    <Router>
      <Routes>
        
        <Route path='/questionnaire' element={<Questionnaire/>}></Route>
        <Route path='/dashboard' element={<Dashboard/>}></Route>

      </Routes>
    </Router>
  )
}

export default App
