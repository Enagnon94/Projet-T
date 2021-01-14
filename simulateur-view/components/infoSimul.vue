<template>
    <div id="infoSimul">
        <ul v-for="(flamme, f) in flammes" :key="'infoFlamme'+f">
            <p>Flamme {{f}} : </p>
            <li>Rayon : {{flamme.Rayon}}</li>
            <li>Intensité : {{flamme.Intensité}}</li>
        </ul>
    </div>
</template>

<script>
import "leaflet/dist/leaflet.css";

export default {
    props: {
        flammes: {type: Array, required: false, default: () => [{rayon: 1, intensite: 1, coord: [45.74, 4.85]}, {rayon: 1, intensite: 1, coord: [45.74, 4.852]}] },
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