<template>
  <div class="l2_main">
    <div
      align="center"
      style="width=100%; padding-top:70px; font-size:2rem;"
    >
      어린이ZIP은 지금?
    </div>
    <div
      align="center"
      style="width=100%; padding-top:30px; font-size:1rem;"
    >
      <button @click="insertICountNumber(200000)">
        사용자 수
      </button>
      <button @click="insertICountNumber(50000)">
        국내 어린이집 수
      </button>
      <button @click="insertICountNumber(12131231)">
        리뷰 수
      </button>
    </div>
    <div
      class="iCountUp"
      align="center"
      style="width=100%;"
    >
      <ICountUp
        :start-val="startVal"
        :end-val="endVal"
        :decimals="decimals"
        :duration="duration"
        :options="options"
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
      startVal: 0,
      endVal: 0,
      decimals: 0,
      duration: 2.5,
      options: {
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
    insertICountNumber (count) {
      this.decimals = 0
      this.startVal = 0
      this.endVal = count
    }
  }
}
</script>

<style>
.l2_main{
    width:100%;
    height:500px;
}
.iCountUp {
    font-size: 9em;
    margin: 0;
    color: #4d63bc;
  }
</style>
