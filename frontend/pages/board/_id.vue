<template>
  <div>
    <!-- 배너 사진 -->
    <BannerImage />

    <!-- 내용물 -->
    <div class="container">
      <v-card
        outlined
        rounded="0"
        :min-width="500"
      >
        <v-list-item>
          <v-row
            justify="center"
            class="pa-5"
          >
            <v-col
              class="py-0"
              :cols="6"
            >
              <v-list-item-title class="headline" style="font-weight:800;">
                {{ boardTitle }}
              </v-list-item-title>
            </v-col>
            <v-col
              class="py-0"
              :cols="6"
            >
              <v-row
                align="end"
                justify="end"
                class="pr-3"
              />
            </v-col>
            <div class="border_black py-2" />
          </v-row>
        </v-list-item>
        <v-list-item class="px-10">
          <v-list-item-content class="pa-0">
            <v-list-item-title><h3>{{ articleTitle }}</h3></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item class="px-8">
          <v-list-item-avatar>
            <v-img
              :src="'https://www.iconfinder.com/data/icons/female-avatars-vol-1/256/female-portrait-avatar-profile-woman-sexy-afro-2-512.png'"
            />
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title>{{ user.nickname }}</v-list-item-title>
          </v-list-item-content>
          <v-list-item-icon class="pr-1">
            조회 7 | 추천 {{ likeCount }} | {{ created | diffDate }}
          </v-list-item-icon>
        </v-list-item>
        <v-row>
          <v-col
            align="center"
            class="pa-0"
          >
            <div class="border_gray" />
          </v-col>
        </v-row>
        <v-row class="px-9 pa-3">
          <v-col>
            {{ articleContent }}
          </v-col>
        </v-row>
        <v-list-item class="px-8">
          <v-btn
            small
            rounded
            outlined
            color="rgb(236, 236, 236)"
            dark
            @click="goToBack"
          >
            <span
              style="color:#212121;"
            >
              목록보기
            </span>
          </v-btn>
          <v-list-item-content />
          <v-list-item-icon class="pr-1">
            <v-btn
              rounded
              outlined
              color="rgb(236, 236, 236)"
              dark
              @click="likeArticle"
            >
              <v-icon
                v-if="!likeYn"
                class="mr-2"
                color="rgb(143, 143, 143)"
                dark
                style="font-size:20px;"
              >
                mdi-thumb-up-outline
              </v-icon>
              <v-icon
                v-else
                class="mr-2"
                color="blue"
                dark
                style="font-size:20px;"
              >
                mdi-thumb-up
              </v-icon>
              <span
                style="color:#212121;"
              >
                {{ likeCount }}
              </span>
            </v-btn>
          </v-list-item-icon>
        </v-list-item>
        <v-row>
          <v-col
            align="center"
            class="pt-5 px-0"
          >
            <div class="border_gray" />
          </v-col>
        </v-row>
        <div
          class="pa-8"
        >
          <v-card
            outlined
            rounded="0"
            :min-width="500"
          >
            <v-list-item class="px-4 pt-2">
              <v-list-item-avatar>
                <v-img
                  :src="'https://www.iconfinder.com/data/icons/female-avatars-vol-1/256/female-portrait-avatar-profile-woman-sexy-afro-2-512.png'"
                />
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title><h4>{{ profile.nickname }}</h4></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-textarea
              v-model="text"
              class="px-4 ma-0"
              rows="1"
              flat
              solo
              no-resize
              height="100"
              label="이 곳에 작성해주세요 :D"
              hide-details
            />
            <v-list-item class="px-8">
              <span
                style="color:orange;"
              >
                주제와 무관한 댓글, 악플은 삭제 될 수 있습니다.
              </span>
              <v-list-item-content />
              <v-list-item-icon class="pr-1">
                <v-btn
                  rounded
                  outlined
                  color="rgb(236, 236, 236)"
                  dark
                  @click="writeComment"
                >
                  <span
                    style="color:#212121;"
                  >
                    등록
                  </span>
                </v-btn>
              </v-list-item-icon>
            </v-list-item>
          </v-card>
        </div>
        <v-list-item class="px-10">
          <v-list-item-content class="pa-0">
            <v-list-item-title>
              <v-icon
                style="font-size:18px;"
              >
                mdi-comment-outline
              </v-icon><span style="font-size:16px; font-weight:700;">&nbsp;댓글 <span style="font-size:16px; color:orange;">{{ comments.length }}</span>개</span>
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-row>
          <v-col
            align="center"
            class="pa-0"
          >
            <div class="border_gray" />
          </v-col>
        </v-row>
        <div
          class="mb-10"
          style="overflow-y: auto; height: 400px;"
        >
          <div
            v-for="(item, index) in comments"
            :key="index"
            class="px-8 py-1"
          >
            <Review :review="item" />
          </div>
        </div>
      </v-card>
    </div>
  </div>
</template>

<script>
import http from '@/util/http_common.js'
import BannerImage from '@/components/Community/Banner.vue'
import Review from '@/components/Community/Review.vue'

export default {
  components: { BannerImage, Review },
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
  asyncData ({ params, query }) {
    return http.axios.get(`/community/${params.id}/article/${query.id}/`)
      .then(({ data }) => {
        return {
          boardId: data.board_id,
          boardTitle: data.board_name,
          commentCount: data.comment_count,
          comments: data.comments.reverse(),
          articleId: data.id,
          likeCount: data.like_count,
          likeYn: data.like_yn,
          user: data.user,
          articleTitle: data.title,
          articleContent: data.content,
          created: data.created_at
        }
      })
  },
  data () {
    return {
      text: '',
      profile: {
        id: 0,
        profile_image: '',
        last_login: '',
        is_superuser: false,
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        is_staff: false,
        is_active: true,
        date_joined: '',
        latitude: 0,
        longitude: 0,
        address: '',
        nickname: '',
        is_director: false,
        kindergarten_id: 0,
        groups: [],
        user_permissions: []
      }
    }
  },
  mounted () {
    http.axios.get('/rest-auth/user/profile/')
      .then(({ data }) => {
        this.profile = data
      })
  },
  methods: {
    goToBack () {
      this.$router.go(-1)
    },
    likeArticle () {
      http.axios.post(`/community/article/${this.articleId}/like/`)
        .then(({ data }) => {
          this.likeYn = !this.likeYn
          this.likeCount = this.likeYn ? this.likeCount + 1 : this.likeCount - 1
        })
    },
    writeComment () {
      http.axios.post(`/community/${this.boardId}/article/${this.articleId}/`, {
        content: this.text
      }).then(({ data }) => {
        http.axios.get(`/community/${this.boardId}/article/${this.articleId}/`)
          .then(({ data }) => {
            this.boardId = data.board_id
            this.boardTitle = data.board_name
            this.commentCount = data.comment_count
            this.comments = data.comments.reverse()
            this.articleId = data.id
            this.likeCount = data.like_count
            this.likeYn = data.like_yn
            this.user = data.user
            this.varticleTitle = data.title
            this.articleContent = data.content
            this.created = data.created_at
            this.text = ''
          })
      })
    }
  }
}
</script>

<style scoped>
.border_black{
  width: 98%;
  border-bottom: 1px solid;
}

.border_gray{
  width: 92%;
  border-bottom: 1px solid rgb(236, 236, 236);
}

</style>
