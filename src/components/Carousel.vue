<template>
<div>
    <div class="container">
        <div id="myCarousel" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
                <li data-target="#myCarousel" data-slide-to="0" class=""></li>
                <li data-target="#myCarousel" data-slide-to="1" class=""></li>
            </ol>
            <li data-target="#myCarousel" data-slide-to="2" class="active"></li>
        <div class="carousel-inner">
          <div class="carousel-item">
            <img class="first-slide" src="@/assets/0.jpg" alt="First slide" style=" height:100%; width:100%;">
            <div class="container">
              <div class="carousel-caption text-left">
                <h1>Example headline.</h1>
                <p>Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.</p>
                </div>
            </div>
          </div>
          <div class="carousel-item">
            <img class="second-slide" src="@/assets/holi.jpg" alt="Second slide" style=" height:100%; width:100%;">
            <div class="container">
              <div class="carousel-caption">
                <h1>Another example headline.</h1>
                <p>Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.</p>
                </div>
            </div>
          </div>
          <div class="carousel-item active">
            <img class="third-slide" src="@/assets/hall 1.jpg" alt="Third slide" style=" height:100%; width:100%;">
            <div class="container">
              <div class="carousel-caption text-right">
                <h1>One more for good measure.</h1>
                <p>Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.</p>
                </div>
            </div>
          </div>
        </div>
        <a class="carousel-control-prev" href="#myCarousel" role="button" data-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#myCarousel" role="button" data-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
      <br>
      <br>
      <br>
    </div>
    <hr>
</div>
</template>

<style>
hr {
  border: none;
  border-top: 2px solid rgba(255,255,255,.3);
  border-bottom: 2px solid rgba(0,0,0,.08);
  margin: 2.5em 0;
  position: relative;
  margin: auto;
  width: 90%;
}
hr:before,hr:after {
  content: '';
  position: absolute;
  bottom:0px;
  height: 5em;
  width: 100%;
  background: radial-gradient(ellipse at bottom, rgba(255,255,255,0.35) 0%,rgba(255,255,255,0) 70%);
  z-index:0;
}
hr:after {
  top:0px;
  bottom:auto;
  height: 1.5em;
  background: radial-gradient(ellipse at top, rgba(0,0,0,0.06) 0%,rgba(0,0,0,0) 70%);
}
</style>