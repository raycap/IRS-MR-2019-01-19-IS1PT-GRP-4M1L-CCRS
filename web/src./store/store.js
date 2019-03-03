import Vuex from 'vuex'
import Vue from 'vue'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    questionareData: {}
  },
  getters: {
    getData (state) {
      return state.questionareData
    }
  },
  mutations: {
    setData (state, payload) {
      // payload: { questionareData : JSON, page: integer }
      state.questionareData[payload.page] = payload.questionareData
    }
  },
  actions: {
  }})
