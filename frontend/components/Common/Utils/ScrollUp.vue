<template>
  <div class="index-floting-button">
    <transition name="fade">
      <v-btn
        v-if="hidden"
        absolute
        dark
        fab
        top
        right
        color="#00BF8C"
        @click="goto(componentName);"
      >
        <v-icon>mdi-arrow-up</v-icon>
      </v-btn>
    </transition>
  </div>
</template>

<script>
export default {
  props: ['componentName'],
  data () {
    return {
      hidden: false
    }
  },
  mounted () {
    document.addEventListener('scroll', this.handleScroll)
  },
  methods: {
    goto (target) {
      this.$vuetify.goTo('#we', {
        duration: 1000,
        offset: 100,
        easing: 'easeInOutCubic'
      })
    },
    handleScroll () {
      this.hidden = window.scrollY !== 0
    }
  }
}
</script>

<style scoped>
.index-floting-button{
  display: inline-block;
  position: fixed !important;
  z-index: 100;
  top: 95%;
  right: 0%;
}
</style>
