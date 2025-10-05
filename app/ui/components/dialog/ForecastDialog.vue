<template>
    <div @click="hideFn()" class="container">
        <div class="forecast-dialog" @click.stop>
            <h2 class="title">Will it rain on my parade?</h2>

            <div class="content" v-if="forecast">
                <p>Вероятность дождя:</p>
                <h2 class="percentage">{{ forecast.rain_probability_percent }}%</h2>
                <p>Температура: {{ forecast.temperature_min }}°C - {{ forecast.temperature_max }}°C</p>
                <p>Источник: {{ forecast.source }}</p>
                <p v-if="forecast.message">{{ forecast.message }}</p>
            </div>

            <div class="buttons">
                <button @click="tellMore">Tell me more!</button>
                <button @click="hideFn()" class="round-btn">❌</button>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
const props = defineProps<{
    hideFn: Function,
    forecast: any
}>()

const tellMore = () => {
    if (props.forecast) {
        alert(`Подробности прогноза:\n
Температура: ${props.forecast.temperature_min}°C - ${props.forecast.temperature_max}°C\n
Вероятность дождя: ${props.forecast.rain_probability_percent}%\n
Источник: ${props.forecast.source}`)
    }
}
</script>
