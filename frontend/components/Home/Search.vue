<template>
  <div class="wrap">
    <!-- <v-card color="red lighten-2" dark> -->
    <v-row style="padding-top:15px;">
      <div style="width:10%" />
      <div style="width:88%; padding: 0 1%">
        지역
      </div>
    </v-row>
    <v-row>
      <div style="width:10%" />
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
          label="시/군/구"
        />
      </div>
      <div style="width:24.7%; padding: 0 1%;">
        <v-overflow-btn
          v-model="selectedDong"
          :items="dong"
          label="읍/면/동"
        />
      </div>

      <div style="width:10%; padding-top: 10px;">
        <v-btn
          class="mx-2"
          fab
          dark
          color="pink"
          @click="searchValidation"
        >
          <v-icon>
            fas fa-search
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
      <v-col cols="3" style="padding-left:3.8vw;">
        <v-btn depressed color="pink" dark style="width:7.5vw;" @click="openMap">
          지도로 보기
        </v-btn>
      </v-col>
      <v-col cols="1" />
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
        <map-view />
        <v-card-actions>
          <v-spacer />
          <v-btn color="error darken-1" @click="isMap = false">
            취소
          </v-btn>
          <v-btn color="primary darken-1" @click="isMap = false">
            검색
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import MapView from '@/components/Home/Map.vue'
export default {
  components: {
    MapView
  },
  data () {
    return {
      si: ['서울특별시'],
      gugun: ['강남구', '강동구', '강북구', '강서구'],
      dong: ['개포1동', '개포2동', '개포4동', '논현1동', '논현2동'],
      selectedSi: '',
      selectedGugun: '',
      selectedDong: '',
      kinderName: '',
      isLoading: false,
      items: ['대봉어린이집', '기념어린이집', '우리어린이집', ''],
      err: false,
      errMessage: "'시/도'를 선택해 주세요.",
      isMap: false,
      map: null,
      mapOption: '',
      mapContainer: '',
      geocoder: ''
    }
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
      }
    },
    openMap () {
      this.isMap = true
    }

  }

}
</script>

<style scoped>
.wrap {
  margin: 0 8vw;
  font-weight: 600;
}
.fas{
  font-size: 30px;
  cursor: pointer;
}
</style>
