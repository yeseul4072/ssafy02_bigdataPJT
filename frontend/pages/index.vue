<template>
  <div class="body-container">
    <section class="section-main">
      <ul class="main-right-nav">
        <li
          v-for="(item, index) in indexList"
          :key="index"
        >
          <v-hover v-slot:default="{ hover }">
            <v-tab
              :ripple="false"
              class="index-v-tab"
              @click="goto(item.goto); selected=index"
            >
              <v-tooltip
                left
                color="#ff5faa"
              >
                <template v-slot:activator="{ on, attrs }">
                  <div
                    v-bind="attrs"
                    style="height: 50px;
                          display: flex;
                          align-items: center;"
                    v-on="on"
                  >
                    <v-icon v-if="hover || selected == index" class="l1_icon_active">
                      {{ item.indexLogo }}
                    </v-icon>
                    <v-icon v-else class="l1_icon_none">
                      mdi-circle
                    </v-icon>
                  </div>
                </template>
                <span>{{ item.text }}</span>
              </v-tooltip>
            </v-tab>
          </v-hover>
        </li>
      </ul>
    </section>
    <div class="launcher_item">
      <v-flex>
        <div id="we">
          <We />
        </div>
        <div id="real">
          <UsePlatform />
        </div>
        <div id="review">
          <Real />
        </div>
        <div id="main">
          <Main />
        </div>
      </v-flex>
    </div>
    <ScrollUp :component-name="`#we`" />
  </div>
</template>

<script>

import We from '@/components/Launcher/We.vue'
import UsePlatform from '@/components/Launcher/UsePlatform.vue'
import Real from '@/components/Launcher/Real.vue'
import Main from '@/components/Launcher/Main.vue'
import ScrollUp from '@/components/Common/Utils/ScrollUp.vue'

export default {
  components: { We, UsePlatform, Real, Main, ScrollUp },
  data () {
    return {
      selected: 0,
      hidden: false,
      indexList: [
        {
          goto: '#we',
          text: '메인',
          indexLogo: 'mdi-home-variant-outline'
        },
        {
          goto: '#real',
          text: '어린이ZIP은 지금',
          indexLogo: 'mdi-trophy-outline'
        },
        {
          goto: '#review',
          text: '리뷰',
          indexLogo: 'mdi-comment-quote-outline'
        },
        {
          goto: '#main',
          text: '메인 페이지',
          indexLogo: 'mdi-motion-play-outline'
        }
      ]
    }
  },
  mounted () {
    document.addEventListener('scroll', this.handleScroll)
  },
  methods: {
    handleScroll () {
      const allHeight = document.documentElement.scrollHeight
      const clientHeight = document.documentElement.clientHeight
      const height = allHeight - clientHeight
      const curPosition = window.scrollY

      if (curPosition === 0) {
        this.selected = 0
      } else if (curPosition >= height) {
        this.selected = 3
      } else if (curPosition > height / 4 * 3) {
        this.selected = 2
      } else if (curPosition > height / 4 * 2) {
        this.selected = 1
      }
    }
  }
}
</script>

<style scoped>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.section-main{
  display: inline-block;
  position: fixed !important;
  z-index: 100;
  top: 40%;
  right: 0%;
}

ul{
   list-style:none;
}

.item{
  font-size: 12px !important;
}

.l1_icon_active{
  padding-left: 10px;
  font-size: 27px;
  color: #ff5faa;
}

.l1_icon_none{
  padding-left: 10px;
  font-size: 6px;
  color: #b9b9b9;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
