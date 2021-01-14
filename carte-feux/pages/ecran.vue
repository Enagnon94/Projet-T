<template>
  <div id="ecranSupervision">
    <h1>Ecran de supervision</h1>
    <h2>Centre de Villeurbanne</h2>

    <div id="simul">
      <carte
        :flammes="capteurs"
        :casernes="casernes"
        :camions="camions"
      ></carte>
      <info-simul
        :flammes="capteurs"
        :casernes="casernes"
        :camions="camions"
      ></info-simul>
    </div>
  </div>
</template>

<script>
import carte from "@/components/carte";
import infoSimul from "@/components/infoSimul";
export default {
  components: {
    carte,
    infoSimul,
  },
  data() {
    return {
      capteurs: [
        { rayon: 1, intensite: 1, coord: [45.7412, 4.836] },
        { rayon: 2, intensite: 1, coord: [45.735, 4.83] },
      ],
      casernes: [],
      camions: [],
      intervalInfos: "",
      intervalCapteurs: "",
      timeout: 1000,
    };
  },
  async mounted() {
    await this.getInfos();
    await this.getCapteurs();
  },
  methods: {
    getInfos() {
      this.intervalInfos = setInterval(() => {
        this.$axios
          .get("/emergency")
          .then((response) => {
            this.casernes = response.data.casernes;
            this.camions = response.data.camions;
          });
      }, 500);
    },
    async getCapteurs() {
      this.intervalCapteurs = setInterval(() => {
        this.$axios
          .get("/simul")
          .then((response) => {
            this.capteurs = response.data.capteurs;
            return response.data;
          });
      }, 1000);
    },
  },
  beforeDestroy() {
    clearInterval(this.intervalInfos);
    clearInterval(this.intervalCapteurs);
  },
};
</script>

<style lang="scss" scoped>
h1,
h2 {
  text-align: center;
}
#simul {
  height: 600px;
  display: flex;
}
</style>
