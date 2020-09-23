<template>
  <div>
    <v-img
      :src="imageUrl"
      height="200"
    />
  </div>
</template>

<script>
export default {
  data () {
    return {
      imageUrl: ''
    }
  },
  created () {
    // imageUrl 들고오는 API..
    this.imageUrl = 'https://cdn2-www.familylife.com/wp-content/uploads/sites/51/2018/04/what-makes-a-child-truly-great-1040x326-1024x321.jpg'
  }
}
</script>

<style>

</style>
