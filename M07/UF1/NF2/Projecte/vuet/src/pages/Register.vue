<template>
  <v-container class="d-flex justify-center align-center fill-height">
    <v-card class="pa-8" width="400">
      <v-card-title class="justify-center title">Registrarse</v-card-title>

      <v-card-text>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field
            v-model="name"
            label="Username"
            :rules="nameRules"
            required
            variant="outlined"
          ></v-text-field>

          <v-text-field
            v-model="email"
            label="Email"
            :rules="emailRules"
            required
            variant="outlined"
          ></v-text-field>

          <v-text-field
            v-model="password"
            label="Password"
            type="password"
            :rules="passwordRules"
            required
            variant="outlined"
          ></v-text-field>
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-btn block color="success" :disabled="!valid" @click="register">
          Registrarse
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup>

import { ref } from 'vue';
import { useRouter } from 'vue-router';  // Importamos el router para navegación

const router = useRouter();  // Usamos el router



const valid = ref(false);
const name = ref("");
const email = ref("");
const password = ref("");

// Reglas de validación
const nameRules = [(v) => !!v || "El nombre es obligatorio"];
const emailRules = [
  (v) => !!v || "El correo electrónico es obligatorio",
  (v) => /.+@.+\..+/.test(v) || "Ingrese un correo válido",
];
const passwordRules = [
  (v) => !!v || "La contraseña es obligatoria",
  (v) => v.length >= 6 || "La contraseña debe tener al menos 6 caracteres",
];

// Función para registrar al usuario
const register = async () => {
  try {
    const response = await fetch("http://localhost:3001/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: name.value,
        email: email.value,
        password: password.value,
      }),
    });

    // Verifica que la respuesta sea exitosa
    if (!response.ok) {
      const errorData = await response.json().catch(() => null); // Captura errores JSON inválidos
      throw new Error(errorData?.message || "Error desconocido en el servidor");
    }

    const data = await response.json();
    alert(`Usuario registrado exitosamente: ${data.username}`);
    router.push('/login');

    // Limpia los campos
    name.value = "";
    email.value = "";
    password.value = "";
  } catch (error) {
    console.error("Error al registrar:", error);
    alert(error.message || "Hubo un problema al registrar el usuario.");
  }
};
</script>

<style scoped>
.title {

  font-weight: bold;
  color: #FF0D00;
  font-weight: bold; /* Asegura un texto destacado */
  color: #FF0D00; /* Rojo vibrante para el texto */
  font-family: Arial, Helvetica, sans-serif; /* Fuentes comunes y modernas */
  text-align: center; /* Centra el texto para mayor impacto */
  margin: 10px 0; /* Espaciado uniforme */
  font-size: 1.5em; /* Tamaño de fuente ajustable */

}
</style>
