import { faJoint } from '@fortawesome/free-solid-svg-icons'

export default {
  /*
  ** Nuxt rendering mode
  ** See https://nuxtjs.org/api/configuration-mode
  */
  mode: 'spa',
  /*
  ** Nuxt target
  ** See https://nuxtjs.org/api/configuration-target
  */
  target: 'static',
  /*
  ** Headers of the page
  ** See https://nuxtjs.org/api/configuration-head
  */
  head: {
    title: '어린이ZIP - No.1 어린이집 추천 플랫폼',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    script: [
      {
        src: 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js',
        type: 'text/javascript'
      },
      {
        // src: 'http://dmaps.daum.net/map_js_init/postcode.v2.js',
        src: 'https://ssl.daumcdn.net/dmaps/map_js_init/postcode.v2.js',
        type: 'text/javascript'
      },
      {
        src: 'https://dapi.kakao.com/v2/maps/sdk.js?appkey=dff523ff715cfa66c3e0461e1f477834&autoload=false',
        type: 'text/javascript'
      },
      {
        src: 'https://dapi.kakao.com/v2/maps/sdk.js?appkey=dff523ff715cfa66c3e0461e1f477834&libraries=services',
        type: 'text/javascript'
      }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Global CSS
  */
  css: [
  ],
  /*
  ** Plugins to load before mounting the App
  ** https://nuxtjs.org/guide/plugins
  */
  plugins: [
    '@/plugins/fontawesome.js',
    '@/plugins/vuetify.js'
  ],
  /*
  ** Auto import components
  ** See https://nuxtjs.org/api/configuration-components
  */
  components: true,
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
    '@nuxtjs/vuetify',
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module'
  ],
  vuetify: {
    /* module options */
  },
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios'
  ],
  /*
  ** Axios module configuration
  ** See https://axios.nuxtjs.org/options
  */
  axios: {},
  /*
  ** Build configuration
  ** See https://nuxtjs.org/api/configuration-build/
  */
  build: {
    transpile: ['vue-clamp', 'resize-detector']
  }
}
