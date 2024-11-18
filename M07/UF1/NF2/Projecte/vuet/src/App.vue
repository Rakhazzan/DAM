<template>
  <v-app>
    <!-- Navigation Drawer -->
    <v-navigation-drawer v-model="drawer" app>
      <v-list>
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
          link
          :href="item.route"
          @click="drawer = false"
          class="d-flex align-center"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>


    <!-- Toolbar -->
    <v-toolbar color="blue" app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Navegador</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
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


const drawer = ref(false);
const items = [
  { title: 'Home', icon: 'mdi-home', route: '/' },
  { title: 'Columnes', icon: 'mdi-pillar', route: '/columnes' },
  { title: 'Fitxa', icon: 'mdi-card-account-mail', route: '/fitxa' },
];
</script>
