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
  props: ['info'],
  data () {
    return {
      series: [{
        data: this.info.data
      }],
      chartOptions: {
        chart: {
          type: 'bar',
          height: 200,
          toolbar: {
            show: false
          },
          unit: this.info.unit
        },
        plotOptions: {
          bar: {
            barHeight: '100%',
            distributed: true,
            horizontal: true,
            dataLabels: {
              position: 'bottom'
            }
          }
        },
        colors: ['#ffa219', '#BDBDBD'],
        dataLabels: {
          enabled: true,
          offsetY: 0,
          formatter (val, { w }) {
            return val + w.config.chart.unit
          },
          offsetX: 200,
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
          categories: ['대봉어린이집', '지역평균']
        },
        yaxis: {
          labels: {
            show: false
          }
        },
        title: {
          text: this.info.title,
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
  },
  watch: {
    info (val) {
      this.chartOptions = {
        chart: {
          type: 'bar',
          height: 200,
          toolbar: {
            show: false
          },
          unit: this.info.unit
        },
        plotOptions: {
          bar: {
            barHeight: '100%',
            distributed: true,
            horizontal: true,
            dataLabels: {
              position: 'bottom'
            }
          }
        },
        colors: ['#ffa219', '#BDBDBD'],
        dataLabels: {
          enabled: true,
          offsetY: 0,
          formatter (val, { w }) {
            return val + w.config.chart.unit
          },
          offsetX: 200,
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
          categories: ['대봉어린이집', '지역평균']
        },
        yaxis: {
          labels: {
            show: false
          }
        },
        title: {
          text: this.info.title,
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
      this.series = [{
        data: this.info.data
      }]
    }
  },
  mounted () {
  }

}
</script>

<style>

</style>
