<template>
  <div class="l2_main">
    <div
      align="center"
      style="width=100%; padding-top:150px; font-size:2.2rem; font-weight:550; color: #0CCB8A;"
    >
      어린이ZIP은 지금?
    </div>
    <div
      align="center"
      style="width=100%; padding-top:30px; font-size:1rem;"
    >
      <span class="l2_button" :style="{textDecoration: underline[0]}" @click="updateCount(userCount);">
        사용자 수
      </span>
      <span class="l2_button" :style="{textDecoration: underline[1]}" @click="updateCount(kindergartenCount)">
        국내 어린이집 수
      </span>
      <span class="l2_button" :style="{textDecoration: underline[2]}" @click="updateCount(reviewCount)">
        리뷰 수
      </span>
    </div>
    <div align="center">
      <div
        class="iCountUp"
        align="center"
        style="width=100%;"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="5vh"
          height="15vh"
          viewBox="0 0 8 19"
          class="aW-AU"
          role="presentation"
        ><path d="M4.8 15.89a10.68 10.68 0 0 1-.05-.05l.05.05zm-1.14-1.93c-.25-.54-.48-1.12-.68-1.75a.3.3 0 0 0 .12-.04c.78-.48 1.41-1.01 1.6-1.55.2-.54.03-1.33-.29-2.16a.31.31 0 0 0-.46-.14c-.66.4-1.2.85-1.47 1.3 0-.34-.04-.65-.15-.89-.01-.55.03-1.07.12-1.57.87.1 1.68.06 2.16-.23.47-.29.87-.99 1.18-1.81a.2.2 0 0 0-.17-.26c-.88-.1-1.7-.06-2.18.23l-.03-.04.03.04c-.2.12-.4.33-.58.59a7.65 7.65 0 0 1 1.39-2.25l.28.02.5.03c.38 0 .67-.08.9-.28A4.8 4.8 0 0 0 7 .9a.2.2 0 0 0-.2-.2c-.7-.01-1.97.33-2.43.71-.24.21-.36.51-.4.96l-.02.4c0 .22-.01.33-.03.44a8.13 8.13 0 0 0-.96 1.35c0-.1 0-.19-.03-.27-.11-.5-.62-1.07-1.27-1.6a.18.18 0 0 0-.28.07C1 3.5.78 4.23.9 4.73c.1.5.62 1.07 1.27 1.58a.2.2 0 0 0 .05.03 8.22 8.22 0 0 0-.29 1.87 5.53 5.53 0 0 0-1.47-.89c-.13-.06-.27.01-.3.14-.2.87-.23 1.68.03 2.17l-.05.02.05-.02c.26.5.97.96 1.83 1.33.06.03.14.02.2 0l.02.11c.2.84.45 1.6.74 2.31a4.77 4.77 0 0 0-2.38-.11c-.16.02-.26.17-.2.3.33.92.79 1.7 1.33 2l-.02.05.02-.05c.54.31 1.46.33 2.47.18l.22.32c.63.87 1.3 1.55 1.98 2.04a5.8 5.8 0 0 0 .66.42 2 2 0 0 0 .3.14c.17.03.3.03.4-.02.24-.13.32-.45.16-.72-.1-.17-.3-.32-.7-.56l-.5-.3a12.12 12.12 0 0 1-.72-.46.21.21 0 0 0 .02-.03c.45-.92.7-1.8.56-2.4-.14-.6-.78-1.25-1.6-1.85a.2.2 0 0 0-.3.09 4.6 4.6 0 0 0-.58 2.25 4.23 4.23 0 0 0-.44-.71z" /></svg>
        <ICountUp
          :delay="delay"
          :end-val="endVal"
          :options="options"
          @ready="onReady"
        />
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="5vh"
          height="15vh"
          viewBox="0 0 8 19"
          class="_1KCw5"
          role="presentation"
        ><path d="M4.8 15.89a10.68 10.68 0 0 1-.05-.05l.05.05zm-1.14-1.93c-.25-.54-.48-1.12-.68-1.75a.3.3 0 0 0 .12-.04c.78-.48 1.41-1.01 1.6-1.55.2-.54.03-1.33-.29-2.16a.31.31 0 0 0-.46-.14c-.66.4-1.2.85-1.47 1.3 0-.34-.04-.65-.15-.89-.01-.55.03-1.07.12-1.57.87.1 1.68.06 2.16-.23.47-.29.87-.99 1.18-1.81a.2.2 0 0 0-.17-.26c-.88-.1-1.7-.06-2.18.23l-.03-.04.03.04c-.2.12-.4.33-.58.59a7.65 7.65 0 0 1 1.39-2.25l.28.02.5.03c.38 0 .67-.08.9-.28A4.8 4.8 0 0 0 7 .9a.2.2 0 0 0-.2-.2c-.7-.01-1.97.33-2.43.71-.24.21-.36.51-.4.96l-.02.4c0 .22-.01.33-.03.44a8.13 8.13 0 0 0-.96 1.35c0-.1 0-.19-.03-.27-.11-.5-.62-1.07-1.27-1.6a.18.18 0 0 0-.28.07C1 3.5.78 4.23.9 4.73c.1.5.62 1.07 1.27 1.58a.2.2 0 0 0 .05.03 8.22 8.22 0 0 0-.29 1.87 5.53 5.53 0 0 0-1.47-.89c-.13-.06-.27.01-.3.14-.2.87-.23 1.68.03 2.17l-.05.02.05-.02c.26.5.97.96 1.83 1.33.06.03.14.02.2 0l.02.11c.2.84.45 1.6.74 2.31a4.77 4.77 0 0 0-2.38-.11c-.16.02-.26.17-.2.3.33.92.79 1.7 1.33 2l-.02.05.02-.05c.54.31 1.46.33 2.47.18l.22.32c.63.87 1.3 1.55 1.98 2.04a5.8 5.8 0 0 0 .66.42 2 2 0 0 0 .3.14c.17.03.3.03.4-.02.24-.13.32-.45.16-.72-.1-.17-.3-.32-.7-.56l-.5-.3a12.12 12.12 0 0 1-.72-.46.21.21 0 0 0 .02-.03c.45-.92.7-1.8.56-2.4-.14-.6-.78-1.25-1.6-1.85a.2.2 0 0 0-.3.09 4.6 4.6 0 0 0-.58 2.25 4.23 4.23 0 0 0-.44-.71z" /></svg>
      </div>
    </div>
  </div>
