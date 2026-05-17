<template>
    
    <div class="body" @pointermove="handlePointerMove">
        <div ref="blob" class="blob"></div>
        <div class="blur"></div>
        <div class="card reveal">
            <div class="card-head">Welcome back</div>
            <div class="card-text">Log in to manage your leagues and tournaments</div>
            <form class="login-form" @submit="login">
                <div class="email-input input">
                    <label for="email" class="input-label">FULL NAME</label>
                    <input type="text" placeholder="Enter your full name" v-model="fullName" />
                </div>
                <div class="password-input input">
                    <label for="password" class="input-label">PASSWORD</label>
                    <input type="password" placeholder="Enter your password" v-model="password" />
                </div>
                <button type="submit" class="submit-btn">Log In</button>
            </form>
            <div class="register-text">Don't have an account? <a href="/register">Sign up</a></div>
        </div>
    </div>

</template>

<script setup>
import { ref } from "vue";
const blob = ref(null);
const handlePointerMove = (event) => {
    if (!blob.value) return;

    const { clientX, clientY } = event;

    blob.value.animate({
        left: `${clientX}px`,
        top: `${clientY}px`
    }, { duration: 50000, fill: "forwards" });
};

import { onMounted, onBeforeUnmount } from 'vue'

onMounted(() => {
  const sections = document.querySelectorAll('.reveal')

  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible')
          observer.unobserve(entry.target)
        }
      })
    },
    { threshold: 0.15 }
  )

  sections.forEach(section => observer.observe(section))
})


import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';
const authStore = useAuthStore();
const router = useRouter();
const fullName = ref('');
const password = ref('');

async function login(event) {
    event.preventDefault();
    
    const loginData = {
        full_name: fullName.value,
        password: password.value
    }

    const response = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(loginData)
    });

    if (response.ok) {
        const data = await response.json();
        console.log('Login successful:', data);
        
        authStore.setAuth(data.access_token, data.full_name);
        router.push('/dashboard');
    } else {
        console.log('Login failed:', response.statusText);
        // Handle login failure (e.g., show error message)
    }

    // console.log(loginData);

    
}


</script>

<style scoped>
.reveal {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 0.6s ease, transform 0.6s ease;
}

.reveal.is-visible {
    opacity: 1;
    transform: translateY(0);
}

.body {
    position: relative;
    width: 100%;
    background-color: rgb(0, 0, 0);
    overflow: hidden;
    max-height: 100vh;
    /* border: 2px solid red; */

    display: flex;
    justify-content: center;
    align-items: center
}


.card {
    height: 35rem;
    width: 40rem;
    padding: 30px 50px;
    border-radius: 50px;
    background-color: rgba(63, 197, 74, 0.075);
    /* backdrop-filter: blur(20px); */
    border-top: 1px solid rgba(255, 255, 255, 0.2);
    border-left: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);

    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    z-index: 3;

    font-family: 'Manrope', sans-serif;
    font-weight: 500;
    color: #dae2ff;
}

.card-head {
    font-size: 2.5rem;
    width: 100%;
    font-weight: 700;
    margin-bottom: 1rem;
    display: flex;
    justify-content: flex-start;
}

.card-text {
    font-size: 1.25rem;
    width: 100%;
    margin-bottom: 2rem;
    display: flex;
    justify-content: flex-start;
}

.login-form {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    gap: 5rem;
    flex: 1;
    padding: 1rem;

    /* border: 2px dashed lime; */
}

.input {
    width: 100%;
    display: flex;
    /* border: 2px solid lime; */
    height: 40px;
    flex-direction: column;
    gap: 0.5rem;
    cursor: text;
}

.input-label {
    font-size: 1rem;
    color: #dae2ff;
    /* margin-right: 1rem; */
    width: 100%;
    font-weight: 700;
}

input {
    width: 100%;
    height: 100%;
    border-radius: 10px;
    border: rgb(46, 89, 46) 1px solid;
    background-color: transparent;
    padding: 1.5rem 1rem;
    color: #40e436;
    font-size: 1.2rem;
    outline: none;
}

input:focus {
    outline: none;
    border-color: #40e436;
}

.submit-btn {
    width: 100%;
    padding: 1rem;
    border-radius: 10px;
    border: none;
    background-color: #40e436;
    color: #000;
    font-size: 1.25rem;
    font-weight: 700;
    cursor: pointer;
    transition: background-color 0.3s ease, scale 0.1s ease-in-out;
}

.submit-btn:hover {
    background-color: #32c92e;
    scale: 1.02;
}

.submit-btn:active {
    scale: 1;
}

.register-text {
    margin-top: 1.5rem;
    color: #dae2ff;
    font-size: 0.95rem;
}

.register-text a {
    color: #40e436;
    text-decoration: none;
}

.register-text a:hover {
    text-decoration: underline;
}

.blur {
    width: 100%;
    height: 100%;
    /* background-color: red; */
    position: absolute;
    z-index: 2;
    backdrop-filter: blur(150px);
    opacity: 1;
}

.blob {
    position: absolute;
    top: 50%;
    left: 50%;
    height: 320px;
    aspect-ratio: 1;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    background: linear-gradient(to right, rgba(63, 228, 54, 0.703), rgba(64, 228, 54, 0.03));
    background-size: 200% 200%;
    animation: spin 8s linear infinite forwards; 
    transition: transform 3s ease-out;
    /* filter: blur(200px); */

}

@keyframes spin {
    from { transform: translate(-50%, -50%) rotate(0deg) scale(1, 1); }
    25% { transform: translate(-50%, -50%) rotate(90deg) scale(1, 1.5); }
    50% { transform: translate(-50%, -50%) rotate(180deg) scale(1.5, 1); }
    to { transform: translate(-50%, -50%) rotate(360deg) scale(1, 1); }
}

/* Medium screens */
@media (max-width: 900px) {
  .card { max-width: 640px; }
  .blob { height: min(30vh, 260px); }
}

/* Small screens / phones */
@media (max-width: 640px) {
  .body { align-items: flex-start; padding-top: 4.2rem; }
  .card {
    width: 92vw;
    padding: 18px;
    border-radius: 18px;
    box-shadow: none;
    border-top: none;
    border-left: none;
    background-color: rgba(63,197,74,0.05);
  }
  .login-form { gap: 1rem; }
  .card-head { 
        margin-bottom: 0.5rem; 
        font-size: 1.75rem; 
    }
    .card-text { 
            margin-bottom: 1rem; 
            font-size: 0.8rem; 
        }
    .login-form {
        justify-content: center;
        gap: 3rem;
    }
}

/* @media (max-width: 420px) {
  .card { padding: 14px; border-radius: 12px; }
  .card-head { font-size: 1.25rem; }
  .card-text { font-size: 0.95rem; }
  input { padding: 0.85rem; font-size: 0.95rem; }
  .submit-btn { padding: 0.8rem; font-size: 1rem; }
  .blob { display: none; }
  .blur { backdrop-filter: blur(40px); }
} */

</style>