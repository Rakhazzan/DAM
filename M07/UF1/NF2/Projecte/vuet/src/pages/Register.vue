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
            label="P  assword"
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
import axios from 'axios';

const valid = ref(false);
const name = ref('');
const email = ref('');
const password = ref('');

const nameRules = [(v) => !!v || 'El nombre es obligatorio'];

const emailRules = [
  (v) => !!v || 'El correo electrónico es obligatorio',
  (v) => /.+@.+\..+/.test(v) || 'Ingrese un correo válido',
];

const passwordRules = [
  (v) => !!v || 'La contraseña es obligatoria',
  (v) => (v && v.length >= 6) || 'La contraseña debe tener al menos 6 caracteres',
];
const register = async () => {
  try {
    // Solicitud POST para registrar al usuario
    const response = await axios.post('http://localhost:3000/register', {
      name: name.value,
      email: email.value,
      password: password.value,
    });

    // Mostrar mensaje de éxito
    alert(response.data.message);
    console.log('Registro exitoso:', response.data);
    // Puedes redirigir al usuario o limpiar el formulario, por ejemplo:
    name.value = '';
    email.value = '';
    password.value = '';
  } catch (error) {
    // Mostrar mensaje de error
    console.error('Error en el registro:', error.response ? error.response.data : error.message);
    alert(error.response ? error.response.data.message : 'Error desconocido');
  }
};

</script>

<style scoped>
.title {
  font-weight: bold;
  color: #FF0D00;
}
</style>
