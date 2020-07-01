<template>
  <div class="every">
    <footer class="section footer-classic context-dark bg-image" style="background-color:#333333;">
        <div class="container">
            <div class="row row-30" style="color:white;">
                <div class="col-md-4">
                    
                      <h3>Contacts</h3>
                        <dl class="contact-list">
                        <dt>Address:</dt>
                        <dd><i class="fas fa-map-marked-alt"></i>  NIT Durgapur, Durgapur, W.B.</dd>
                        </dl>
                        <dl class="contact-list">
                      <dt>Email:</dt>
                        <dd><i class="fas fa-envelope"></i><a href="mailto:eces.nitdgp@gmail.com">  eces.nitdgp@gmail.com</a></dd>
                        </dl>
                      <dl class="contact-list">
                        <dt>Phones:</dt>
                        <dd><i class="fas fa-phone-square"></i><a href="tel:+919876543210">  XYZ: +919876543210 </a>
                        </dd>
                        </dl>
                         
                    </div>
                    <div class="col-md-4">
                        <h3 class="ml-0">Links</h3>
                        <ul class="nav-list ml-1" style="list-style-type:none;padding-left: 0;">
                            <li >
                              <router-link :to="{ name: 'Calender'}">Calender</router-link>
                            </li>
                            <li>
                              <router-link :to="{ name: 'Academics'}">Academics</router-link>
                            </li>
                            <li>
                              <a href="https://nitdgp.ac.in/department/EC/people">Faculty</a>
                            </li>
                            <li>
                              <router-link :to="{ name:'Team' }">Team</router-link>
                            </li>
                            <li>
                              <router-link :to="{ name:'WebDTeam' }">WebDTeam</router-link>
                            </li>
                        </ul>
                    </div>
                <div class="col-md-4">
                <h3 class="ml-0">Reach us</h3>
                <div class="mapouter">
                  <div class="gmap_canvas">
                    <iframe width=100% height=100% id="gmap_canvas" src="https://maps.google.com/maps?q=department%20of%20electronics%20nit%20dgp&t=&z=13&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
                    <a href="https://www.embedgooglemap.net/blog/divi-discount-code-elegant-themes-coupon/">divi discount</a>
                    </div>
                    </div>
                </div>
        </div>
    </div>
</footer>
</div>
</template>

<style scoped>
.every {
  margin-top: 40px;
  margin-bottom: 0px;
}
.container {
  bottom: 0px;
}

.contact-list {
  padding-top: 10px;
}
.col-md-4{
  padding-top:30px;
}
.footer-classic li{
  padding: 7px 0px;
	
}
.footer-classic a:last-child{
  margin-bottom: 0px;
}
.footer-classic a:hover{
  color: #fff;
  text-decoration: none;
}
.footer-classic a{
	color:gray;
	font-size:19px;
	font-weight:normal;
	font-family:"Ariel";
	transition:all 300ms linear;
}
.mapouter {
  position:relative;
  text-align:right;
  height:90%;
  width:95%;
}
.gmap_canvas {
  overflow:hidden;
  background:none!important;
  height:90%;
  width:95%;
  }
  
</style>