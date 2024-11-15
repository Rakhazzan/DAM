<script setup>
import { ref } from 'vue'
const entrarTasca = ref('')
const emit = defineEmits(['agregar'])
// funció que s'activa quan fem click a entrar
function femClick() {
  // crida a l'event "agregar" del pare i passa com a paràmetre l'string del input
  emit('agregar', entrarTasca.value)
}
</script>

<template>
  <h2>Afegir Tasca</h2>
  <input type="text" name="inputTasca" v-model="entrarTasca" />
  <button @click="femClick">Entrar</button>
</template>

<style scoped></style>
