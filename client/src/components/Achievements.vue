<template>
    <div class="container">
        <h1><strong>Student Achievements</strong></h1>

        <div v-for="item in items" :key="item.year">
            <h2><strong>Batch of {{item.year}}</strong></h2>
            <div class="row justify-content-around">

                    <div v-for="guy in item.people" :key="guy.name" class="col-md-6 xxx">
                        <div class="card">
                            <div class="row">
                                <div class="col-lg-5 yyy">
                                    <img src="@/assets/0.jpg" alt="">
                                </div>
                                <div class="col-lg-7">
                                    <p>
                                        {{guy.message}}
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
                    { year:2020, people: [
                        {name: 'aaa', message: 'Congaratulations to Mr.ongaratulations to Mr.ongaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                    ] },
                    { year:2021, people: [
                        {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                    ] },
                    { year:2022, people: [
                        {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                {name: 'aaa', message: 'Congaratulations to Mr. aaa for securing a rank of aaa in the aaaaa.'},
                    ] },
                ],
        }
    },
    methods: {
        getData: function() {
            this.$http
                .get('http://localhost:8000/achievements')
                .then(response => {
                    this.items = response.data;
                })
                .catch(err => console.log(err));
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
.xxx{
}

.card img, cardText{
    padding: 10px 10px 10px 8px;
}
.col-lg-5, {
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