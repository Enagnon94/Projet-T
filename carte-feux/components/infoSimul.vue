<template>
    <div id="infoSimul">
        <div>{{casernes}}</div>
        <ul v-for="(flamme, f) in flammes" :key="'infoFlamme'+f">
            <input type="checkbox" @change="displayFlamme">
                Flamme {{f}} : 
            <li>Coordonnées : {{flamme.coord}}</li>
            <li>Rayon : {{flamme.rayon}}</li>
            <li>Intensité : {{flamme.intensite}}</li>
        </ul>
        
        <ul v-for="(caserne, c) in casernes" :key="'infoCaserne'+c">
            <p>Casernes {{c}} : </p>
            <li>Casernes : {{caserne.Idcaserne}}</li>
        </ul>
    </div>
</template>

<script>
import "leaflet/dist/leaflet.css";

export default {
    props: {
        flammes: {type: Array, required: false, default: () => [{rayon: 1, intensite: 1, X: 1, Y: 1}] },
        casernes: {type: Array, required: false},
        camions: {type: Array, required: false}
    },
    methods: {
        displayFlamme() {
            console.log("jrjrjrjrj")
        }
    }
}
</script>

<style lang="scss" scoped>
#infoSimul {
  border-style: solid;
  border-color: darkblue;
  overflow-y: scroll;
  margin-right: 10px;
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