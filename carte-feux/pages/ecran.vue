<template>
  <div id="ecranSupervision">
    <h1>Ecran de supervision</h1>
    <h2>Centre de Villeurbanne</h2>
    <div id="simul">
    <carte :flammes="flammes" :caserne="casernes" :camions="camions" ></carte>
    <info-simul :flammes="flammes" :caserne="casernes" :camions="camions"></info-simul>
    </div>
  </div>
</template>

<script>
import carte from "@/components/carte";
import infoSimul from "@/components/infoSimul"
import InfoSimul from '~/components/infoSimul.vue';
export default {
  components: {
    carte,
    infoSimul
  },
  props: {
        flammes: {type: Array, required: false, default: () => [{rayon: 1, intensite: 1, coord: [45.74, 4.85]}, {rayon: 2, intensite: 1, coord: [45.74, 4.852]}] },
        casernes: {type: Array, required: false, default: () => [{name: "Dami", coord: [45.746, 4.856]}, {name: "Nami", coord: [45.748, 4.858]}]},
        camions: {type: Array, required: false, default: () => [{name: "Rescue Truck", coord: [45.746, 4.856]}, {name: "Tric Truck", coord: [45.748, 4.858]}]}
    },
  data() {
    return {

    }
  }
}
</script>

<style lang="scss" scoped>
h1, h2 {
  text-align: center;
}
#simul {
  height: 500px;
  display: flex;
}
</style>