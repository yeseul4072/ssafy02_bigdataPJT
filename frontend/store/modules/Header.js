export default ({
  state: {
    token: sessionStorage.getItem('token')
  },
  getters: {
    getToken (state) {
      return state.token
    }
  },
  mutations: {
    setToken (state, payload) {
      state.token = payload
      sessionStorage.setItem('token', payload)
    }
  },
  actions: {
  }
})
