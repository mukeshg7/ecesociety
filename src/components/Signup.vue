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
                                <label for="reg_num">Registration No.: </label>
                                <input type="text" name="reg_num" v-model="reg_num" 
                                id="reg_num" placeholder="xxUxxxx"/>
                            </div>
                            <div class="form-group">
                                <label for="roll_num">Roll No.: </label>
                                <input type="text" name="roll_num" v-model="roll_num" 
                                id="roll_num" placeholder="xxECxxxx"/>
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
                                id="re_password" placeholder="Confirm password"/>
                            </div>
                            <div class="form-group form-button">
                                <button @click="validate">Validate</button>
                                <input type="submit" name="signup" disabled="ok" id="signup" class="form-submit" value="Register"/>
                            </div>
            </form>
    </div>
</template>

<script>
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
    is_right: true,
    ok: false,

    methods: {
        validate(){
            if(this.password != this.re_password){
                this.is_right = false
            }

            if(reg_num.length != 8 || roll_num.length != 8 || roll_num[2] != 'E' || roll_num[3] != 'C') this.is_right = false;

            this.$http.get('url/users')
            .then(response => {
                var data = response.data;
                if(data.reg_num.includes(this.reg_num)) this.is_right = false;
                if(data.roll_num.includes(this.roll_num)) this.is_right = false;
            })
            .catch(error => console.log(error));

            if(!this.is_right) alert("Invalid Credentials");
            else {
                alert("Valid Credentials");
                this.ok = true;
            }
        },
        
        onSignup(){
            console.log({email: this.email, password: this.password, confirm_password: this.re_password})
            this.$http
            .post('url', {
                name: this.name,
                reg_num: this.reg_num,
                roll_num: this.roll_num,
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