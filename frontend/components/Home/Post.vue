<template>
  <div>
    <BoardDetail :board="board" style="1px solid gray !important" />
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
  }
}
</script>

<style scoped>

</style>
