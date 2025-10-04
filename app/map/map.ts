import "leaflet/dist/leaflet.css"
import L from "leaflet"

export const map = L.map("map", {zoomControl: false}).setView([42.881896, 74.596731], 14)

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);