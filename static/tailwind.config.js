module.exports = {
  purge: {
    enabled: true,
    content: ['../templates/**/*.html']
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},

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
    },
    fontFamily: {
      welcome: ['Jaldi'],
      title: ['Roboto Slab'],
      body: ['Lato']
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
