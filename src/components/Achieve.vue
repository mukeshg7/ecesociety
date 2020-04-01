<!--<template>
    <div>
        <h1>Achievements</h1> 
        <div class="container">
            <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <div class="row">
                            <div class="col-md-3">
                                <div class="card">
                                    <img class="card-img-top" src="@/assets/familyguy.png" alt="Card image cap">
                                    <div class="card-body">
                                        <h5 class="card-title">Name Name Name</h5>
                                        <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                                        <i class="fab fa-facebook-f"></i>
                                        <a href="#" class="btn btn-primary">Go somewhere</a>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="card">
                                    <img class="card-img-top" src="@/assets/familyguy.png" alt="Card image cap">
                                    <div class="card-body">
                                    <h5 class="card-title">Name Name Name</h5>
                                    <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                                    <a href="#" class="btn btn-primary">Go somewhere</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img class="d-block w-100" src="@/assets/sasuke (1).jpg" alt="Second slide">
                    </div>
                    <div class="carousel-item">
                        <img class="d-block w-100" src="@/assets/holi.jpg" alt="Third slide">
                    </div>
                </div>
                <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </a>
                <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </a>
            </div>    
        </div>  
    </div>
</template>-->
<template>
<div class="achie">
    <h1><strong>Achievement</strong></h1>
<div id="carouselExampleIndicators" class="carousel slide testimonials_area container" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
  </ol>
<div class="testi_slider">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <div class="item">
                        <div class="testi_item">
                            <img src="img/testimonials/testi-3.png" alt="">
                            <h4>Fannie Rowe</h4>
                            <p>Accessories Here you can find the best computer accessory for your laptop, monitor, printer, scanner, speaker. Here you can find the best computer accessory for your laptop, monitor, printer, scanner, speaker.</p>
                        </div>
                    </div>
    </div>
    <div class="carousel-item">
     <div class="item">
                        <div class="testi_item">
                            <img src="img/testimonials/testi-3.png" alt="">
                            <h4>Fannie Rowe</h4>
                            <p>Accessories Here you can find the best computer accessory for your laptop, monitor, printer, scanner, speaker. Here you can find the best computer accessory for your laptop, monitor, printer, scanner, speaker.</p>
                        </div>
                    </div>
    </div>
    <div class="carousel-item">
      <div class="item">
                        <div class="testi_item">
                            <img src="img/testimonials/testi-3.png" alt="">
                            <h4>Fannie Rowe</h4>
                            <p>Accessories Here you can find the best computer accessory for your laptop, monitor, printer, scanner, speaker. Here you can find the best computer accessory for your laptop, monitor, printer, scanner, speaker.</p>
                        </div>
                    </div>
    </div>
  </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</div>
</template>

<style>
.achie{
    padding-top: 30px;
    padding-bottom: 30px;
}
.achie h1{
    text-align: center;
    font-size: 50px;
}
.testimonials_area{
	position: relative;	
}
.testi_slider{
	max-width: 945px;
	margin: auto;
}
.testi_slider .item{
	padding-top: 50px;
}
.testi_slider .testi_item{
	text-align: center;
	border: 1px solid #eeeeee;
}
.testi_item img{
	width: auto;
	margin: auto;
	margin-top: -50px;
}
.owl-dots{
		text-align: center;
		margin-top: 50px;
}
.owl-dot{
	height: 14px;
	width: 14px;
	border-radius: 50%;
	background: #eeeeee;
	display: inline-block;
	margin-right: 10px;
    @include transition;
}

.owl-dot:last-child{
	margin-right: 0px;
}
.owl-dot:hover.active{
	background: white;
}

.testi_item h4{
	color: black;
	font-size: 18px;
	margin-top: 20px;
	margin-bottom: 15px;
}
.testi_item .list{
	margin-bottom: 20px;
	
}
.testi_item li{
	display: inline-block;
}
.testi_item a{
	color: #ffc000;
	font-size: 14px;
}
.testi_item p{
	max-width: 760px;
	margin: auto;
	margin-bottom: 60px;
}

</style>