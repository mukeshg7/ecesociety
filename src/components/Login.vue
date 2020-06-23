<template>
    <div>
        <h1 class="login-head">Login</h1>
        <div class="text-center" data-gr-c-s-loaded="true">
            <form @submit.prevent="login" class="form-signin">
                <img class="mb-4" src="@/assets/nitdgp_logo_black.png" alt="" width="72" height="72">
                <h1 class="h3 mb-3 font-weight-normal">Please log in</h1>
                <label for="inputEmail" class="sr-only">Email address</label>
                <input type="email" id="inputEmail" class="form-control" placeholder="Email address" v-model="email">
                <label for="inputPassword" class="sr-only">Password</label>
                <input type="password" id="inputPassword" class="form-control" placeholder="Password" required="" v-model="password">
                <div class="checkbox mb-3">
                    <label>
                        <input type="checkbox" value="remember-me"> Remember me
                    </label>
                </div>
                <button class="btn btn-lg btn-primary btn-block" type="submit">Log in</button>
                <div>
                    <router-link :to="{name: 'Signup'}">Don't have a account. Signup!</router-link>
                </div>
            </form>
        </div>
    </div>
    
</template>

<script>
export default {
    name: 'Login',
    data(){
        return{
            email: "",
            password: "",
        }
    },
    methods: {
        login: function() {
            let data= {
                email: this.email,
                password: this.password,
            }
            this.$http
            .post('/login', data)
            .then(response => {
                console.log("Logged In");
                router.push("/team");
            })
            .catch(e => {
                console.log("Cannot log in");
                console.log(e);
            })
        },
    }
}
</script>

<style>

.login-head{
    text-align : center;
    padding-top: 20px;
    padding-bottom: 30px;;
}
.form-signin{
    width: 100%;
    max-width: 330px;
    margin: 0px auto;
    padding-bottom: 50px;
}

</style>