<template>
  <div @click="goArticle">
    <BoardDetail :article="board" />
  </div>
</template>

<script>
import BoardDetail from '@/components/Community/BoardDetail.vue'
export default {
  components: { BoardDetail },
  props: ['board'],
  data () {
    return {

    }
  },
  mounted () {
  },
  methods: {
    goArticle () {
      this.$router.push(`/board/${this.board.board.id}?id=${this.board.id}`)
    }
  }
}
</script>

<style scoped>

</style>
