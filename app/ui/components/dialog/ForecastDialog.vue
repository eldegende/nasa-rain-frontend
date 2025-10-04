<script setup lang="ts">
import Spinner from "@/ui/components/Spinner.vue";

const props = defineProps<{
    hideFn: Function
}>()

</script>

<template>
    <div @click="() => hideFn()" class="container">
        <div class="forecast-dialog" @click.stop>
            <h2 class="title">Will it rain on my parade?</h2>

            <div class="content">
                <p>
                    ...probably yes<br>
                    as there's a chance of
                </p>
                <h2 class="percentage">67% of raining</h2>
            </div>

            <div class="buttons">
                <button>Tell me more!</button>
                <button @click="() => hideFn()" class="round-btn">❌</button>
            </div>
        </div>
    </div>
</template>

<style scoped>

.container {
    width: 100vw;
    height: 100vh;

    backdrop-filter: blur(2px) brightness(.6);
}

.forecast-dialog {
    padding: 12px 22px;
    width: 550px;

    display: flex;
    flex-direction: column;
    gap: 32px;

    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

    background-color: white;
    box-shadow: 0 0 12px rgba(0, 0, 0, 0.5);
    border-radius: 32px;
}

.content {
    margin: 0 auto;
    width: 50%;
}

.title {
    font-size: 2.2rem;
}

.percentage {
    width: 100%;

    text-align: center;
    font-size: 2.4rem;
}

.buttons {
    display: flex;
    justify-content: space-between;
    gap: 4px;
}
.buttons button:first-child {
    flex: 1;
}


p, h2 {
    margin: 0;
}
p {
    font-size: 1.5rem;
}
h2 {
    margin: 4px 0;
}

</style>