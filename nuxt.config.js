export default {
  mode: 'universal',
  generate: {
    dir: 'public'
  },
  /*
   ** Headers of the page
   */
  head: {
    title: 'Milestone Analysis',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: './favicon.ico' }]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: ['vuetify/dist/vuetify.css'],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [],

  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    '@nuxtjs/vuetify'
    // Doc: https://github.com/nuxt-community/eslint-module
    // '@nuxtjs/eslint-module'
  ],
  router: {
    base: '/reports/milestone/',
    extendRoutes(routes, resolve) {
      const route = routes.find((r) => r.path === '/')
      route.redirect = '/Overview'
    }
  },
  styleResources: {},
  /*
   ** Nuxt.js modules
   */
  modules: [],

  /*
   ** Build configuration
   */
  build: {
    analyze: false,
    extractCSS: false,
    extend(config, ctx) {}
  }
}
