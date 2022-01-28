<template>
  <table>
    <thead>
      <th>Programa</th>
      <th>Conexões</th>
      <th>Total</th>
      <th>Download</th>
      <th>Upload</th>
    </thead>
    <tr v-for="program in Object.keys(data)" :key="program.id">
      <td>
        {{program}}
      </td>
      <td>
        {{data[program].connections}}
      </td>
      <td>
        {{data[program].total}}
      </td>
      <td>
        {{data[program].incoming}}
      </td>
      <td>
        {{data[program].outgoing}}
      </td>
    </tr>
  </table>
</template>

<script>
export default {
  props: ['data']
}
</script>

<style>

</style>