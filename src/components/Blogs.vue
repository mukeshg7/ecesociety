<template>
    <div class="body">
        <h1>Blogs</h1>
        <div class="gallery">
            <div class="gallery-panel" v-for="article in articles" :key="article.id">
                <div class="card" style="width: 18rem;">
                    <img class="card-img-top" src="@/assets/l-blog-1.jpg" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title">Date  |  {{ article.author }}</h5>
                        <p class="card-text">{{ article.title }}</p>
                        <p>Brief</p>
                        <a href="#" class="btn btn-primary">Read</a>
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
        this.$http.get('https://jsonplaceholder.typicode.com/posts')
        .then(response => {
            this.articles = response.data;
            this.articles.reverse();
            console.log(this.article)
        })
        .catch(error => {
            console.log(error)
        })
    }
}
</script>

<style scoped>

h1{
    text-align: center;
    padding-top: 20px;
    padding-bottom: 20px;
    color:black;
}
.body {
    align-content: center;
}
.gallery {
    display: grid;
    grid-template-columns: repeat(4, auto);
    grid-gap: 50px;
    max-width: 80%;
    right: 0px;
    left: 0px;
}
.gallery-panel img {
    width: 100%;
    height: 15vw;
    object-fit: cover;
}

</style>