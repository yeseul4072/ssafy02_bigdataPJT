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
<<<<<<< HEAD
        baseURL: 'https://childrenzip.site/api',
=======
        baseURL: 'http://j3a111.p.ssafy.io:8000',
>>>>>>> ced6f5026ae4b166e1aadd7c32d6a073c6b0b098
        headers: {
          Authorization: this.token ? this.token : '',
          'Content-type': 'application/json'
        }
      })
    },
    formAxios () {
      return axios.create({
<<<<<<< HEAD
        baseURL: 'https://childrenzip.site/api',
=======
        baseURL: 'http://j3a111.p.ssafy.io:8000',
>>>>>>> ced6f5026ae4b166e1aadd7c32d6a073c6b0b098
        headers: {
          Authorization: this.token ? this.token : '',
          'Content-Type': 'multipart/form-data'
        }
      })
    }
  }
})
