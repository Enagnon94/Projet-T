<template>
  <div id="ecranSupervision">
    <carte :flammes="flammes" :caserne="casernes" :camions="camions" ></carte>
    <info-simul :flammes="flammes" :caserne="casernes" :camions="camions"></info-simul>
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
#ecranSupervision {
  height: 500px;
  display: flex;
}
</style>