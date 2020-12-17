<template>
  <div id="carte">
    <l-map :center="[45.74, 4.85]" :min-zoom="10" :zoom="15" :max-bounds="zoneRestreinte">
      <l-tile-layer
        :url="url.api + url.mapStyle[1] + url.tilesToken"
        :attribution="attribution"
      />
      <l-marker ref="myMarker" :lat-lng="[45.74, 4.85]" />
    </l-map>
  </div>
</template>



<script>
import 'leaflet/dist/leaflet.css'
import 'leaflet.markercluster/dist/MarkerCluster.css'
import 'leaflet.markercluster/dist/MarkerCluster.Default.css'

export default {
  data() {
    return {
      url: {
        api: 'https://api.mapbox.com/styles/v1/',
        mapStyle: ['mapbox/streets-v11', 'ddddd44/ckdk8f3d80wpo1ipci6mv9bo5'],
        tilesToken:
          '/tiles/{z}/{x}/{y}?fresh=true&title=copy&access_token=pk.eyJ1IjoiZGRkZGQ0NCIsImEiOiJjazRtdm01NHQwOG14M21wNWdsdXY1djhqIn0.GuEePwUCtxgMwBMdjBy7WA',
      },
      zoneRestreinte: [[45, 4.8], [46, 4.9]],
      attribution: "&copy; <a href=\"https://docs.mapbox.com/api/\">Mapbox</a>",
    }
  },
  mounted() {
      this.$nextTick(() => {
        let reff = this.$refs.myMarker.mapObject;
        reff._icon.src = "http://cdn.onlinewebfonts.com/svg/img_267353.svg"
        console.log(reff);
      });
    },
}
</script>
<style lang="scss" scoped>
#carte {
  height: 500px;
  border-style: solid;
  border-color: darkblue;
}
</style>
