<template>
  <div class="callButton" @mouseover="$emit('showSidebar', true)" @mouseleave="$emit('showSidebar', false)">
    <i class="fas fa-bars"></i>
  </div>
</template>

<script>

export default {
  name: 'callButton',
  props: ['showSidebar'],
  components: {
  },
  mounted() {
  }
}
</script>

<style>
.callButton {
  position: absolute;
  z-index: 100;
  width: 5%;
  margin-top: 15px;
  margin-left: 15px;
}
</style>
