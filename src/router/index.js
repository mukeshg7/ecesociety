import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Academics from '@/components/Academics'
import Faculty from '@/components/Faculty'
import Team from '@/components/Team'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/academics',
      name: 'Academics',
      component: Academics
    },
    {
      path: '/faculty',
      name: 'Faculty',
      component: Faculty
    },
    {
      path: '/team',
      name: 'Team',
      component: Team,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
  ]
})
