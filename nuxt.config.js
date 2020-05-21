export default {
  mode: 'universal',
  /*
   ** Headers of the page
   */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: ['@assets/scss/main.scss'],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module',
    // Doc: https://github.com/nuxt-community/nuxt-tailwindcss
    '@nuxtjs/tailwindcss'
  ],styleResources: {
    scss: [
      './assets/scss/variables.scss',
      './assets/scss/fluid-fonts.scss',
      './assets/scss/fluid-spacing.scss',
    ],
  },
  /*
   ** Nuxt.js modules
   */
  modules: [
    'nuxt-purgecss',
    '@nuxtjs/style-resources',],

  purgeCSS: {
    mode: 'postcss',
  },
  /*
   ** Build configuration
   */
  build: {
    analyze: false,
    extractCSS: false,
    extend(config, ctx) {
    },
    postcss: {
      plugins: {
        tailwindcss: './tailwind.config.js',
      },
    }
  }
}
