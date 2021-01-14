<template>
  <div id="carte">
    <l-map
      :center="centreCarte"
      :min-zoom="15"
      :zoom="15"
      :max-bounds="zoneRestreinte"
    >
      <l-tile-layer :url="urlTuiles" :attribution="attribution" />

        <l-marker v-for="(flamme, f) in flammes" ref="flamme" :lat-lng="conversion2(flamme.X, flamme.Y)" :key="'flamme'+f">

          <l-icon :iconUrl="iconFlamme" :iconSize="[flamme.Rayon*coefficientIconSize, flamme.Rayon*coefficientIconSize ]"></l-icon>
        </l-marker>
        
    </l-map>
  </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import itineraireMixins from "@/mixins/itineraireMixins";
import coordMixins from "@/mixins/coordMixins";

export default {
  mixins: [itineraireMixins, coordMixins],
  props: {
    flammes: {
      type: Array,
      required: false,
      default: () => [],
    },
  },
  data() {
    return {
      urlTuiles:
        "https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?fresh=true&title=copy&access_token=pk.eyJ1IjoiZGRkZGQ0NCIsImEiOiJjazRtdm01NHQwOG14M21wNWdsdXY1djhqIn0.GuEePwUCtxgMwBMdjBy7WA",
      zoneRestreinte: [
        [45.725, 4.83],
        [45.74, 4.86],
      ],
      attribution: '&copy; <a href="https://docs.mapbox.com/api/">Mapbox</a>',
      iconFlamme: "/feu.svg",
      coefficientIconSize: 40,
      centreCarte: [45.74, 4.85]
    };
  },
  methods: {
    conversion2(x, y) {
      if(x && y) {
        const tab = [x, y];
        const testc = this.conversion(tab, this.zoneRestreinte);
        
        return testc;
      }
      else {
        return [1, 1];
      }
    }
  }
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
