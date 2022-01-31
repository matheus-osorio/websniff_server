<template>
  <div id="config-page" v-if="loaded">
    <form>
      <div class="mb-3">
        <label for="urlInput" class="form-label">Url da busca</label>
        <input type="text" class="form-control" id="urlInput"  @change="updateConfigs('url','str')" v-model="url">
        <div id="textHelp" class="form-text">Local onde o programa irá buscar informações</div>
      </div>
      <div class="mb-3">
        <label for="graphSize" class="form-label">Tamanho do Gráfico</label>
        <input type="text" class="form-control" id="graphSize" @change="updateConfigs('max_hold','int')" v-model="max_hold">
      </div>
      <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1">
        <label class="form-check-label" for="exampleCheck1">Salvar Histórico</label>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
</form>
  </div>
</template>

<script>
export default {
  data(){
    return {
      loaded: false,
      url: '/',
      max_hold: 60,
    }
  },
  methods: {
    updateConfigs(config, type) {
      fetch('http://localhost:5000/update_configs', {
        headers: {
          config,
          value: this[config],
          type,
        }
      })
    }
  },
  mounted() {
    fetch('http://localhost:5000/get_config')
    .then(res => res.json())
    .then(response => {
      this.max_hold = response.max_hold
      this.loaded = true
    })
  },
}
</script>

<style>

</style>