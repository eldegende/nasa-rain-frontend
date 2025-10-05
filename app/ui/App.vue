<template>
    <ZoomControls />
    <SearchBar :search-fn="queryStreet"/>
    
    <input type="date" v-model="markerStore.date" />

    <LocationPopUp 
        :is-hidden="!markerStore.latlng" 
        :forecast-fn="fetchForecast" 
    />

    <Transition>
        <ForecastDialog
            v-if="showForecast && markerStore.forecast"
            :forecast="markerStore.forecast"
            :hide-fn="hideForecast"
        />
    </Transition>

    <button v-if="markerStore.latlng && markerStore.date" @click="fetchForecast">
        Forecast
    </button>
</template>

<script setup lang="ts">
import ZoomControls from "@/ui/components/ZoomControls.vue";
import SearchBar from "@/ui/components/SearchBar.vue";
import ForecastDialog from "@/ui/components/dialog/ForecastDialog.vue";
import LocationPopUp from "@/ui/components/LocationPopUp.vue";
import {useMarkerStore} from "@/store/marker.ts";
import {map} from "@/main.ts";
import {geocodeSearch} from "@/api/geocode/geocodeRequests.ts";
import {LatLng} from "leaflet";
import {ref} from "vue";

const markerStore = useMarkerStore()
const showForecast = ref(true)
const hideForecast = () => showForecast.value = false

const queryStreet = async (street: string) => {
    const response = await geocodeSearch(street)
    if (!response.data || response.data.length === 0) return
    const firstResult = response.data[0]
    map.setView([firstResult.lat, firstResult.lon], 20)
    markerStore.latlng = new LatLng(firstResult.lat, firstResult.lon)
}

const fetchForecast = async () => {
    if (!markerStore.latlng || !markerStore.date) {
        alert("Выберите точку на карте и дату!")
        return
    }

    try {
        const res = await fetch(`http://127.0.0.1:8000/forecast?lat=${markerStore.latlng.lat}&lon=${markerStore.latlng.lng}&date=${markerStore.date}`)
        const data = await res.json()
        markerStore.setForecast(data)
        showForecast.value = true
    } catch (err) {
        console.error(err)
        alert("Ошибка при получении прогноза")
    }
}
</script>
