<template>
  <div class="getting-started">
    <div>Getting Started. Welcome !!</div>
    <router-link :to="{ name: 'questionsPage', query: {page: 1} }">Start</router-link>
  </div>
</template>

<script>
export default {
  data () {
    return {}
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
