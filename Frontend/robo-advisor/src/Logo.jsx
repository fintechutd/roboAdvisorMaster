import logo from './assets/fintechLogo.png'
import { Link } from "react-router-dom"

function Logo() {

    return (
      <Link to ="/">
      <div className="flex p-5">
          <img className="w-20 rounded-lg" src = {logo}></img>
          <h1 className="font-semibold p-2 text-xl">
            Fintech
            <br/>
            Robo Advisor
          </h1>
      </div>
      </Link>
    )
  }
  
export default Logo

// ./src/assets/fintechLogo.png