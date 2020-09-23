<template>
  <div class="board-detail-box">
    <div class="board-detail-title">
      <v-html
        class="title-hover"
        style="font-size:1.2rem; width:80% !important;"
      >
        <a
          href
          style="text-decoration:none; color:#555555;"
          v-html="title.replace(text, '<strong>'+ text + '</strong>')"
        >
          {{ title }}
        </a>
      </v-html>
      <div
        style="text-align: right !important;
            width:20%;"
      >
        <v-icon style="font-size:13px; color:#999999;">
          mdi-comment-text-multiple-outline
        </v-icon>
        <span style="font-size:13px; color:#999999;">
          {{ boardCount }}
        </span>
      </div>
    </div>
    <div style="margin-bottom:20px !important;">
      <v-text
        style="font-size:0.9rem; color:#555555;"
        v-html="content.replace(text, '<strong>'+ text + '</strong>')"
      >
        {{ content }}
      </v-text>
    </div>
  </div>
</template>

<script>
export default {
  props: ['id', 'title', 'content', 'boardCount', 'text']
}
</script>

<style scoped>
.board-detail-box{
    margin-top: 20px;
    margin-right: 20px;
    border-bottom: 1px solid #eee;
}
.board-detail-title{
    display: flex;
    width: 100%;
}
.title-hover:hover{
    text-decoration: underline;
}
</style>