</template>

<script>
import ICountUp from 'vue-countup-v2'
import http from '@/util/http_common.js'
export default {
  components: {
    ICountUp
  },
  data () {
    return {
      // 사용자 수, 어린이집 수, 리뷰 수
      userCount: 0,
      kindergartenCount: 0,
      reviewCount: 0,

      // CountUp.js에서 쓸 데이터
      delay: 1000,
      endVal: 0,
      startVal: 0,
      options: {
        duration: 3,
        useEasing: true,
        useGrouping: true,
        separator: ',',
        decimal: '.',
        prefix: '',
        suffix: ''
      },
      underline: []
    }
  },
  mounted () {
    http.axios.get('/kindergartens/counts/')
      .then(({ data }) => {
        this.userCount = (data.users + 1) * 57
        this.kindergartenCount = (data.kindergartens + 1) * 57
        this.reviewCount = (data.reviews + 1) * 113
        this.endVal = this.userCount
        this.underline[0] = 'underline'
        this.test()
      })
  },
  methods: {
    onReady (instance, CountUp) {
      const that = this
      instance.update(that.endVal)
    },
    updateCount (count) {
      this.endVal = count
    },
    test () {
      const uc = this.updateCount
      const euc = this.userCount
      const ekc = this.kindergartenCount
      const erc = this.reviewCount
      const ul = this.underline
      let i = 1
      setInterval(function () {
        if (i % 3 === 0) {
          for (let j = 0; j < 3; j++) {
            ul[j] = 'none'
          }
          ul[0] = 'underline'
          uc(euc)
        } else if (i % 3 === 1) {
          for (let j = 0; j < 3; j++) {
            ul[j] = 'none'
          }
          ul[1] = 'underline'
          uc(ekc)
        } else if (i % 3 === 2) {
          for (let j = 0; j < 3; j++) {
            ul[j] = 'none'
          }
          ul[2] = 'underline'
          uc(erc)
        }
        i++
      }, 5000)
    }
  }
}
</script>

<style scoped>
.l2_main{
    width:100%;
    height:600px;
}
.iCountUp {
    font-size: 8em;
    margin: 0;
    color: #0CCB8A;
}

.l2_button{
  margin-left: 10px;
  margin-right: 10px;
}

.l2_button:hover{
  text-decoration: underline !important;
  cursor: pointer;
}

._1KCw5 {
    fill: #E9E9E9;
    padding-top: 35px;
    margin-left: 40px;
    margin-right: 5px ;
    transform: scaleX(-1) rotate(-20deg);

}
.aW-AU {
    fill: #E9E9E9;
    padding-top: 35px;
    margin-left: 5px;
    margin-right: 35px;
    transform: rotate(-20deg);
}
</style>
