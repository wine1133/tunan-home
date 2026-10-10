<script setup>
import NavBar from '../components/NavBar.vue'
import Footer from '../components/Footer.vue'
import '../style.css'
</script>

<template>
  <div class="site">
    <NavBar />
    <main class="site-main"><slot /></main>
    <Footer />
  </div>
</template>

<style scoped>
.site {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.site-main {
  flex: 1;
}
</style>