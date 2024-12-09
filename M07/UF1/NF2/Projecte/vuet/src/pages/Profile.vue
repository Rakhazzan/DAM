<template>
  <v-container class="d-flex justify-center align-center fill-height">
    <v-card class="pa-8" width="400">
      <v-card-title class="d-flex justify-center align-center">
        <v-img src="C:/Users/Mohamed/Documents/DAM/M07/UF1/NF2/Projecte/vuet/public/img/HeavenTaste_Logo.jpg"
          alt="HeavenTaste Logo" max-width="150" />
      </v-card-title>

      <v-card-title class="justify-center title">Perfil del Usuario</v-card-title>

      <v-card-text>
        <v-row>
          <v-col cols="12">
            <v-text-field label="Nombre de Usuario" :value="username" readonly outlined dense clearable
              :style="{ backgroundColor: '#292929', color: 'white' }"></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field label="Correo Electrónico" :value="email" readonly outlined dense
              :style="{ backgroundColor: '#292929', color: 'white' }"></v-text-field>
          </v-col>
        </v-row>


        <v-divider class="my-4"></v-divider>

        <v-row>
          <v-col cols="12">
            <v-text-field v-model="newPassword" label="Nueva Contraseña" type="password" outlined></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-btn block color="primary" @click="updatePassword">Actualizar Contraseña</v-btn>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const username = ref("");
const email = ref("");
const newPassword = ref("");

// Función para obtener el perfil del usuario
const fetchUserProfile = async () => {
  const userEmail = localStorage.getItem("userEmail"); // Recuperamos el email del LocalStorage

  if (!userEmail) {
    alert("No se encuentra sesión activa.");
    router.push("/login"); // Redirige al login si no hay email
    return;
  }

  try {
    const response = await fetch("http://localhost:3001/profile", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: userEmail }), // Ahora usamos POST
    });

    if (!response.ok) throw new Error("Error al obtener el perfil");

    const data = await response.json();
    username.value = data.username;
    email.value = data.email;
  } catch (error) {
    console.error("Error al cargar el perfil:", error);
    alert(error.message || "Error desconocido al cargar el perfil.");
  }
};

// Función para actualizar la contraseña
const updatePassword = async () => {
  if (!newPassword.value) {
    alert("Por favor, ingrese una nueva contraseña.");
    return;
  }

  try {
    const response = await fetch("http://localhost:3001/profile", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: email.value, // Usamos el email almacenado para identificar al usuario
        newPassword: newPassword.value, // Nueva contraseña
      }),
    });

    if (!response.ok) throw new Error("Error al actualizar la contraseña.");

    alert("Contraseña actualizada correctamente.");
    newPassword.value = ""; // Limpiar el campo de contraseña
  } catch (error) {
    console.error("Error al actualizar la contraseña:", error);
    alert(error.message || "Error desconocido al actualizar la contraseña.");
  }
};

// Llamada para obtener el perfil al montar el componente
onMounted(() => {
  fetchUserProfile();
});
</script>

<style scoped>
.title {
  font-weight: bold;
  color: #FF0D00;
  font-family: "Arial", sans-serif;
  text-align: center;
  margin: 15px 0;
  font-size: 1.8em;
}

.v-card {
  background-color: #292929;
}
</style>
