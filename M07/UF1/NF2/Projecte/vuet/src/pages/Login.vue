<template>
  <v-container class="d-flex justify-center align-center fill-height login-container">
    <v-card class="pa-8" width="400">
      <!-- Logo -->
      <v-card-title class="d-flex justify-center align-center">
        <v-img src="C:/Users/Mohamed/Documents/DAM/M07/UF1/NF2/Projecte/vuet/public/img/HeavenTaste_Logo.jpg"
          alt="HeavenTaste Logo" max-width="150" />
      </v-card-title>

      <!-- Title -->
      <v-card-title class="justify-center title">Iniciar Sesión</v-card-title>

      <v-card-text>
        <v-form ref="form" v-model="valid" lazy-validation>
          <!-- Email -->
          <v-text-field v-model="email" label="Correo electrónico" :rules="emailRules" required
            variant="outlined"></v-text-field>

          <!-- Password -->
          <v-text-field v-model="password" label="Contraseña" type="password" :rules="passwordRules" required
            variant="outlined"></v-text-field>

          <!-- Forgot password -->
          <div class="d-flex justify-center align-center">
            <v-btn text class="forgot-password">¿Olvidaste tu contraseña?</v-btn>
          </div>
        </v-form>
      </v-card-text>

      <!-- Actions -->
      <v-card-actions>
        <v-btn block color="primary" @click="goToRegister">Registrarse</v-btn>
      </v-card-actions>

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
const goToRegister = () => {
  window.location.href = 'http://localhost:3000/register'; // Redirige a la página de registro
};

const emailRules = [
  (v) => !!v || 'El correo electrónico es obligatorio',
  (v) => /.+@.+\..+/.test(v) || 'Ingrese un correo válido',
];

const passwordRules = [
  (v) => !!v || 'La contraseña es obligatoria',
  (v) => (v && v.length >= 6) || 'La contraseña debe tener al menos 6 caracteres',
];

// Función para manejar el inicio de sesión
const login = async () => {
  try {
    const response = await fetch("http://localhost:3001/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: email.value,
        password: password.value,
      }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || "Error desconocido en el servidor");
    }

    const data = await response.json();
    alert(`Inicio de sesión exitoso: Bienvenido, ${data.username}`);
    // Redirigir a otra página o guardar el estado del usuario
  } catch (error) {
    console.error("Error al iniciar sesión:", error);
    alert(error.message || "Error desconocido en el servidor.");
  }
};
</script>

<style scoped>
.title {
  font-weight: bold;
  font-weight: bold;
  /* Asegura un texto destacado */
  color: #FF0D00;
  /* Rojo del branding */
  font-family: 'Arial', sans-serif;
  /* Fuente limpia y accesible */
  text-align: center;
  /* Centra el título para mejor presentación */
  margin: 15px 0;
  /* Espaciado vertical */
  font-size: 1.8em;
  /* Ajusta el tamaño para resaltar */
}

.forgot-password {
  text-transform: none;
  text-transform: none;
  /* Mantiene el texto en su formato original */
  color: #FF9400;
  /* Naranja del branding */
  font-size: 0.9em;
  /* Tamaño más pequeño para jerarquía visual */
  text-decoration: underline;
  /* Sugiere que es un enlace */
  cursor: pointer;
  /* Indica que es interactivo */
  margin-top: 10px;
  /* Espaciado superior */
  display: inline-block;
  /* Permite margen controlado */
}

.center-content {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  /* Asegura que ocupe el alto disponible */
  width: 100%;
  /* Opción adicional para alinear correctamente */
}
</style>
