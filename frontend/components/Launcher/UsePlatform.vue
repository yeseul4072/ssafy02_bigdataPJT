<template>
  <div class="l2_main">
    <div
      align="center"
      style="width=100%; padding-top:70px; font-size:2.2rem; font-weight:550; color: #F257A0;"
    >
      어린이ZIP은 지금?
    </div>
    <div
      align="center"
      style="width=100%; padding-top:30px; font-size:1rem;"
    >
      <button class="l2_button" @click="test(123)">
        사용자 수
      </button>
      <button class="l2_button" @click="test(50000)">
        국내 어린이집 수
      </button>
      <button class="l2_button" @click="test(12131231)">
        리뷰 수
      </button>
    </div>
    <div
      class="iCountUp"
      align="center"
      style="width=100%;"
    >
      <ICountUp
        :delay="delay"
        :end-val="endVal"
        :options="options"
        @ready="onReady"
      />
    </div>
  </div>
</template>

<script>
import ICountUp from 'vue-countup-v2'

export default {
  components: {
    ICountUp
  },
  data () {
    return {
      delay: 1000,
      endVal: 120500,
      startVal: 0,
      options: {
        duration: 3,
        useEasing: true,
        useGrouping: true,
        separator: ',',
        decimal: '.',
        prefix: '',
        suffix: ''
      }
    }
  },
  mounted () {

  },
  methods: {
    onReady (instance, CountUp) {
      const that = this
      instance.update(that.endVal)
    },
    test (count) {
      this.endVal = count
    }
  }
}
</script>

<style scoped>
.l2_main{
    width:100%;
    height:500px;
}
.iCountUp {
    font-size: 8em;
    margin: 0;
    color: #F257A0;
}

.l2_button{
  margin-left: 10px;
  margin-right: 10px;
}
</style>
