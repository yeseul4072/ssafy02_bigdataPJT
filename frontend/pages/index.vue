<template>
  <div class="body-container">
    <section class="section-main">
      <ul class="main-right-nav">
        <li class="item item-we" data-scroll="main-we">
          <v-hover v-slot:default="{ hover }">
            <v-tab @click="goto('#we')">
              <v-tooltip left>
                <template v-slot:activator="{ on, attrs }">
                  <div
                    v-bind="attrs"
                    v-on="on"
                  >
                    <v-icon v-show="hover">
                      mdi-checkbox-marked-circle-outline
                    </v-icon>
                    <v-icon v-show="!hover">
                      mdi-circle
                    </v-icon>
                  </div>
                </template>
                <span>메인</span>
              </v-tooltip>
            </v-tab>
          </v-hover>
        </li>
        <li class="item item-real" data-scroll="main-real">
          <v-hover v-slot:default="{ hover }">
            <v-tab @click="goto('#real')">
              <v-tooltip left>
                <template v-slot:activator="{ on, attrs }">
                  <div
                    v-bind="attrs"
                    v-on="on"
                  >
                    <v-icon v-show="hover">
                      mdi-checkbox-marked-circle-outline
                    </v-icon>
                    <v-icon v-show="!hover">
                      mdi-circle
                    </v-icon>
                  </div>
                </template>
                <span>어린이ZIP은 지금</span>
              </v-tooltip>
            </v-tab>
          </v-hover>
        </li>
        <li class="item item-review" data-scroll="main-review">
          <v-hover v-slot:default="{ hover }">
            <v-tab @click="goto('#review')">
              <v-tooltip left>
                <template v-slot:activator="{ on, attrs }">
                  <div
                    v-bind="attrs"
                    v-on="on"
                  >
                    <v-icon v-show="hover">
                      mdi-checkbox-marked-circle-outline
                    </v-icon>
                    <v-icon v-show="!hover">
                      mdi-circle
                    </v-icon>
                  </div>
                </template>
                <span>리뷰</span>
              </v-tooltip>
            </v-tab>
          </v-hover>
        </li>
        <li class="item item-main" data-scroll="main-main">
          <v-hover v-slot:default="{ hover }">
            <v-tab @click="goto('#main')">
              <v-tooltip left>
                <template v-slot:activator="{ on, attrs }">
                  <div
                    v-bind="attrs"
                    v-on="on"
                  >
                    <v-icon v-show="hover">
                      mdi-checkbox-marked-circle-outline
                    </v-icon>
                    <v-icon v-show="!hover">
                      mdi-circle
                    </v-icon>
                  </div>
                </template>
                <span>메인 페이지</span>
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
  </div>
</template>

<script>

import We from '@/components/Launcher/We.vue'
import UsePlatform from '@/components/Launcher/UsePlatform.vue'
import Real from '@/components/Launcher/Real.vue'
import Main from '@/components/Launcher/Main.vue'

export default {
  components: { We, UsePlatform, Real, Main },
  methods: {
    goto (target) {
      this.$vuetify.goTo(target, {
        duration: 300,
        offset: 100,
        easing: 'easeInOutCubic'
      })
    }
  }
}
</script>

<style>
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
  position: fixed;
  z-index: 100;
  top: 40%;
  right: 0%;
}

.dp-2{
  color: #F257A0;
}

.dp-1{
  font-size:17px;
}

ul{
   list-style:none;
}

li{
  margin-top: 25px;
  margin-bottom: 25px;
}

.item{
  font-size: 12px !important;
}
</style>
