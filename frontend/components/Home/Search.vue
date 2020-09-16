<template>
  <div class="wrap">
    <!-- <v-card color="red lighten-2" dark> -->
    <v-row>
      <v-col cols="12" style="padding-bottom:0;">
        <p style="margin-bottom:0;">
          지역
        </p>
      </v-col>
    </v-row>
    <v-row align:center>
      <v-col
        cols="12"
        sm="4"
        style="padding-top:0;"
      >
        <v-overflow-btn
          v-model="selectedSi"
          :items="si"
          label="시/도"
        />
      </v-col>
      <v-col
        cols="12"
        sm="4"
        style="padding-top:0;"
      >
        <v-overflow-btn
          v-model="selectedGugun"
          :items="gugun"
          label="시/군/구"
        />
      </v-col>
      <v-col
        cols="12"
        sm="4"
        style="padding-top:0;"
      >
        <v-overflow-btn
          v-model="selectedDong"
          :items="dong"
          label="읍/면/동"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" style="padding-bottom:0;">
        <p style="margin-bottom:0;">
          어린이집 명
        </p>
      </v-col>
    </v-row>
    <v-row align:center>
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
    </v-row>
    <!-- </v-card> -->
  </div>
</template>

<script>
export default {
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
      items: ['대봉어린이집', '기념어린이집', '우리어린이집'],
      err: false,
      errMessage: "'시/도'를 선택해 주세요."
    }
  },
  methods: {
    searchValidation () {
      if (this.selectedSi === '') {
        this.err = true
        this.errMessage = "'시/도'를 선택해 주세요."
        console.log(this.errMessage)
      } else if (this.selectedGugun === '') {
        this.errMessage = "'시/군/구'를 선택해 주세요."
        this.err = true
        console.log(this.errMessage)
      } else if (this.selectedDong === '') {
        this.err = true
        this.errMessage = "'읍/면/동'을 선택해 주세요."
        console.log(this.errMessage)
      } else {
        this.errMessage = ''
      }
    }
  }
}
</script>

<style scoped>
.wrap {
  margin: 0 8vw;
}
.fas{
  font-size: 30px;
  cursor: pointer;
}
</style>
