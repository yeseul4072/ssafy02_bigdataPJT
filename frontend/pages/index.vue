<template>
  <div class="container-fluid">
    <div class="launcher_index">
      <v-ul class="main-right-nav">
        <li class="item item-main" data-scroll="main-banner">
          <v-tab @click="goto('#infomation')">
            <span style="font-size:16px">Infomation</span>
          </v-tab>
        </li>
        <li class="item item-main" data-scroll="main-banner">
          <v-tab @click="goto('#helped2')">
            <span style="font-size:16px">UsePlatform</span>
          </v-tab>
        </li>
        <li class="item item-main" data-scroll="main-banner">
          <v-tab @click="goto('#helped3')">
            <span style="font-size:16px">Title3</span>
          </v-tab>
        </li>
        <li class="item item-main" data-scroll="main-banner">
          <v-tab @click="goto('#helped4')">
            <span style="font-size:16px">Title4</span>
          </v-tab>
        </li>
        <li class="item item-main" data-scroll="main-banner">
          <v-tab @click="goto('#helped5')">
            <span style="font-size:16px">Title5</span>
          </v-tab>
        </li>
      </v-ul>
    </div>
    <div class="launcher_item">
      <v-flex>
        <div id="infomation">
          <Infomation />
        </div>
        <div id="helped2">
          <UsePlatform />
        </div>
        <div id="helped3">
          <title3 />
        </div>
        <div id="helped4">
          <title4 />
        </div>
        <div id="helped5">
          <title5 />
        </div>
      </v-flex>
    </div>
  </div>
</template>

<script>

import Infomation from '@/components/Launcher/Infomation.vue'
import UsePlatform from '@/components/Launcher/UsePlatform.vue'
import Title3 from '@/components/Launcher/Title3.vue'
import Title4 from '@/components/Launcher/Title4.vue'
import Title5 from '@/components/Launcher/Title5.vue'

export default {
  components: { Infomation, UsePlatform, Title3, Title4, Title5 },
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

.launcher_index{
  display: inline-block;
  position: fixed;
  z-index: 100;
  top: 40%;
  right: 0%;
}
</style>
