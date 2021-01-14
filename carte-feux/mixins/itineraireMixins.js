export default {
    methods: {
        async calculItineraire(depart, arrivee) {
            const res = await this.$mapaboxItineraire
                .$get(
                `${depart[1]},${depart[0]};${arrivee[1]},${arrivee[0]}?steps=true&geometries=geojson&access_token=pk.eyJ1IjoiZGRkZGQ0NCIsImEiOiJjazRtdm01NHQwOG14M21wNWdsdXY1djhqIn0.GuEePwUCtxgMwBMdjBy7WA`
                )
                .then((response) => {
                const data = response;
                const route = data.routes[0].geometry.coordinates;
        
                let geojson = {
                    features: [
                    {
                        type: "Feature",
                        properties: {},
                        geometry: {
                        type: "LineString",
                        coordinates: route,
                        },
                    },
                    ],
                };
                return geojson;
                });
            return res;
        }
    }
}