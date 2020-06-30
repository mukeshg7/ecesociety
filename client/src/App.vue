<template>
  <div id="app">
    <Navbar/>
    <router-view/>
    <Footer/>
  </div>
</template>

<script>
 import Navbar from '@/components/Navbar'
 import Footer from '@/components/Footer'
 import Home from '@/components/Home'
 const API_URL = 'http://localhost:8000'

export default {
  name: 'App',
  components:{
    Navbar,Footer,Home
  }
}
</script>

<style>

</style>
