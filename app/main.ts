import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './ui/App.vue'
import router from './ui/router'

import "leaflet/dist/leaflet.css"
import L from "leaflet";
import Marker from "./map/Marker.ts";
import {useMarkerStore} from "./store/marker.ts";

// vuejs, pinia init
const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')

// map init
export const map = L.map("map", {zoomControl: false}).setView([42.881896, 74.596731], 14)

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


new Marker(map)
