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
              :value="(rateDirector+rateTeacher+rateEnv)/3"
              color="orange"
              background-color="orange lighten-3"
              dense
              half-increments
              readonly
              size="1.5vw"
              style="display:inline-block;"
            />
            <span style="font-size:1.2vw;font-weight:800;">{{ ((rateDirector+rateTeacher+rateEnv)/3).toFixed(1) }}</span>
          </v-col>
          <v-col cols="12" align="center" class="py-0">
            <v-row class="py-0">
              <v-col cols="4" class="py-0" align="left" style="padding-right:0;">
                <span style="font-size:1.0vw;font-weight:800;">원장님</span>
              </v-col>
              <v-col cols="8" class="py-0">
                <v-rating
                  v-model="rateDirector"
                  color="orange"
                  background-color="orange lighten-3"
                  dense
                  hover
                  half-increments
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
                  v-model="rateTeacher"
                  color="orange"
                  background-color="orange lighten-3"
                  dense
                  hover
                  half-increments
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
                  v-model="rateEnv"
                  color="orange"
                  background-color="orange lighten-3"
                  dense
                  hover
                  half-increments
                  size="1.0vw"
                  style="display:inline-block;"
                />
              </v-col>
            </v-row>
          </v-col>
          <v-col cols="12" align="center" class="py-0">
            <span style="font-size:0.8vw;color:#4f4f4f;">* 항목별 별을 눌러 평점을 주세요</sapn>
            </span>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="9" class="py-7">
        <v-row class="pa-3" style="border-left:thin solid #E6E6E6;">
          <v-row style="padding-left:16px;font-size:2vh;font-weight:800;width:100%;">
            <v-col>
              <v-row>
                <v-text-field
                  v-model="title"
                  class="px-3"
                  :rules="rules.require"
                  label="제목을 입력하세요"
                  required
                />
              </v-row>
            </v-col>
          </v-row>

          <v-card-text style="overflow:hidden;">
            <!-- https://www.npmjs.com/package/vue-line-clamp -->
            <v-textarea
              v-model="pros"
              color="teal"
              :rules="rules.text"
              label="장점"
            />
          </v-card-text>
          <v-divider />
          <v-card-text style="overflow:hidden;">
            <v-textarea
              v-model="cons"
              color="#ffabf0"
              :rules="rules.text"
              label="단점"
            />
            <div style="text-align:center; color:red;">
              {{ msg }}
            </div>
            <div style="text-align:right;">
              <v-btn
                rounded
                outlined
                color="rgb(236, 236, 236)"
                dark
                @click="writeReview"
              >
                <span style="color:orange;">작성</span>
              </v-btn>
            </div>
          </v-card-text>
        </v-row>
      </v-col>
    </v-row>
    </v-col>
    </v-row>
  </div>
</template>

<script>
import http from '@/util/http_common.js'

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
      rateDirector: 0,
      rateTeacher: 0,
      rateEnv: 0,
      title: '',
      pros: '',
      cons: '',
      rules: {
        require: [val => (val || '').length > 0 || '입력이 필요합니다.'],
        text: [val => (val || '').length > 9 || '10자이상 입력이 필요합니다.']
      },
      msg: ''
    }
  },
  methods: {
    writeReview () {
      let msg = ''
      if (this.rateDirector === 0 || this.rateTeacher === 0 || this.rateEnv === 0) { msg = '별점을 입력해주세요.' }
      if (this.title.length <= 0 || this.pros.length <= 9 || this.cons.length <= 9) { msg += ' 올바른 형식으로 입력해주세요.' }
      if (msg !== '') {
        this.msg = msg
      } else {
        this.msg = ''

        http.axios.post(`/kindergartens/${this.$route.params.id}/reviews/`, {
          title: this.title,
          score_teacher: this.rateTeacher,
          score_director: this.rateDirector,
          score_environment: this.rateEnv,
          pros: this.pros,
          cons: this.cons
        }).then(({ data }) => {
          this.$emit('close-write')
        })
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
