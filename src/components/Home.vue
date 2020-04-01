<template>
  <div class="hello">
    <Carousel/>
    <About/>
    <Achieve/>
    <Blogarea/>
  </div>
</template>

<script>
import Carousel from '@/components/Carousel';
import Achieve from '@/components/Achieve';
import Blogarea from '@/components/Blogarea';
import About from '@/components/About';

export default {
  name: 'Home',
  data () {
    return {

    }
  },
  components: {
    Carousel, Achieve, Blogarea, About,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
