<script setup lang="ts">
import ZoomControls from "@/ui/components/ZoomControls.vue";
import SearchBar from "@/ui/components/SearchBar.vue";
import {useMarkerStore} from "@/store/marker.ts";
import {map} from "@/main.ts";
import {geocodeSearch} from "@/api/geocode/geocodeRequests.ts";
import {LatLng} from "leaflet";

const markerStore = useMarkerStore()

const queryStreet = async (street: string) => {
    const response = await geocodeSearch(street)
    console.log(response.data)
    const firstResult = response.data[0]

    if (response.data.length === 0) {
        console.warn("Not found...")
        return
    }
    map.setView([firstResult.lat, firstResult.lon], 20)

    markerStore.latlng = new LatLng(firstResult.lat, firstResult.lon)
}

</script>

<template>
    <h3>pos: {{markerStore.latlng && markerStore.latlng.toString()}}</h3>
    <ZoomControls />

    <SearchBar :search-fn="queryStreet"/>
</template>

<style scoped></style>
