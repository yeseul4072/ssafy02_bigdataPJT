<template>
  <div>
    <v-row style="border:thin solid #E6E6E6; border-radius:15px;">
      <v-col cols="3" align-self="center">
        <v-row justify="center">
          <v-col cols="12" align="center">
            <v-avatar size="12vw">
              <v-img
                :src="'https://www.iconfinder.com/data/icons/female-avatars-vol-1/256/female-portrait-avatar-profile-woman-sexy-afro-2-512.png'"
                height="150px"
                width="150px"
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
      <v-col cols="9" class="py-7">
        <v-row class="pa-3" style="border-left:thin solid #E6E6E6;">
          <v-row style="padding-left:16px;font-size:2vh;font-weight:800;width:100%;">
            "{{ review.title }}""
          </v-row>
          <v-row class="pl-4" style="font-size:1.5vh;width:100%;">
            <div style="display:inline-block" class="pr-3">
              unseng@gmail.com
            </div>
            <i class="fas fas fa-ellipsis-v" style="color:#DEDEDE" />
            <div style="display:inline-block" class="pl-3">
              {{ '2020.09.25' | diffDate }}
            </div>
          </v-row>
          <v-row>
            <v-card-title class="px-4 pt-2 pb-1">
              <v-chip class="success white--text">
                장점
              </v-chip>
            </v-card-title>

            <v-card-text style="overflow:hidden;">
              <!-- https://www.npmjs.com/package/vue-line-clamp -->
              <div v-html="review.pros.replace(/(?:\r\n|\r|\n)/g, '<br />')" />
            </v-card-text>
            <v-divider />
            <v-card-title class="px-4 pt-2 pb-1">
              <v-chip class="pink white--text">
                단점
              </v-chip>
            </v-card-title>

            <v-card-text style="overflow:hidden;">
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
  props: ['review'],
  data () {
    return {
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
