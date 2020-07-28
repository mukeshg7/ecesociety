<template>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark py-0 sticky-top" >
        <div class="d-flex flex-grow-1 py-0">
            <span class="w-100 d-lg-none d-block"><!-- hidden spacer to center brand on mobile --></span>
            <router-link :to="{ name: 'Home' }" class="navbar-brand">
            <img id="logoNitDgp" src="@/assets/nitdgp_logo_white.png" style="width:50px; height:50px" alt="logo">
            <strong>ECESS</strong>
            </router-link>
        <!-- <a class="navbar-brand-two mx-auto d-lg-none d-inline-block py-0" href="#">
            <img src="/static/image/logo.png" width="20%" alt="logo">
            </a> -->
            <div class="w-100 text-right py-0">
                <button class="navbar-toggler mt-2" type="button" data-toggle="collapse" data-target="#myNavbar">
                   <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
        <div class="collapse navbar-collapse flex-grow-1 text-right py-0" id="myNavbar">
         <ul class="navbar-nav ml-auto flex-nowrap"> 
            <li class="nav-item">
                <router-link :to="{ name: 'Home'}" class="nav-link m-2 menu-item">Home</router-link>
            </li>
            <li class="nav-item">
                <router-link :to="{ name: 'Academics'}" class="nav-link m-2 menu-item">Academics</router-link>
            </li>
            <li class="nav-item">
                <a href="https://nitdgp.ac.in/department/EC/people" class="nav-link m-2 menu-item">Faculty</a>
            </li>
            <li class="nav-item ">
                <router-link :to="{ name: 'Team'}" class="nav-link m-2 menu-item">Team</router-link>
            </li>
            <li class="nav-item">
                <router-link :to="{ name: 'Achievements'}" class="nav-link m-2 menu-item">Achievements</router-link>
            </li>
            <!-- <li class="nav-item ">
                <router-link :to="{ name: 'Blogs'}" class="nav-link m-2 menu-item">Blog</router-link>
            </li>
            <li class="nav-item">
                <router-link :to="{ name: 'Login'}" class="nav-link m-2 menu-item">Login</router-link>
            </li> -->
            </ul>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'Navbar',
    data() {
        return{
        
        }
    }
}
</script>

<style>

</style>

