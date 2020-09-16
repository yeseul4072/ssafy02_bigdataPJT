<template>
  <div class="HomeWrapper">
    This is homeThis is homeThis is homeThis is homeThis is homeThis is homeThis is homeThis is homeThis is homeThis is homeThis is homeThis is homeThis is homeThis is homeThis is homeThis is home
    <div @click="changelogin">
      로그인상태변경
    </div>
    <div v-if="isLogin">
      로그인상태
    </div>
    <div v-else>
      로그아웃상태
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
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
  height:2000px;
}
</style>
