<script setup lang="ts">
import {map} from "@/main.ts";

const zoomIn = () => map.zoomIn(1.2)
const zoomOut = () => map.zoomOut(1.2)

</script>

<template>
    <div class="zoom-controls">
        <button @click="zoomIn" class="round-btn">+</button>
        <button @click="zoomOut" class="round-btn">-</button>
    </div>
</template>

<style scoped>
.zoom-controls {
    padding: 4px;

    position: fixed;
    bottom: 12px;
    left: 12px;

    display: flex;
    flex-direction: column;
    gap: 4px;

    background-color: white;
    border-radius: 64px;
}
</style>