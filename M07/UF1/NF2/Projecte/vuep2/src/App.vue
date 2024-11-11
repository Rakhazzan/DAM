<script setup>
import { ref } from 'vue'
import MostrarTasques from './components/MostrarTasques.vue'
import NovaTasca from './components/NovaTasca.vue'
import SlotsComponent from './components/SlotsComponent.vue'
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
  <SlotsComponent>
    <h1>Llista de Tasques</h1>
    <img
      width="200px"
      src="https://agora.xtec.cat/ceipstamargarida/wp-content/uploads/usu106/2020/03/Deures.jpg"
    />
    <hr />
  </SlotsComponent>
  <br />
  <MostrarTasques :tasques="llistaTasques" />
  <NovaTasca @agregar="onAgregar" />
</template>

<style scoped></style>
