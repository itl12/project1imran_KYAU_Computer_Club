/** @type {import('tailwindcss').Config} */
module.exports = {
  content:
          [
            '../templates/**/*.html',
            '../noticeapp/**/*.html',
            '../galleryapp/**/*.html',
            '../students/**/*.html',
            '../Faculty_app/**/*.html',
            '../Alumni_app/**/*.html',
            'src/js/**/*.js',
          
          ],

  important : true, 
  theme: {
    extend: {
      screens: {
        'b-lg': '992px',
        // => @media (min-width: 992px) { ... } match with bootstrap lg
      },
    },
    
  },
  plugins: [
    function ({ addUtilities }) {
      addUtilities({
        '.collapse': {
          visibility: 'visible',   // Overriden by me to avoid conflick with bootstrap
        },
      });
    },
  ],
}

