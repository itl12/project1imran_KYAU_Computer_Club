/** @type {import('tailwindcss').Config} */
module.exports = {
  content:
          [
            '../templates/**/*.html',
            '../noticeapp/**/*.html',
            '../galleryapp/**/*.html',
            '../students/**/*.html',
            'src/js/**/*.js',
          
          ],

  important : true, 
  theme: {
    extend: {},
  },
  plugins: [],
}

