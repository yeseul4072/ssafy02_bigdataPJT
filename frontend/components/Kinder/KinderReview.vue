<template>
  <div>
    <v-row style="border:thin solid #E6E6E6;">
      <v-col cols="3" align-self="center">
        <v-row justify="center">
          <v-col cols="12" align="center">
            <v-avatar size="18vh">
              <v-img
                :src="'https://www.iconfinder.com/data/icons/female-avatars-vol-1/256/female-portrait-avatar-profile-woman-sexy-afro-2-512.png'"
              />
            </v-avatar>
          </v-col>
          <v-col cols="12" align="center">
            <v-rating
              :value="4.5"
              color="orange"
              background-color="orange lighten-3"
              dense
              half-increments
              readonly
              size="1.5vw"
              style="display:inline-block;"
            />
            <span style="font-size:1.2vw;font-weight:800;">4.5</span>
          </v-col>
          <v-col cols="12" align="center" class="py-0">
            <v-row class="py-0">
              <v-col cols="4" class="py-0" align="left" style="padding-right:0;">
                <span style="font-size:1.0vw;font-weight:800;">원장님</span>
              </v-col>
              <v-col cols="8" class="py-0">
                <v-rating
                  :value="5"
                  color="orange"
                  background-color="orange lighten-3"
                  dense
                  half-increments
                  readonly
                  size="1.0vw"
                  style="display:inline-block;"
                />
              </v-col>
            </v-row>
          </v-col>
          <v-col cols="12" align="center" class="py-0">
            <v-row class="py-0">
              <v-col cols="4" class="py-0" align="left" style="padding-right:0;">
                <span style="font-size:1.0vw;font-weight:800;">선생님</span>
              </v-col>
              <v-col cols="8" class="py-0">
                <v-rating
                  :value="4.5"
                  color="orange"
                  background-color="orange lighten-3"
                  dense
                  half-increments
                  readonly
                  size="1.0vw"
                  style="display:inline-block;"
                />
              </v-col>
            </v-row>
          </v-col>
          <v-col cols="12" align="center" class="py-0">
            <v-row class="py-0">
              <v-col cols="4" class="py-0" align="left" style="padding-right:0;">
                <span style="font-size:1.0vw;font-weight:800;">보육환경</span>
              </v-col>
              <v-col cols="8" class="py-0">
                <v-rating
                  :value="4"
                  color="orange"
                  background-color="orange lighten-3"
                  dense
                  half-increments
                  readonly
                  size="1.0vw"
                  style="display:inline-block;"
                />
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="9" style="padding-top:50px;padding-bottom:50px;">
        <v-row style="padding:10px;border-left:thin solid #E6E6E6;">
          <v-row style="padding-left:16px;font-size:2vh;font-weight:800;width:100%;">
            "{{ review.title }}""
          </v-row>
          <v-row style="padding-left:16px;font-size:1.5vh;width:100%;">
            <div style="display:inline-block" class="pr-3">
              unseng@gmail.com
            </div>
            <i style="color:#DEDEDE" class="fas fas fa-ellipsis-v" />
            <div style="display:inline-block" class="pl-3">
              {{ '2020.09.25' | diffDate }}
            </div>
          </v-row>
          <v-row>
            <v-card-title style="height:10%">
              <v-chip class="success white--text">
                장점
              </v-chip>
            </v-card-title>

            <v-card-text style="height:13vh;overflow:hidden;">
              <!-- https://www.npmjs.com/package/vue-line-clamp -->
              <div v-html="review.pros.replace(/(?:\r\n|\r|\n)/g, '<br />')" />
            </v-card-text>
            <v-divider />
            <v-card-title style="height:10%">
              <v-chip class="pink white--text">
                단점
              </v-chip>
            </v-card-title>

            <v-card-text style="height:13vh">
              <div v-html="review.cons.replace(/(?:\r\n|\r|\n)/g, '<br />')" />
            </v-card-text>
          </v-row>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  filters: {
    diffDate (val) {
      let diff = (new Date() - new Date(val)) / 1000
      if (diff < 60) { return '방금 전' }
      diff /= 60
      if (diff < 60) { return parseInt(diff) + '분 전' }

      diff /= 60
      if (diff < 24) { return parseInt(diff) + '시간 전' }

      diff /= 24
      if (diff < 7) { return parseInt(diff) + '일 전' }
      if (diff < 30) { return parseInt(diff / 7) + '주 전' }
      if (diff < 365) { return parseInt(diff / 30) + '달 전' }
      return parseInt(diff / 365) + '년 전'
    },
    filterWriter (val) {
      return `by ${val}`
    }
  },
  data () {
    return {
      review: {
        name: '대봉어린이집',
        tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
        url: 'kinder_temp.jpg',
        title: '믿고 맡길 수 있는 어린이집',
        stars: 5,
        pros: '1원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.',
        cons: '1원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.'
      }
    }
  }
}
</script>

<style scoped>
  .vertical-line{
      display: inline-block;
      border-left: 1px solid #ccc;
      margin: 0 10px;
      height: 125px;
  }
</style>
