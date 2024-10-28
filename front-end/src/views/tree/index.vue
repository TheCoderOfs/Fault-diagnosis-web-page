<template>
  <!-- <div>
    <div ref="chartColumn" style="width:100%; height:400px;"></div>
    <button @click="changeOption">点击改变内容</button>
  </div> -->

  <div class="container">
    <div class="item" ref="PtWAWQntHtvI" style="width:900px;height:500px;"></div>
  </div>
</template>

<script>
import echarts from 'echarts'
import 'echarts-gl'
export default {
  data() {
    return {
      chartColumn: null,
      option: {}
    }
  },
  methods: {

    initChart() {
      // this.chartColumn = echarts.init(this.$refs.chartColumn)
      // this.chartColumn.setOption(this.option)

      let goecharts_PtWAWQntHtvI = echarts.init(this.$refs.PtWAWQntHtvI);
      let option_PtWAWQntHtvI = {"color":["#5470c6","#91cc75","#fac858","#ee6666","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"grid3D":{},"legend":{"show":false},"series":[{"name":"scatter3d","type":"scatter3D","waveAnimation":false,"coordinateSystem":"cartesian3D","renderLabelForZeroData":false,"selectedMode":false,"animation":false,"data":[{"value":[2310.738003,-413.6453804,-413.6453804]},{"value":[3551.8411,-634.9234278,-634.9234278]},{"value":[4709.251392,-842.8580857,-842.8580857]},{"value":[7150.631825,-1275.40662,-1275.40662]},{"value":[7889.578078,-1407.728665,-1407.728665]},{"value":[8261.092496,-1474.445733,-1474.445733]},{"value":[8493.799314,-1515.587917,-1515.587917]},{"value":[9183.754656,-1642.350191,-1642.350191]},{"value":[9412.378906,-1681.268362,-1681.268362]},{"value":[9873.709996,-1764.664629,-1764.664629]},{"value":[11908.87412,-2127.160322,-2127.160322]},{"value":[13108.13082,-2343.990579,-2343.990579]},{"value":[14307.38751,-2561.93278,-2561.93278]},{"value":[15549.51125,-2782.098866,-2782.098866]},{"value":[17767.37065,-3179.064999,-3179.064999]},{"value":[18965.6067,-3393.671325,-3393.671325]},{"value":[20028.0971,-3581.590872,-3581.590872]},{"value":[23552.38081,-2538.581803,-2538.581803]},{"value":[24653.65568,-2614.194463,-2614.194463]},{"value":[25600.81331,-2706.48628,-2706.48628]},{"value":[26671.46886,-3149.042365,-3149.042365]},{"value":[27528.80982,-4030.818688,-4030.818688]},{"value":[29577.24231,-6432.630612,-6432.630612]},{"value":[30754.04484,-7098.688644,-7098.688644]},{"value":[32139.05874,-7422.266086,-7422.266086]},{"value":[33556.73325,-7500.102601,-7500.102601]},{"value":[36759.51411,-8297.370724,-8297.370724]},{"value":[38187.39506,-8483.06637,-8483.06637]},{"value":[39377.46595,-8520.872581,-8520.872581]},{"value":[42875.21292,-6233.591504,-6233.591504]},{"value":[45208.40509,-5675.392615,-5675.392615]},{"value":[46029.00286,-5431.875558,-5431.875558]},{"value":[47245.50844,-6663.026559,-6663.026559]}]}],"title":{"text":"basic Scatter3D example"},"tooltip":{"show":false},"visualMap":[{"calculable":true,"max":100,"inRange":{"color":["#313695","#4575b4","#74add1","#abd9e9","#e0f3f8","#fee090","#fdae61","#f46d43","#d73027","#a50026"]}}],"xAxis3D":{},"yAxis3D":{},"zAxis3D":{}};
      goecharts_PtWAWQntHtvI.setOption(option_PtWAWQntHtvI);
    }
  },
  mounted: function() {
    this.initChart()
  }
}
</script>
