export default function ({ $axios }, inject) {
  // Create a custom axios instance
  const mapaboxItineraire = $axios.create({
    headers: {
      common: {
        Accept: "text/plain, */*",
      },
    },
  });

  mapaboxItineraire.setBaseURL(
    "https://api.mapbox.com/directions/v5/mapbox/driving"
  );

  inject("mapaboxItineraire", mapaboxItineraire);
}
