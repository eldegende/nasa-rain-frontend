import {defineStore} from "pinia";
import type {LatLng} from "leaflet";

interface MarkerState {
    latlng: LatLng | undefined,
    isVisible: boolean
}

export const useMarkerStore = defineStore("marker", {
    state: (): MarkerState => ({
        latlng: undefined,
        isVisible: false
    })
})