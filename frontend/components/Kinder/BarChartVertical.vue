<template>
  <div id="chart">
    <apexchart type="bar" height="200" :options="chartOptions" :series="series" />
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
  components: {
    apexchart: VueApexCharts
  },
  props: ['title'],
  data () {
    return {
      series: [{
        data: [43, 20]
      }],
      chartOptions: {
        chart: {
          type: 'bar',
          height: 380,
          toolbar: {
            show: false
          }
        },
        plotOptions: {
          bar: {
            barHeight: '100%',
            distributed: true,
            dataLabels: {
              position: 'bottom'
            }
          }
        },
        colors: ['#6cd3c7', '#fd8c63'],
        dataLabels: {
          enabled: true,
          formatter (val) {
            return val + '명'
          },
          offsetY: 100,
          style: {
            fontSize: '12px',
            colors: ['#304758'],
            fontFamily: 'NanumSquareRound'
          },
          dropShadow: {
            enabled: true
          }
        },
        stroke: {
          width: 1,
          colors: ['#fff']
        },
        xaxis: {
          categories: ['아동', '교사']
        },
        yaxis: {
          labels: {
            show: false
          }
        },
        title: {
          text: this.title,
          align: 'center',
          margin: 10,
          offsetX: 0,
          offsetY: 0,
          floating: false,
          style: {
            fontSize: '18px',
            fontWeight: '800',
            fontFamily: 'NanumSquareRound',
            color: '#263238'
          }
        },
        tooltip: {
          enabled: false,
          theme: 'dark',
          x: {
            show: false
          },
          y: {
            title: {
              formatter () {
                return ''
              }
            }
          }
        },
        states: {
          hover: {
            filter: {
              type: 'none',
              value: 0.15
            }
          },
          active: {
            allowMultipleDataPointsSelection: false,
            filter: {
              type: 'none',
              value: 0.35
            }
          }
        }
      }
    }
  }

}
</script>

<style>

</style>
