import L, { type LeafletMouseEvent } from "leaflet";
import { useMarkerStore } from "../store/marker.ts";

export default class Marker {

    private readonly markerStore = useMarkerStore()
    private readonly map: L.Map
    public readonly marker: L.Marker

    constructor(map: L.Map) {
        this.map = map

        this.marker = L.marker([0, 0]).addTo(this.map).setOpacity(0)
        this.map.on("click", this.onMapClick.bind(this))
    }

    private onMapClick(e: LeafletMouseEvent) {
        this.markerStore.latlng = e.latlng
        this.marker.setLatLng(e.latlng)
        this.marker.setOpacity(1)
    }
}
