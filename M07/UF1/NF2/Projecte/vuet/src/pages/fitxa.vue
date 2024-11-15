<template>
  <v-container>
    <v-card color="blue" class="ma-1 pa-1">
      <v-row>
        <v-col cols="6">
          <v-img src="https://img.freepik.com/free-vector/bird-colorful-logo-gradient-vector_343694-1365.jpg?t=st=1730029690~exp=1730033290~hmac=d3ebc9f71b5615696033dbe93fdc70c240fab2b9e9512971be97ae787655a2b6&w=826"></v-img>
        </v-col>
        <v-col cols="6">
          <h1 class="text-center">{{ company }}</h1>
          <h2>{{ nom }}</h2>
          <p>{{ contingut }}</p>
          <v-icon>mdi-phone</v-icon>
          <p>{{ tel1 }}</p>
          <v-icon>mdi-map-marker</v-icon>
          <p>Sant Vicenç de Castellet</p>
          <v-icon>mdi-email</v-icon>
          <p>pepe@inscastellet.cat</p>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'

const company = ref("Castellet Company")
const nom = ref("Pepe Pepitez")
const contingut = ref("Cap superior")
const tel1 = ref("98983209")
</script>
