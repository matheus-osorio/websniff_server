<template>
  <div class="scroller">
  <table class="table">
    <thead>
      <th scope="col">Protocolo</th>
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
  border: solid;
  border-color: white;
  background: #fff!important;
  box-shadow: 0 0 5px 0 #9f9f9f;
  padding:10px;
}

.pointer-click{
  color: black;
  font-weight: bolder;
  text-decoration: none; /* no underline */
  cursor: pointer;
}

.pointer-click:hover{
  color: rgb(76, 169, 212);
}
</style>