<template>
  <div class="KinderWrapper">
    <v-container fluid>
      <v-row no-gutters style="height:300vh;margin:40px 0px;">
        <!-- 좌측 -->
        <v-col cols="3" style="padding-right:30px;">
          <v-row style="width:100%;">
            <v-col cols="12" class="card">
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
          <v-row style="width:100%;height:2%;" />
          <v-row style="width:100%;">
            <v-col cols="12" class="card">
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
          <v-row style="width:100%;height:2%;" />
          <v-row style="width:100%;">
            <v-col cols="12" class="card">
              <v-img
                :src="require('@/assets/monitor.png')"
              />
              <div style="text-align:center;font-size:1.2vw;font-weight:800;">
                원격 상담
              </div>
            </v-col>
          </v-row>
          <v-row style="width:100%;height:2%;" />
          <v-row style="width:100%;">
            <v-col cols="12" class="card">
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
          <v-row>
            <v-col cols="12" class="cardRight">
              <v-row>
                <div style="font-size:2.5vw;font-weight:800;">
                  어린이집 소개
                </div>
              </v-row>
              <v-row>
                <v-col cols="12">
                  <v-chip
                    v-for="(tag, i) in info.tags"
                    :key="i"
                    class="ma-1 chip"
                    color="#ff9800"
                    text-color="#black"
                    outlined
                  >
                    <v-icon left color="#ff9800">
                      mdi-server-plus
                    </v-icon>
                    {{ tag }}
                  </v-chip>
                </v-col>
                <v-col cols="12" />
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
              </v-row>
              <v-row>
                <v-col cols="12">
                  <div style="width:100%;text-align:right">
                    <v-btn icon>
                      <v-icon>fas fa-angle-left</v-icon>
                    </v-btn>
                    <v-btn icon>
                      <v-icon>fas fa-angle-right</v-icon>
                    </v-btn>
                  </div>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="4">
                  <bar-chart title="교사평균 근속연수" />
                </v-col>
                <v-col cols="4">
                  <bar-chart title="교사 1인당 유아 수" />
                </v-col>
                <v-col cols="4">
                  <bar-chart title="100m²당 CCTV수" />
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
                    :number="[Math.round(100 * info.nOne / (info.nOne + info.nTwo + info.nThree)),Math.round(100 * info.nTwo / (info.nOne + info.nTwo + info.nThree)),Math.round(100 * info.nThree / (info.nOne + info.nTwo + info.nThree))]"
                    :name="['1급','2급','3급']"
                    :color="color2"
                    :unit="unit2"
                    style="height:100%"
                  />
                </v-col>
                <v-col cols="4">
                  <kinder-chart
                    title="근속 년수"
                    :number="info.yearInfo"
                    :name="['1년미만', '1년이상 2년미만', '2년이상 4년미만', '4년이상 6년미만', '6년이상'] "
                    :color="color3"
                    :unit="unit2"
                    style="height:100%"
                  />
                </v-col>
                <v-col cols="2" />
              </v-row>
            </v-col>
          </v-row>
          <v-row style="height:3.3%" />
          <v-row style="height:20%">
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
          <v-row style="height:3.3%" />
          <v-row>
            <v-col cols="12" class="cardRight">
              <v-row>
                <div style="font-size:2.5vw;font-weight:800;">
                  <span style="color:#F5A9E1;">"ZIP"</span>&nbsp;리뷰
                </div>
              </v-row>
              <v-row style="height:95%">
                <v-col cols="12">
                  <kinder-review />
                </v-col>
                <v-col cols="12">
                  <kinder-review />
                </v-col>
                <!-- <v-col cols="12">
                  <kinder-review />
                </v-col> -->
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
// import BarChartVertical from '@/components/Kinder/BarChartVertical.vue'
export default {
  components: {
    MapView,
    KinderChart,
    BarChart,
    KinderReview
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
      color1: ['#e25668', '#e2cf56', '#69e256', '#56e2cf', '#5669e2', '#e256ae'],
      color2: ['#6cd3c7', '#e2cf56', '#fd8c63', '#e256ae', '#e25668', '#e2cf56'],
      color3: ['#6cd3c7', '#ff789c', '#63fda6', '#e2cf56', '#fd8c63', '#78acff'],
      unit1: '명',
      unit2: '%'
    }
  },
  method: {

  },
  mounted () {

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
</style>
