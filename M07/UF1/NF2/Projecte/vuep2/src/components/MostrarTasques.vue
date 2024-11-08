<script setup>
const props = defineProps({
  tasques: Array,
})
</script>

<template>
  <h2>tasques actuals</h2>
  <ul>
    <li v-for="tsc of props.tasques" :key="tsc.id">{{ tsc.id }} ... {{ tsc.tasca }}</li>
  </ul>
</template>

<style scoped></style>
