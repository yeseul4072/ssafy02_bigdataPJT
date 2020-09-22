<template>
  <div class="KinderWrapper">
    <v-container fluid>
      <v-row no-gutters style="height:150vh;margin:40px 0px;">
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
                {{ info.name }}
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
          <v-row style="height:30%">
            <v-col cols="12" class="cardRight">
              <v-row style="height:15%">
                <div style="font-size:2.0vw;font-weight:800;">
                  어린이집 소개
                </div>
              </v-row>
              <v-row style="height:85%">
                <kinder-chart title="교사대 아동비율" :number="[info.nteacher, info.nchildren]" :name="['교사','아동']" :color="color1" />
              </v-row>
            </v-col>
          </v-row>
          <v-row style="height:3.3%" />
          <v-row style="height:30%">
            <v-col cols="12" class="cardRight">
              <v-row style="height:15%;">
                <div style="font-size:2.0vw;font-weight:800;">
                  주변정보
                </div>
              </v-row>
              <v-row style="height:85%;">
                <map-view />
              </v-row>
            </v-col>
          </v-row>
          <v-row style="height:3.3%" />
          <v-row style="height:30%">
            <v-col cols="12" class="cardRight">
              <v-row style="height:15%;">
                <div style="font-size:2.0vw;font-weight:800;">
                  <span style="color:#F5A9E1;">"ZIP"</span>&nbsp;리뷰
                </div>
              </v-row>
              <v-row style="height:85%">
                리뷰 컴포넌트
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
export default {
  components: {
    MapView,
    KinderChart

  },
  data () {
    return {
      id: this.$route.params.id,
      info: {
        name: '대봉어린이집',
        address: '서울특별시 강남구 테헤란로 212 (역삼동 718-5번지)',
        stars: 4.3,
        tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
        nteacher: 14,
        nchildren: 46,
        nOne: 20,
        nTwo: 15,
        nThree: 11,
        yearInfo: [21.4, 28.6, 50, 0, 0]
      },
      color1: ['#e25668', '#e2cf56', '#69e256', '#56e2cf', '#5669e2', '#e256ae']

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
