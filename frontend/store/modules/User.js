export default ({
  state: () => ({
    isLogin: false
  }),
  getters: {
    isLogin (state) {
      return state.isLogin
    }
  },
  mutations: {
    setIsLogin (state, payload) {
      state.isLogin = payload
    }
  },
  actions: {
  }
})
