<template>
  <div class="questions-page">
    <div v-for="(question,i) in questionsConfigs['questions']" :key="i" class="questions-box">
      <div class="questions-question">{{ i+1 }}. {{ question[`question`] }}</div>
      <div class="questions-answer">
        <input v-if="question['answerType'] === 'string'" type="text"
               v-model="question['answer']"/>

        <input v-else-if="question['answerType'] === 'integer'" type="number"
               v-model="question['answer']"/>

        <input v-else-if="question['answerType'] === 'float'" type="number"
               v-model="question['answer']"/>

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

    <router-link :to="{ name: pageName.questionsPage, params: {page: nextPage} }" v-if="!isLastPage" @click.native="submit">Next</router-link>
    <router-link :to="{ name: pageName.recommendPage }" v-else @click.native="submit">Submit</router-link>
  </div>
</template>

<script>
import {pageName} from '../../commons/constants/constants'
import questionares from '../../fixtures/questionares'

export default {
  data () {
    return {
      pageName: pageName,
      pageNumber: 0,
      nextPage: 0,
      isLastPage: false,
      questionsConfigs: {}
    }
  },
  methods: {
    submit () {
      this.$store.commit('setData', { questionareData: this.questionsConfigs, page: this.pageNumber })
      console.log('Submit on page : ' + this.pageNumber)
      console.log(this.$store.getters.getData)
    }
  },
  mounted () {
    this.pageNumber = parseInt(this.$route.params['page'])
    this.nextPage = this.pageNumber + 1
    this.questionsConfigs = questionares['questions']['page_' + this.pageNumber]
    if (questionares['questions']['page_' + this.nextPage] === undefined) {
      this.isLastPage = true
    }
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
