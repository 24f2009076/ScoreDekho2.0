<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from './stores/auth'
import NavBar from './components/NavBar.vue'
import LoginNavBar from './components/LoginNavBar.vue'
import DashboardNavBar from './components/DashboardNavBar.vue'

const route = useRoute()
const authStore = useAuthStore()
const showNavBar = computed(() => !route.meta?.hideNavBar)
const type = computed(() => route.meta?.type || 'default')
const isAuthenticated = computed(() => authStore.isLoggedIn)
</script>

<template>
  <div class="app">
    <div v-if="showNavBar" class="nav-bar">
      <div v-if="isAuthenticated">
        <DashboardNavBar />
      </div>
      <div v-else>
        <NavBar v-if="type === 1"/>
        <LoginNavBar v-if="type === 2"/>
      </div>
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
