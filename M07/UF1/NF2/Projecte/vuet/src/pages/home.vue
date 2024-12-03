<template>
  <v-app>
    <v-container>
      <!-- Sección de Productos -->
      <v-row class="section">
        <v-col cols="12">
          <h1 class="text-center section-title">Nuestros Productos</h1>
        </v-col>
        <v-col
          v-for="(product, index) in products"
          :key="index"
          cols="12"
          md="6"
          lg="4"
          class="product-card"
        >
          <v-card class="hoverable">
            <v-img :src="product.image" height="200px" class="product-image"></v-img>
            <v-card-title class="product-title">{{ product.name }}</v-card-title>
            <v-card-subtitle class="product-description">
              {{ product.description }}
            </v-card-subtitle>
            <v-card-subtitle class="product-price">
              Precio: {{ product.price.toFixed(2) }} €
            </v-card-subtitle>
            <v-card-actions>
              <v-btn color="primary" class="add-to-cart" @click="addToCart(product)">
                Añadir a la cesta
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>

      <!-- Sección de Descuentos -->
      <v-row class="section">
        <v-col cols="12">
          <h1 class="text-center section-title">Descuentos</h1>
        </v-col>
        <v-col
          v-for="(discount, index) in discounts"
          :key="index"
          cols="12"
          md="6"
          lg="4"
          class="product-card"
        >
          <v-card class="hoverable">
            <v-img :src="discount.image" height="200px" class="product-image"></v-img>
            <v-card-title class="product-title">{{ discount.name }}</v-card-title>
            <v-card-subtitle class="product-description">
              {{ discount.description }}
            </v-card-subtitle>
            <v-card-subtitle class="product-price">
              Precio: {{ discount.price.toFixed(2) }} €
            </v-card-subtitle>
            <v-card-actions>
              <v-btn color="secondary" class="add-to-cart" @click="addToCart(discount)">
                Añadir a la cesta
              </v-btn>
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
        { name: "Hamburguesa Clásica", description: "Deliciosa hamburguesa con queso.", image: "img/Burger.jpg", price: 5.99 },
        { name: "Papas Fritas", description: "Crujientes y doradas.", image: "img/fries.jpg", price: 2.99 },
      ],
      discounts: [
        { name: "Combo Familiar", description: "Hamburguesas y papas para 4 personas.", image: "img/Combo.jpg", price: 15.99 },
      ],
      cart: [],
    };
  },
  methods: {
    addToCart(product) {
      this.cart.push(product);
      localStorage.setItem("cart", JSON.stringify(this.cart));
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
}

.section {
  margin-bottom: 2rem;
}

.section-title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1rem;
  color: #4caf50; /* Verde resalta los títulos */
}

.product-card {
  margin-bottom: 1rem;
}

.product-image {
  border-radius: 8px 8px 0 0;
}

.product-title {
  font-size: 1.2rem;
  font-weight: bold;
}

.product-description {
  font-size: 0.9rem;
  color: #757575;
}

.product-price {
  font-size: 1rem;
  font-weight: bold;
  color: #f57c00; /* Naranja resalta el precio */
  margin-top: 0.5rem;
}

.add-to-cart {
  width: 100%;
  color: white;
  font-weight: bold;
}

.hoverable {
  transition: box-shadow 0.3s;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.hoverable:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}
</style>
