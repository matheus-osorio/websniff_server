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
        for(let name in this.rawData){
            let prog = this.rawData[name]
            len = prog.length
            let obj = {
                type: 'line',
                data: prog,
                name,
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
            legend:{
                data: ['total']
            },
            xAxis: {
                data: Array.from({length: len}, (x,i) => i+1)
            },
            yAxis: {
                type: 'value'
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

.echarts {
    height: 100%;
    width: 100%;
}

</style>