import Vue from "vue";
import { LMap, LTileLayer, LMarker, LTooltip, LCircleMarker, LPopup, LIcon, LGeoJson, LPolygon } from "vue2-leaflet";

Vue.component("l-map", LMap);
Vue.component("l-tile-layer", LTileLayer);
Vue.component("l-marker", LMarker);
Vue.component("l-tooltip", LTooltip);
Vue.component("l-popup", LPopup);
Vue.component("l-circle-marker", LCircleMarker);
Vue.component("l-icon", LIcon);
Vue.component("l-geo-json", LGeoJson);
Vue.component("l-polygon", LPolygon);