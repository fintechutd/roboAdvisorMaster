import Logo from "./Logo";
import Signup from "./Signup";
import './index.css'

function SignupPage() {
  return (
    <div className="text-white">
      <div className="h-screen flex flex-col sm:w-full lg:w-1/3 backdrop-blur-lg border-r-4">
        <Logo />
        <div className="h-screen flex justify-center items-center">
          <Signup />
        </div>
      </div>
    </div>
  );
}

export default SignupPage;