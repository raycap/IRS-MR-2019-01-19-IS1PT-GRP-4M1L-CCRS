<template>
  <div class="recommend-page">
    <!--<div>You're result is:</div>-->
    <!--<div>{{ questionareData }}</div>-->

    <!--<hr/>-->
    <div class="recommend-page-title">Based on your answers, we recommend you:</div>
    <div class="recommend-table-wrapper" v-for="(item,i) in resultList" :key="i">
      <div class="recommend-result-item">
        <a class="recommend-result-item-img" target="_blank" :href="item['url']">
          <img :src="item['image']"/>
        </a>
        <div class="recommend-result-item-desc">
          <a class="recommend-result-item-name" target="_blank" :href="item['url']">{{ item['name'] }}</a>
          <ul id="ul-item">
            <li v-for="(it,j) in item['details']" :key="j">{{ it }}</li>
          </ul>
        </div>
      </div>
    </div>
    <router-link class="btn btn-secondary btn-lg active btn-change-page" :to="{ name: pageName.getStarted }">
        Go back to Homepage
    </router-link>
  </div>
</template>

<script>
import {pageName} from '../../commons/constants/constants'
import axios from 'axios'
import creditCardsInfo from '../../fixtures/creditCards'

export default {
  data () {
    return {
      pageName: pageName,
      questionareData: {},
      resultList: []
    }
  },
  methods: {},
  mounted () {
    this.questionareData = this.$store.getters.getData
    axios.post('localhost:5000', {body: this.questionareData}).then(
      response => {
        console.log('got response : ')
        console.log(response)
      }
    ).catch(e => {
      console.log('got err : ')
      console.log(e)
    }
    )
    // TODO: fix this
    this.resultList.push(creditCardsInfo['1'])
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.recommend-page {
  display: flex;
  flex-direction: column;
  width: 65%;
  margin: auto;
}
.recommend-page-title{
  font-weight: bold;
  margin-bottom: 24px;
  font-size: x-large;
}
.recommend-table-wrapper{
  background: white;
  margin-bottom: 8px;
  margin-top: 8px;
}
.recommend-result-item{
  display: flex;
  flex-direction: row;
  margin: 16px 24px;
}
.recommend-result-item-desc{
  padding-left: 24px;
  text-align: left;
}
.recommend-result-item-name{
  font-weight: bold;
  color: #2c3e50;
}
.recommend-result-item-details{
}
.btn-change-page{
  max-width: 300px;
  margin: 16px auto;
}
h1, h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}
</style>
