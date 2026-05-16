<script setup>
import NavBar from './components/NavBar.vue'
</script>

<template>
  <div class="app">
    <div class="nav-bar">
      <NavBar />
    </div>

    <div class="view-container">
      <RouterView />
    </div>

  </div>
</template>

<style scoped>


.app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    background-color: #000;
    /* border: 2px dashed blue; */
    width: 100%;
    /* overflow-x: hidden; */
    position: relative;
    min-width: 100%;
  }



.view-container {
  flex: 1;
  min-height: 0;
  display: flex;
  /* border: 2px dashed red; */
  width: 100%;
  display: flex;
  min-width: 0;
}

.nav-bar {
  position: sticky;
  top: 0%;
  z-index: 1000;
    /* border: 2px dashed green; */
}

</style>
