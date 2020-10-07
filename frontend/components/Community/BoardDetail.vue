<template>
  <div class="bd-body-container">
    <v-list three-line>
      <v-list-item>
        <v-list-item-avatar>
          <v-img
            v-if="article.user.profile_image != null"
            :src="article.user.profile_image"
          />
          <v-img
            v-else
            :src="require('@/assets/default_profile.png')"
          />
        </v-list-item-avatar>
        <v-list-item-content>
          <v-col
            class="px-3 py-0"
            :cols="12"
            align="start"
          >
            <h3>
              <v-clamp
                :max-lines="1"
                ellipsis="..."
              >
                {{ article.title }}
              </v-clamp>
            </h3>
          </v-col>
          <v-list-item-subtitle>
            <v-col
              class="px-3 py-0"
              :cols="12"
              align="start"
            >
              <span>
                {{ article.user.nickname | filterWriter }}
              </span>
              <span style="margin-left:10px;">
                <v-icon class="vd-icon" color="primary">
                  mdi-comment-text-outline
                </v-icon>
                {{ article.comment_count }}
                <v-icon class="vd-icon pl-2" color="error">
                  mdi-thumb-up-outline
                </v-icon>
                {{ article.like_count }}
                <v-icon class="vd-icon pl-2">
                  mdi-eye
                </v-icon>
                {{ article.hit }}
              </span>
              <span style="margin-left:10px;">
                {{ article.created_at | diffDate }}
              </span>
            </v-col>
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
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
  props: ['article'],
  data () {
    return {
      line: 1
    }
  },
  mounted () {

  }
}
</script>

<style scoped>
.bd-body-container{
  padding-top: 4px;
  padding-left:20px;
  padding-right: 20px;
}
.bd-body-container:hover {
  box-shadow: 0 3px 8px 0 rgba(0,0,0,.08), 0 0 1px 0 rgba(0,0,0,.44);
  cursor:pointer;
}
.divider {
  border-bottom:2px solid #f5f5f5;
  width: 100%;
  border-width: 1px;
}
.vd-icon{
  font-size:16px;
  padding-bottom: 4px;
}
</style>
