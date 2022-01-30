<template>
  <table class="table scroller">
    <thead>
      <th scope="col">Programa</th>
      <th scope="col">Conexões</th>
      <th scope="col">Total</th>
      <th scope="col">Download</th>
      <th scope="col">Upload</th>
    </thead>
    <tbody>
    <tr v-for="program in Object.keys(parsedData)" :key="program.id">
      <th>
        {{program}}
      </th>
      <td>
        {{parsedData[program].connections}}
      </td>
      <td>
        {{parsedData[program].total}}
      </td>
      <td>
        {{parsedData[program].incoming}}
      </td>
      <td>
        {{parsedData[program].outgoing}}
      </td>
    </tr>
    </tbody>
  </table>
</template>

<script>
import {sizeData} from '@/utils'
export default {
  props: ['data'],
  computed: {
    parsedData() {
      const data = {}
      for(let program in this.data) {
        const {
          connections,
          total,
          incoming,
          outgoing
        } = this.data[program]
        data[program] = {
          connections,
          total: sizeData(total),
          incoming: sizeData(incoming),
          outgoing: sizeData(outgoing)
        }
      }
      console.log(data)
      return data
    }
  }
}
</script>

<style>

.scroller {
  overflow: auto;
}

</style>