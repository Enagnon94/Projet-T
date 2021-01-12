<template>
  <div id="carte">
    <l-map
      :min-zoom="15"
      :zoom="15"
      :max-bounds="zoneRestreinte"
    >
      <l-tile-layer :url="urlTuiles" :attribution="attribution" />
      <l-geo-json :geojson="itineraire"> 
      </l-geo-json>

        <l-marker v-for="(flamme, f) in flammes" ref="flamme" :lat-lng="conversion([flamme.X, flamme.Y], zoneRestreinte)" :key="'flamme'+f">
          <l-popup>ça brule ici</l-popup>
          <l-icon :iconUrl="iconFlamme" :iconSize="[2*coefficientIconSize, 2*coefficientIconSize ]"></l-icon>
        </l-marker>

        <l-marker v-for="(caserne, c) in casernes" ref="caserne" :lat-lng="[conversion([caserne.X, caserne.Y], zoneRestreinte)]" :key="'caserne'+c">
          <l-popup>{{caserne.name}}</l-popup>
          <l-icon :iconUrl="iconCaserne" :iconSize="[60, 40]"></l-icon>
        </l-marker>

        <l-marker v-for="(camion, c) in camions" ref="camion" :lat-lng="conversion([camion.X, camion.Y], zoneRestreinte)" :key="'camion'+c">
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
    camions: {type: Array, required: false, default: () => [{name: "Rescue Truck", coord: [45.746, 4.856]}, {name: "Tric Truck", coord: [45.748, 4.858]}]}
  },
  data() {
    return {
      urlTuiles:
        "https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?fresh=true&title=copy&access_token=pk.eyJ1IjoiZGRkZGQ0NCIsImEiOiJjazRtdm01NHQwOG14M21wNWdsdXY1djhqIn0.GuEePwUCtxgMwBMdjBy7WA",
      zoneRestreinte: [
        [45.735, 4.83],
        [45.75, 4.86],
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
  beforeMount() {
    console.log(this.camions);console.log("Carte.vue - this.camions");
  },
  methods: {
    async getItineraire(depart, arrivee) {
      this.itineraire = await this.$calculItineraire(depart, arrivee).then(response => { return response})
    },
    conversion(gridCoord, zoneRestreinte) {
        const testc = this.$conversion(gridCoord, zoneRestreinte);
        return testc;    
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
