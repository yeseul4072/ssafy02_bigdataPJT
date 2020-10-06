<template>
  <div class="HomeWrapper">
    <v-container fluid>
      <search-bar />
      <v-row no-gutters>
        <v-row style="width:100%;height:70px">
          <v-col cols="12">
            <div style="font-size:2vw">
              이런 어린이집 어때요?
            </div>
          </v-col>
        </v-row>
        <v-row class="mb-2" style="width:100%;height:620px;">
          <v-col cols="12">
            <kinder-box :kinders="kinders1" class="card" :title="`근처 ${feature1} 어린이집`" />
          </v-col>
        </v-row>
        <v-row style="width:100%;height:620px;">
          <v-col cols="12">
            <kinder-box :kinders="kinders2" class="card" :title="`근처 ${feature2} 어린이집`" />
          </v-col>
        </v-row>
      </v-row>
      <v-row class="mt-1" style="height:790px;">
        <v-col cols="6" style="height:100%">
          <div class="card" style="height:100%">
            <v-row>
              <v-col cols="12">
                <div style="font-size:2vw">
                  지금 뜨는 게시글
                </div>
              </v-col>
            </v-row>
            <v-row
              v-for="(item, index) in board"
              :key="index"
            >
              <v-col
                cols="12"
                class="py-0"
              >
                <post-box :board="item" />
              </v-col>
            </v-row>
          </div>
        </v-col>
        <v-col cols="6" style="height:100%">
          <div class="card" style="height:100%">
            <v-row style="height:80px;">
              <v-col cols="12">
                <v-row>
                  <v-col cols="6" style="font-size:2vw;">
                    지금 뜨는 리뷰
                  </v-col>
                  <v-col cols="6" style="text-align:right">
                    <v-btn icon @click="changeReview(-1)">
                      <v-icon>fas fa-angle-left</v-icon>
                    </v-btn>
                    <v-btn icon @click="changeReview(1)">
                      <v-icon>fas fa-angle-right</v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
            <v-row
              v-if="review.length!=0"
              style="height:660px;"
            >
              <review-box :review="review[reviewIdx]" />
            </v-row>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import SearchBar from '@/components/Home/Search.vue'
import KinderBox from '@/components/Home/Kinder.vue'
import PostBox from '@/components/Home/Post.vue'
import ReviewBox from '@/components/Home/Review.vue'
import http from '@/util/http_common.js'

export default {
  components: {
    SearchBar,
    KinderBox,
    PostBox,
    ReviewBox
  },
  data () {
    return {
      kinders1: [],
      kinders2: [],
      feature1: '',
      feature2: '',
      features: ['방과후 전담', '방과후 통합', '24시간', '협동', '법인 단체', '문화/예술', '장애아전문', '장애아통합', '야간연장', '가정', '일반', '연장 보육반', '휴일보육',
        '영아전담', '언어', '직장', '시간제보육', '민간', '국공립', '통학버스', '과학/창의', '체육', '사회복지법인'
      ],
      featuresEng: ['after_school', 'after_school_inclusion', 'all_day', 'cooperation', 'corporate', 'culture', 'disabled', 'disabled_integration', 'extension', 'family',
        'general', 'has_extension_class', 'holiday', 'infants', 'language', 'office', 'part_time', 'private', 'public', 'school_bus', 'science', 'sport', 'welfare'
      ],
      featuresKo: ['방과후 전담', '방과후 통합', '24시간', '협동', '법인 단체', '문화/예술 교육', '장애아전문', '장애아통합', '야간연장', '가정', '일반', '연장 보육반이 있는', '휴일보육제공',
        '영아전담', '언어 교육', '직장', '시간제보육 가능', '민간', '국공립', '통학버스 시행', '과학/창의 교육', '체육 교육', '사회복지법인'
      ],
      board: [],
      review: [],
      reviewIdx: 0
    }
  },
  computed: {
    ...mapGetters(['isLogin'])
  },
  watch: {

  },
  created () {
    if (!this.isLogin) { this.$router.push('/login') } else {
      http.axios.get('/kindergartens/feature-based-recommend/')
        .then(({ data }) => {
          // 특징 매핑
          for (let i = 0; i < this.featuresEng.length; i++) {
            if (data[0].feature === this.featuresEng[i]) {
              this.feature1 = this.featuresKo[i]
            }
          }
          for (let i = 0; i < this.featuresEng.length; i++) {
            if (data[6].feature === this.featuresEng[i]) {
              this.feature2 = this.featuresKo[i]
            }
          }
          // 데이터 형태 처리
          for (let i = 0; i < 12; i++) {
            const temp = {}
            data[i].url = 'kinder_temp.jpg'
            data[i].distance = data[i].distance.toFixed(1)

            // 토큰 처리
            data[i].tags = []
            let idx = 0
            for (const j in data[i].features) {
              if (data[i].features[j]) {
                data[i].tags.push(this.features[idx])
              }
              idx++
            }
            temp.left = data[i++]

            data[i].url = 'kinder_temp.jpg'
            data[i].distance = data[i].distance.toFixed(1)

            // 토큰 처리
            data[i].tags = []
            idx = 0
            for (const j in data[i].features) {
              if (data[i].features[j]) {
                data[i].tags.push(this.features[idx])
              }
              idx++
            }

            temp.right = data[i]
            if (i < 6) { this.kinders1.push(temp) } else { this.kinders2.push(temp) }
          }

          for (const i in data[6].features) {
            if (data[0].features[i] === this.featuresEng[i]) {
              this.feature2 = this.features[i]
              break
            }
          }
        })

      http.axios.get('/community/main-articles/')
        .then(({ data }) => {
          this.board = data
        })

      http.axios.get('/kindergartens/activated-reviews/')
        .then(({ data }) => {
          for (const i in data) {
            data[i].url = 'kinder_temp.jpg'
            data[i].avg_score = Number(data[i].avg_score.toFixed(1))
            data[i].tags = []
            let idx = 0
            for (const j in data[i].kindergarten.features) {
              if (data[i].kindergarten.features[j]) {
                data[i].tags.push(this.features[idx])
              }
              idx++
            }
          }

          this.review = data
        })
    }
  },
  methods: {
    changelogin () {
      const cur = this.$store.state.User.isLogin
      this.$store.commit('setIsLogin', !cur)
    },
    changeReview (num) {
      const len = this.review.length
      this.reviewIdx = ((this.reviewIdx + num) + len) % len
    }
  }
}
</script>

<style scoed>
.HomeWrapper{
  margin: 0 8vw;
  font-weight: 600;
  font-size: 1.2vw;
  }
.card{
  border-radius: 4px;
  padding: 15px;
  border : thin solid #E6E6E6;
}
</style>
