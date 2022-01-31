<template>
  <div class="scroller">
  <table class="table">
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
      <a class="pointer-click" @click="goToSpecific(program)">{{program}}</a>
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
  </div>
</template>

<script>
import {sizeData} from '@/utils'
export default {
  props: ['data'],
  methods:{
    goToSpecific(program){
      this.$router.push(`/${program}`)
    }
  },
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
}

.pointer-click{
  cursor: pointer;
}
</style>