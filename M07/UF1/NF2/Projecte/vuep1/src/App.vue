<template>
  <div class="date-time-container">
    <p>{{ currentDate }}</p>
    <p>{{ currentTime }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentDate: '',
      currentTime: '',
    }
  },
  created() {
    this.updateDateTime()
    setInterval(this.updateDateTime, 1000)
  },
  methods: {
    updateDateTime() {
      const now = new Date()
      this.currentDate = `${now.getDate()}/${now.getMonth() + 1}/${now.getFullYear()}`
      this.currentTime = now.toLocaleTimeString()
    },
  },
}
</script>

<style scoped>
.date-time-container {
  background-color: black;
  color: white;
  text-align: center;
  padding: 20px;
  font-family: Arial, sans-serif;
  font-size: 2rem;
}
</style>
