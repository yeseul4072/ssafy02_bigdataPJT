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
        <v-row
          class="pt-3 pl-8"
          align="center"
          justify="center"
        >
          <v-col>
            <h2>{{ board_title }}</h2>
            <div class="border_gray pt-3 mr-8" />
          </v-col>
        </v-row>
        <div
          class="pt-3 pl-8"
        >
          <h3>
            제목
          </h3>
        </div>
        <div
          class="pl-8 pr-8"
        >
          <v-text-field
            v-model="title"
            class="pa-0"
            :rules="rules"
            hide-details="auto"
          />
        </div>
        <div
          class="pt-10 pl-8"
        >
          <h3>
            내용
          </h3>
        </div>
        <div
          class="pl-8 pr-8 pt-0 pb-4"
        >
          <v-card
            class="pl-3 pt-1"
            outlined
            rounded="0"
            :min-width="500"
          >
            <v-textarea
              v-model="content"
              class="mb-3"
              rows="1"
              flat
              solo
              no-resize
              height="300"
              label="이 곳에 작성해주세요 :D"
              hide-details
            />
          </v-card>
        </div>
        <v-row
          class="pl-11 pr-11 pt-0 pb-8"
        >
          <v-col
            class="pa-0"
          >
            <v-dialog
              v-model="dialog"
              persistent
              max-width="290"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  depressed
                  v-bind="attrs"
                  v-on="on"
                >
                  작성 취소
                </v-btn>
              </template>
              <v-card>
                <v-card-title class="headline">
                  확인
                </v-card-title>
                <v-card-text>정말 작성을 취소하시 겠습니까?</v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn
                    color="green darken-1"
                    text
                    @click="dialog = false"
                  >
                    작성
                  </v-btn>
                  <v-btn
                    color="red darken-1"
                    text
                    @click="dialog = false; goToBack()"
                  >
                    취소
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-col>
          <v-col
            class="pa-0"
            align="end"
          >
            <v-btn
              depressed
              color="#2adba3"
              @click="write"
            >
              작성 완료
            </v-btn>
            <v-snackbar
              v-model="snackbar"
            >
              {{ text }}

              <template v-slot:action="{ attrs }">
                <v-btn
                  color="red"
                  text
                  v-bind="attrs"
                  @click="snackbar = false"
                >
                  닫기
                </v-btn>
              </template>
            </v-snackbar>
          </v-col>
        </v-row>
      </v-card>
    </div>
  </div>
</template>

<script>
import http from '@/util/http_common.js'
import BannerImage from '@/components/Community/Banner.vue'

export default {
  components: { BannerImage },
  asyncData ({ params, query }) {
    return {
      board_pk: params.id,
      board_title: query.title
    }
  },
  validate ({ params, query }) {
    // validation 체크 파라미터 값이 숫자가 아니면 page falut 에러 반환하게
    return /^\d+$/.test(params.id)
  },
  data () {
    return {
      rules: [
        value => !!value || '필수로 입력해야합니다.'
      ],
      title: '',
      content: '',
      dialog: false,
      snackbar: false,
      text: '제목과 내용 작성이 필요합니다.'
    }
  },
  mounted () {
  },
  methods: {
    goToBack () {
      this.$router.go(-1)
    },
    write () {
      if (this.title !== '' && this.content !== '') {
        http.axios.post(`/community/${this.board_pk}/article/`, {
          title: this.title,
          content: this.content
        }).then(({ data }) => {
          this.$router.go(-1)
        })
      } else {
        this.snackbar = true
      }
    }
  }
}
</script>

<style scoped>
.border_gray{
  border-bottom: 1px solid rgb(236, 236, 236);
}
</style>
