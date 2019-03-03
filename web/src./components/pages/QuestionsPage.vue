<template>
  <div class="questions-page">
    <div class="questions-page-title">{{ questionsConfigs['pageTitle'] }}</div>
    <div v-for="(question,i) in questionsConfigs['questions']" :key="i" class="questions-box">
      <div class="questions-question">{{ i+1 }}. {{ question[`question`] }}</div>
      <div class="questions-answer form-group">
        <input v-if="question['answerType'] === 'string'" type="text" class="form-control"
               v-model="question['answer']" :placeholder="question['placeholder']"/>

        <input v-else-if="question['answerType'] === 'integer'" type="number" class="form-control"
               v-model="question['answer']" :placeholder="question['placeholder']"/>

        <input v-else-if="question['answerType'] === 'float'" type="number" class="form-control"
               v-model="question['answer']" :placeholder="question['placeholder']"/>

        <div v-else-if="question['answerType'] === 'checkbox'" class="form-check">
          <div v-for="(choice,j) in question['choices']" :key="j">
            <input type="checkbox" :id="choice['id']" :value="choice['value']"
                   v-model="question['answer']"/>
            <label :for="choice['id']" class="form-check-label"> {{ choice['label'] }} </label>
          </div>
        </div>

        <div v-else-if="question['answerType'] === 'radio'" class="form-check">
          <div v-for="(choice,k) in question['choices']" :key="k">
            <input type="radio" :id="choice['id']" :value="choice['value']" v-model="question['answer']"/>
            <label :for="choice['id']"> {{ choice['label'] }} </label>
          </div>
        </div>
      </div>
    </div>

    <button class="btn btn-secondary btn-lg active btn-submit" v-if="!isLastPage" @click="toNextPage">Next</button>
    <button class="btn btn-primary btn-lg active btn-submit" v-else @click="submit">Submit</button>
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
    toNextPage () {
      this.$store.commit('setData', { questionareData: this.questionsConfigs, page: this.pageNumber })
      this.$router.push({ name: this.pageName.questionsPage, params: { page: this.nextPage } })
    },
    submit () {
      this.$store.commit('setData', { questionareData: this.questionsConfigs, page: this.pageNumber })
      this.$router.push({ name: this.pageName.recommendPage })
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
.questions-page {
  display: flex;
  flex-direction: column;
}
.questions-page-title{
  font-weight: bold;
  margin-bottom: 24px;
  font-size: x-large;
}
.questions-box {
  display: flex;
  flex-direction: column;
  width: 50%;
  margin: auto;
  text-align: left;
  margin-bottom: 32px;
  border: solid 1px darkgrey;
  padding: 16px 24px;
  box-shadow: 4px 4px 18px #88889B;
  background-color: white;
}
.questions-question{
  margin-bottom: 8px;
}
.questions-page .btn-submit {
  max-width: 120px;
  margin-left: 25%;
}
.bmd-group-form{
  padding-top: 8px;
}
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
