<template>
  <div class="HomeWrapper">
    <search-bar />
    <div v-if="isLogin">
      로그인상태
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import SearchBar from '@/components/Home/Search.vue'

export default {
  components: {
    SearchBar
  },
  data () {
    return {

    }
  },
  computed: {
    ...mapGetters(['isLogin'])
  },
  watch: {

  },
  methods: {
    changelogin () {
      const cur = this.$store.state.User.isLogin
      this.$store.commit('setIsLogin', !cur)
    }
  }
}
</script>

<style scoed>
.HomeWrapper{
  margin: 0 8vw;
  min-height: 100vh;
  font-weight: 600;
  font-size: 1.2vw;
  }
</style>
