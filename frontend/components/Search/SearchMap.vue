<template>
  <div id="map" ref="map" style="width:960px;height:600px;margin:0;" />
</template>

<script>
export default {
  props: ['items', 'lat', 'lng', 'change'],
  data () {
    return {
      kakao_API: 'dff523ff715cfa66c3e0461e1f477834',
      selected_lat: '',
      selected_lng: '',
      map: {},
      markers: []
    }
  },
  watch: {
    change () {
      this.changeMarkers()
    }
  },
  mounted () {
    window.kakao && window.kakao.maps ? this.initMap() : this.addScript()
  },
  methods: {
    moveKinder (id) {
      this.$emit('moveKinder', id)
    },
    openMap () {
      this.isMap = true
    },
    changeMarkers () {
      const map = this.map
      const moveKinder = this.moveKinder
      const items = this.items
      for (const i in this.markers) {
        this.markers[i].setMap(null)
      }

      this.markers = []
      for (const i in items) {
        if (!items[i].isShow) { continue }
        const imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png'
        const imageSize = new kakao.maps.Size(24, 35)
        const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize)
        const markerPosition = new kakao.maps.LatLng(items[i].lat, items[i].lng)
        const marker = new kakao.maps.Marker({ position: markerPosition, image: markerImage })
        marker.setMap(this.map)
        this.markers.push(marker)

        const content =
        '<div class="customoverlay">' +
        '  <a href="https://map.kakao.com/link/map/11394059" target="_blank">' +
        `    <span class="title">${items[i].organization_name}</span>` +
        '  </a>' +
        '</div>'

        const position = new kakao.maps.LatLng(items[i].lat, items[i].lng)

        const customOverlay = new kakao.maps.CustomOverlay({
          position,
          content,
          yAnchor: 0.2,
          xAnchor: 0.49
        })
        kakao.maps.event.addListener(marker, 'mouseover', function () {
          customOverlay.setMap(map)
        })

        kakao.maps.event.addListener(marker, 'click', function () {
          moveKinder(items[i].id)
        })

        kakao.maps.event.addListener(marker, 'mouseout', function () {
          customOverlay.setMap(null)
        })
      }
    },
    setMap (map) {
      this.map = map
    },
    initMap () {
      const lat = this.lat
      const lng = this.lng

      const setMap = this.setMap
      const changeMarkers = this.changeMarkers
      setTimeout(function () {
        const container = document.getElementById('map')

        const options = { center: new kakao.maps.LatLng(lat, lng), level: 5 }
        const map = new kakao.maps.Map(container, options)
        setMap(map)
        // 컨트롤러 생성
        const mapTypeControl = new kakao.maps.MapTypeControl()
        map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT)
        const zoomControl = new kakao.maps.ZoomControl()
        map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT)
        changeMarkers()
      }, 100)
    },
    addScript () {
      const script = document.createElement('script')
      /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap)
      script.src = 'https://dapi.kakao.com/v2/maps/sdk.js?appkey=' + this.kakao_API + '&autoload=false'
      document.head.appendChild(script)
    }

  }
}
</script>

<style scoped>
#id {
  position:static !important;
}
.customoverlay {position:relative;bottom:85px;border-radius:6px;border: 1px solid #ccc;border-bottom:2px solid #ddd;float:left;}
.customoverlay:nth-of-type(n) {border:0; box-shadow:0px 1px 2px #888;}
.customoverlay a {display:block;text-decoration:none;color:#000 !important;text-align:center;border-radius:6px;font-size:16px !important;font-weight:bold;overflow:hidden;background: #FFBF00;background: #FFBF00 url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/arrow_white.png) no-repeat right 14px center;}
.customoverlay .title {display:block;text-align:center;background:#fff;margin-right:35px;padding:10px 15px;font-size:16px !important;font-weight:bold;}
.customoverlay:after {content:'';position:absolute;margin-left:-12px;left:50%;bottom:-12px;width:22px;height:12px;background:url('https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/vertex_white.png')}

</style>
