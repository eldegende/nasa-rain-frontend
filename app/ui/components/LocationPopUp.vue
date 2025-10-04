<script setup lang="ts">
import {useMarkerStore} from "@/store/marker.ts";
import {computed, ref} from "vue";

const props = defineProps<{
    isHidden: boolean
}>()

const date = ref<Date | null>(null)
const markerStore = useMarkerStore()

const cleanMarkerPos = () => markerStore.latlng = undefined

const pos = computed((): string => {
    const lat: number | undefined = markerStore.latlng?.lat
    const lng: number | undefined = markerStore.latlng?.lng

    if (lat !== undefined && lng !== undefined) return lat.toFixed(6) + " " + lng.toFixed(6)
    else return "0 0"
})

</script>

<template>
    <div :class="['loc-pop-up', isHidden ? 'hide' : '']">
        <p class="coordinates">{{pos}}</p>

        <div class="date-input">
            <input v-model="date" id="date-input" type="date">
        </div>

        <div class="buttons">
            <button :disabled="!date">Forecast</button>
            <button @click="cleanMarkerPos" class="round-btn">❌</button>
        </div>
    </div>
</template>

<style scoped>

.loc-pop-up {
    padding: 12px;
    width: 300px;

    display: flex;
    flex-direction: column;
    gap: 12px;

    position: fixed;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);

    box-shadow: 0 0 12px rgba(0, 0, 0, 0.5);
    background-color: white;
    border-top-left-radius: 32px;
    border-top-right-radius: 32px;

    transition: .6s;
}
.hide {
    transform: translate(-50%, 100%);

    transition: .3s cubic-bezier(0.11, 0, 0.5, 0);
}

.coordinates {
    margin: 4px 4px 0;
    font-size: 1.5rem;
}

.buttons {
    display: flex;
    justify-content: space-between;
    gap: 4px;
}
.buttons button:first-child {
    flex: 1;
}

.date-input {
    display: flex;
}
.date-input input:first-child {
    flex: 1;
}
</style>