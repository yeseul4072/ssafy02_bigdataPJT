<template>
  <div id="map" ref="map" style="width:96vw;height:80vh;" />
</template>

<script>
export default {
  data () {
    return {
      kakao_API: 'dff523ff715cfa66c3e0461e1f477834',
      selected_lat: '',
      selected_lng: ''
    }
  },
  watch: {
    selected_lat (lat) {
      this.$emit('setLat', lat)
    },
    selected_lng (lng) {
      this.$emit('setLng', lng)
    }
  },
  mounted () {
    window.kakao && window.kakao.maps ? this.initMap() : this.addScript()
  },
  methods: {
    openMap () {
      this.isMap = true
    },
    initMap () {
      const self = this
      setTimeout(function () {
        const container = document.getElementById('map')
        const options = { center: new kakao.maps.LatLng(33.450701, 126.570667), level: 3 }
        const map = new kakao.maps.Map(container, options)
        // 컨트롤러 생성
        const mapTypeControl = new kakao.maps.MapTypeControl()
        map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT)
        const zoomControl = new kakao.maps.ZoomControl()
        map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT)
        const center = map.getCenter()
        const imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png'
        const imageSize = new kakao.maps.Size(24, 35)
        const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize)
        const marker = new kakao.maps.Marker({ position: center, image: markerImage })
        marker.setMap(map)
        const content = '<div class="customoverlay">' +
                          '  <a href="javascript:void(0);">' +
                          '    <span class="title">선택된 중심지역</span>' +
                          '  </a>' +
                          '</div>'
        const position = new kakao.maps.LatLng(center.getLat(), center.getLng())

        // 오버레이생성
        let customOverlay = new kakao.maps.CustomOverlay({
          map,
          position,
          content,
          yAnchor: 0.2,
          xAnchor: 0.49
        })
        kakao.maps.event.addListener(map, 'click', function (mouseEvent) {
          const latlng = mouseEvent.latLng
          marker.setPosition(latlng)
          self.selected_lat = latlng.getLat()
          self.selected_lng = latlng.getLng()
          const position = new kakao.maps.LatLng(latlng.getLat(), latlng.getLng())

          customOverlay.setMap(null)
          customOverlay = new kakao.maps.CustomOverlay({
            map,
            position,
            content,
            yAnchor: 0.2,
            xAnchor: 0.49
          })
        })
      }, 100)
    },
    addScript () {
      const script = document.createElement('script')
      /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap)
      script.src = 'http://dapi.kakao.com/v2/maps/sdk.js?appkey=' + this.kakao_API + '&autoload=false'
      document.head.appendChild(script)
    }

  }
}
</script>

<style>
#id {
  position:static !important;
}
.customoverlay {position:relative;bottom:85px;border-radius:6px;border: 1px solid #ccc;border-bottom:2px solid #ddd;float:left;}
.customoverlay:nth-of-type(n) {border:0; box-shadow:0px 1px 2px #888;}
.customoverlay a {display:block;text-decoration:none;color:#000 !important;text-align:center;border-radius:6px;font-size:16px !important;font-weight:bold;overflow:hidden;background: #FFBF00;background: #FFBF00 url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/arrow_white.png) no-repeat right 14px center;}
.customoverlay .title {display:block;text-align:center;background:#fff;margin-right:35px;padding:10px 15px;font-size:16px !important;font-weight:bold;}
.customoverlay:after {content:'';position:absolute;margin-left:-12px;left:50%;bottom:-12px;width:22px;height:12px;background:url('https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/vertex_white.png')}

</style>
