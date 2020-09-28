<template>
  <div id="chart">
    <v-row>
      <apexchart type="donut" :options="chartOptions" :series="series" />
    </v-row>
  </div>
</template>

<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></script>
<script>
import VueApexCharts from 'vue-apexcharts'
export default {
  props: ['title','number','name','color','unit'],
  components: {
    apexchart: VueApexCharts
  },
  data () {
    return {
      series: this.number,
      chartOptions: {
        chart: {
          type: 'donut',
          width: 500,
          unit: this.unit
        },
        dataLabels: {
          enabled: true,
          formatter (val, { seriesIndex, dataPointIndex, w }) {
            return w.config.series[seriesIndex] + w.config.chart.unit
          },
          style: {
            fontSize: '12px',
            colors: ['#304758'],
            fontFamily: 'NanumSquareRound'
          }
        },
        colors: this.color,
        labels: this.name,
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 380
            }
          }
        }],
        legend: {
          show: false,
          position: 'right',
          offsetY: 0,
          onItemHover: {
            highlightDataSeries: true
          }
        },
        tooltip: {
          enabled: true,
          enabledOnSeries: undefined,
          shared: true,
          followCursor: false,
          intersect: false,
          inverseOrder: false,
          fillSeriesColor: false,
          theme: 'dark',
          style: {
            fontSize: '12px'
          },
          onDatasetHover: {
            highlightDataSeries: true
          },
          x: {
            show: false,
            format: '',
            formatter: undefined
          },
          y: {
              formatter: function(value, w){
                return value + w.config.chart.unit;
            }
          },
          z: {
            formatter: undefined,
            title: 'Size: '
          },
          marker: {
            show: true
          },
          fixed: {
            enabled: false,
            position: 'topRight',
            offsetX: 0,
            offsetY: 0
          }
        },
        plotOptions: {
          pie: {
            expandOnClick: false,
            donut: {
              labels: {
                value: {

                }
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
        },
        title: {
            text: this.title,
            align: 'center',
            margin: 10,
            offsetX: 0,
            offsetY: 0,
            floating: false,
            style: {
              fontSize:  '18px',
              fontWeight:  '800',
              fontFamily:  'NanumSquareRound',
              color:  '#263238'
            },
        }
      }

    }
  },
  methods: {

  },
  mounted() {
    $('.apexcharts-pie-area').on('mouseover', (event) => {
      $(`#${event.target.ownerSVGElement.id}`).find('.apexcharts-pie-area').attr('fill-opacity', 0.3);
      $(`#${event.target.id}`).attr('fill-opacity', 1.0);
    })
    $('.apexcharts-pie-area').on('mouseleave', (event) => {
      $(`#${event.target.ownerSVGElement.id}`).find('.apexcharts-pie-area').attr('fill-opacity', 1.0);
    })
  }
}
</script>

<style scoped>
.apexcharts-pie-series :hover{
  background-color:black !important;
}
</style>
