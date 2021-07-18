module.exports = {
  purge: {
    enabled: true,
    content: ['../templates/**/*.html']
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        gorm: {
          '100': '#1A535C'
        },
        glas: {
          '100': '#4ECDC4'
        },
        ban: {
          '100': '#F7FFF7'
        },
        rua: {
          '100': '#FF6B6B'
        },
        bui: {
          '100': '#FFE66D'
        },
        liath: {
          '100': '#504A5C'
        },
        gruama: {
          '100': '#E9E9EB'
        }
      },
      fontFamily: {
        title: ['Jaldi'],
        heading: ['Roboto Slab'],
        body: ['Lato']
      },

      backgroundSize: {
        'auto': 'auto',
        'cover': 'cover',
        'contain': 'contain',
        '50%': '50%',
        '40%': '40%',
      },
      backgroundImage: {
        'bird1': "url('https://res.cloudinary.com/the-mater-foundation/image/upload/v1626533136/bird_friend/wallpapers/bird1.png')",
        'bird2': "url('https://res.cloudinary.com/the-mater-foundation/image/upload/v1626533136/bird_friend/wallpapers/bird2.png')"
      },
      minHeight: {
        "screen/2": "50vh",
        "screen-less-nav": "calc(calc(var(--vh, 1vh) * 100) - 4rem)",
        "screen-less-both-nav": "calc(calc(var(--vh, 1vh) * 100) - 8rem)"
      },
      maxHeight: {
        "screen/2": "50vh",
        "screen-less-nav": "calc(calc(var(--vh, 1vh) * 100) - 4rem)"
      },
      width: {
        "screen/2": "calc(100vw / 2)",
      },
      screens: {
        'landscape': {'raw': '(orientation: landscape)'},
      },
    },
  },
  variants: {
    extend: {
      fontStyle: ['hover', 'focus'],
      opacity: ['disabled']
    },
  },
  plugins: [],
}
