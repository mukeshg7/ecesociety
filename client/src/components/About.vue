<template>
<div>
    <div class="container" align="center">
        
        <div id="main" class="row">

            <div class="col-lg-8">
                <div id="about">
                    <h1><strong>About</strong></h1>
                    <p>The embryonic formation of the Department of Electronics and Communication 
                        Engineering was in the year 1983 with the introduction of an undergraduate course. 
                        Situated amidst lush green campus with teak plantations, the Department, over the time,
                        has grown in several dimensions and provides a magnetic ambience in teaching and learning.
                        The faculties are engaged in research in diverse topics focussing in Telecommunication, 
                        Antenna and Microwave, Microelectronics and VLSI, Signal and Image processing and Computational Systems Biology. 
                        It is well equipped with sophisticated laboratories in the areas of VLSI, Signal Processing, Microwave, Antenna 
                        and Wireless Communication. The Department has been supported by, SMDP for VLSI, DST-FIST for Wireless 
                        Communications and NPMASS for MEMS Research. Sponsored research from research initiation grant as well as DST 
                        and SERB have been initiated over the years.The Department is committed to impart quality education at undergraduate 
                        as well as postgraduate level and promulgate quality research in diverse fields of application of electronics engineering.</p>
                </div>
            </div>


            <div class="col-lg-4">
                <div id="notice">
                    <h1><strong>Notice</strong></h1>

                    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                        <ol class="carousel-indicators">
                            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                        </ol>
                        
                        <div class="carousel-inner">
                            <div class="page carousel-item active">
                                <li v-for="item in items[0].notice" :key="item.messgae">
                                    <div class="inbox">
                                            <div class="row">
                                                <div class="date col-"><p>{{ item.day }}</p><p>{{ item.month }}</p></div> 
                                                <div class="title col"><p>{{ item.message }} iig di  ejfoej eojw we wijfij.iig di  ejfoej eojw we wijfij.iig di  ejfoej eojw we wijfij.</p></div>
                                            </div>
                                    </div>
                                </li>
                            </div>
                            
                                <div class="page page carousel-item">
                                    <li v-for="item in items[1].notice" :key="item.messgae">
                                        <div class="inbox">
                                                <div class="row">
                                                    <div class="date col-"><p>{{ item.day }}</p><p>{{ item.month }}</p></div> 
                                                    <div class="title"><p>{{ item.message }}</p></div>
                                                </div>
                                        </div>
                                    </li>
                                </div>
                            
                                <div class="page page carousel-item">
                                    <li v-for="item in items[2].notice" :key="item.messgae">
                                        <div class="inbox">
                                                <div class="row">
                                                    <div class="date col-"><p>{{ item.day }}</p><p>{{ item.month }}</p></div> 
                                                    <div class="title">{{ item.title }}</div>
                                                </div>
                                        </div>
                                    </li>
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
            </div>

        </div>
    </div>
    <br>
    <br>
    <hr>
</div>
</template>

<script>
export default {
    name: 'About',
    data(){
        return{
            nums: [1,2,3],
            items: [
                { index: 0,  notice: [] },
                { index: 1,  notice: [] },
                { index: 2,  notice: [] },
            ],
            month: [
                "JAN", 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'
            ]
        }
    },

    methods: {
        addData: (data, items, month) => {
            for(let j = 0; j < 3; j++) {
                for(let i = 0; i < 5 && 5*j+i < data.length; i++) {
                    let note = {
                        day: data[5*j+i].date_time.slice(8, 10),
                        month: month[parseInt(data[5*j+i].date_time.slice(6, 7))-1],
                        message: data[5*j+i].title,
                    };
                    items[j].notice.push(note);
                }
            }
        },
        getNotice: function() {
            this.$http
            .get('http://rounak1812.pythonanywhere.com/notice/')
            .then(response => {
                this.addData(response.data, this.items, this.month);
            })
            .catch(e => console.log(e))
        },
    },
    created() {
        this.getNotice();
        
    }
}
</script>

<style>
.cont{
    margin-bottom: 150px;
}

#notice li{
    text-align: left;
    list-style: none;
}

h1{
  font-size: 50px;
}
.carousel-item p {
    overflow:hidden
}
#about h1{
    text-align: center;
    padding-top: 5px;
    padding-bottom: 20px;
}
#about p{
    font-size: 20px;
    font-weight: 500;
    text-align: center;
}
#notice h1{
    text-align: center;
    padding-top: 5px;
    padding-bottom: 20px;
}
.title{
    overflow:hidden;
}
.carousel-indicators {
    height: 10px;
}
.carousel-control-prev {
    display: none;
}
.carousel-control-next {
    display: none;
}
.page{
    height: 480px;
    border: 2px solid gray;
    border-radius: 10px;
    padding: 2px 2px;
    background-color: #333333;
}
.title{
    font-weight:600;
}
.inbox{
    border: 2px solid gray;
    background-color: #fff;
    border-radius: 7px;
    padding: 5px 5px;
    height: 80px;
    margin: 5px 5px;
}
.inbox p{
    height: 78px;
}
.date{
    background-color: #494848;
    border: 2px solid gray;
    border-radius: 5px;
    margin-left: 15px;
    padding: auto 5px;
    height: 66px;
    width: 70px;
}
.date p{
    font-weight: 700;
    color: #fff;
    text-align:center;
    padding: auto auto;
    margin: auto auto;
}
p{
    text-align: left;
    font-size: 100%;
}

#main{
    margin: 30px auto 20px;
}
.cont{
    background-color: white;
    max-width: 90%;
    padding-left: 10%;
    padding-top: 30px;
}
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