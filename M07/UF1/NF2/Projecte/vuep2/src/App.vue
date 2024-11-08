<script setup>
import { ref } from 'vue'
import MostrarTasques from './components/MostrarTasques.vue'
import NovaTasca from './components/NovaTasca.vue'
const llistaTasques = ref([
  {
    id: 1,
    tasca: 'Comprar donuts',
  },
  {
    id: 2,
    tasca: 'Reclamar pagament hisenda',
  },
  {
    id: 3,
    tasca: 'Pagar rebut gimnàs',
  },
])
function onAgregar(parametre) {
  llistaTasques.value.push({
    id: llistaTasques.value.length + 1,
    tasca: parametre,
  })
}
</script>

<template>
  <MostrarTasques :tasques="llistaTasques" />
  <NovaTasca @agregar="onAgregar" />
</template>

<style scoped></style>
