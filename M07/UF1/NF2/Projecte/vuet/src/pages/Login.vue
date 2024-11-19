<template>
  <v-container class="fill-height d-flex align-center justify-center" fluid>
    <v-card class="pa-6" width="400" elevation="3">
      <v-card-title class="text-h5">Iniciar Sesión</v-card-title>
      <v-card-subtitle>Accede a tu cuenta</v-card-subtitle>
      <v-divider></v-divider>
      <v-card-text>
        <v-form ref="loginForm" v-model="isValid">
          <v-text-field
            v-model="email"
            label="Correo Electrónico"
            type="email"
            :rules="[rules.required, rules.email]"
            required
          ></v-text-field>
          <v-text-field
            v-model="password"
            label="Contraseña"
            type="password"
            :rules="[rules.required, rules.min]"
            required
          ></v-text-field>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn
          color="primary"
          :disabled="!isValid"
          block
          @click="handleLogin"
        >
          Entrar
        </v-btn>
      </v-card-actions>
      <v-card-subtitle class="text-center mt-2">
        ¿No tienes cuenta? <a href="/registro">Regístrate aquí</a>
      </v-card-subtitle>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';

// Formulario Reactivo
const email = ref('');
const password = ref('');
const isValid = ref(false);

// Reglas de validación
const rules = {
  required: (value) => !!value || 'Este campo es obligatorio',
  email: (value) =>
    /.+@.+\..+/.test(value) || 'Ingresa un correo válido',
  min: (value) =>
    (value && value.length >= 6) || 'Debe tener al menos 6 caracteres',
};

// Acción del botón de login
const handleLogin = () => {
  // Simulación de autenticación
  if (email.value === 'admin@example.com' && password.value === '123456') {
    alert('Inicio de sesión exitoso');
  } else {
    alert('Credenciales incorrectas');
  }
};
</script>
