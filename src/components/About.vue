<template>
<div>
<div class="cont" align="center">
    
    <div id="main" class="row">
        <div class="col-8">
        <div id="about">
            <h1>About</h1>
            <p>lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
                tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
                fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
                sunt in culpa qui officia deserunt mollit anim id est laborum.
                Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque 
                laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi 
                architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas 
                sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione 
                voluptatem sequi nesciunt.</p>
        </div>
    </div>
    <div class="col-4">
        <div id="notice">
            <h1>Notice Board</h1>
            <div id="content">
               <li v-for="item in items" :key="item.message">
                   <div class="inbox">
                        <div class="row">
                            <div class="date col-"><p>{{ item.day }}</p><p>{{ item.month }}</p></div> 
                            <div class="col-sm">{{ item.message }}</div>
                        </div>
                   </div>
               </li>
            </div>
        </div>
    </div>
    </div>
    </div>
    <hr>
</div>
</template>

<script>
export default {
    data(){
        return{
            items:[
                    {  
                        message: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.",
                        day: "01",
                        month: "MAY"
                    },
                    {
                        message: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.",
                        day: "18",
                        month: "APR"
                    },
                    {
                        message: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.",
                        day: "11",
                        month: "APR"
                    },
                    {
                        message: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.",
                        day: "03",
                        month: "APR"
                    },
                    {
                        message: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.",
                        day: "17",
                        month: "MAR"
                    },
                ]
        }
    }
}
</script>

<style>
.cont{
    margin-bottom: 150px;
}

li{
    text-align: left;
    list-style: none;
}
#about h1{
    text-align: center;
    padding-top: 5px;
    padding-bottom: 20px;
}
#notice h1{
    text-align: center;
    padding-top: 5px;
    padding-bottom: 20px;
}
#content{
    border: 2px solid gray;
    border-radius: 10px;
    padding: 2px 2px;
    background-color: #333333;
}
.col-sm{
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
    font-size: 20px;
}
.col-8{
    
}
.col-4{
  
}
#main{
    margin: 30px auto 20px;
}
.cont{
    background-color: white;
    max-width: 90%;
   padding-left: 10%;
   height: 500px;
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