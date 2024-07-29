import { Link } from "react-router-dom";
import { useState } from "react";
import { toast } from 'react-toastify';
import { useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const navigate = useNavigate();

  const proceedLogin = (e) => {
    e.preventDefault();

    if (validate()) {
      fetch("http://localhost:3000/user/?email=" + email)
        .then((res) => res.json())
        .then((resp) => {
          if (Object.keys(resp).length === 0) {
            toast.error('Please Enter a Valid Email');
          } else {
            if (resp[0].password === password) {
              navigate('/TestHome');
            } else {
              toast.error('Please enter Valid Credentials');
            }
          }
        });
    }
  };

  const validate = () => {
    let result = true;
    return result;
  };

  return (
    <div className="max-w-md w-full">
      <div className="my-8">
        <h1 className="flex text-5xl font-semibold justify-center">
          Log In
        </h1>
      </div>
      <form className="outline-0" onSubmit={proceedLogin}>
        <div className="mb-4 flex justify-center">
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            name="user_email"
            placeholder="Email"
            className="transition-all duration-500 w-1/2 px-3 py-3 border-2 border-teal-800 rounded-xl bg-transparent backdrop-blur-lg focus:bg-teal-950 font-semibold focus:outline-none"
            required
          />
        </div>
        <div className="mb-4 flex justify-center">
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            name="user_password"
            placeholder="Password"
            className="transition-all duration-500 w-1/2 px-3 py-3 border-2 border-teal-800 rounded-xl bg-transparent backdrop-blur-lg focus:bg-teal-950 font-semibold focus:outline-none"
            required
          />
        </div>
        <div className="justify-center flex mb-1">
          <button
            type="submit"
            value="Send"
            className="px-3 py-2 rounded-2xl font-semibold text-white transition-all duration-500 bg-gradient-to-br to-cyan-600 via-cyan-800 from-teal-600 bg-size-200 bg-pos-0 hover:bg-pos-100"
          >
            Continue
          </button>
        </div>
        <p className="justify-center flex mb-1 font-semibold whitespace-pre">
          Don&apos;t have an account?{" "}
          <span>
            <Link to="pageSignup" className="text-teal-400 hover:underline">
              Sign up
            </Link>{" "}
          </span>
        </p>
        <p className="justify-center flex mb-1 font-semibold whitespace-pre">
          <span>
            <a href="" className="text-teal-400 hover:underline">Forgot your Password?</a>{" "}
          </span>
        </p>
      </form>
    </div>
  );
}

export default Login;