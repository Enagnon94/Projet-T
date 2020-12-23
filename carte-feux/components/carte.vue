<template>
  <div id="carte">
    <l-map
      :center="centreCarte"
      :min-zoom="10"
      :zoom="15"
      :max-bounds="zoneRestreinte"
    >
      <l-tile-layer :url="urlTuiles" :attribution="attribution" />
      <l-geo-json :geojson="geojson"> 
      </l-geo-json>

        <l-marker v-for="(flamme, f) in flammes" ref="flamme" :lat-lng="flamme.coord" :key="f">
          <l-popup>ça brule ici</l-popup>
          <l-icon :iconUrl="iconFlamme" :iconSize="[flamme.rayon*coefficientIconSize, flamme.rayon*coefficientIconSize ]"></l-icon>
        </l-marker>

        <l-marker v-for="(caserne, c) in casernes" ref="caserne" :lat-lng="caserne.coord" :key="c">
          <l-popup>{{caserne.name}}</l-popup>
          <l-icon :iconUrl="iconCaserne" :iconSize="[60, 40]"></l-icon>
        </l-marker>
        
    </l-map>
  </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import "leaflet.markercluster/dist/MarkerCluster.css";
import "leaflet.markercluster/dist/MarkerCluster.Default.css";
import vuex from "vuex";

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
      iconCaserne: "https://www.flaticon.com/de/premium-icon/icons/svg/3211/3211981.svg",
      iconCaserne2: "https://www.flaticon.com/de/premium-icon/icons/svg/3211/3211981.svg",
      coefficientIconSize: "20",
      geojson: null

    };
  },
  beforeMount() {
    let depart = [this.casernes[0].coord[0], this.casernes[0].coord[1]];
    let arrivee = [this.flammes[1].coord[0], this.flammes[1].coord[1]];
    this.calculItineraire(depart, arrivee)
  },
  methods: {
    async calculItineraire(pointDepart, pointArrivee) {
      this.loading = true;
      const urlApiItineraire = `https://api.mapbox.com/directions/v5/mapbox/cycling/${pointDepart[1]},${pointDepart[0]};${pointArrivee[1]},${pointArrivee[0]}?steps=true&geometries=geojson&access_token=pk.eyJ1IjoiZGRkZGQ0NCIsImEiOiJjazRtdm01NHQwOG14M21wNWdsdXY1djhqIn0.GuEePwUCtxgMwBMdjBy7WA`;
      const response = await fetch(urlApiItineraire)
      const data = await response.json();
      const route = data.routes[0].geometry.coordinates;
      this.geojson = {
        
        features: [{
          type: 'Feature',
          properties: {},
        geometry: {
          type: 'LineString',
          coordinates: route
        }
        }],
      };
      this.loading = false;
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
