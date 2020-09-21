<template>
  <div class="KinderWrapper">
    <v-container fluid>
      <v-row no-gutters style="height:150vh;">
        <v-col cols="3">
          <v-row style="width:100%;height:30%;">
            <v-col cols="12" style="width:100%;height:100%">
              <v-card>
                <v-card-subtitle style="text-align:center;font-size:1.5vw;font-weight:700;">
                  <v-img
                    class="white--text align-end"
                    height="270px"
                    width="270px"
                    :src="require('@/assets/lion.jpg')"
                  />
                  {{ info.name }}
                </v-card-subtitle>

                <v-card-text class="text--primary">
                  <div>{{ info.address }}</div>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
          <v-row style="width:100%;height:8%;">
            <v-col cols="12">
              <v-row style="vertical-align:bottom;">
                <v-col cols="12" style="text-align:center;">
                  <v-card>
                    <v-card-text class="text--primary">
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
                    </v-card-text>
                  </v-card>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
          <v-row style="width:100%;height:24%;">
            <v-col cols="12">
              <v-card>
                <v-card-subtitle style="text-align:center;font-size:1.2vw;font-weight:800;">
                  <v-img
                    class="white--text align-end"
                    height="100%"
                    width="100%"
                    :src="require('@/assets/monitor.png')"
                  />
                  원격 상담
                </v-card-subtitle>
              </v-card>
            </v-col>
          </v-row>
          <v-row style="width:100%;height:10%;">
            <v-col cols="12">
              <v-card>
                <v-card-subtitle style="text-align:center;font-size:1.2vw;font-weight:800;">
                  <v-icon color="red">
                    fas fa-bullhorn
                  </v-icon>&nbsp;잘못된 정보 신고
                </v-card-subtitle>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="9" style="border:1px solid black;">
          <v-row style="height:33.3%">
            <v-col cols="12">
              어린이집 정보
            </v-col>
          </v-row>
          <v-row style="height:33.3%">
            <v-col cols="12">
              어린이집 리뷰
            </v-col>
          </v-row>
          <v-row style="height:33.3%">
            <v-col cols="12">
              어린이집 지도
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data () {
    return {
      id: this.$route.params.id,
      info: {
        name: '대봉어린이집',
        address: '서울특별시 강남구 테헤란로 212 (역삼동 718-5번지)',
        stars: 4.3,
        tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영']
      }
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
</style>
