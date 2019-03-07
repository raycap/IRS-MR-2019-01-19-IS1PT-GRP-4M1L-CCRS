<template>
  <div class="recommend-page">
    <div class="recommend-page-title" v-show="eligible === 'N' || eligible === 'n'">
      Looks like you are not eligible for any credit cards. Please try again in the future :)
    </div>
    <div class="recommend-page-title" v-show="eligible === ''">
      Oops something went wrong.<br>
      We cannot reach out to our server :(
    </div>
    <div v-show="eligible === 'Y' || eligible === 'y'">
      <div class="recommend-page-title">Based on your answers, we recommend you:</div>
      <div class="recommend-table-wrapper" v-for="(item,i) in resultList" :key="i">
        <div class="recommend-result-item">
          <a class="recommend-result-item-img" target="_blank" :href="item['url']">
            <img :src="item['image']"/>
          </a>
          <div class="recommend-result-item-desc">
            <a class="recommend-result-item-name" target="_blank" :href="item['url']">{{ item['name'] }}</a>
            <div v-show="cashbackList[i] > 0" class="recommend-result-item-name">You can get cashback up to: S${{ cashbackList[i] }}</div>
            <ul id="ul-item">
              <li v-for="(it,j) in item['details']" :key="j">{{ it }}</li>
            </ul>
          </div>
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
      queryid: 1,
      pageName: pageName,
      questionareData: {},
      resultList: [],
      cashbackList: [],
      eligible: 'y'
    }
  },
  methods: {
    getRawField (rawData, field) {
      for (var key in rawData) {
        for (var i in rawData[key]['questions']) {
          if (rawData[key]['questions'][i]['questionName'] === field) {
            let ans = rawData[key]['questions'][i]['answer']
            if (rawData[key]['questions'][i]['answerType'] === 'integer') {
              if (ans === '') {
                return 0
              } else {
                return parseInt(ans)
              }
            } else {
              return ans
            }
          }
        }
      }
      return ''
    },
    constructRequest (rawData) {
      return {
        name: 'John',
        isSingaporean: this.getRawField(rawData, 'nationality'),
        age: this.getRawField(rawData, 'age'),
        income: this.getRawField(rawData, 'income'),
        spending: this.getRawField(rawData, 'total_spending'),
        expense_bill: this.getRawField(rawData, 'spend_bills'),
        expense_phv: this.getRawField(rawData, 'spend_taxi'),
        expense_petrol: this.getRawField(rawData, 'spend_petrol'),
        expense_pubtrpt: this.getRawField(rawData, 'spend_public_transport'),
        expense_dining: this.getRawField(rawData, 'spend_dining')
      }
    },
    getResult () {
      axios.get('http://localhost:5000/search/' + this.queryid).then(
        response => {
          console.log('search/ got response : ')
          console.log(response)
          this.eligible = response.data['Eligible']
          if (this.eligible === 'Y' || this.eligible === 'y') {
            this.cashbackList.push(parseInt(response.data['CashbackAmount']))
            this.resultList.push(creditCardsInfo[response.data['Cardname']])
          }
        }).catch(e => {
        console.log('search/ got err : ')
        console.log(e)
      })
    }
  },
  mounted () {
    let rawData = this.$store.getters.getData
    console.log(this.constructRequest(rawData))
    axios.post('http://localhost:5000/recommendation', {
      name: 'John',
      isCitizen: this.getRawField(rawData, 'nationality'),
      age: this.getRawField(rawData, 'age'),
      income: this.getRawField(rawData, 'income'),
      spending: this.getRawField(rawData, 'total_spending'),
      expense_bill: this.getRawField(rawData, 'spend_bills'),
      expense_phv: this.getRawField(rawData, 'spend_taxi'),
      expense_petrol: this.getRawField(rawData, 'spend_petrol'),
      expense_pubtrpt: this.getRawField(rawData, 'spend_public_transport'),
      expense_dining: this.getRawField(rawData, 'spend_dining'),
      queryid: this.queryid
    }).then(
      response => {
        console.log('got response : ')
        console.log(response.data)
        setTimeout(() => {
          this.getResult()
        }, 2000)
      }
    ).catch(e => {
      console.log('got err : ')
      console.log(e)
      this.eligible = ''
    })
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
  padding-top: 16px;
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
