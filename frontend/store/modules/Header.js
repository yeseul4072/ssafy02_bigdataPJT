export default ({
  state: {
    token: sessionStorage.getItem('token'),
    overlay: false
  },
  getters: {
    getToken (state) {
      return state.token
    },
    getOverlay (state) {
      return state.overlay
    }
  },
  mutations: {
    setToken (state, payload) {
      state.token = payload
      sessionStorage.setItem('token', payload)
    },
    setOverlay (state, payload) {
      state.overlay = payload
    }
  },
  actions: {
  }
})
