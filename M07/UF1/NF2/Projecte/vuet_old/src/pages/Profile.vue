<template>
  <v-container class="d-flex justify-center align-center fill-height">
    <v-card class="pa-8" width="400">
      <v-card-title class="d-flex justify-center align-center">
        <h2>Bienvenido</h2>
      </v-card-title>
      <v-card-text>
        <p>Email: {{ email }}</p>
      </v-card-text>
      <v-card-text>
        <p>Username: {{ username }}</p>
      </v-card-text>
      <v-card-actions>
        <v-btn block color="red" @click="logout">
          Cerrar Sesión
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const username = ref('');
const email = ref('');

onMounted(() => {
  const user = JSON.parse(localStorage.getItem('user'));
  if (!user) {
    router.push('/login'); // Redirige al login si no hay usuario autenticado
  } else {
    username.value = user.username;
    email.value = user.email;
  }
});

const logout = () => {
  localStorage.removeItem('user');
  router.push('/login'); // Redirige al login al cerrar sesión
};
</script>

<style scoped>
/* Agrega estilo según necesites */
</style>
