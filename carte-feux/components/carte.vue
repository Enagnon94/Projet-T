<template>
  <div id="carte">
    <l-map
      :center="centreCarte"
      :min-zoom="12"
      :zoom="15"
      :max-bounds="zoneRestreinte"
    >
      <l-tile-layer :url="urlTuiles" :attribution="attribution" />
      <l-geo-json :geojson="itineraire"> 
      </l-geo-json>

        <l-marker v-for="(flamme, f) in flammes" ref="flamme" :lat-lng="flamme.coord" :key="'flamme'+f">
          <l-popup>ça brule ici</l-popup>
          <l-icon :iconUrl="iconFlamme" :iconSize="[flamme.rayon*coefficientIconSize, flamme.rayon*coefficientIconSize ]"></l-icon>
        </l-marker>

        <l-marker v-for="(caserne, c) in casernes" ref="caserne" :lat-lng="caserne.coord" :key="'caserne'+c">
          <l-popup>{{caserne.name}}</l-popup>
          <l-icon :iconUrl="iconCaserne" :iconSize="[60, 40]"></l-icon>
        </l-marker>

        <l-marker v-for="(camion, c) in camions" ref="camion" :lat-lng="camion.coord" :key="'camion'+c">
          <l-popup>{{camion.name}}</l-popup>
          <l-icon :iconUrl="iconCamion" :iconSize="[60, 40]"></l-icon>
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
    casernes: { type: Array, required: false },
    camions: { type: Array, required: false },
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
      iconCaserne: "https://www.flaticon.com/de/premium-icon/icons/svg/3211/3211981.svg",
      iconCaserne2: "https://www.flaticon.com/de/premium-icon/icons/svg/3211/3211981.svg",
      iconCamion: "/Fire_truck.svg",
      coefficientIconSize: "20",
      itineraire: null,
      centreCarte: [45.74, 4.85]
    };
  },
  mounted() {
    this.$nextTick(() => {
      let depart = [this.casernes[0].coord[0], this.casernes[0].coord[1]];
      let arrivee = [this.flammes[1].coord[0], this.flammes[1].coord[1]];
      
      this.getItineraire(depart, arrivee);
    })
  },
  methods: {
    async getItineraire(depart, arrivee) {
      this.itineraire = await this.$calculItineraire(depart, arrivee).then(response => { return response})
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
