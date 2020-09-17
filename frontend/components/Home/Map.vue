<template>
  <div id="map" ref="map" style="width:100vw;height:80vh;margin:0;" />
</template>

<script>
export default {
  mounted () {
    window.kakao && window.kakao.maps ? this.initMap() : this.addScript()
  },
  methods: {
    openMap () {
      this.isMap = true
    },
    initMap () {
      setTimeout(function () {
        const container = document.getElementById('map')
        const options = { center: new kakao.maps.LatLng(33.450701, 126.570667), level: 3 }
        const map = new kakao.maps.Map(container, options)
        const marker = new kakao.maps.Marker({ position: map.getCenter() })
        marker.setMap(map)
      // this.$refs.map.style.position = 'relative'
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
</style>
