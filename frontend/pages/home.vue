<template>
  <div class="HomeWrapper">
    <search-bar />
    <div v-if="isLogin">
      로그인상태
    </div>
    <v-container fluid>
      <v-row style="height:70vh;">
        <v-col cols="12" style="border: 1px solid black;">
          <h4>이런 어린이집 어때요?</h4>
        </v-col>
      </v-row>
      <v-row style="height:70vh;">
        <v-col cols="6" style="border: 1px solid black;">
          <h4>우리 아이</h4>
        </v-col>
        <v-col cols="6" style="border: 1px solid black;">
          <h4>지금 뜨는 리뷰</h4>
        </v-col>
      </v-row>
    </v-container>
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
  font-weight: 600;
  font-size: 1.2vw;
  }
</style>
