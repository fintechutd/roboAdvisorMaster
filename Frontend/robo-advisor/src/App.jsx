import Logo from "./Logo"
import Login from "./Login"
import './index.css'

function App() {

  return (
    <div className="text-white">
      <div className=" text-white  h-screen flex flex-col sm:w-dvw lg:w-1/3 backdrop-blur-lg border-r-4" >
      <Logo>
      </Logo>
      <div className=" h-screen flex justify-center items-center">
        <Login>
        </Login>
      </div>
      </div>
      <h1 className=" text-red-700">Hello</h1>
    </div>
  )
}

export default App