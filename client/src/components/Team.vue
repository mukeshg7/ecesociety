<template>
    <div id="team">
        <h1><strong>Meet the Team</strong></h1>

        <div class="container">
            <div v-for="num in nums" :key="num">
              <h2>{{ team[num].year }} years</h2>
                <div class="row">
                <div class="col-md-4" v-for="member in team[num].members" :key="member.year">
                  
                    <div class="card">
                        <img class="card-img-top" :src="member.image" alt="Card image cap">
                        <div class="card-body">
                          <h5 class="card-title">{{ member.name }}</h5>
                          <p class="card-text">{{ member.designation }}</p>
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
            { year: "Final",  members: [] },
            { year: "Third",  members: [] },
            { year: "Second", members: [] },
            { year: "First",  members: [] },
          ],
        }
    },

    methods: {
        getMember: function() {
          this.$http
          .get('http://localhost:8000/member/')
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