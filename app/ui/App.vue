<script setup lang="ts">
import ZoomControls from "@/ui/components/ZoomControls.vue";
import SearchBar from "@/ui/components/SearchBar.vue";
import {useMarkerStore} from "@/store/marker.ts";
import {map} from "@/main.ts";
import {geocodeSearch} from "@/api/geocode/geocodeRequests.ts";
import {LatLng} from "leaflet";
import LocationPopUp from "@/ui/components/LocationPopUp.vue";
import {ref} from "vue";
import ForecastDialog from "@/ui/components/dialog/ForecastDialog.vue";

const markerStore = useMarkerStore()

const showForecast = ref(true)
const hideForecast = () => showForecast.value = false

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
    <ZoomControls />

    <SearchBar :search-fn="queryStreet"/>

    <LocationPopUp :is-hidden="!markerStore.latlng" :forecast-fn="() => showForecast = true" />

    <Transition>
        <ForecastDialog v-if="showForecast" :hide-fn="hideForecast" />
    </Transition>
</template>

<style scoped>

.v-enter-active,
.v-leave-active {
    transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
    opacity: 0;
}

</style>
