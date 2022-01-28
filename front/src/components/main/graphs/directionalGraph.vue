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
            xAxis: {
                data: this.rawData.total.map((v, index) => index + 1)
            },
            yAxis: {
                type: 'value'
            },
            series: [
                {
                    type: 'line',
                    data: this.rawData.incoming
                },
                 {
                    type: 'line',
                    data: this.rawData.outgoing
                },
            ]
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

xAxis: {
        data: 
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            type: 'bar',
            data: [63, 75, 24, 92]
        }
        ]