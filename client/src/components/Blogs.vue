<template>
    <div class="body">
        <h1><strong>Blogs</strong></h1>
        <div class="container">

            <div v-if="articles.length === 0" align="center">
                <p>Blogs will be uploaded soon :)</p>
            </div>


            <div v-else>
                <div class="row">
                    <div v-for="article in articles" :key="article.id" class="vol-md-3">
                        <div class="each">
                            <div class="card">
                            <img class="card-img-top" src="@/assets/l-blog-1.jpg" alt="Card image cap">
                                <div class="card-body">
                                    <h5 class="card-title">Date  |  {{ articles.length }}</h5>
                                    <p class="card-text">{{ article.title }}</p>
                                    <p>Brief</p>
                                    <a href="#" class="btn btn-primary">Read</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>


        </div>
    </div>
    <!--Reference-->
    <!--https://travishorn.com/creating-a-photo-gallery-with-vue-css-grid-3e0a3dd25285-->
</template>

<script>
export default {
    name: 'Blogs',
    data() {
        return {
            articles: [],
        }
    },
    methods: {

    },
    created() {
        this.$http.get('http://rounak1812.pythonanywhere.com/blogs')
        .then(response => {
            this.articles = response.data;
        })
        .catch(error => {
            console.log(error)
        })
    }
}
</script>

<style scoped>

h1{
    font-size: 50px;
    text-align: center;
    padding-top: 20px;
    padding-bottom: 20px;
    color:black;
}
p {
    font-size: 1cm;
}
.body {
    align-content: center;
}
.each {
    padding: 20px;
}

</style>