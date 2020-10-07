import Vue from 'vue'
import axios from 'axios'
import store from '@/store/modules/Header.js'

export default new Vue({
  computed: {
    token () {
      return store.state.token
    },
    axios () {
      return axios.create({
        baseURL: 'http://localhost:8800',
        headers: {
          Authorization: this.token ? this.token : '',
          'Content-type': 'application/json'
        }
      })
    }
  }
})
