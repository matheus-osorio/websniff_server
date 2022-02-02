<template>
  <div @mouseover="$emit('showSidebar', true)" @mouseleave="$emit('showSidebar', false)" class="sidebar" :class="{'activate-hover': show}">
    <img src="logo.png" alt="" class="logo-icon">
    <ul class="nav nav-pills flex-column mb-auto padded-list">
      <li class="nav-item">
        <a href="#" class="nav-link link-dark" @click="changePage('')" aria-current="page" :class="{'active': this.$route.name === 'geral'}">
          <i class="fas fa-home"></i>
          Gráficos Gerais
        </a>
      </li>
      <li>
        <a href="#" class="nav-link link-dark" :class="{'active': this.$route.name === 'especifico'}">
          <i class="fas fa-search"></i>
          Gráficos do Programa
        </a>
      </li>
      <li>
        <a href="#" class="nav-link link-dark" :class="{'active': this.$route.name === 'conexao'}">
          <i class="fas fa-search-plus"></i>
          Gráficos da Conexão
        </a>
      </li>
      <li>
        <a href="#" class="nav-link link-dark" :class="{'active': this.$route.name === 'configuracao'}"  @click="changePage('configuration')">
          <i class="fas fa-cog"></i>
          Configurações
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ['show'],
  methods: {
    changePage(page) {
      this.$router.push(`/${page}`)
    }
  },
  data() {
    return {
      active: 1,
    }
  }
}
</script>

<style>
.sidebar {
  height: 100%;
  position: absolute;
  z-index: 10000; 
  top: 0;
  background-color: #93a9cc;
  width: 15%;
  left: -300px;
  transition: all 0.5s ease 0s;
  
  display: grid;

  row-gap: 10px;
  grid-template-rows: repeat(10, 1fr);
}

.logo-icon {
  grid-row: span 4;
  width: 100%;
  height: auto;
}

.active {
  background-color: black !important;
}

.padded-list {
  margin: 0px 5px;
}

</style>