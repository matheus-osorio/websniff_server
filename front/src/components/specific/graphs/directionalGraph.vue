<template>
  <div id="dirGraph">
    <e-chart :option="graph"></e-chart>
  </div>
</template>

<script>
export default {
props: ['rawData'],
data () {
return {
    loading: true,
    }
},
computed: {
    graph(){
        if(!this.rawData?.total) {
            return {}
        }
        return {
            axisPointer: {
                animation: false
            },
            tooltip: {
                trigger: 'axis',
            },
            xAxis: {
                data: this.rawData.total.map((v, index) => index + 1)
            },
            yAxis: {
                type: 'value'
            },
            series: [
                {
                    name: 'download',
                    type: 'line',
                    data: this.rawData.incoming
                },
                 {
                    name: 'upload',
                    type: 'line',
                    data: this.rawData.outgoing
                },
            ],
            legend: {
                data: ['download', 'upload']
            }
        }
    }
},
components: {
},
}
</script>

<style>

.echarts {
    height: 100%;
    width: 100%;
}

</style>
