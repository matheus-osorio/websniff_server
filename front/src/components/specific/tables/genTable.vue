<template>
  <div class='scroller'><table class="table">
    <thead>
      <th>Programa</th>
      <th>Conexões</th>
      <th>Total</th>
      <th>Download</th>
      <th>Upload</th>
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
  </table></div>
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