<script setup>
import { ref } from 'vue'
const ciutats = ref([
  {
    nom: 'Barcelona',
    imatge:
      'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Aerial_view_of_Barceloneta_Beach_and_Port_Vell_in_Barcelona%2C_Spain.jpg/1920px-Aerial_view_of_Barceloneta_Beach_and_Port_Vell_in_Barcelona%2C_Spain.jpg',
  },
  {
    nom: 'Madrid',
    imatge:
      'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Palaciorealycatedraldelaalmudena_retouched.jpg/1920px-Palaciorealycatedraldelaalmudena_retouched.jpg',
  },
  {
    nom: 'València',
    imatge:
      'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Iglesia_de_Santa_Catarina%2C_Valencia%2C_Espa%C3%B1a%2C_2014-06-30%2C_DD_143.jpg/420px-Iglesia_de_Santa_Catarina%2C_Valencia%2C_Espa%C3%B1a%2C_2014-06-30%2C_DD_143.jpg',
  },
  {
    nom: 'Sevilla',
    imatge:
      'https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/La_Giralda_August_2012_Seville_Spain.jpg/360px-La_Giralda_August_2012_Seville_Spain.jpg',
  },
  {
    nom: 'Bilbao',
    imatge:
      'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Bilbao_-_Ayuntamiento_24.jpg/1280px-Bilbao_-_Ayuntamiento_24.jpg',
  },
])
</script>

<template>
  <section>
    <div id="app">
      <h1>Ciutats</h1>
      <div class="ciutats-container">
        <div class="ciutat" v-for="ciutat in ciutats" :key="ciutat.nom">
          <img :src="ciutat.imatge" :alt="ciutat.nom" />
          <p>{{ ciutat.nom }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
section {
  text-align: center;
  margin-top: 20px;
}

#app {
  color: white;
  background-color: black;
}

h1 {
  color: #ffd700;
  font-size: 2em;
  margin-bottom: 20px;
}

.ciutats-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  justify-content: center;
  padding: 20px;
}

.ciutat {
  text-align: center;
}

.ciutat img {
  width: 100%;
  height: auto;
  border-radius: 5px;
}

.ciutat p {
  margin-top: 10px;
  font-size: 1.2em;
  color: white;
}

@media (max-width: 768px) {
  .ciutats-container {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
