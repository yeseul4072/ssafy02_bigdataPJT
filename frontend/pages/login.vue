<template>
  <div class="login">
    <div class="login-box">
      <v-img
        class="logo"
        :src="require('@/assets/logo.png')"
        contain
        @click="$router.push('/')"
      />
      <a href="/" class="logo" />

      <div class="login-box-wrap">
        <h2 class="login-text">
          대한민국 No.1 어린이집 추천 플랫폼
        </h2>
        <div class="divider" />

        <div class="form">
          <v-text-field
            v-model="id"
            outlined
            color="success"
            label="아이디"
            hide-details
          />
          <v-text-field
            class="mt-5"
            ref="id"
            v-model="password"
            outlined
            color="#0CC476"
            label="비밀번호"
            type="password"
            @keydown.enter="login"
            :error-messages=" error ? error_text : ''"
          />
          <v-list-item style="padding:0;">
            <v-list-item-content style="padding:0">
              <v-checkbox label="아이디 저장" color="success" dense style="margin:0px" />
            </v-list-item-content>
            <v-list-item-action style="margin:0;">
              <a href="#" style="margin-bottom:15px;"> 혹시 비밀번호를 잊으셨나요? </a>
            </v-list-item-action>
          </v-list-item>
          <v-row
            align="center"
            justify="center"
          >
            <v-btn
              color="#0dCA78"
              rounded
              x-large
              dark
              style="margin-top:10px; width:90%;"
              @click="login"
            >
              <span style="font-size:20px">로그인</span>
            </v-btn>
            <div class="add-option">
              <nuxt-link to="/signup">
                회원가입
              </nuxt-link>

              <span class="bar" aria-hidden="true">|</span>
              <a href="#">아이디 찾기</a>
              <span class="bar" aria-hidden="true">|</span>
              <a href="#">비밀번호 찾기</a>
            </div>
          </v-row>
        </div>

        <!-- <div class="other-service">
          <div class="add-option">
            <div class="wrap">
              <p>다른 서비스로 로그인</p>
              <a class="_kakao _serviceIcon" title="kakao" href="#" @mouseover="switchButton" />
              <a class="_naver _serviceIcon" title="naver" href="#" @mouseover="switchButton" />
              <a class="_facebook _serviceIcon" title="facebook" href="#" @mouseover="switchButton" />
            </div>
          </div>
        </div> -->
      </div>
    </div>
    <v-dialog
      v-model="success"
      max-width="400"
    >
      <v-card>
        <v-card-title class="headline">
          <v-container class="justify-center wrap" fluid fill-height>
            <v-row justify="center">
              <v-img
                :src="require('@/assets/success.png')"
                max-width="50"
              />
            </v-row>
            <v-row justify="center" class="mt-3">
              <span style="font-weight:700;">회원가입을 축하드립니다</span>
            </v-row>
          </v-container>
        </v-card-title>
        <v-card-text>대한민국 No.1 어린이집 추천 플랫폼! '어린이ZIP'에서 사랑하는 우리아이가 다닐 어린이집을 찾아보세요!</v-card-text>
        <v-card-actions style="text-align:center">
          <v-spacer></v-spacer>
          <v-btn
            color="primary darken-1"
            text
            @click="success = false"
          >
            확인
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <div class="banner" />
  </div>
</template>

