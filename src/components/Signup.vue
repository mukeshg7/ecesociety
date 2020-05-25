<template>
    <div class="container text-center">
        <h1>Signup</h1>
            <form @submit.prevent="onSignup" class="register-form" id="register-form">
                            <div class="form-group">
                                <label for="name">Name: </label>
                                <input type="text" name="name" v-model="name" 
                                id="name" placeholder="Name"/>
                            </div>
                            <div class="form-group">
                                <label for="reg_num">Email: </label>
                                <input type="text" name="reg_num" v-model="reg_num" 
                                id="reg_num" :rules="[check_reg]" placeholder="xxUxxxx"/>
                            </div>
                            <div class="form-group">
                                <label for="roll_num">Email: </label>
                                <input type="text" name="roll_num" v-model="roll_num" 
                                id="roll_num" :rules="[check_roll]" placeholder="xxECxxxx"/>
                            </div>
                            <div class="form-group">
                                <label for="email">Email: </label>
                                <input type="email" name="email" v-model="email" 
                                id="email" placeholder="Email"/>
                            </div>
                            <div class="form-group">
                                <label for="pass">Password</label>
                                <input type="password" name="password" v-model="password" 
                                id="password" placeholder="Password"/>
                            </div>
                            <div class="form-group">
                                <label for="re-pass">Password again: </label>
                                <input type="password" name="re_password" v-model="re_password" 
                                id="re_password" placeholder="Confirm password"
                                :rules="[confirmPassword]"/>
                            </div>
                            <div class="form-group form-button">
                                <input type="submit" name="signup" id="signup" class="form-submit" value="Register"/>
                            </div>
            </form>
    </div>
</template>

<script>
import common from '@/services/common.js'
export default {
    name: 'Signup',
    data(){
        return {
            name: "", 
            email: "",
            reg_num: "",
            roll_num: "",
            password: "",
            re_password: "",
        }
    },
    is_right: false,
    methods: {
        confirmPassword(){
            if(this.password != this.re_password){
                is_right = false
                return "Passwords do no match" 
            }
            else is_right = true
        },
        check_reg(){

        },
        check_roll(){

        },
        onSignup(){
            console.log({email: this.email, password: this.password, confirm_password: this.re_password})
            this.$http
            .post('api/users', {
                name: this.name,
                email: this.email,
                password: this.password
            })
            .then((response) => {
                console.log(response)
            })
            .catch((error => 
                console.log(error)
            ))
        }
    }
}
</script>

<style>

</style>