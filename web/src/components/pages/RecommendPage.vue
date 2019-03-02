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
          <div class="recommend-result-item-name">{{ item['name'] }}</div>
          <div class="recommend-result-item-details">{{ item['details'] }}</div>
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

export default {
  data () {
    return {
      pageName: pageName,
      questionareData: {},
      resultList: [{
        image: 'https://photos.cdn-moneysmart.com/uploads/ms_core/product/image/65/listing_image_amex_krisflyerbrown_cmyk_2x_480.png',
        url: 'https://www.google.com',
        name: 'American Express',
        details: 'benefits 1 \nbenefits 2.'
      },
      {
        image: 'https://photos.cdn-moneysmart.com/uploads/ms_core/product/image/63/listing_credit-cards_874__2x.png',
        url: 'https://www.moneysmart.sg/credit-cards',
        name: 'City Bank',
        details: 'Cashback 5% with min $500 spending\nNothing else'
      }]
    }
  },
  methods: {},
  mounted () {
    this.questionareData = this.$store.getters.getData
    axios.post('https://www.google.com/', {body: this.questionareData}).then(
      response => {
        console.log('got response : ')
        console.log(response)
      }
    ).catch(e => {
      console.log('got err : ')
      console.log(e)
    }
    )
    console.log('recommend page')
    console.log(this.questionareData)
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
}
.recommend-result-item-details{
  white-space: pre;
}
.btn-change-page{
  max-width: 300px;
  margin: 16px auto;
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
