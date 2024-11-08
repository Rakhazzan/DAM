<script setup>
import { ref } from 'vue'

// Riddle text, hint, and solution variables
const endevinalla =
  'Una pedra que camina sense ser pedra; té quatre cames i no és ovella, pon ous i no és gallina'
const pista = 'És un animal que comença per T'
const solucio = 'LA TORTUGA'

// Reactive variables to control hint and solution visibility
const veurePista = ref(false)
const veureSolucio = ref(false)

// Functions to set visibility of hint and solution
function funcioVeurePista() {
  veurePista.value = true
}

function funcioVeureSolucio() {
  veureSolucio.value = true
}
</script>

<template>
  <section>
    <p>{{ endevinalla }}</p>
    <p v-if="veurePista">{{ pista }}</p>
    <p v-if="veureSolucio">{{ solucio }}</p>
    <button @click="funcioVeurePista">Veure Pista</button>
    <button @click="funcioVeureSolucio">Veure Solucio</button>
  </section>
</template>

<style scoped>
section {
  text-align: center;
  margin-top: 20px;
}

button {
  margin: 5px;
  padding: 10px 15px;
  font-size: 1rem;
  cursor: pointer;
}
</style>
