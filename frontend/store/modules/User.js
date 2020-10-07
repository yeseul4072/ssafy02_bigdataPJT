export default ({
  state: {
    isLogin: sessionStorage.getItem('isLogin'),
    user: sessionStorage.getItem('user')

  },
  getters: {
    isLogin (state) {
      return state.isLogin
    },
    getUser (state) {
      if (state.user) {
        return JSON.parse(state.user)
      } else {
        return null
      }
    }
  },
  mutations: {
    setIsLogin (state, payload) {
      state.isLogin = payload
      sessionStorage.setItem('isLogin', payload)
    },
    setUser (state, payload) {
      state.user = JSON.stringify(payload)
      sessionStorage.setItem('user', state.user)
    }
  },
  actions: {
  }
})
