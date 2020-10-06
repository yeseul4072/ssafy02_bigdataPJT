<template>
  <v-img
    class="hl-logo"
    :src="require('@/assets/logo.png')"
    contain
    style="max-height:70px;"
    @click="goToRoot"
  />
</template>

<script>
export default {
  methods: {
    goToRoot () {
      this.$store.commit('setIsBoard', false)
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
.hl-logo:hover{
  cursor: pointer;
}
</style>
