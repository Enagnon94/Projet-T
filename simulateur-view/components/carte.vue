<template>
  <div id="carte">
    <l-map
      :center="centreCarte"
      :min-zoom="12"
      :zoom="15"
      :max-bounds="zoneRestreinte"
    >
      <l-tile-layer :url="urlTuiles" :attribution="attribution" />

        <l-marker v-for="(flamme, f) in flammes" ref="flamme" :lat-lng="flamme.coord" :key="'flamme'+f">
          <l-popup>ça brule ici</l-popup>
          <l-icon :iconUrl="iconFlamme" :iconSize="[flamme.rayon*coefficientIconSize, flamme.rayon*coefficientIconSize ]"></l-icon>
        </l-marker>
        
    </l-map>
  </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import { mapActions, mapMutations, mapGetters } from "vuex";

export default {
  props: {
    flammes: {
      type: Array,
      required: false,
      default: () => [
        { rayon: 1, intensite: 1, coord: [45.74, 4.85] },
        { rayon: 3, intensite: 1, coord: [45.74, 4.89] },
      ],
    },
  },
  data() {
    return {
      urlTuiles:
        "https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?fresh=true&title=copy&access_token=pk.eyJ1IjoiZGRkZGQ0NCIsImEiOiJjazRtdm01NHQwOG14M21wNWdsdXY1djhqIn0.GuEePwUCtxgMwBMdjBy7WA",
      zoneRestreinte: [
        [45.7, 4.8],
        [45.8, 4.9],
      ],
      attribution: '&copy; <a href="https://docs.mapbox.com/api/">Mapbox</a>',
      iconFlamme: "/feu.svg",
      coefficientIconSize: "20",
      centreCarte: [45.74, 4.85]
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
