import { defineStore } from "pinia";
import L from "leaflet";

export const useMarkerStore = defineStore("marker", {
    state: () => ({
        latlng: null as L.LatLng | null,
        date: "",           
        forecast: null
    }),
    actions: {
        setDate(d: string) {
            this.date = d
        },
        setForecast(data: any) {
            this.forecast = data
        }
    }
})
