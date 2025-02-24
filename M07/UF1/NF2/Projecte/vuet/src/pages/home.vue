<template>
  <v-app>
    <v-container>
     
      <v-row class="section">
        <v-col cols="12">
          <v-text-field
            v-model="searchQuery"
            label="Buscar productos u ofertas"
            prepend-icon="mdi-magnify"
            class="mb-4"
            outlined
          ></v-text-field>
        </v-col>
      </v-row>

      
      <v-row class="section">
        <v-col cols="12">
          <h1 class="text-center section-title">Nuestros Productos</h1>
        </v-col>
        <v-col
          v-for="(product, index) in filteredProducts"
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

     
      <v-row class="section">
        <v-col cols="12">
          <h1 class="text-center section-title">Promociones</h1>
        </v-col>
        <v-col
          v-for="(discount, index) in filteredDiscounts"
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
      searchQuery: "", 
      products: [
        { name: "Hamburguesa Clásica", description: "Deliciosa hamburguesa con queso.", image: "img/Burger.jpg", price: 5.99 },
        { name: "Papas Fritas", description: "Crujientes y doradas.", image: "img/fries.jpg", price: 2.99 },
        { name: "Wrap", description: "Wrap estilo mejicano.", image: "img/Wrap.jpg", price: 7.99 },
        { name: "Ensalada Cesar", description: "Todas las ensaladas llevan al Cesar.", image: "img/Ensalada.jpg", price: 8.99 },
        { name: "Nuggets extra grandes", description: "Doradas y grandes.", image: "img/Nuggets.jpg", price: 8.99 },
        { name: "Helado polar", description: "Importado del polo norte.", image: "img/Helado.jpg", price: 3.99 },
      ],
      discounts: [
        { name: "Combo Familiar", description: "Hamburguesas y patatas para 4 personas.", image: "img/Combo.jpg", price: 15.99 },
        { name: "Combo de soltero", description: "Hamburguesas y patatas para un soltero.", image: "img/combo2.jpg", price: 9.50 },
        { name: "Patatas extra grandes", description: "Patatas,para papanatas,tu.", image: "img/Patatas.jpg", price: 9.50 },
      ],
      cart: [],
    };
  },
  computed: {
    filteredProducts() {
      
      return this.products.filter((product) =>
        product.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
    filteredDiscounts() {
      
      return this.discounts.filter((discount) =>
        discount.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
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
  color: #c82323;
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
  color: #f57c00;
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
  background-color: beige;
}
</style>

