<template>
  <div id="ecranSupervision">
    <h1>Ecran de supervision</h1>
    <h2>Centre de Villeurbanne</h2>

    <div id="simul">
      <carte :flammes="flammes" ></carte>
      <info-simul :flammes="flammes" ></info-simul>
    </div>
  </div>
</template>

<script>
import carte from "@/components/carte";
import infoSimul from "@/components/infoSimul";
export default {
  components: {
    carte,
    infoSimul
  },
  props: {
        flammes: {type: Array, required: false, default: () => [{rayon: 1, intensite: 1, coord: [45.7412, 4.836]}, {rayon: 2, intensite: 1, coord: [45.74, 4.852]}] },
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