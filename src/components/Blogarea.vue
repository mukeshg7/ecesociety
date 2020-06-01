<template> 
    <section class="latest_blog_area p_120">
        	<div class="container">
        		<div class="main_title">
        			<h2><strong>Latest Posts From Blog</strong></h2>
        			<p>There is a moment in the life of any aspiring astronomer that it is time to buy that first telescope. It’s exciting to think about setting up your own viewing station.</p>
        		</div>
        		<div class="row latest_blog_inner">
					
						<div class="col-lg-3 col-md-6" v-for="article in articles" :key="article.id">
							<div class="l_blog_item">
								<img class="img-fluid" src="@/assets/l-blog-1.jpg" alt="">
								<a class="date1" href="#">25 October, 2018  |  By {{ article.author }}</a>
								<a href="single-blog.html"><h4>{{ article.title }}</h4></a>
								<p>Computers have become ubiquitous in almost every facet of our lives. At work, desk jockeys spend hours in front of their desktops, while delivery</p>
							</div>
						</div>
					
        			
        		</div>
        	</div>
        </section>
</template>

<script>
export default {
	data() {
		return {
			articles: [],
		}
	},
	methods: {

	},
	created(){
		this.$http.get('https://jsonplaceholder.typicode.com/posts')
		.then(response => {
				var len = response.data.length;
				this.articles = response.data.slice(len-4, len);
				this.articles.reverse();
				console.log(this.articles);
            })
        .catch(error => {
            console.log(error)
			})
	}
}
</script>

<style scoped>
.latest_blog_area{
    margin-bottom: 60px;
}
.main_title{
    text-align: center;
    margin-top: 30px ;
    margin-bottom: 20px;
}
.main_title h2{
    font-size: 50px;
}
.main_title p{
    padding-bottom: 50px;
}
.latest_blog_area{
	padding: 20px 20px 20px 20px;
}
.latest_blog_inner{
	margin-bottom: -30px;
}
.l_blog_item{
	margin-bottom: 30px;
}	
.date1{
	font-size: 13px;
	font-family: "Ariel";
	font-weight: normal;
	color: gray;
	margin-top: 20px;
	display: block;
	margin-bottom: 15px;
}
h4{
	font-size: 20px;
	line-height: 24px;
	color: #737373;
	border-bottom: 1px solid #eeeeee;
	padding-bottom: 20px;
	margin-bottom: 20px;
    font-weight: bold;
	transition: all 300ms linear;
}
l_blog_item p{
	margin-bottom: 0px;
}
h4:hover{
    color:black;
}
</style>