<template>
  <nav class="navbar">
    <div class="blur"></div>
    <div class="nav-brand">
      <RouterLink to="/">ScoreDekho</RouterLink>
    </div>
    <div class="nav-menu">
      <RouterLink to="/" class="nav-link">Home</RouterLink>
      <RouterLink to="/tournaments" class="nav-link">Tournaments</RouterLink>
    </div>
    
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'

</script>

<style scoped>

    .navbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      /* background-color: #000; */
      color: #fff;
      padding: 1rem 0.5rem;

      /* border: 2px dashed red; */
    }

    .blur {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
        z-index: -1;
    }

    .nav-brand a {
        font-size: 1.75rem;
        font-weight: bold;
        font-family: 'Manrope', sans-serif;
        color: #40e436;
        text-decoration: none;
    }

    .nav-menu {
      display: flex;
      gap: 1.5rem;
      font-size: 1.05rem;
      padding: 0.65rem 2rem;
      align-items: center;
      flex: 1;
      /* border: 2px solid red; */
    }

    .nav-menu a {
        color: #7c808e;
        text-decoration: none;
    }

    .nav-menu a:hover {
        color: #40e436;
    }

    .nav-menu .router-link-active {
        color: #40e436;
        position: relative;
    }
    .nav-menu .router-link-active::after {
      content:'';
      background-color: #40e436;
      position: absolute;
      left: 50%;
      bottom: -10px;
      transform: translateX(-50%);

      width: 80%;
      height: 1.5px;
    }

    .nav-login {
        display: flex;
        gap: 1.5rem;
        font-size: 1.05rem;
        padding: 0 2rem;
        align-items: center;
        border: 2px solid green;
    }

    .login {
        color: #7c808e;
        text-decoration: none;
    }

    .login:hover {
        color: #40e436;
    }

    .get-started {
        background-color: #40e436;
        padding: 0.65rem 1.5rem;
        border-radius: 4px;
        color: #000;
        font-weight: 500;
        text-decoration: none;
    }

    .get-started:hover {
        background-color: #32c92e;
    }

    @media (max-width: 720px) {
      .nav-menu { display: none; }
      .nav-login .login { display: none; }
      .nav-login { padding: 0 0.5rem; }
      .get-started { padding: 0.5rem 1rem; }
    }

</style>