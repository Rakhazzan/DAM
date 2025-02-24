<template>
  <v-app>
    <v-container>
      
      <v-row>
        <v-col cols="12">
          <h1 class="text-center">Detalles de la Compra</h1>
        </v-col>
        <v-col v-if="cart.length" v-for="(item, index) in cart" :key="index" cols="12">
          <v-card>
            <v-card-title>{{ item.name }}</v-card-title>
            <v-card-subtitle>{{ item.description }}</v-card-subtitle>
            <v-card-subtitle>Precio: {{ item.price.toFixed(2) }} €</v-card-subtitle>
            <v-card-actions>
              <v-btn color="error" @click="removeFromCart(index)">Eliminar</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="12" v-if="cart.length">
          <v-card>
            <v-card-title>Total: {{ totalPrice.toFixed(2) }} €</v-card-title>
          </v-card>
          <v-btn block color="success" @click="pay">Pagar</v-btn>
        </v-col>
        <v-col cols="12" v-else>
          <p class="text-center">La cesta está vacía.</p>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      cart: [], 
    };
  },
  computed: {
    totalPrice() {
      return this.cart.reduce((total, item) => total + item.price, 0);
    }
  },
  created() {
    
    const storedCart = JSON.parse(localStorage.getItem('cart'));
    if (storedCart) {
      this.cart = storedCart;
    }
  },
  methods: {
    removeFromCart(index) {
      this.cart.splice(index, 1);
      localStorage.setItem('cart', JSON.stringify(this.cart)); 
    },
    pay() {
      alert('¡Compra realizada con éxito!');
      this.cart = [];
      localStorage.removeItem('cart'); 
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

.product-card {
  margin-bottom: 1rem;
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
  color: #e40505;
  margin-top: 0.5rem;
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
