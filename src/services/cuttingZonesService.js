import api from '@/services/api'

export default {
  fetchZones() {
    // console.log(api.defaults)
    return api.get(`/polygons`)
              .then(response => response.data.polygons)
  },
}
