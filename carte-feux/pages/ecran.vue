<template>
  <div id="ecranSupervision">
    <h1>Ecran de supervision</h1>
    <h2>Centre de Villeurbanne</h2>

    <div id="simul">
      <carte :flammes="capteurs" :casernes="casernes" :camions="camions" ></carte>
      <info-simul :flammes="capteurs" :caserne="casernes" :camions="camions"></info-simul>
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
  data() {
    return {
      capteurs: [{rayon: 1, intensite: 1, coord: [45.7412, 4.836]}, {rayon: 2, intensite: 1, coord: [45.735, 4.83]}],
      casernes: [{name: "Dami", coord: [45.7467, 4.856]}, {name: "Nami", coord: [45.748, 4.858]}],
      camions: []
    }
  },
  mounted() {
    this.getInfos();
  },
  methods: {
    async getInfos() {
      const infos = await this.$axios
      .get('http://localhost:5002/emergency')
      .then(response => response.data)

      this.casernes = infos.casernes;
      this.camions = infos.camions;
      console.log(this.camions);console.log("infos.camions");
    }
  }
}
</script>

<style lang="scss" scoped>
h1, h2 {
  text-align: center;
}
#simul {
  height: 600px;
  display: flex;
}
</style>