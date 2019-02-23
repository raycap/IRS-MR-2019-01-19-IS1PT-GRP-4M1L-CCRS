<template>
  <div class="question">
    <div v-for="(question,i) in questionsConfigs['questions']" :key="i">
      {{ question[`question`] }}
      <input v-if="question['answerType'] === 'string'" type="text"
             v-model="question['answer']" @keyup.enter="submit"/>

      <input v-else-if="question['answerType'] === 'integer'" type="number"
             v-model="question['answer']" @keyup.enter="submit"/>

      <input v-else-if="question['answerType'] === 'float'" type="number"
             v-model="question['answer']" @keyup.enter="submit"/>

      <input v-else-if="question['answerType'] === 'float'" type="number"
             v-model="question['answer']" @keyup.enter="submit"/>

      <div v-else-if="question['answerType'] === 'checkbox'">
        <div v-for="(choice,j) in question['choices']" :key="j">
          <input type="checkbox" :id="choice['id']" :value="choice['value']" v-model="question['answer']"/>
          <label :for="choice['id']"> {{ choice['label'] }} </label>
        </div>
      </div>

      <div v-else-if="question['answerType'] === 'radio'">
        <div v-for="(choice,k) in question['choices']" :key="k">
          <input type="radio" :id="choice['id']" :value="choice['value']" v-model="question['answer']"/>
          <label :for="choice['id']"> {{ choice['label'] }} </label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import questionares from '../fixtures/questionares'

export default {
  data () {
    return {
      pageNumber: 0,
      questionsConfigs: {}
    }
  },
  methods: {
    submit () {
      this.$store.commit('setData', { questionareData: this.questionsConfigs })
      console.log('the configs now : ')
      console.log(this.$store.getters.getData)
    }
  },
  mounted () {
    this.pageNumber = this.$route.query['page']
    this.questionsConfigs = questionares['questions']['page_' + this.pageNumber]
    console.log(this.pageNumber)
    console.log(this.questionsConfigs)
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
