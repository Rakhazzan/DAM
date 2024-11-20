<template>
  <v-app>
    <v-container>
      <!-- Sección de Productos -->
      <v-row>
        <v-col cols="12">
          <h1 class="text-center">Nuestros Productos</h1>
        </v-col>
        <v-col v-for="(product, index) in products" :key="index" cols="12" md="6" lg="4">
          <v-card>
            <v-img :src="product.image" height="200px"></v-img>
            <v-card-title>{{ product.name }}</v-card-title>
            <v-card-subtitle>{{ product.description }}</v-card-subtitle>
            <v-card-actions>
              <v-btn color="primary" @click="addToCart(product)">Añadir a la cesta</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>

      <!-- Sección de Descuentos -->
      <v-row>
        <v-col cols="12">
          <h1 class="text-center">Descuentos</h1>
        </v-col>
        <v-col v-for="(discount, index) in discounts" :key="index" cols="12" md="6" lg="4">
          <v-card>
            <v-img :src="discount.image" height="200px"></v-img>
            <v-card-title>{{ discount.name }}</v-card-title>
            <v-card-subtitle>{{ discount.description }}</v-card-subtitle>
            <v-card-actions>
              <v-btn color="secondary" @click="addToCart(discount)">Añadir a la cesta</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      products: [
        { name: "Hamburguesa Clásica", description: "Deliciosa hamburguesa con queso.", image: "img/Burger.jpg" },
        { name: "Papas Fritas", description: "Crujientes y doradas.", image: "img/fries.jpg" },
      ],
      discounts: [
        { name: "Combo Familiar", description: "Hamburguesas y papas para 4 personas.", image: "img/Combo.jpg" },
      ],
      cart: [],
    };
  },
  methods: {
    addToCart(product) {
    this.cart.push(product);
    localStorage.setItem('cart', JSON.stringify(this.cart)); // Guarda en localStorage
  },
    removeFromCart(index) {
      this.cart.splice(index, 1);
    },
  },
};
</script>

<style scoped>
.text-center {
  text-align: center;
  color: black;
}
.v-application {
  background-color: transparent !important; /* Fondo transparente para toda la app */
}

.v-container {
  background-color: transparent !important; /* Fondo transparente para el contenedor */
  box-shadow: none !important; /* Sin sombras */
  padding: 0 !important; /* Opcional, elimina márgenes internos */
}
</style>
