<template>
  <v-container>
    <v-card class="pa-4 mt-4 mx-auto info-card">
      <v-row>
        <!-- Imagen -->
        <v-col cols="12" md="6" class="d-flex justify-center align-center">
          <v-img
            src="/img/HeavenTaste.jpg"
            max-width="300"
            class="rounded"
            alt="HeavenTaste"
          ></v-img>
        </v-col>

        <!-- Información -->
        <v-col cols="12" md="6">
          <h1 class="text-center company-title">{{ company }}</h1>
          <h2 class="text-center company-subtitle">{{ nom }}</h2>
          <div class="info-item">
            <v-icon color="primary">mdi-phone</v-icon>
            <span>{{ tel1 }}</span>
          </div>
          <div class="info-item">
            <v-icon color="primary">mdi-map-marker</v-icon>
            <span>Catalunya, Manresa</span>
          </div>
          <div class="info-item">
            <v-icon color="primary">mdi-email</v-icon>
            <span>heaventaste@fd.net</span>
          </div>
        </v-col>
      </v-row>

      <!-- Mapa -->
      <v-row>
        <v-col cols="12">
          <div class="map-container">
            <iframe
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d47496.67388966143!2d1.7981695!3d41.7246818!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12a4c062b2bc5b0b%3A0x4a67f7db5c472f32!2sManresa%2C%20Barcelona!5e0!3m2!1sen!2ses!4v1698688330141!5m2!1sen!2ses"
              width="100%"
              height="300"
              style="border:0;"
              allowfullscreen=""
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
            ></iframe>
          </div>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from "vue";

const company = ref("HeavenTaste");
const nom = ref("Fast Food");
const tel1 = ref("97783707");
</script>

<style scoped>
.info-card {
  background-color: #f44336; /* Color rojo moderno */
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2); /* Sombra suave */
  max-width: 800px; /* Centrado para mejor presentación */
}

.company-title {
  font-size: 2rem;
  font-weight: bold;
  color: white;
  margin-bottom: 0.5rem;
}

.company-subtitle {
  font-size: 1.5rem;
  color: #ffe0b2; /* Color crema claro */
  margin-bottom: 1rem;
}

.info-item {
  display: flex;
  align-items: center;
  margin-bottom: 0.8rem;
  font-size: 1.1rem;
  color: white;
}

.info-item v-icon {
  margin-right: 8px;
}

.text-center {
  text-align: center;
}

.rounded {
  border-radius: 12px;
}

.map-container iframe {
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}
</style>
