<template>
  <div class="wrap">
    <!-- <v-card color="red lighten-2" dark> -->
    <v-row style="padding-top:15px;padding-left:8vw;">
      <div style="width:90%; padding: 0 1%; font-size:1.5vw;">
        지역
      </div>
    </v-row>
    <v-row style="padding-left:8vw;">
      <div style="width:24.7%; padding: 0 1%">
        <v-overflow-btn
          v-model="selectedSi"
          :items="si"
          label="시/도"
        />
      </div>
      <div style="width:24.7%; padding: 0 1%">
        <v-overflow-btn
          v-model="selectedGugun"
          :items="gugun"
          :disabled="(selectedSi=='')?true:false"
          label="시/군/구"
        />
      </div>
      <div style="width:24.7%; padding: 0 1%;">
        <v-overflow-btn
          v-model="selectedDong"
          :items="dong"
          :disabled="(selectedGugun=='')?true:false"
          label="읍/면/동"
        />
      </div>

      <div style="padding-top: 10px;">
        <v-btn
          class="mx-2"
          fab
          dark
          color="#0CC476"
          style="margin:0px !important;"
          @click="searchValidation"
        >
          <v-icon>
            fas fa-search
          </v-icon>
        </v-btn>
        <v-btn
          class="mx-2"
          fab
          dark
          color="#0CC476"
          style="margin:0px !important;"
          @click="openMap"
        >
          <v-icon>
            fas fa-map
          </v-icon>
        </v-btn>
      </div>
    </v-row>
    <v-row>
      <v-col cols="4" />
      <v-col cols="4">
        <div v-show="err" style="color:red; text-align:center; padding-left:1.0vw">
          {{ errMessage }}
        </div>
      </v-col>
      <v-col cols="4" />
    </v-row>
    <!-- 검색창 UI -->
    <!-- <v-row>
      <v-col cols="12" style="padding-bottom:0;">
        <p style="margin-bottom:0;">
          어린이집 명
        </p>
      </v-col>
    </v-row> -->
    <!-- <v-row align:center>
      <div style="width:96%">
        <v-autocomplete
          :items="items"
          :loading="isLoading"
          :search-input.sync="kinderName"
          color="black"
          hide-no-data
          placeholder="어린이집 명을 입력하세요."
          prepend-icon="mdi-layers-search"
          return-object
        />
        <div v-show="err" style="color:red; text-align:center;">
          {{ errMessage }}
        </div>
      </div>
      <div style="width:4%; padding-top:20px; padding-left:1.0vw">
        <v-icon @click="searchValidation">
          fas fa-search
        </v-icon>
      </div>
    </v-row> -->
    <!-- </v-card> -->
    <v-dialog v-model="isMap">
      <v-card>
        <!-- kakao map -->
        <map-view @setLat="setLat" @setLng="setLng" />
        <v-card-actions>
          <v-spacer />
          <v-btn color="error darken-1" @click="isMap = false">
            취소
          </v-btn>
          <v-btn color="primary darken-1" @click="mapSearch">
            검색
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script type="text/JavaScript" src="http://dapi.kakao.com/v2/maps/sdk.js?appkey=dff523ff715cfa66c3e0461e1f477834&autoload=false"></script>
<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=dff523ff715cfa66c3e0461e1f477834&libraries=services"></script>
<script>
import MapView from '@/components/Home/Map.vue'
import http from '@/util/http_common.js'

export default {
  components: {
    MapView
  },
  data () {
    return {
      si: ['서울특별시'],
      gugun: [],
      dong: [],
      selectedSi: '서울특별시',
      selectedGugun: '',
      selectedDong: '',
      gugunList: [],
      dongList: [],
      err: false,
      errMessage: "'시/도'를 선택해 주세요.",
      isMap: false,
      map: null,
      mapOption: '',
      mapContainer: '',
      geocoder: '',
      lat: 0,
      lng: 0,
    }
  },
  watch: {
    selectedGugun (val) {
      for (const i in this.gugunList) {
        if (this.gugunList[i].name === val) {
          this.selectedDong = ''
          this.dong = []
          this.getDong(this.gugunList[i].id)
          break
        }
      }
    }
  },
  created () {
    this.getGuGun()
  },
  methods: {
    searchValidation () {
      if (this.selectedSi === '') {
        this.err = true
        this.errMessage = "'시/도'를 선택해 주세요."
      } else if (this.selectedGugun === '') {
        this.errMessage = "'시/군/구'를 선택해 주세요."
        this.err = true
      } else if (this.selectedDong === '') {
        this.err = true
        this.errMessage = "'읍/면/동'을 선택해 주세요."
      } else {
        this.errMessage = ''
        this.getLatLNG()
      }
    },
    openMap () {
      this.isMap = true
    },
    getGuGun () {
      http.axios.get('/kindergartens/boroughs/')
        .then(({ data }) => {
          for (const i in data) {
            this.gugun.push(data[i].name)
          }
          this.gugunList = data
        })
    },
    getDong (id) {
      http.axios.get(`/kindergartens/boroughs/${id}/`)
        .then(({ data }) => {
          for (const i in data) {
            this.dong.push(data[i].name)
          }
          this.dongList = data
        })
    },
    getLatLNG () {
      var setAddress = this.setAddress;
      const geocoder = new kakao.maps.services.Geocoder()

      const callback = function (result, status) {
        if (status === kakao.maps.services.Status.OK) {
          setAddress(result[0].x, result[0].y)
        }
      }
      geocoder.addressSearch(this.selectedSi+" "+this.selectedGugun+" "+this.selectedDong, callback)
    },
    setAddress(lng, lat) {
      this.lng = lng
      this.lat = lat
      this.$router.push({
          path: '/searchkind',
          query: {
              "lng": this.lng,
              "lat": this.lat
          }
      });
    },
    setLng(lng){
      this.lng = lng
    },
    setLat(lat){
      this.lat = lat
    },
    mapSearch(){
      this.isMap = false
      this.setAddress(this.lng, this.lat)
    }
  }

}
</script>

<style scoped>
.wrap {
  font-weight: 600;
  padding-top:50px;
}
.fas{
  font-size: 30px;
  cursor: pointer;
}
</style>
