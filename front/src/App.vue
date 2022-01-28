<template>
  <div id="root">
    <callButton @showSidebar="changeSidebar"/>
    <SideBar :show="showSidebar" @showSidebar="changeSidebar"/>
    <router-view />
  </div>
</template>

<script>
import callButton from './components/CallButton.vue'
import SideBar from './components/SideBar.vue'

export default {
  name: 'App',
  components: {
    callButton,
    SideBar,
  },
  data() {
    return {
      showSidebar: false,
      general: {
        directional: {}
      }
    }
  },
  mounted(){
  },
  methods: {
    changeSidebar(value) {
      this.showSidebar = value;
    }
  }
}
</script>

<style>
html, body {
  height: 100vh;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
}

.activate-hover {
  left: 0px;
  transition: all 0.5s ease 0s;
}
</style>
