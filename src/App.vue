<template>
  <div id="app">
    <cutting-map />
  </div>
</template>

<script>
import CuttingMap from '@/components/CuttingMap.vue'

export default {
  components: {
    CuttingMap
  }
}
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
