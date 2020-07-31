<template>
    <div id="team">
        <h1><strong>Meet the Team</strong></h1>

        <div class="container">
            <div v-for="num in nums" :key="num">
              <h2></h2>
                <div class="row">
                <div class="col-lg-4" v-for="member in team[num].members" :key="member.designation">
                  
                    <div class="card">
                        <img class="card-img-top" :src="member.image" alt="Card image cap">
                        <div class="card-body">
                          <h3 class="card-title"><strong>{{ member.name }}</strong></h3>
                          <h4 class="card-text">{{ team[num].designation }}</h4>
                          <a v-bind:href="member.fb"><i class="fab fa-facebook"></i></a>
                          <a v-bind:href="`mailto:${member.email}`"><i class="fas fa-envelope"></i></a>
                          <a v-bind:href="member.ln"><i class="fab fa-linkedin"></i></a>
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
    name: 'Team',
    data(){
        return{
          nums: [0,1,2,3],
          team: [
            { designation: "Chair",  members: [] },
            { designation: "Secretary",  members: [] },
            { designation: "Web Designer", members: [] },
            { designation: "Graphic Designer",  members: [] },
            { designation: "Executive member", members: []}
          ],
        }
    },

    methods: {
        getMember: function() {
          this.$http
          .get('http://rounak1812.pythonanywhere.com/member/')
          .then(response => {console.log(this.team);
            var members = response.data;
             members.forEach(member => {
                this.segregate(member, this.team);
             })
             console.log(this.team);
            })
          .catch(e => {
            console.log(e);
          })
        },

        segregate: (member, team) => {
          if(member.yr === null) console.log("null");
          else if(member.yr === 4) team[0].members.push(member);
          else if(member.yr === 3) team[1].members.push(member);
          else if(member.yr === 2) team[2].members.push(member);
          else if(member.yr === 1) team[3].members.push(member);
          else if(member.yr === 1) team[4].members.push(member);
        },
     },

    created() {
      this.getMember();
    }
}
</script>

<style scoped>

#team h1{
    text-align: center;
    padding-top: 20px;
    padding-bottom: 20px;
    color:black;
}

h1{
  font-size: 50px;
}
h2 {
  padding: 40px;
}
i {
  font-size: 30px;
  padding: 5px;
  color:rgb(94, 93, 93)
}
.card{
  width: 85%;
}
img {
  width: 100%;
  height: 100%;
}
.fa-linkedin:hover {
  color:rgba(0, 87, 250, 0.884)
}
.fa-facebook:hover {
  color: rgba(0, 89, 255, 0.678);
}
.fa-envelope:hover {
  color: rgb(0, 0, 0)
}
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1), 0 6px 20px 0 rgba(0, 0, 0, 0.8);
  text-align: center;
}
</style>