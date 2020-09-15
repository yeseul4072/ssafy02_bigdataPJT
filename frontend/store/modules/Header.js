export default ({
  state: () => ({
    isBoard: false
  }),
  getters: {
    isBoard (state) {
      return state.isBoard
    }
  },
  mutations: {
    setIsBoard (state, payload) {
      state.isBoard = payload
    }
  },
  actions: {
  }
})
