<template>
  <div class="review-body">
    <v-list-item>
      <v-list-item-avatar>
        <v-img
          :src="'https://www.iconfinder.com/data/icons/female-avatars-vol-1/256/female-portrait-avatar-profile-woman-sexy-afro-2-512.png'"
        />
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title>{{ review.user.nickname }}</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title>{{ review.content }}</v-list-item-title>
        <v-list-item-subtitle>{{ review.created_at | diffDate }}</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
  </div>
</template>

<script>
export default {
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
    }
  },
  props: ['review'],
  mounted () {
  }
}
</script>

<style scoped>
.review-body{
    border-left: 1px solid rgb(236, 236, 236);
}
</style>
