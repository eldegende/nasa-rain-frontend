<script setup lang="ts">

const props = defineProps<{
    searchFn: Function
}>()

const submitQuery = (e: SubmitEvent) => {
    const form = e.target as HTMLFormElement;
    const input = form.elements.namedItem('search') as HTMLInputElement | null;

    props.searchFn(input?.value)
}

</script>

<template>
    <div class="search-bar">
        <form @submit.prevent="submitQuery">
            <input id="search" type="text" placeholder="Street, address, coordinates...">
            <button type="submit">Search</button>
        </form>
    </div>
</template>

<style scoped>

.search-bar {
    position: fixed;
    top: var(--fixed-margin);
    left: 50%;
    transform: translateX(-50%);
}

#search {
    width: 30vw;
}

</style>