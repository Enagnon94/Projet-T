<template>
  <div id="carte">
    <l-map
      :center="[45.74, 4.85]"
      :min-zoom="10"
      :zoom="15"
      :max-bounds="zoneRestreinte"
    >
      <l-tile-layer :url="urlTuiles" :attribution="attribution" />
      <span v-for="(flamme, f) in flammes" :key="f">
        <l-marker ref="flamme" :lat-lng="flamme.coord" :key="f">
          <l-popup>ça brule ici</l-popup>
          <l-icon :iconUrl="iconFlamme" :iconSize="flamme.rayon*coefficientIconSize"></l-icon>
        </l-marker>
      </span>
    </l-map>
  </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import "leaflet.markercluster/dist/MarkerCluster.css";
import "leaflet.markercluster/dist/MarkerCluster.Default.css";

export default {
  props: {
    flammes: {
      type: Array,
      required: false,
      default: () => [
        { rayon: 1, intensite: 1, coord: [45.74, 4.85] },
        { rayon: 3, intensite: 1, coord: [45.74, 4.852] },
      ],
    },
    casernes: { type: Array, required: false },
    camions: { type: Array, required: false },
  },
  data() {
    return {
      urlTuiles:
        "https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?fresh=true&title=copy&access_token=pk.eyJ1IjoiZGRkZGQ0NCIsImEiOiJjazRtdm01NHQwOG14M21wNWdsdXY1djhqIn0.GuEePwUCtxgMwBMdjBy7WA",
      zoneRestreinte: [
        [45, 4.8],
        [46, 4.9],
      ],
      attribution: '&copy; <a href="https://docs.mapbox.com/api/">Mapbox</a>',
      iconFlamme: "http://cdn.onlinewebfonts.com/svg/img_267353.svg",
      coefficientIconSize: "20"
    };
  },
};
</script>
<style lang="scss" scoped>
#carte {
  height: 100%;
  width: 100%;
  border-style: solid;
  border-color: darkblue;
}
</style>
