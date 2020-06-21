<template>
    <div id="team">
        <h1>Meet the Team</h1>

        <div class="body">

            <div v-for="num in nums" :key="num">
                <div class="grid-item" v-for="member in team[num].members" :key="member">

                    <div class="card">
                        <img class="card-img-top" src="@/assets/familyguy.png" alt="Card image cap">
                        <div class="card-body">
                          <h5 class="card-title">{{ member.first_name }} {{ member.second_name }}</h5>
                          <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                        </div>
                    </div>

                </div>
            </div>

        </div>
        

    </div>    
</template>

<script>
export default {
    name: 'Login',
    data(){
        return{
          nums: [0,1,2,3],
          team: [
            { year: "Final",  members: [1] },
            { year: "Third",  members: [2] },
            { year: "Second", members: [3] },
            { year: "First",  members: [4] },
          ],
        }
    },

    methods: {
        getMember: function() {console.log("b");
          this.$http
          .get('api/members')
          .then(response => {
            const members = response.data;
            members.forEach(member => {
                segregate(member);
            });
          })
          .catch(e => console.log(e))
        },

        segregate: function(member) {
          if(member.year == 4) this.team[0].members.push(member);
          else if(member.year == 3) this.team[1].members.push(member);
          else if(member.year == 2) this.team[2].members.push(member);
          else if(member.year == 1) this.team[3].members.push(member);
        },
     },

    created() {
      console.log("a");
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
.body {
  display: grid;
  grid-template-columns: repeat(4, auto);
  padding: 10px;
}

.grid-item {
  padding: 20px;
  font-size: 30px;
  max-width: 22rem;
  text-align: center;
}

</style>