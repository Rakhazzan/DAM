<template>
  <v-container>
    <v-card color="red" class="ma-1 pa-1">
      <v-row>
        <v-col cols="6">
          <v-img src="C:\Users\Adrià\Desktop\DAM-1\M07\UF1\NF2\Projecte\vuet\public\img\HeavenTaste.jpg"></v-img>
        </v-col>
        <v-col cols="6">
          <h1 class="text-center">{{ company }}</h1>
          <h2>{{ nom }}</h2>
          <v-icon>mdi-phone</v-icon>
          <p>{{ tel1 }}</p>
          <v-icon>mdi-map-marker</v-icon>
          <p>Catalunya, Manresa</p>
          <v-icon>mdi-email</v-icon>
          <p>heaventaste@fd.net</p>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'

const company = ref("HeavenTaste")
const nom = ref("Fast Food")
const tel1 = ref("97783707")
</script>
