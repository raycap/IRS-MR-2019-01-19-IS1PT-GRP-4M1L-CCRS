<template>
  <div class="getting-started-page">
    <div>Getting Started. Welcome !!</div>
    <router-link class="btn btn-secondary btn-lg active btn-change-page" :to="{ name: pageName.questionsPage, params: {page: 1} }">
        Start
    </router-link>
  </div>
</template>

<script>
import {pageName} from '../../commons/constants/constants'

export default {
  data () {
    return {
      pageName: pageName
    }
  },
  methods: {},
  mounted () {}
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
