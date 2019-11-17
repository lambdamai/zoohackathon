<template>
  <div class="map" ref="map"></div>
</template>

<script>
import Ymaps from 'ymaps'

export default {
  data() {
    return {
      ymaps: null
    }
  },

  async mounted() {
    await this.initYmaps()

    this.initMapEl()
    await this.initMapData()

    this.drawZonesForStage(0)
  },

  methods: {
    async initYmaps() {
      this.ymaps = await Ymaps.load('https://api-maps.yandex.ru/2.1/?lang=ru_RU')
    },

    initMapEl() {
      this.map = new this.ymaps.Map(this.$refs.map, {
        center: [55.855096, 37.577580],
        zoom: 9,
        controls: ['zoomControl'],
      }, {
        searchControlProvider: 'yandex#map',
        suppressMapOpenBlock: true,
        // restrictMapArea: [
        //   [46.23951188728651, 32.332576171872425],
        //   [43.310741618995125, 36.749080078119746],
        // ],
      })
    },

    initMapData() {
      return this.$store.dispatch('getZones')
    },

    drawZonesForStage(stageIdx) {
      this.drawCuttingZones(this.$store.state.cuttingZones[stageIdx])
    },

    drawCuttingZones(zones) {
      const legalZonesCollection = new this.ymaps.GeoObjectCollection(null, { fillColor: '#4caf50', opacity: 0.5 })
      const illegalZonesCollection = new this.ymaps.GeoObjectCollection(null, { fillColor: '#f44336', opacity: 0.5 })

      zones.forEach(zone => {
        const coords = zone.points.map(point => [ point.latitude, point.longitude ])
        if (zone.color == 'green') {
          legalZonesCollection.add(this.createPolygon(coords))
        } else {
          illegalZonesCollection.add(this.createPolygon(coords))
        }
      })

      this.map.geoObjects.add(legalZonesCollection).add(illegalZonesCollection)
    },

    createPolygon(coords) {
      return new this.ymaps.GeoObject({
        geometry: {
          type: "Polygon",
          coordinates: [
            coords
          ],
          fillRule: "nonZero"
        }
      }, {
        // fillColor: '#00FF00',
        strokeColor: '#0000FF',
        // opacity: 0.5,
        strokeWidth: 1
      })
    },
  },
}
</script>

<style scoped>
.map {
  height: 400px;
}
</style>