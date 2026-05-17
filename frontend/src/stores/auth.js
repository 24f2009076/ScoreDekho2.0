import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', () => {
    const token = ref(localStorage.getItem('token') || '')
    const full_name = ref(localStorage.getItem('full_name') || '')

    const isLoggedIn = computed(() => Boolean(token.value))

    function setAuth(newToken, newFullName) {
        token.value = newToken || '';
        full_name.value = newFullName || '';

        if(token.value) {
            localStorage.setItem('token', token.value);
            localStorage.setItem('full_name', full_name.value);
        } else {
            localStorage.removeItem('token');
            localStorage.removeItem('full_name');
        }
    }

    function clearAuth() {
        token.value = ''
        role.value = ''
        username.value = ''

        localStorage.removeItem('token')
        localStorage.removeItem('role')
        localStorage.removeItem('username')
    }

    return { token, full_name, isLoggedIn, setAuth, clearAuth };
})