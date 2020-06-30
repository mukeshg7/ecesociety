<template>
  <div class="hello">
    <Carousel/>
    <About/>
    <Cards/>
    <Achieve/>
    <Blogarea/>
  </div>
</template>

<script>
import Carousel from '@/components/Carousel';
import Achieve from '@/components/Achieve';
import Blogarea from '@/components/Blogarea';
import About from '@/components/About';
import Cards from '@/components/Cards';

export default {
  name: 'Home',
  data () {
    return {

    }
  },
  components: {
    Carousel, Achieve, Blogarea, About, Cards
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
