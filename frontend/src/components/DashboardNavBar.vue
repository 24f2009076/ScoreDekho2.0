<template>
  <nav class="navbar">
    <div class="blur"></div>
    <div class="nav-brand">
      <RouterLink to="/dashboard">ScoreDekho</RouterLink>
    </div>
    <div class="nav-login">
      <div class="login">
        <img src="/icons/user.png" alt="profile-pic" class="profile-pic">
        <span class="name">
          {{ full_name }}
        </span>
      </div>

      <div class="options">
        <RouterLink to="/dashboard" class="option">Profile</RouterLink>
        <a class="option" @click="logout">Logout</a>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { onMounted, onBeforeUnmount } from 'vue';

const authStore = useAuthStore();
const router = useRouter();
const full_name = authStore.full_name;

onMounted(() => {
  const nav_login = document.querySelector('.nav-login');
  nav_login.addEventListener('click', () => {
    const options = document.querySelector('.options');
    if (options.style.display === 'flex') {
      options.style.display = 'none';
    } else {
      options.style.display = 'flex';
    }
  });
  
  const onDocMouseDown = (e) => {
    const options = document.querySelector('.options');
    const navLogin = document.querySelector('.nav-login');
    if (!options) return;
    // if options is open and the click is outside options and outside nav-login, close it
    if (options.style.display === 'flex') {
      if (!options.contains(e.target) && !navLogin.contains(e.target)) {
        options.style.display = 'none';
      }
    }
  };

  document.addEventListener('mousedown', onDocMouseDown);

  // store the handler so it can be removed on unmount
  window.__dashboard_nav_mousedown = onDocMouseDown;
  
  

onBeforeUnmount(() => {
  const handler = window.__dashboard_nav_mousedown;
  if (handler) document.removeEventListener('mousedown', handler);
  delete window.__dashboard_nav_mousedown;
});
});

function logout() {
  authStore.logOut();
  router.push('/login');
}



</script>

<style scoped>
.options {
  position: fixed;
  top: 60px;
  right: 70px;
  width: 100px;
  height: auto;

  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  background-color: rgba(8, 98, 9, 0.12);
  padding: 0.5rem;

  border: 2px solid rgba(8, 98, 9, 0.8);
  border-radius: 4px;

  font-size: 1.1rem;
  display: none;
}

.option {
  color: #7c808e;
  text-decoration: none;
  cursor: pointer;
}

.option:hover {
  color: #40e436;
}

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
  content: '';
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
  /* border: 2px solid green; */
}

.login {
  color: #7c808e;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  cursor: pointer;
}

.login:hover {
  color: #40e436;
}

.profile-pic {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  margin-right: 0.5rem;
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
  .nav-menu {
    display: none;
  }

  .nav-login .name {
    display: none;
  }
  .nav-login {
    padding: 0 0.5rem;
  }

  .get-started {
    padding: 0.5rem 1rem;
  }
}
</style>