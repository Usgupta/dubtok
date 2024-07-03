/** @type {import('tailwindcss').Config} */
const flowbite = require("flowbite-react/tailwind");
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
    flowbite.content(),
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      colors:{
        "blue": "#97C7FF",
        "darkgrey": "#D9D9D9",
        "lightgrey": '#EBEBEB',
        "purple": "#A2A8FF",
        "black": '#000000',
        "red":"#fe2c55",
      },
      fontFamily:{
          default: ['Roboto', 'sans-serif'],
          poppins: ["Poppins", 'sans-serif'],
      }
    },
    
  },
  plugins: [ flowbite.plugin(),],
};
