export default ({
  state: () => ({
    token: ''
  }),
  getters: {
    getToken (state) {
      return state.token
    }
  },
  mutations: {
    setToken (state, payload) {
      state.token = payload
    }
  },
  actions: {
  }
})
