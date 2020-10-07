<template>
  <div>
    <v-app>
      <common-header v-if="notMain" />
      <!-- <v-expand-transition > -->
      <nav-board
        v-if="notMain"
        ref="test"
        :class="{pt150 : notMain}"
        @child-event="checkHeight"
      />
      <!-- </v-expand-transition> -->
      <div :style="{'height' : (boardHeight) + 'px' }" />
      <Nuxt :key="$route.fullPath" />
      <common-footer v-if="notMain" />
    </v-app>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import CommonHeader from '@/components/Common/Header.vue'
import CommonFooter from '@/components/Common/Footer.vue'
import NavBoard from '@/components/Common/Header/NavBoard.vue'

export default {
  components: { CommonHeader, CommonFooter, NavBoard },
  data () {
    return {
      boardHeight: 0
    }
  },
  computed: {
    notMain () {
      // ignore = ['/', '/']
      return this.$route.path !== '/' && this.$route.path !== '/login' && this.$route.path.indexOf('/signup')
    },
    ...mapGetters(['isBoard'])
  },
  methods: {
    checkHeight (height) {
      this.boardHeight = height
    }
  }
}
</script>

<style>
@import url('https://cdn.rawgit.com/innks/NanumSquareRound/master/nanumsquareround.min.css');
* { font-family: 'NanumSquareRound',sans-serif; }

html {
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}

.button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}

.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}

.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}

.button--grey:hover {
  color: #fff;
  background-color: #35495e;
}

.pt150 {
  padding-top: 125px !important;
  padding-left:0;
  padding-right:0;
}
</style>
