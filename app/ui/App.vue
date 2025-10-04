<script setup lang="ts">
import ZoomControls from "@/ui/components/ZoomControls.vue";
import {useMarkerStore} from "@/store/marker.ts";

const markerStore = useMarkerStore()

</script>

<template>
    <h3>pos: {{markerStore.latlng && markerStore.latlng.toString()}}</h3>
    <ZoomControls />
    <button>button</button>
</template>

<style scoped></style>
