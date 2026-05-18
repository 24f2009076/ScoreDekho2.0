import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue' 
import LoginView from '@/views/LoginView.vue'
import DashboardView from '@/views/User/DashboardView.vue'
import RegisterView from '@/views/RegisterView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        hideNavBar: false,
        type: 1
      }
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
      meta: {
        hideNavBar: false,
        type: 2
      }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      meta: {
        hideNavBar: false,
        type: 2
      }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      meta: {
        hideNavBar: false,
        type: 3
      }
    }
  ],
})

export default router
