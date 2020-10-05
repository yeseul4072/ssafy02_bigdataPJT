<template>
  <div class="KinderWrapper">
    <v-container fluid>
      <v-row no-gutters style="margin:40px 0px;">
        <!-- 좌측 -->
        <v-col cols="3" style="padding-right:30px;">
          <v-row style="width:100%;">
            <v-col cols="12" class="mb-8 card">
              <v-img
                class="white--text align-end"
                height="270px"
                width="270px"
                :src="require('@/assets/lion.jpg')"
              />
              <div style="text-align:center;font-size:1.5vw;font-weight:800;">
                {{ info.organizationName }}
              </div>
              <div style="text-align:center;">
                {{ info.address }}
              </div>
            </v-col>
          </v-row>
          <v-row style="width:100%;">
            <v-col cols="12" class="mb-8 card">
              <v-row style="vertical-align:bottom;">
                <v-col cols="12" style="text-align:center;">
                  <span style="font-size:1.7vw;font-weight:800;">{{ info.stars }}</span>/5
                  <v-rating
                    :value="info.stars"
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
          <v-row style="width:100%;">
            <v-col cols="12" class="mb-8 card">
              <v-img
                :src="require('@/assets/monitor.png')"
              />
              <div style="text-align:center;font-size:1.2vw;font-weight:800;">
                원격 상담
              </div>
            </v-col>
          </v-row>
          <v-row style="width:100%;">
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
                <div style="font-size:2.5vw;font-weight:800;">
                  어린이집 소개
                </div>
              </v-row>
              <v-row>
                <v-col cols="12" style="pd-12">
                  <v-chip
                    v-for="(tag, i) in info.tags"
                    :key="i"
                    class="ma-1 chip"
                    color="#41b883"
                    text-color="#black"
                    outlined
                  >
                    <v-icon left color="#41b883">
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
                      </v-icon><a :href="info.homepage">{{ info.homepage }}</a>
                    </v-col>
                    <v-col cols="12">
                      <v-icon style="padding:0px 25px 0px 20px;height:100%;width:0;">
                        fas fa-clock
                      </v-icon><span>{{ info.operating_time }}</span>
                    </v-col>
                    <v-col cols="12">
                      <v-icon style="padding:0px 25px 0px 20px;height:100%;width:0;">
                        fas fa-phone-alt
                      </v-icon><span>{{ info.tel }}</span>
                    </v-col>
                    <v-col cols="12">
                      <v-icon style="padding:0px 25px 0px 20px;height:100%;width:0;">
                        fas fa-user-tie
                      </v-icon><span>{{ info.director_name }} 원장선생님</span>
                    </v-col>
                  </v-col>
                  <v-col cols="6">
                    <v-col col="12">
                      <div align="center">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="5vh"
                          height="10vh"
                          viewBox="0 0 8 19"
                          class="aW-AU"
                          role="presentation"
                        ><path d="M4.8 15.89a10.68 10.68 0 0 1-.05-.05l.05.05zm-1.14-1.93c-.25-.54-.48-1.12-.68-1.75a.3.3 0 0 0 .12-.04c.78-.48 1.41-1.01 1.6-1.55.2-.54.03-1.33-.29-2.16a.31.31 0 0 0-.46-.14c-.66.4-1.2.85-1.47 1.3 0-.34-.04-.65-.15-.89-.01-.55.03-1.07.12-1.57.87.1 1.68.06 2.16-.23.47-.29.87-.99 1.18-1.81a.2.2 0 0 0-.17-.26c-.88-.1-1.7-.06-2.18.23l-.03-.04.03.04c-.2.12-.4.33-.58.59a7.65 7.65 0 0 1 1.39-2.25l.28.02.5.03c.38 0 .67-.08.9-.28A4.8 4.8 0 0 0 7 .9a.2.2 0 0 0-.2-.2c-.7-.01-1.97.33-2.43.71-.24.21-.36.51-.4.96l-.02.4c0 .22-.01.33-.03.44a8.13 8.13 0 0 0-.96 1.35c0-.1 0-.19-.03-.27-.11-.5-.62-1.07-1.27-1.6a.18.18 0 0 0-.28.07C1 3.5.78 4.23.9 4.73c.1.5.62 1.07 1.27 1.58a.2.2 0 0 0 .05.03 8.22 8.22 0 0 0-.29 1.87 5.53 5.53 0 0 0-1.47-.89c-.13-.06-.27.01-.3.14-.2.87-.23 1.68.03 2.17l-.05.02.05-.02c.26.5.97.96 1.83 1.33.06.03.14.02.2 0l.02.11c.2.84.45 1.6.74 2.31a4.77 4.77 0 0 0-2.38-.11c-.16.02-.26.17-.2.3.33.92.79 1.7 1.33 2l-.02.05.02-.05c.54.31 1.46.33 2.47.18l.22.32c.63.87 1.3 1.55 1.98 2.04a5.8 5.8 0 0 0 .66.42 2 2 0 0 0 .3.14c.17.03.3.03.4-.02.24-.13.32-.45.16-.72-.1-.17-.3-.32-.7-.56l-.5-.3a12.12 12.12 0 0 1-.72-.46.21.21 0 0 0 .02-.03c.45-.92.7-1.8.56-2.4-.14-.6-.78-1.25-1.6-1.85a.2.2 0 0 0-.3.09 4.6 4.6 0 0 0-.58 2.25 4.23 4.23 0 0 0-.44-.71z" /></svg>
                        <span class="px-5" style="color:#2adba3;font-size:4vh;vertical-align:top;">등급 {{ info.grade }}</span>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="5vh"
                          height="10vh"
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
              <v-row>
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
                <v-col cols="4">
                  <kinder-chart
                    title="교사 자격"
                    :number="[info.nOne,info.nTwo,info.nThree]"
                    :name="['1급','2급','3급']"
                    :color="color2"
                    :unit="'명'"
                    style="height:100%"
                  />
                </v-col>
                <v-col cols="4">
                  <kinder-chart
                    title="근속 년수"
                    :number="info.yearInfo"
                    :name="['1년미만', '1년이상 2년미만', '2년이상 4년미만', '4년이상 6년미만', '6년이상'] "
                    :color="color3"
                    :unit="'%'"
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
              <v-row style="height:85%;">
                <map-view />
              </v-row>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" class="cardRight">
              <v-row>
                <v-col cols="6">
                  <div style="font-size:2.5vw;font-weight:800;">
                    <span style="color:#F5A9E1;">"ZIP"</span>&nbsp;리뷰
                  </div>
                </v-col>
                <v-col cols="6" align-self="center" style="text-align:right;">
                  <v-btn
                    rounded
                    outlined
                    color="rgb(236, 236, 236)"
                    dark
                    @click="changeReview"
                  >
                    <span style="color:orange;">글쓰기</span>
                  </v-btn>
                </v-col>
              </v-row>
              <v-row style="height:95%">
                <v-col
                  v-if="reviewFlag"
                  cols="12"
                >
                  <write-review />
                </v-col>
                <v-col
                  v-for="(review, i) in reviews"
                  :key="i"
                  cols="12"
                >
                  <kinder-review :review="review" />
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
import MapView from '@/components/Kinder/Map.vue'
import KinderChart from '@/components/Kinder/PieChart.vue'
import BarChart from '@/components/Kinder/BarChart.vue'
import KinderReview from '@/components/Kinder/KinderReview.vue'
import WriteReview from '@/components/Kinder/WriteReview.vue'
// import BarChartVertical from '@/components/Kinder/BarChartVertical.vue'
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
      id: this.$route.params.id,
      info: {
        organizationName: '대봉어린이집', // 기관명
        address: '서울특별시 강남구 테헤란로 212 (역삼동 718-5번지)',
        stars: 4.3,
        tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
        nteacher: 14,
        nchildren: 46,
        nOne: 20,
        nTwo: 15,
        nThree: 11,
        yearInfo: [21.4, 28.6, 50, 0, 0],
        director_name: '윤혜경', // 원장명
        establishment_type: '직장', // 설립유형
        created_date: '2014-01-29', // 설립(개원)일
        tel: '(02)3789-5971',
        homepage: 'http://www.puruni.com/gsconst',
        operating_time: '평일기준시간 : 07:30 ~ 19:30',
        services: ['일반'], // 제공 서비스 [일반 / 영아전담 / 장애아전문 / 장애아통합 / 방과후 전담 / 방과후 통합 / 야간연장 / 휴일보육 / 24시간 / 시간제보육]
        school_bus: '미운영', // 통학 버스 운영여부 (운영 또는 미운영)
        grade: 'A' // 어린이집의 등급 또는 종합 평점
      },
      barTap: 0,
      bar: [
        {
          title: '교사평균 근속연수', unit: '년', data: ['1.2', '2.0']
        },
        {
          title: '교사 1인당 유아 수', unit: '명', data: ['10', '18.2']
        },
        {
          title: '100m²당 CCTV수', unit: '개', data: ['3.2', '3.0']
        },
        {
          title: '교사 수', unit: '명', data: ['14', '13.5']
        },
        {
          title: '유아 수', unit: '명', data: ['45', '51']
        },
        {
          title: '실내 면적', unit: 'm²', data: ['146', '101']
        }
      ],
      color1: ['#e25668', '#e2cf56', '#69e256', '#56e2cf', '#5669e2', '#e256ae'],
      color2: ['#6cd3c7', '#e2cf56', '#fd8c63', '#e256ae', '#e25668', '#e2cf56'],
      color3: ['#6cd3c7', '#ff789c', '#63fda6', '#e2cf56', '#fd8c63', '#78acff'],
      reviews: [
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          title: '믿고 맡길 수 있는 어린이집',
          stars: 5,
          pros: '1원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.',
          cons: '1원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.'
        },
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          title: '믿고 맡길 수 있는 어린이집',
          stars: 5,
          pros: '1원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.',
          cons: '1원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.'
        },
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          title: '믿고 맡길 수 있는 어린이집',
          stars: 5,
          pros: '1원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.',
          cons: '1원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.'
        }
      ],
      reviewFlag: false
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
  methods: {
    scroll (e) {
      // if(flag) return
      const scrollH = e.target.scrollingElement.scrollHeight
      const scrollT = e.target.scrollingElement.scrollTop
      const clientH = e.target.scrollingElement.clientHeight
      if (scrollT + clientH >= scrollH) {
        // axios들어갈 때 flag하나 세워주고 finally해야지 바꿔줘서 다른작업 들어오지못하게 막는다.
        const data = {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          title: '믿고 맡길 수 있는 어린이집',
          stars: 5,
          pros: '1원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.',
          cons: '1원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.'
        }
        for (let i = 0; i < 3; i++) {
          this.reviews.push(data)
        }
      }
    },
    changeBar (num) {
      this.barTap = (((this.barTap + num) + 2) % 2) * 3
    },
    callBar (num) {
      return this.bar[num]
    },
    changeReview () {
      this.reviewFlag = !this.reviewFlag
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
    fill: #2adba3;
    margin-right: 5px ;
    transform: scaleX(-1) rotate(-20deg);

}
.aW-AU {
    fill: #2adba3;
    margin-left: 5px;
    transform: rotate(-20deg);
}
</style>
