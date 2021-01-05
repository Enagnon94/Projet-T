export { default as Carte } from '../..\\components\\carte.vue'
export { default as InfoSimul } from '../..\\components\\infoSimul.vue'
export { default as Logo } from '../..\\components\\Logo.vue'

export const LazyCarte = import('../..\\components\\carte.vue' /* webpackChunkName: "components_carte" */).then(c => c.default || c)
export const LazyInfoSimul = import('../..\\components\\infoSimul.vue' /* webpackChunkName: "components_infoSimul" */).then(c => c.default || c)
export const LazyLogo = import('../..\\components\\Logo.vue' /* webpackChunkName: "components_Logo" */).then(c => c.default || c)
