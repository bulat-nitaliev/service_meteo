import { createRouter, createWebHistory } from "vue-router";

import Login from  '@/pages/Login'
import SignUp from  '@/pages/SignUp'
import Home from '@/pages/Home'




const routes = [
    {
        path:'/',
        component: Home
    },
    {
        path:'/login',
        component: Login
    },
    
    {
        path:'/registr',
        component: SignUp
    },
    
    
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router