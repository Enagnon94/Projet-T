<template>
    <div id="infoSimul">
        <ul v-for="(flamme, f) in flammes" :key="'infoFlamme'+f">
            <p>Flamme {{f}} : </p>
            <li>Coordonnées : {{flamme.coord}}</li>
            <li>Rayon : {{flamme.rayon}}</li>
            <li>Intensité : {{flamme.intensite}}</li>
        </ul>
        
        <ul v-for="(caserne, c) in casernes" :key="'infoCaserne'+c">
            <p>Casernes {{c}} : </p>
            <li>Casernes : {{caserne.name}}</li>
        </ul>
    </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import "leaflet.markercluster/dist/MarkerCluster.css";
import "leaflet.markercluster/dist/MarkerCluster.Default.css";

export default {
    props: {
        flammes: {type: Array, required: false, default: () => [{rayon: 1, intensite: 1, coord: [45.74, 4.85]}, {rayon: 1, intensite: 1, coord: [45.74, 4.852]}] },
        casernes: {type: Array, required: false, default: () => [{name: "Dami", coord: [45.746, 4.856]}, {name: "Nami", coord: [45.748, 4.858]}]},
        camions: {type: Array, required: false, default: () => [{name: "Rescue Truck", coord: [45.746, 4.856]}, {name: "Tric Truck", coord: [45.748, 4.858]}]}
    }
}
</script>

<style lang="scss" scoped>
#infoSimul {
  border-style: solid;
  border-color: darkblue;
  p {
      width: max-content;
  }
  ul {
      width: max-content;
      border-style: solid;
      border-color: lightblue;
  }
}
</style>