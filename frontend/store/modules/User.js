export default ({
  state: {
    isLogin: sessionStorage.getItem('isLogin')
  },
  getters: {
    isLogin (state) {
      return state.isLogin
    }
  },
  mutations: {
    setIsLogin (state, payload) {
      state.isLogin = payload
      sessionStorage.setItem('isLogin', payload)
    }
  },
  actions: {
  }
})