<!-- <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></script> -->
<script>
import http from '@/util/http_common.js'
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
      id: '',
      password: '',
      error: false,
      error_text: '',
      success: false
    }
  },
  computed: {
    ...mapGetters(['isLogin', 'getToken'])
  },
  mounted () {
    this.success = this.$route.query.success
    history.pushState({ data: '' }, '', '/login')
  },
  methods: {
    // switchButton (e) {
    //   const kakaoIcon = $('._kakao')
    //   let className = e.target.classList
    //   for (let i = 0; i < e.target.classList.length; i++) {
    //     if (e.target.classList[i] != '_serviceIcon') { className = e.target.classList[i] }
    //   }
    //   const targetIcon = $(`.${className}`)
    //   kakaoIcon.attr('class', `${className} _serviceIcon`)
    //   targetIcon.attr('class', '_kakao _serviceIcon')
    // },
    getSession () {
      http.axios.get('/rest-auth/user/profile').then(({ data }) => {
        this.$router.app.$store.commit('setUser', data)
      })
      this.$router.push('/home')
    },
    login () {
      http.axios.post('/rest-auth/login/', {
        username: this.id,
        password: this.password
      }).then(({ data }) => {
        this.$router.app.$store.commit('setIsLogin', true)
        this.$router.app.$store.commit('setToken', `Token ${data.key}`)
        this.getSession()
      }).catch(() => {
        this.error = true
        this.error_text = '아이디 또는 비밀번호가 일치하지 않습니다.'
        this.$refs.id.focus()
      })
    }
  }
}
</script>

<style scoped>
    a {
      text-decoration: none;
    }

    .login{
        display: flex;
        min-width: 1200px;
    }
    .banner {
        position: relative;
        padding: 48px;
        width: 100%;
        min-height: 100vh;
        max-width: 768px;
        /* background: url(/bg.png) center center / cover no-repeat; */
        background-image: linear-gradient(45deg, rgb(13,202,120), rgb(11,203,156)); min-height:100%;
        display: flex;
    }
    .login-box {
        display: flex;
        flex-direction: column;
        background-color: rgb(255, 255, 255);
        width: calc(100% - 768px);
        min-height: 100vh;
    }
    .login-box-wrap {
        width: 480px;
        margin: auto;
    }
    .login-text{
      text-align:center;
      color:#0CC476;
      padding-bottom:20px;
    }

    .divider {
      margin:auto;
      margin-bottom:20px;
      border-bottom:1px solid #0CC476;
      width:75px;
      border-width: 5px;
      border-radius: 5px;
    }

    .other-service {
        font-size:14px;
        line-height:14px;
        padding-top:18px;
        text-align:center;
        color:#8e8e8e;
    }
    .bar{
        display: inline-block;
        width:1px;
        height:18px;
        margin: 2px 3px;
        text-indent: -999em;
        background: #e4e4e5;
        vertical-align: bottom;
    }
    .other-service .bar {
        margin: 0 3px;
    }

    ._kakao{
        background-color: #ffcd00;
        background-image: url(https://statics.goorm.io/images/social/logo/kakaoLogo.svg);
    }

    ._naver{
        background-color: #1dc800;
        background-image: url(https://statics.goorm.io/images/social/logo/naverLogo.svg);
    }
    ._facebook{
        background-color: #3d5a98;
        background-image: url("https://statics.goorm.io/images/social/logo/FacebookLogo.svg");
    }

     ._serviceIcon{
        background-repeat: no-repeat;
        background-position: center;
        width: 40px;
        height: 40px;
        border-radius: 3px;
        -webkit-box-shadow: 0 0 1px 0 rgba(0, 0, 0, 0.12), 0 1px 1px 0 rgba(0, 0, 0, 0.24);
        box-shadow: 0 0 1px 0 rgba(0, 0, 0, 0.12), 0 1px 1px 0 rgba(0, 0, 0, 0.24);
        display: -ms-inline-flexbox;
        display: inline-flex;
        -ms-flex-pack: center;
        justify-content: center;
        margin:10px;
     }
    .add-option{
        margin-top: 30px;
    }
    .v-input__slot{
      margin:0 !important;
    }

    .v-ripple__container {
      display:none;
    }

    @media(max-width:768px){
      .banner {
        display: none;
      }
    }
    .logo {
      margin-top:1%;
      margin-left:3%;
      height:50px;
      max-height:70px;
      width:50px;
    }
    .logo:hover{
      cursor: pointer;
    }
</style>
