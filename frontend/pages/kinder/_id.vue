<template>
  <div class="KinderWrapper">
    <v-container fluid>
      <v-row no-gutters style="margin:40px 0px;">
        <!-- 좌측 -->
        <v-col cols="3" style="padding-right:30px;">
          <v-row style="width:100%;">
            <v-col cols="12" class="mb-8 card">
              <v-img
                class="white--text align-end mb-3"
                height="270px"
                width="270px"

                :src="kinder.image"
              />
              <div style="text-align:center;font-size:1.5vw;font-weight:800;">
                {{ kinder.organization_name }}
              </div>
              <div style="text-align:center;">
                {{ kinder.address }}
              </div>
            </v-col>
          </v-row>
          <v-row style="width:100%;">
            <v-col cols="12" class="mb-8 card">
              <v-row style="vertical-align:bottom;">
                <v-col cols="12" style="text-align:center;">
                  <span style="font-size:1.7vw;font-weight:800;">{{ kinder.score_avg }}</span>/5
                  <v-rating
                    :value="Number(kinder.score_avg)"
                    color="orange"
                    background-color="orange lighten-3"
                    dense
                    half-increments
                    readonly
                    size="2.0vw"
                    style="display:inline-block;"
                  />
                </v-col>
              </v-row>
            </v-col>
          </v-row>
          <!-- <v-row style="width:100%;">
            <v-col cols="12" class="mb-8 card">
              <v-img
                :src="require('@/assets/monitor.png')"
              />
              <div style="text-align:center;font-size:1.2vw;font-weight:800;">
                원격 상담
              </div>
            </v-col>
          </v-row> -->
          <v-row style="width:100%;cursor: pointer;" @click="gotoBoard">
            <v-col cols="12" class="mb-8 card">
              <div style="text-align:center;font-size:1.2vw;font-weight:800;">
                <v-icon color="red">
                  fas fa-bullhorn
                </v-icon>&nbsp;
                잘못된 정보 신고
              </div>
            </v-col>
          </v-row>
        </v-col>
        <!-- 우측 -->
        <v-col cols="9">
          <v-row class="pb-8">
            <v-col cols="12" class="cardRight">
              <v-row>
                <v-col cols="6">
                  <div style="font-size:2.5vw;font-weight:800;">
                    어린이집 소개
                  </div>
                </v-col>
                <v-col cols="6" align="end" align-self="center">
                  <v-tooltip top>
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                        icon
                        x-large
                        :color="(kinder.wishlist_yn == 1)?'pink':'gray'"
                        v-bind="attrs"
                        v-on="on"
                        @click="changeWishList"
                      >
                        <v-icon>mdi-heart</v-icon>
                      </v-btn>
                    </template>
                    <span>찜하기</span>
                  </v-tooltip>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" style="pd-12">
                  <v-chip
                    v-for="(tag, i) in kinder.tags"
                    :key="i"
                    class="ma-1 chip"
                    color="green accent-4"
                    text-color="#black"
                    outlined
                  >
                    <v-icon left color="green accent-4">
                      mdi-server-plus
                    </v-icon>
                    {{ tag }}
                  </v-chip>
                </v-col>
                <v-row>
                  <v-col cols="6">
                    <v-col cols="12">
                      <v-icon style="padding:0px 25px 0px 20px;height:100%;width:0;">
                        fas fa-home
                      </v-icon>
                      <a v-if="kinder.homepage!=''" :href="kinder.homepage">{{ kinder.homepage }}</a>
                      <span v-else>홈페이지가 없습니다</span>
                    </v-col>
                    <v-col cols="12">
                      <v-icon style="padding:0px 25px 0px 20px;height:100%;width:0;">
                        fas fa-clock
                      </v-icon>
                      <span> {{ kinder.operating_time }}</span>
                    </v-col>
                    <v-col cols="12">
                      <v-icon style="padding:0px 25px 0px 20px;height:100%;width:0;">
                        fas fa-phone-alt
                      </v-icon>
                      <span>{{ kinder.tel }}</span>
                    </v-col>
                    <v-col cols="12">
                      <v-icon style="padding:0px 25px 0px 20px;height:100%;width:0;">
                        fas fa-user-tie
                      </v-icon>
                      <span>{{ kinder.director_name }} 원장선생님</span>
                    </v-col>
                  </v-col>
                  <v-col cols="6">
                    <v-col col="12">
                      <div align="center">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="4.5vh"
                          height="9vh"
                          viewBox="0 0 8 19"
                          class="aW-AU"
                          role="presentation"
                        ><path d="M4.8 15.89a10.68 10.68 0 0 1-.05-.05l.05.05zm-1.14-1.93c-.25-.54-.48-1.12-.68-1.75a.3.3 0 0 0 .12-.04c.78-.48 1.41-1.01 1.6-1.55.2-.54.03-1.33-.29-2.16a.31.31 0 0 0-.46-.14c-.66.4-1.2.85-1.47 1.3 0-.34-.04-.65-.15-.89-.01-.55.03-1.07.12-1.57.87.1 1.68.06 2.16-.23.47-.29.87-.99 1.18-1.81a.2.2 0 0 0-.17-.26c-.88-.1-1.7-.06-2.18.23l-.03-.04.03.04c-.2.12-.4.33-.58.59a7.65 7.65 0 0 1 1.39-2.25l.28.02.5.03c.38 0 .67-.08.9-.28A4.8 4.8 0 0 0 7 .9a.2.2 0 0 0-.2-.2c-.7-.01-1.97.33-2.43.71-.24.21-.36.51-.4.96l-.02.4c0 .22-.01.33-.03.44a8.13 8.13 0 0 0-.96 1.35c0-.1 0-.19-.03-.27-.11-.5-.62-1.07-1.27-1.6a.18.18 0 0 0-.28.07C1 3.5.78 4.23.9 4.73c.1.5.62 1.07 1.27 1.58a.2.2 0 0 0 .05.03 8.22 8.22 0 0 0-.29 1.87 5.53 5.53 0 0 0-1.47-.89c-.13-.06-.27.01-.3.14-.2.87-.23 1.68.03 2.17l-.05.02.05-.02c.26.5.97.96 1.83 1.33.06.03.14.02.2 0l.02.11c.2.84.45 1.6.74 2.31a4.77 4.77 0 0 0-2.38-.11c-.16.02-.26.17-.2.3.33.92.79 1.7 1.33 2l-.02.05.02-.05c.54.31 1.46.33 2.47.18l.22.32c.63.87 1.3 1.55 1.98 2.04a5.8 5.8 0 0 0 .66.42 2 2 0 0 0 .3.14c.17.03.3.03.4-.02.24-.13.32-.45.16-.72-.1-.17-.3-.32-.7-.56l-.5-.3a12.12 12.12 0 0 1-.72-.46.21.21 0 0 0 .02-.03c.45-.92.7-1.8.56-2.4-.14-.6-.78-1.25-1.6-1.85a.2.2 0 0 0-.3.09 4.6 4.6 0 0 0-.58 2.25 4.23 4.23 0 0 0-.44-.71z" /></svg>
                        <span class="px-5" style="color:#0CC476;font-size:4vh;vertical-align:top;">등급 {{ kinder.grade }}</span>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="4.5vh"
                          height="9vh"
                          viewBox="0 0 8 19"
                          class="_1KCw5"
                          role="presentation"
                        ><path d="M4.8 15.89a10.68 10.68 0 0 1-.05-.05l.05.05zm-1.14-1.93c-.25-.54-.48-1.12-.68-1.75a.3.3 0 0 0 .12-.04c.78-.48 1.41-1.01 1.6-1.55.2-.54.03-1.33-.29-2.16a.31.31 0 0 0-.46-.14c-.66.4-1.2.85-1.47 1.3 0-.34-.04-.65-.15-.89-.01-.55.03-1.07.12-1.57.87.1 1.68.06 2.16-.23.47-.29.87-.99 1.18-1.81a.2.2 0 0 0-.17-.26c-.88-.1-1.7-.06-2.18.23l-.03-.04.03.04c-.2.12-.4.33-.58.59a7.65 7.65 0 0 1 1.39-2.25l.28.02.5.03c.38 0 .67-.08.9-.28A4.8 4.8 0 0 0 7 .9a.2.2 0 0 0-.2-.2c-.7-.01-1.97.33-2.43.71-.24.21-.36.51-.4.96l-.02.4c0 .22-.01.33-.03.44a8.13 8.13 0 0 0-.96 1.35c0-.1 0-.19-.03-.27-.11-.5-.62-1.07-1.27-1.6a.18.18 0 0 0-.28.07C1 3.5.78 4.23.9 4.73c.1.5.62 1.07 1.27 1.58a.2.2 0 0 0 .05.03 8.22 8.22 0 0 0-.29 1.87 5.53 5.53 0 0 0-1.47-.89c-.13-.06-.27.01-.3.14-.2.87-.23 1.68.03 2.17l-.05.02.05-.02c.26.5.97.96 1.83 1.33.06.03.14.02.2 0l.02.11c.2.84.45 1.6.74 2.31a4.77 4.77 0 0 0-2.38-.11c-.16.02-.26.17-.2.3.33.92.79 1.7 1.33 2l-.02.05.02-.05c.54.31 1.46.33 2.47.18l.22.32c.63.87 1.3 1.55 1.98 2.04a5.8 5.8 0 0 0 .66.42 2 2 0 0 0 .3.14c.17.03.3.03.4-.02.24-.13.32-.45.16-.72-.1-.17-.3-.32-.7-.56l-.5-.3a12.12 12.12 0 0 1-.72-.46.21.21 0 0 0 .02-.03c.45-.92.7-1.8.56-2.4-.14-.6-.78-1.25-1.6-1.85a.2.2 0 0 0-.3.09 4.6 4.6 0 0 0-.58 2.25 4.23 4.23 0 0 0-.44-.71z" /></svg>
                      </div>
                    </v-col>
                  </v-col>
                </v-row>
              </v-row>
              <v-row>
                <v-col cols="12">
                  <div style="width:100%;text-align:right">
                    <v-btn icon @click="changeBar(-1)">
                      <v-icon>
                        fas fa-angle-left
                      </v-icon>
                    </v-btn>
                    <v-btn icon @click="changeBar(1)">
                      <v-icon>
                        fas fa-angle-right
                      </v-icon>
                    </v-btn>
                  </div>
                </v-col>
              </v-row>
              <v-row v-if="bar[1].data.length == 2">
                <v-col cols="4">
                  <bar-chart :info="bar[barTap]" />
                </v-col>
                <v-col cols="4">
                  <bar-chart :info="bar[barTap+1]" />
                </v-col>
                <v-col cols="4">
                  <bar-chart :info="bar[barTap+2]" />
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="2">
                  <!-- <bar-chart-vertical title="교사대 아동비율" /> -->
                  <!-- <kinder-chart
                    title="교사대 아동비율"
                    :number="[info.nteacher, info.nchildren]"
                    :name="['교사','아동']"
                    :color="color1"
                    :unit="unit1"
                    style="height:100%"
                  /> -->
                </v-col>
                <v-col
                  v-if="tOne != -1"
                  cols="4"
                >
                  <kinder-chart
                    title="교사 자격"
                    :number="[tOne, tTwo, tThree]"
                    :name="['1급','2급','3급']"
                    :color="color2"
                    :unit="'명'"
                    style="height:100%"
                  />
                </v-col>
                <v-col
                  v-if="cInfo.length == 5"
                  cols="4"
                >
                  <kinder-chart
                    title="근속 년수"
                    :number="cInfo"
                    :name="['1년미만', '1년이상 2년미만', '2년이상 4년미만', '4년이상 6년미만', '6년이상'] "
                    :color="color3"
                    :unit="'명'"
                    style="height:100%"
                  />
                </v-col>
                <v-col cols="2" />
              </v-row>
            </v-col>
          </v-row>
          <v-row class="mb-8" style="height:50vh">
            <v-col cols="12" class="cardRight">
              <v-row style="height:15%;">
                <div style="font-size:2.5vw;font-weight:800;">
                  주변정보
                </div>
              </v-row>
              <v-row class="mt-2" style="height:85%;">
                <map-view v-if="lat!=0" :lat="lat" :lng="lng" :name="kinder.organization_name" />
              </v-row>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" class="cardRight">
              <v-row>
                <v-col cols="6">
                  <div style="font-size:2.5vw;font-weight:800;">
                    <span style="color:#0CC476;">"ZIP"</span>&nbsp;리뷰
                  </div>
                </v-col>
                <v-col cols="6" align-self="center" style="text-align:right;">
                  <v-btn
                    rounded
                    outlined
                    color="rgb(236, 236, 236)"
                    dark
                    @click="changeReview(true)"
                  >
                    <span style="color:orange;">글쓰기</span>
                  </v-btn>
                </v-col>
              </v-row>
              <v-row style="height:95%">
                <v-col
                  v-if="write"
                  cols="12"
                >
                  <write-review @close-write="changeReview(false)" />
                </v-col>
                <v-col
                  v-for="(review, i) in reviews"
                  :key="i"
                  cols="12"
                >
                  <kinder-review :review="review" @reviewLike="changeReviewLike(i)" @reviewDelete="reviewDelete(review.id)" />
                </v-col>
                <v-col
                  v-if="reviews.length==0"
                  cols="12"
                  style="text-align:center;"
                >
                  작성된 리뷰가 없네요. 리뷰를 작성해주세요!
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import MapView from '@/components/Kinder/KinderMap.vue'
import KinderChart from '@/components/Kinder/PieChart.vue'
import BarChart from '@/components/Kinder/BarChart.vue'
import KinderReview from '@/components/Kinder/KinderReview.vue'
import WriteReview from '@/components/Kinder/WriteReview.vue'
// import BarChartVertical from '@/components/Kinder/BarChartVertical.vue'
import http from '@/util/http_common.js'

