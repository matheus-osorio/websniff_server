<template>
  <div id="genGraph">
    <e-chart :option="graph" autoresize></e-chart>
  </div>
</template>

<script>
export default {
props: ['rawData'],
data () {
return {
    loading: true
}
},
computed: {
    graph(){
        if(this.rawData === {}){
            return {}
        }
        const series = []
        let len = 0
        const legendData = [];
        for(let name in this.rawData){
            legendData.push(name)
            let prog = this.rawData[name]
            len = prog.length
            let obj = {
                name,
                type: 'line',
                data: prog
            }
            series.push(obj)
        }

        return {
            axisPointer: {
                animation: false
            },
            tooltip: {
                trigger: 'axis',
            },
            xAxis: {
                data: Array.from({length: len}, (x,i) => i+1)
            },
            yAxis: {
                type: 'value'
            },
            legend: {
                data: legendData
            },
            series,
        }
    }
},
components: {
},
}
</script>

<style>

#genGraph{
    border: solid;
    border-color: white;
    background: #fff!important;
    box-shadow: 0 0 5px 0 #9f9f9f;
    padding:10px;
}

.echarts {
    height: 100%;
    width: 100%;
}

</style>