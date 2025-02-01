/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    '../templates/**/*.html', // Adjust this path to scan your Django templates
    '../templates/*.html', // Adjust this path to scan your Django templates
    '../static/assets/js/*.js', // If you have JavaScript files using Tailwind
    '../static/assets/css/*.css', // If you have other CSS files that might use Tailwind classes
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};