export default {
  components: {
    MapView,
    KinderChart,
    BarChart,
    KinderReview,
    WriteReview
    // BarChartVertical

  },
  data () {
    return {
      id: '',
      kinder: {},
      features: ['방과후 전담', '방과후 통합', '24시간', '협동', '법인 단체', '문화/예술', '장애아전문', '장애아통합', '야간연장', '가정', '일반', '연장 보육반', '휴일보육',
        '영아전담', '언어', '직장', '시간제보육', '민간', '국공립', '통학버스', '과학/창의', '체육', '사회복지법인'
      ],
      features2: {
        after_school: '방과후 전담',
        after_school_inclusion: '방과후 통합',
        all_day: '24시간',
        cooperation: '협동',
        corporate: '법인 단체',
        culture: '문화/예술',
        disabled: '장애아전문',
        disabled_integration: '장애아통합',
        extension: '야간연장',
        family: '가정',
        general: '일반',
        has_extension_class: '연장 보육반',
        holiday: '휴일보육',
        infants: '영아전담',
        language: '언어',
        office: '직장',
        part_time: '시간제보육',
        private: '민간',
        public: '국공립',
        school_bus: '통학버스',
        science: '과학/창의',
        sport: '체육',
        welfare: '사회복지법인'
      },
      grade: ['Z', 'A', 'B', 'C', 'D', 'Z'],
      lat: 0,
      lng: 0,
      barTap: 0,
      bar: [
        {
          title: '교사평균 근속연수', unit: '년', data: ['3.5']
        },
        {
          title: '교사 1인당 유아 수', unit: '명', data: ['2.7']
        },
        {
          title: '100m²당 CCTV수', unit: '개', data: ['20.6']
        },
        {
          title: '교사 수', unit: '명', data: ['13.5']
        },
        {
          title: '유아 수', unit: '명', data: ['36.5']
        },
        {
          title: '실내 면적', unit: 'm²', data: ['227.4']
        }
      ],
      cont: [0.5, 1.5, 3, 5, 6.5],
      tOne: -1,
      tTwo: -1,
      tThree: -1,
      cInfo: [],
      color1: ['#e25668', '#e2cf56', '#69e256', '#56e2cf', '#5669e2', '#e256ae'],
      color2: ['#6cd3c7', '#e2cf56', '#fd8c63', '#e256ae', '#e25668', '#e2cf56'],
      color3: ['#6cd3c7', '#ff789c', '#63fda6', '#e2cf56', '#fd8c63', '#78acff'],
      reviews: [],
      reviewFlag: false,
      write: false,
      page: 1
    }
  },
  mounted () {
    const self = this
    window.addEventListener('scroll', self.scroll)
  },
  beforeDestroy () {
    const self = this
    window.removeEventListener('scroll', self.scroll)
  },
  created () {
    this.id = this.$route.params.id
    http.axios.get(`/kindergartens/${this.id}`)
      .then(({ data }) => {
        // 평점
        data.score_avg = (data.score_avg).toFixed(1)
        // 시간
        data.operating_time = '평일기준시간 : 07:30 ~ 19:30'
        // 태그
        data.tags = []
        for (const tag in data.features) {
          if (data.features[tag]) {
            data.tags.push(this.features2[tag])
          }
        }
        // 등급
        data.grade = this.grade[data.grade]
        if (data.grade === 'Z') {
          data.grade = data.score + '점'
        }
        // 위도경도
        this.lng = data.lng
        this.lat = data.lat
        // barchart
        const cinfo = data.continuous_info.split(',')
        cinfo.shift()
        data.sum_continuous_info = 0
        data.avg_continuous_info = 0
        for (const i in cinfo) {
          data.sum_continuous_info += Number(cinfo[i])
          data.avg_continuous_info += Number(cinfo[i] * this.cont[i])
        }
        data.avg_continuous_info = (data.avg_continuous_info / data.sum_continuous_info).toFixed(1)

        this.bar[0].data.unshift(data.avg_continuous_info)
        this.bar[1].data.unshift(data.child_per_staff.toFixed(1))
        this.bar[2].data.unshift(data.area_per_cctv.toFixed(1))

        const teacher = data.staff_info.split(',')
        this.bar[3].data.unshift(teacher[0])
        const child = data.age_by_class_info.split(',')
        this.bar[4].data.unshift(child[1])
        const area = data.area_info.split(',')
        this.bar[5].data.unshift(area[1])

        // piechart
        this.tOne = Number(teacher[teacher.length - 3])
        this.tTwo = Number(teacher[teacher.length - 2])
        this.tThree = Number(teacher[teacher.length - 1])
        for (const i in cinfo) {
          this.cInfo.push(Number(cinfo[i]))
        }
        this.kinder = data
        this.loadReview()
      })
  },
  methods: {
    scroll (e) {
      const scrollH = e.target.scrollingElement.scrollHeight
      const scrollT = e.target.scrollingElement.scrollTop
      const clientH = e.target.scrollingElement.clientHeight
      if (scrollT + clientH >= scrollH - 5) {
        this.loadReview()
      }
    },
    changeBar (num) {
      this.barTap = (((this.barTap + num) + 2) % 2) * 3
    },
    callBar (num) {
      return this.bar[num]
    },
    changeReview (flag) {
      this.write = !this.write
      if (!flag) { // 새글 작성
        this.write = false
        this.page = 1
        this.reviews = []
        this.loadReview()
      }
    },
    changeWishList () {
      http.axios.post(`/kindergartens/wishlist/${this.id}/`, {

      }).then(({ data }) => {
        this.kinder.wishlist_yn = (this.kinder.wishlist_yn + 1) % 2
      })
    },
    loadReview () {
      if (this.page === 0) { return }
      // axios들어갈 때 flag하나 세워주고 finally해야지 바꿔줘서 다른작업 들어오지못하게 막는다.
      if (!this.reviewFlag) {
        this.reviewFlag = true
        http.axios.get(`/kindergartens/${this.id}/reviews/?page=${this.page}`)
          .then(({ data }) => {
            this.reviewFlag = false
            this.page = (data.next != null) ? this.page + 1 : 0
            for (const i in data.results) {
              this.reviews.push(data.results[i])
            }
          })
      }
    },
    changeReviewLike (idx) {
      http.axios.post(`/kindergartens/review/${this.reviews[idx].id}/like/`, {

      }).then(({ data }) => {
        const flag = !this.reviews[idx].like_yn
        this.reviews[idx].like_yn = flag
        if (flag) { this.reviews[idx].like_count++ } else { this.reviews[idx].like_count-- }
      })
    },
    reviewDelete (id) {
      http.axios.delete(`/kindergartens/${this.id}/review/${id}`)
        .then(({ data }) => {
          this.page = 1
          this.reviews = []
          this.loadReview()
        })
    },
    gotoBoard () {
      this.$router.push('/community/3')
    }
  }
}
</script>

<style>
.KinderWrapper{
  margin: 0 8vw;
  font-weight: 600;
  font-size: 1.2vw;
  }
.card{
    border-radius: 4px;
    /* box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
    border-width: thin; */
    padding: 15px;
    border : thin solid #E6E6E6;
}
.cardRight{
    border-radius: 4px;
    /* box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
    border-width: thin; */
    padding: 30px;
    border : thin solid #E6E6E6;
}
._1KCw5 {
    fill: #ebebeb;
    margin-right: 5px ;
    transform: scaleX(-1) rotate(-20deg);

}
.aW-AU {
    fill: #ebebeb;
    margin-left: 5px;
    transform: rotate(-20deg);
}
</style>
