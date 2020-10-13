<template>
  <div class="review-body">
    <v-list-item>
      <v-list-item-avatar>
        <v-img
          v-if="review.user.profile_image != null"
          :src="review.user.profile_image"
        />
        <v-img
          v-else
          :src="require('@/assets/default_profile.png')"
        />
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title>{{ review.user.nickname }}</v-list-item-title>
      </v-list-item-content>
      <v-list-item-action v-if="review.user.id == profile.id">
        <v-btn
          depressed
          small
          color="error"
          @click="deleteComment(review.id)"
        >
          삭제
        </v-btn>
      </v-list-item-action>
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
  props: ['review', 'profile'],
  data () {
    return {
    }
  },
  mounted () {
  },
  methods: {
    deleteComment (id) {
      this.$emit('delete-comment', id)
    }
  }
}
</script>

<style scoped>
.review-body{
    border-left: 1px solid rgb(236, 236, 236);
}
</style>
