<template>
    <div class="container">
        <h1><strong>Student Achievements</strong></h1>

        <div v-for="item in items" :key="item.year">
            <h2><strong>Batch of {{item.year}}</strong></h2>
            <div class="row justify-content-around">

                    <div v-for="guy in item.people" :key="guy.id" class="col-md-6 xxx">
                        <div class="card">
                            <div class="row">
                                <div class="col-lg-5 yyy">
                                    <img src="@/assets/0.jpg" alt="">
                                </div>
                                <div class="col-lg-7">
                                    <p>
                                        {{guy.achievement}}
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>

            </div>

        </div>

        

    </div>
</template>

<script>
export default {
    name: 'Achievements',
    data(){
        return {
            items: [
                    { year: 2020, people: [] },
                    { year: 2021, people: [] },
                    { year: 2022, people: [] },
                ],
        }
    },
    methods: {
        getData: function() {
            this.$http
                .get('http://rounak1812.pythonanywhere.com/achievement/')
                .then(response => {
                    var users = response.data;
                    users.forEach(user => {
                        if(user.yr > 2019) {
                            this.segregate(user, this.items);
                        }
                    })
                    this.items.reverse();
                    console.log('a', this.items);
                })
                .catch(err => console.log(err));
        },
        segregate: (user, items) => {
            let index = user.yr - 2020;
            items[index].people.push(user);
        }
    },
    created() {
        this.getData();
    }
}
</script>

<style scoped>
.container{
    max-width: 80%;
    
}
h1{
    text-align: center;
    padding-top: 20px;
    padding-bottom: 20px;
    color:black;
}
img{
    width: 100%;
    height: 100%;
    object-fit:contain;
}

.card img, cardText{
    padding: 10px 10px 10px 30px;
}
.col-lg-5 {
    padding: 0px;
}
.col-lg-7 p {
    padding: 10px 10px 10px 10px;
    font-size: 20px;
    font-weight: 500;
}
 .card {
    margin: 50px auto;
    text-align: center;
    box-shadow: 0px 6px 5px 0px rgba(176,164,176,1);
}

</style>