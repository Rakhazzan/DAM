<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const catImages = ref([])

async function funcioGat() {
  try {
    const res = await fetch('https://api.thecatapi.com/v1/images/search?limit=10')
    const data = await res.json()
    catImages.value = data
  } catch (error) {
    alert('Error en cargar las imágenes: ' + error)
  }
}

onMounted(() => {
  funcioGat()
  const intervalId = setInterval(funcioGat, 3000)
  onUnmounted(() => clearInterval(intervalId))
})
</script>
<template>
  <main>
    <header>
      <h1>Gatets</h1>
    </header>
    <section class="images-container">
      <div v-for="(cat, index) in catImages" :key="index" class="cat-image">
        <img :src="cat.url" alt="Imatge de gat" loading="lazy" />
      </div>
    </section>
  </main>
</template>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f7f7f7;
  color: #333;
}

main {
  width: 100%;
  max-width: 1200px;
  padding: 20px;
  text-align: center;
}

header h1 {
  font-size: 2rem;
  margin-bottom: 20px;
}

.images-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 15px;
}

.cat-image img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.cat-image img:hover {
  transform: scale(1.05);
}
</style>
