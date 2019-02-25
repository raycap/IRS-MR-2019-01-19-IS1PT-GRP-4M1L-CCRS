<template>
  <div class="recommend-page">
    <div>You're result is:</div>
    <div>{{ questionareData['2'] }}</div>
    <router-link :to="{ name: pageName.getStarted }">Go back to Homepage</router-link>
  </div>
</template>

<script>
import {pageName} from '../../commons/constants/constants'

export default {
  data () {
    return {
      pageName: pageName,
      questionareData: {}
    }
  },
  methods: {},
  mounted () {
    this.questionareData = this.$store.getters.getData
    console.log(this.questionareData)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
