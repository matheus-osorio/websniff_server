<template>
  <div id="mainPage">
    <genGraph :rawData="total"/>
    <dirGraph :rawData="directional"/>
    <genTable :data="table" />
    <bulletArea :bullet1="bullet.total" :bullet2="bullet.incoming" :bullet3="bullet.timed" :bullet4="bullet.outgoing"/>
  </div>
</template>

<script>
import {sizeData} from '@/utils'
import genGraph from './graphs/generalGraph.vue'
import dirGraph from './graphs/directionalGraph.vue'
import genTable from './tables/genTable.vue'
import bulletArea from '../bulletArea.vue'
export default {
  components: {
    genGraph,
    dirGraph,
    genTable,
    bulletArea,
  },
  data(){
    return {
      directional: {},
      total: {},
      bullet: {
        timed: {
          title: 'Fluxo Atual',
          content: 0
        },
        incoming: {
          title: 'Total Download',
          content: 0
        },
        outgoing: {
          title: 'Total Upload',
          content: 0
        },
        total: {
          title: 'Total',
          content: 0
        },
      }
    }
  },
  mounted(){
    const connection = setInterval(() => {
      if(this.$route.name !== 'conexao') {
        clearInterval(connection)
        return
      }
      console.log({
        program: this.$route.params.program,
        connection: this.$route.params.connection,
      })
      fetch('http://localhost:5000/connection', {
        headers: {
          program: this.$route.params.program,
          conn: this.$route.params.connection,
        }
      })
      .then(res => res.json())
      .then((obj) => {
        console.log(obj)
        this.directional = obj.directional
        this.total = obj.total
        this.table = obj.table
        const bulletTitle = ['total', 'incoming', 'outgoing', 'timed']
        bulletTitle.forEach((entry) => {
          this.bullet[entry].content = sizeData(obj.bullet[entry])
        })

      })
    }, 1000)
  }

}
</script>

<style>
#mainPage {
  height: 100vh;
  width: 100vw;
  display: grid;
  background-color: #f5f5f5;
  grid-template-rows: 1fr 1fr;
  grid-template-columns: 1fr 1fr;
  row-gap: 30px;
  column-gap: 30px;
  padding: 2%;
}
</style>