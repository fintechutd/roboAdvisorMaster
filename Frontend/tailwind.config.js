<<<<<<<< HEAD:Frontend/robo-advisor/src/tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/*.{js,jsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
========
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundSize: {
        'size-200': '200% 200%',
      },
      backgroundPosition: {
        'pos-0': '0% 0%',
        'pos-100': '100% 100%',
      }
    },
  },
  plugins: [],
>>>>>>>> sourish:Frontend/tailwind.config.js
}