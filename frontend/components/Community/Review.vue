<template>
  <div class="review-body">
    <v-list-item>
      <v-list-item-avatar>
        <v-img
          :src="'https://www.iconfinder.com/data/icons/female-avatars-vol-1/256/female-portrait-avatar-profile-woman-sexy-afro-2-512.png'"
        />
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title>유저 이름</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title>댓글 내용</v-list-item-title>
        <v-list-item-subtitle>2020.12.12 12:12</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.review-body{
    border-left: 1px solid rgb(236, 236, 236);
}
</style>
