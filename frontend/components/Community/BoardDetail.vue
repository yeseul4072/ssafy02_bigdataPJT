<template>
  <div class="bd-body-container">
    <v-row>
      <v-col
        class="py-1"
        :cols="12"
        align="start"
      >
        <h3>
          <v-clamp
            autoresize
            :max-lines="1"
            ellipsis="..."
          >
            {{ board.title }}
          </v-clamp>
        </h3>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        class="py-0"
        :cols="1"
      >
        {{ board.dateTime | diffDate }}
      </v-col>
      <v-col
        class="py-0"
        align="start"
        :cols="2"
      >
        <v-icon class="vd-icon" color="blue">
          mdi-comment-text-outline
        </v-icon>
        {{ board.boardCount }}
        <v-icon class="vd-icon" color="pink">
          mdi-thumb-up-outline
        </v-icon>
        {{ board.boardCount }}
      </v-col>
      <v-col
        class="py-0"
        :cols="9"
        align="end"
      >
        {{ board.writer | filterWriter }}
      </v-col>
    </v-row>
    <div class="divider" />
  </div>
</template>

<script>
import VClamp from 'vue-clamp'

export default {
  components: {
    VClamp
  },
  filters: {
    diffDate (val) {
      let diff = (new Date() - new Date(val)) / 1000
      if (diff < 60) { return '방금 전' }
      diff /= 60
      if (diff < 60) { return parseInt(diff) + '분 전' }

      diff /= 60
      if (diff < 24) { return parseInt(diff) + '시간 전' }

      diff /= 24
      if (diff < 7) { return parseInt(diff) + '일 전' }
      if (diff < 30) { return parseInt(diff / 7) + '주 전' }
      if (diff < 365) { return parseInt(diff / 30) + '달 전' }
      return parseInt(diff / 365) + '년 전'
    },
    filterWriter (val) {
      return `by ${val}`
    }
  },
  props: ['board'],
  data () {
    return {
      line: 1
    }
  }
}
</script>

<style scoped>
.bd-body-container{
  padding-top: 20px;
  padding-left:20px;
  padding-right: 20px;
}
.divider {
  margin-top: 20px;
  border-bottom:1px solid #f5f5f5;
  width: 100%;
  border-width: 1px;
}
.vd-icon{
  font-size:16px;
  padding-bottom: 4px;
}
</style>
