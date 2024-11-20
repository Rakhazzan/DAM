<template>
  <v-app>
    <v-container>
      <!-- Sección de Cesta -->
      <v-row>
        <v-col cols="12">
          <h1 class="text-center">Detalles de la Compra</h1>
        </v-col>
        <v-col v-if="cart.length" v-for="(item, index) in cart" :key="index" cols="12">
          <v-card>
            <v-card-title>{{ item.name }}</v-card-title>
            <v-card-subtitle>{{ item.description }}</v-card-subtitle>
            <v-card-actions>
              <v-btn color="error" @click="removeFromCart(index)">Eliminar</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="12" v-if="cart.length">
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
      cart: [], // Se llenará con datos desde el almacenamiento global o un servicio
    };
  },
  created() {
    // Carga la cesta desde almacenamiento global o props
    const storedCart = JSON.parse(localStorage.getItem('cart'));
    if (storedCart) {
      this.cart = storedCart;
    }
  },
  methods: {
    removeFromCart(index) {
      this.cart.splice(index, 1);
      localStorage.setItem('cart', JSON.stringify(this.cart)); // Actualiza el almacenamiento
    },
    pay() {
      alert('¡Compra realizada con éxito!');
      this.cart = [];
      localStorage.removeItem('cart'); // Limpia el carrito
    },
  },
};
</script>

<style scoped>
.text-center {
  text-align: center;
}
.text-center {
  text-align: center;
}
.v-application {
  background-color: transparent !important; /* Fondo transparente para toda la app */
}

.v-container {
  background-color: transparent !important; /* Fondo transparente para el contenedor */
  box-shadow: none !important; /* Sin sombras */
  padding: 0 !important; /* Opcional, elimina márgenes internos */
}
.text-center {
  text-align: center;
  color: black;
}
</style>
