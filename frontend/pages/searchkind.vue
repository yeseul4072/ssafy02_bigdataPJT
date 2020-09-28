<template>
  <div class="body-container">
    <!-- 여기는 검색 하는 부분 -->
    <div class="search-box">
      <search-bar />
    </div>
    <v-container>
      <v-layout wrap>
        <v-flex id="left-panel" md4 lg3 xl3>
          <div class="age">
            <h2>자녀 나이</h2>
            <v-radio-group v-model="age" row>
              <v-radio v-for="idx in 5" :key="`${idx}_age`" :label="`${idx}살`" :value="idx" />
            </v-radio-group>
          </div>
          <div
            v-show="age > -1"
            class="price"
          >
            <h2>보육료</h2>
            <v-sparkline
              :gradient="['#d4d4d4','#d4d4d4']"
              line-width="5"
              padding="0"
              type="bar"
              height="100"
              :value="value"
            />
            <v-range-slider
              v-model="price"
              :max="300000"
              :min="0"
              :step="10000"
              color="primary"
              thumb-color="primary"
              thumb-label="always"
              thumb-size="48"
              :ripple="false"
              style="margin:0;transform: translateY(-15px)"
            >
              <template v-slot:thumb-label="number">
                ￦{{ number.value }}
              </template>
            </v-range-slider>
          </div>
          <div
            class="services"
          >
            <h2> 제공 서비스 </h2>
            <v-radio-group v-model="services" column>
              <v-checkbox v-for="(item,idx) in ['a','b','c']" :key="`${idx}_services`" :label="item" :value="idx" hide-details />
            </v-radio-group>
          </div>

          <div
            class="other_services"
          >
            <h2> 기타 서비스 </h2>
            <v-checkbox label="통학 버스" />
            <v-checkbox label="연장 보육반" />
          </div>
          <div
            class="establishment"
          >
            <h2> 설립유형 </h2>
            <v-radio-group v-model="establishment" column>
              <v-checkbox v-for="(item,idx) in ['a','b','c']" :key="`${idx}_es`" :label="item" :value="idx" />
            </v-radio-group>
          </div>
          <div
            class="establishment"
          >
            <h2> 특별활동 </h2>
            <v-radio-group v-model="activity" column>
              <v-checkbox v-for="(item,idx) in ['a','b','c']" :key="`${idx}_es`" :label="item" :value="idx" />
            </v-radio-group>
          </div>
        </v-flex>
        <!-- <v-flex
          id="right-panel"
          xs12
          sm12
          md8
          lg8
          xl9
        >
          test
        </v-flex> -->
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import SearchBar from '@/components/Home/Search.vue'

export default {
  components:
  {
    SearchBar
  },
  data () {
    return {
      max_age: 5,
      age: -1,
      price: [0, 300000],

      establishment_list: ['직장', '국공립', '민간', '가정', '법인·단체등', '협동', '사회복지법인'],
      establishment: '',
      service_list: ['일반', '영아전담', '장애아전문', '장애아통합', '방과후 전담', '방과후 통합', '야간연장', '휴일보육', '24시간', '시간제보육'],
      service: '',
      other_services_list: ['통학 버스', '연장 보육반'],
      other_services: '',
      activity_list: ['언어', '문화/예술', '체육', '과학/창의'],
      activity: '',

      value: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    }
  }
}
</script>

<style>
@media (min-width:320px) and (max-width:960px) {
    #left-panel {
        display:none
    }
}

.search-box{
  background-color: rgb(251, 251, 251);
  border-bottom: 1px solid #eee;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 270px;
}

.v-slider--horizontal {
  margin-left:4px !important;
  margin-right:4px !important;
}

.v-ripple__contents {
  display: none !important;
}

.v-slider__thumb-label{
}
</style>
