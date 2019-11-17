import Vue from 'vue'
import Vuex from 'vuex'
import cuttingZonesService from '@/services/cuttingZonesService'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    cuttingZones: []
  },
  
  actions: {
    async getZones ({ commit }) {
      const zones = await cuttingZonesService.fetchZones()
      commit('setZones', zones)
    }
  },
  
  mutations: {
    setZones (state, zones) {
      state.cuttingZones = [ zones ]
    }
  }
})