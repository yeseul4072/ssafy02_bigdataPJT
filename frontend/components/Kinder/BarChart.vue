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
  data () {
    return {
      series: [{
        data: [43, 20]
      }],
      chartOptions: {
        chart: {
          type: 'bar',
          height: 380
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
        colors: ['#FACC2E', '#BDBDBD'],
        dataLabels: {
          enabled: true,
          textAnchor: 'start',
          style: {
            colors: ['#fff']
          },
          formatter (val, opt) {
            return opt.w.globals.labels[opt.dataPointIndex] + ':  ' + val
          },
          offsetX: 0,
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
          text: '교사평균 근속연수',
          align: 'center',
          floating: true
        },
        tooltip: {
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
        }
      }
    }
  }

}
</script>

<style>

</style>
