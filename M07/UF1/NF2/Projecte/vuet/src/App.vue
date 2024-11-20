<template>
  <v-app>
    <!-- Navigation Drawer -->
    <v-navigation-drawer v-model="drawer" app class="custom-drawer">
      <v-list>
        <v-list-item v-for="(item, index) in items" :key="index" link :href="item.route" @click="drawer = false"
          class="d-flex align-center custom-list-item">
          <v-list-item-icon>
            <v-icon class="custom-icon">{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="custom-title">{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>


    <!-- Toolbar -->
    <v-toolbar color="#f06b64" app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title> HeavenTaste</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-btn icon @click="goToCheckout">
        <v-icon>mdi-cart</v-icon>
      </v-btn>
      <v-btn icon @click="navigateToLogin">
        <v-icon>mdi-login</v-icon>
      </v-btn>
    </v-toolbar>
    <!-- Main Content -->
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>


<script setup>
import { ref } from 'vue';

import { useRouter } from 'vue-router';

const router = useRouter();

const navigateToLogin = () => {
  router.push('/login'); // Redirige a la ruta del componente Login.vue
};
const goToCheckout = () =>{
   router.push('/checkout'); // Redirige a la nueva página

};

const drawer = ref(false);
const items = [
  { title: 'Home', icon: 'mdi-home', route: '/home' },
  { title: 'Columnes', icon: 'mdi-pillar', route: '/columnes' },
  { title: 'Informació', icon: 'mdi-card-account-mail', route: '/fitxa' },
];
</script>
