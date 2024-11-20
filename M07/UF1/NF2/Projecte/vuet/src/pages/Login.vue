<template>
  <v-container class="d-flex justify-center align-center fill-height login-container">
    <v-card class="pa-8" width="400">
      <!-- Logo -->
      <v-card-title class="justify-center align-center">
        <v-img
          src="C:/Users/Mohamed/Documents/DAM/M07/UF1/NF2/Projecte/vuet/src\pages\img\HeavenTaste_Logo.jpg"
          alt="HeavenTaste Logo"
          max-width="150"
        />
      </v-card-title>

      <!-- Title -->
      <v-card-title class="justify-center title">Iniciar Sesión</v-card-title>

      <v-card-text>
        <v-form ref="form" v-model="valid" lazy-validation>
          <!-- Email -->
          <v-text-field
            v-model="email"
            label="Correo electrónico"
            :rules="emailRules"
            required
            variant="outlined"
          ></v-text-field>

          <!-- Password -->
          <v-text-field
            v-model="password"
            label="Contraseña"
            type="password"
            :rules="passwordRules"
            required
            variant="outlined"
          ></v-text-field>

          <!-- Forgot password -->
          <v-btn text class="forgot-password">¿Olvidaste tu contraseña?</v-btn>
        </v-form>
      </v-card-text>

      <!-- Actions -->
      <v-card-actions>
        <v-btn block :disabled="!valid" color="red" @click="login">
          Iniciar Sesión
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';

const valid = ref(false);
const email = ref('');
const password = ref('');

const emailRules = [
  (v) => !!v || 'El correo electrónico es obligatorio',
  (v) => /.+@.+\..+/.test(v) || 'Ingrese un correo válido',
];

const passwordRules = [
  (v) => !!v || 'La contraseña es obligatoria',
  (v) => (v && v.length >= 6) || 'La contraseña debe tener al menos 6 caracteres',
];

const login = () => {
  console.log('Iniciando sesión con:', email.value, password.value);
};
</script>

<style scoped>

.title {
  font-weight: bold;
  color: #FF0D00; /* Rojo del branding */
}

.forgot-password {
  text-transform: none;
  color: #FF9400; /* Naranja del branding */
}
</style>
