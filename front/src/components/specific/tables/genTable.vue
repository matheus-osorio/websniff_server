<template>
  <div class='scroller'><table class="table">
    <thead>
      <th>Conexão</th>
      <th>Protocolo</th>
      <th>Total</th>
      <th>Download</th>
      <th>Upload</th>
    </thead>
    <tbody>
    <tr v-for="connection in Object.keys(parsedData)" :key="connection.id">
      <th>
        <a class="pointer-click" @click="goToConnection(connection)">{{connection}}</a>
      </th>
      <td>
      {{parsedData[connection].protocol}}
      </td>
      <td>
        {{parsedData[connection].total}}
      </td>
      <td>
        {{parsedData[connection].incoming}}
      </td>
      <td>
        {{parsedData[connection].outgoing}}
      </td>
    </tr>
    </tbody>
  </table></div>
</template>

<script>
import {sizeData} from '@/utils'

export default {
  props: ['data'],
  methods:{
    goToConnection(connection){
      this.$router.push(`/${this.$route.params.program}/${connection}`)
    }
  },
  computed: {
    parsedData() {
      const data = {}
      for(let program in this.data) {
        const {
          connections,
          total,
          protocol,
          incoming,
          outgoing
        } = this.data[program]
        data[program] = {
          connections,
          protocol,
          total: sizeData(total),
          incoming: sizeData(incoming),
          outgoing: sizeData(outgoing)
        }
      }
      return data
    }
  }
}
</script>

<style>

.scroller {
  overflow: auto;
  height: 100%;
}

</style>