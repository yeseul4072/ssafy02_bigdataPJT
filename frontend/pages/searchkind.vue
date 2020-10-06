<template>
  <div class="body-container">
    <!-- 여기는 검색 하는 부분 -->
    <div class="search-box">
      <search-bar />
    </div>
    <v-container class="result">
      <v-layout wrap class="mb-4">
        <h2> 검색 결과 <a v-text="count" />개</h2>
        <v-spacer />
        <a id="map-header-cta" class=" show_map sr_header--map " data-map-id="map-header-cta" data-source="map-header-cta" @click="dialog=true">
          <div class="sr_header--map_pin" />
          <span class="switch-map-view">
            지도로 보기
          </span>
        </a>
      </v-layout>
      <v-layout wrap>
        <v-flex id="left-panel" md3 lg3 xl3>
          <v-card flat outlined>
            <div class="age pa-3">
              <h3>
                자녀 나이
              </h3>
              <v-radio-group v-model="age" row hide-details>
                <v-radio
                  v-for="idx in 6"
                  :key="`${idx}_age`"
                  class="ma-0 mr-4"
                  :label="`${idx-1}살`"
                  :value="idx-1"
                />
              </v-radio-group>
            </div>
            <v-divider />
            <div
              v-show="age > -1"
              class="price pa-3"
            >
              <h3>보육료</h3>
              <v-sparkline
                :gradient="['#d4d4d4','#d4d4d4']"
                line-width="5"
                padding="0"
                type="bar"
                height="100"
                :value="value[age]"
              />
              <v-range-slider
                v-model="price"
                class="pa-0"
                :max="300000"
                :min="0"
                :step="10000"
                color="primary"
                thumb-color="primary"
                thumb-label="always"
                thumb-size="48"
                tick-size="1"
                hide-details
                :ripple="false"
                style="margin:0;transform: translateY(-15px)"
              >
                <template v-slot:thumb-label="number">
                  {{ number.value }}
                </template>
              </v-range-slider>
            </div>
            <v-divider v-show="age > -1" />

            <div
              class="services pa-3"
            >
              <h3> 제공 서비스 </h3>
              <v-layout wrap>
                <v-flex
                  v-for="(item,idx) in service_list"
                  :key="`${idx}_services`"
                  md6
                  lg6
                  xl6
                >
                  <v-checkbox
                    v-model="selected[0]"
                    class="ma-0 mt-1"
                    :label="item"
                    :value="en[0][idx]"
                    hide-details
                  />
                </v-flex>
              </v-layout>
            </div>
            <v-divider />
            <div
              class="other_services pa-3"
            >
              <h3> 기타 서비스 </h3>
              <v-layout wrap>
                <v-flex
                  v-for="(item,idx) in other_services_list"
                  :key="`${idx}other_services`"
                  md6
                  lg6
                  xl6
                >
                  <v-checkbox
                    v-model="selected[1]"
                    class="ma-0 mt-1"
                    :label="item"
                    :value="en[1][idx]"
                    hide-details
                  />
                </v-flex>
              </v-layout>
            </div>
            <v-divider />
            <div
              class="establishment pa-3"
            >
              <h3> 설립유형 </h3>
              <v-layout wrap>
                <v-flex
                  v-for="(item,idx) in establishment_list"
                  :key="`${idx}_establishment`"
                  md6
                  lg6
                  xl6
                >
                  <v-checkbox
                    v-model="selected[2]"
                    class="ma-0 mt-1"
                    :label="item"
                    :value="en[2][idx]"
                    hide-details
                  />
                </v-flex>
              </v-layout>
            </div>
            <v-divider />
            <div
              class="activity pa-3"
            >
              <h3> 특별활동 </h3>
              <v-layout wrap>
                <v-flex
                  v-for="(item,idx) in activity_list"
                  :key="`${idx}_activity`"
                  md6
                  lg6
                  xl6
                >
                  <v-checkbox
                    v-model="selected[3]"
                    class="ma-0 mt-1"
                    :label="item"
                    :value="en[3][idx]"
                    hide-details
                  />
                </v-flex>
              </v-layout>
            </div>
          </v-card>
        </v-flex>
        <v-flex
          id="right-panel"
          xs12
          sm12
          md9
          lg9
          xl9
        >
          <v-card
            v-for="(item,idx) in items"
            v-show="item.isShow"
            :key="`${idx}_list`"
            flat
            outlined
            class="pa-4 ml-5 mb-5"
            @click="moveKinder(item.id)"
          >
            <v-list three-line>
              <v-list-item class="kinder_list">
                <v-list-item-content style="max-width:200px;max-height:200px;">
                  <v-img src="https://picsum.photos/200/200?image=20" style="border-radius:3px;" />
                </v-list-item-content>
                <v-list-item-content class="pl-4" style="height:200px; padding-top:3px;">
                  <v-list-item-title style="font-size:20px; font-weight:700">
                    {{ item.organization_name }}
                    <v-rating
                      v-model="item.score_avg"
                      dense
                      background-color="orange lighten-3"
                      color="orange"
                      small
                      readonly
                      empty-icon=""
                      style="display:inline;"
                    />
                  </v-list-item-title>
                  <v-list-item-subtitle class="mt-2">
                    {{ (item.address.split('\n'))[1] }} &middot; {{ item.distance.toFixed(1) }}km
                  </v-list-item-subtitle>
                  <!-- <v-list-item-subtitle> -->

                  <v-chip
                    v-for="(flag,key,index) in item.features"
                    v-show="flag"
                    :key="`${index}_chip`"
                    class="mt-2 mr-1"
                    color="green accent-4"
                    text-color="#black"
                    outlined
                    small
                  >
                    <v-icon color="green accent-4" left>
                      mdi-server-plus
                    </v-icon>

                    <span class="success--text" style="color:#69F0AE"> {{ features[key] }}</span>
                  </v-chip>

                  <!-- </v-list-item-subtitle> -->
                </v-list-item-content>
                <v-list-item-action class="ma-0 mt-1" style="min-width:160px; min-height:200px;">
                  <v-row
                    justify="end"
                    style="margin-right:20px;"
                  >
                    <div style="margin-right:20px;text-align:right;">
                      <v-list-item-title>
                        <span
                          :style="{'color': item.color}"
                        >
                          {{ item.grade|grade }}
                        </span>
                        <v-list-item-subtitle>
                          {{ item.reviews_count }}개 리뷰
                        </v-list-item-subtitle>
                        <!-- <span style="text-align:right;">우수</span>
                      <br> -->
                      </v-list-item-title>
                    </div>
                    <v-row
                      align="center"
                      justify="center"
                      :style="{'background-color': item.color}"
                      style="
                        background-color:#00C853;
                        max-width:32px;
                        height:32px;
                        border-radius:6px;border-bottom-left-radius:0px;
                      "
                    >
                      <span class="white--text">{{ item.grade | getGrade }}</span>
                    </v-row>
                  </v-row>
                </v-list-item-action>
              </v-list-item>
            </v-list>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    <v-dialog v-model="dialog" width="960" height="600">
      <!-- <div style="width:100%; height:100%;"> -->
      <search-map
        :items="items"
        :lat="lat"
        :lng="lng"
        :change="change"
        @moveKinder="moveKinder"
      />
      <!-- </div> -->
    </v-dialog>
  </div>
