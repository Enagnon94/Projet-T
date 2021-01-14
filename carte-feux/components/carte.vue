<template>
  <div id="carte">
    <l-map :min-zoom="15" :zoom="15" :max-bounds="zoneRestreinte">
      <l-tile-layer :url="urlTuiles" :attribution="attribution" />
      <l-geo-json :geojson="itineraire"> </l-geo-json>

      <l-marker
        v-for="(flamme, f) in flammes"
        ref="flamme"
        :lat-lng="conversion2(flamme.X, flamme.Y)"
        :key="'flamme' + f"
      >
        <l-icon
          :iconUrl="iconFlamme"
          :iconSize="[2 * coefficientIconSize, 2 * coefficientIconSize]"
        ></l-icon>
      </l-marker>

      <l-marker
        v-for="(caserne, c) in casernes"
        ref="caserne"
        :lat-lng="conversion2(caserne.X, caserne.Y)"
        :key="'caserne' + c"
      >

        <l-icon :iconUrl="iconCaserne" :iconSize="[60, 40]"></l-icon>
      </l-marker>

      <l-marker
        v-for="(camion, c) in camions"
        ref="camion"
        :lat-lng="conversion2(camion.X, camion.Y)"
        :key="'camion' + c"
      >
        <l-icon :iconUrl="iconCamion" :iconSize="[60, 40]"></l-icon>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import { mapActions, mapMutations, mapGetters } from "vuex";
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
    casernes: {
      type: Array,
      required: false,
    },
    camions: {
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
      iconCaserne:
        "https://www.flaticon.com/de/premium-icon/icons/svg/3211/3211981.svg",
      iconCaserne2:
        "https://www.flaticon.com/de/premium-icon/icons/svg/3211/3211981.svg",
      iconCamion: "/Fire_truck.svg",
      coefficientIconSize: 20,
      itineraire: null,
      centreCarte: [45.74, 4.85],
      display: false
    };
  },
  methods: {
    async getItineraire(depart, arrivee) {
      this.itineraire = await this.calculItineraire(depart, arrivee).then(
        (response) => {
          return response;
        }
      );
    },
    conversion2(x, y) {
      if (x && y) {
        const tab = [x, y];
        const res = this.conversion(tab, this.zoneRestreinte);
        return res;
      } else {
        return [0, 0];
      }
    },
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
