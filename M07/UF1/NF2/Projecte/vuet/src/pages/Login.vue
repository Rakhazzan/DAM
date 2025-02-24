<template>
  <v-container class="d-flex justify-center align-center fill-height login-container">
    <v-card class="pa-8" width="400">
      <!-- Logo -->
      <v-card-title class="d-flex justify-center align-center">
        <v-img src="/img/HeavenTaste_Logo.jpg"
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
import { useRouter } from 'vue-router';  

const router = useRouter();  

const valid = ref(false);
const email = ref('');
const password = ref('');


const goToRegister = () => {
  router.push('/register');  
};

const emailRules = [
  (v) => !!v || 'El correo electrónico es obligatorio',
  (v) => /.+@.+\..+/.test(v) || 'Ingrese un correo válido',
];

const passwordRules = [
  (v) => !!v || 'La contraseña es obligatoria',
  (v) => (v && v.length >= 6) || 'La contraseña debe tener al menos 6 caracteres',
];


const login = async () => {
  try {
    const response = await fetch("http://localhost:3001/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
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
   
    localStorage.setItem('user', JSON.stringify(data)); 
   
    window.location.href = "/home"; 
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

  color: #FF0D00;

  font-family: 'Arial', sans-serif;

  text-align: center;
  
  margin: 15px 0;
 
  font-size: 1.8em;
 
}

.forgot-password {
  text-transform: none;
  text-transform: none;
 
  color: #FF9400;
 
  font-size: 0.9em;
  
  text-decoration: underline;
 
  cursor: pointer;
  
  margin-top: 10px;
 
  display: inline-block;
 
}

.forgot-password {
  text-transform: none;
  text-transform: none; 
  color: #FF9400; 
  font-size: 0.9em; 
  text-decoration: underline; 
  cursor: pointer; 
  margin-top: 10px; 
  display: inline-block; 
}

.center-content {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  
  width: 100%;
  
}
</style>