</template>

<script>
import SearchBar from '@/components/Home/Search.vue'
import SearchMap from '@/components/Search/SearchMap.vue'
import http from '@/util/http_common.js'

export default {
  components:
  {
    SearchBar,
    SearchMap
  },
  filters: {
    getGrade (val) {
      if (val === 1) {
        return 'A'
      } else if (val === 2) {
        return 'B'
      } else if (val === 3) {
        return 'C'
      } else {
        return '-'
      }
    },
    grade (val) {
      if (val === 1) {
        return '우수'
      } else if (val === 2) {
        return '적합'
      } else if (val === 3) {
        return '개선 필요'
      } else {
        return '미인증'
      }
    },
    color (val) {
      if (val === 1) {
        return '#00C853'
      } else if (val === 2) {
        return '#FDD835'
      } else if (val === 3) {
        return '#FFA726'
      } else {
        return '#F4511E'
      }
    }
  },

  data () {
    return {
      dialog: false,
      max_age: 5,
      age: -1,
      price: [0, 300000],

      en: [
        ['general', 'infants', 'disabled', 'disabled_integration', 'after_school', 'after_school_inclusion', 'extension', 'holiday', 'all_day', 'part_time'],
        ['school_bus', 'has_extension_class'],
        ['office', 'public', 'private', 'family', 'corporate', 'cooperation', 'welfare'],
        ['language', 'culture', 'sport', 'science']
      ],

      service_list: ['일반', '영아전담', '장애아전문', '장애아통합', '방과후 전담', '방과후 통합', '야간연장', '휴일보육', '24시간', '시간제보육'],
      other_services_list: ['통학 버스', '연장 보육반'],
      establishment_list: ['직장', '국공립', '민간', '가정', '법인·단체등', '협동', '사회복지법인'],
      activity_list: ['언어', '문화/예술', '체육', '과학/창의'],

      features: {
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
      value: [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      ],
      items: [],
      selected: [
        [],
        [],
        [],
        []
      ],
      ageColumns: ['zero_year_old', 'one_year_old', 'two_year_old', 'three_year_old', 'four_year_old', 'five_year_old'],
      count: 0,
      lat: '37.4798',
      lng: '127.0677',
      change: false
    }
  },
  watch: {
    selected () {
      this.filtering()
    },
    age () {
      this.filtering()
    },
    price () {
      this.filtering()
    }
  },
  mounted () {
    // console.log(this.$route)
    this.lat = this.$route.query.lat
    this.lng = this.$route.query.lng
    console.log(this.$route)
    this.getKindergartenList()
  },
  methods: {
    moveKinder (id) {
      this.dialog = false
      this.$router.push(`/kinder/${id}`)
    },
    filtering () {
      this.change = !this.change
      this.count = 0
      for (const i in this.items) {
        this.items[i].isShow = true
        for (const j in this.selected) {
          let flag = false
          let flag2 = false
          for (const k in this.selected[j]) {
            flag |= this.items[i].features[this.selected[j][k]]
            flag2 = true
          }
          if (flag2) {
            this.items[i].isShow &= flag
          }
        }

        if (this.age !== -1) {
          if (this.price[0] > this.items[i][this.ageColumns[this.age]] || this.items[i][this.ageColumns[this.age]] >= this.price[1] + 10000) {
            this.items[i].isShow = false
          }
        }
        if (this.items[i].isShow) { this.count++ }
      }
    },
    getColor (val) {
      if (val === 1) {
        return '#00C853'
      } else if (val === 2) {
        return '#F9A825'
      } else if (val === 3) {
        return '#F57F17'
      } else {
        return '#F4511E'
      }
    },
    getKindergartenList () {
      http.axios.get(`/kindergartens/?lat=${this.lat}&lng=${this.lng}`).then(({ data }) => {
        for (const i in data) {
          data[i].isShow = true
          data[i].color = this.getColor(data[i].grade)
        }
        this.count = data.length

        this.items = data
        for (const i in data) {
          for (const j in this.ageColumns) {
            let val = Math.floor(data[i][this.ageColumns[j]] / 10000)
            if (val > 30) { val = 30 }
            this.value[j][val]++
          }
        }
      })
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
/* @media (min-width: 1264px){ */
  .result {
    max-width: 1200px !important;
  }
/* } */

label {
  font-size:13px !important;
}

h3 {
  font-size:16px;
}

.v-input--selection-controls__input{
  margin:0 !important;
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
  margin-left:2px !important;
  margin-right:2px !important;
}

.v-ripple__contents {
  display: none !important;
}

.v-list, .v-list-item {
  padding:0;
}

.v-list-item__content {
  padding:0;
  display:block;
}

.kinder_list {
  height:200px;
}

.sr_header--map {
    margin-left: 10px;
    background: URL(//cf.bstatic.com/static/img/map/cta_material/map_cta_background/ab82d9bf871cfe28b1f98ca73ff9c4e41378baef.jpg) no-repeat;
    background-position: center;
    position: relative;
    text-align: center;
    border: 1px solid #bababa;
    border-radius: 3px;
    -webkit-flex-shrink: 0;
    -ms-flex-negative: 0;
    flex-shrink: 0;
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: center;
    -webkit-justify-content: center;
    -ms-flex-pack: center;
    justify-content: center;
    text-decoration: none;
    min-height: 50px;
    max-height: 150px;
}

.sr_header--map_pin {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 20px;
    height: 30px;
    background: URL(//cf.bstatic.com/static/img/map/cta_material/map_cta_pin/630b60fdd032b0b47748700f4d87f64ff78d84cb.png) no-repeat;
    background-size: 20px 30px;
    background-position: 0 0;
    margin-top: -10px;
    -webkit-transform: translateX(-50%) translateY(-50%);
    -ms-transform: translateX(-50%) translateY(-50%);
    transform: translateX(-50%) translateY(-50%);
}
.sr_header--map .switch-map-view {
    min-width: 75px;
    font-size:13px;
    font-weight:700;
    line-height:15.6px;
    display: block;
    white-space: nowrap;
    margin-top: auto;
    -webkit-align-self: flex-end;
    -ms-flex-item-align: end;
    align-self: flex-end;
    background: rgba(255,255,255,0.6);
    color: #0071c2;
    margin: 0;
    margin-top:2px;
    padding: 4px 10px;
}
#right-panel .v-card:hover {
  cursor:pointer;
  border-color: #69F0AE !important;
  box-shadow: 0 0 10px #69F0AE !important;
}
</style>
