<template>
  <div id="gen-bullet-area">
    <bullet :data="bullet1"/>
    <bullet :data="bullet2"/>
    <bullet :data="bullet3"/>
    <bullet :data="bullet4"/>
  </div>
</template>

<script>
import bullet from './bullet.vue'
export default {
  props: ['bullet1','bullet2','bullet3','bullet4'],
  components: {
    bullet
  }
}
</script>

<style>
#gen-bullet-area{
  display: grid;
  grid-template-rows: 1fr 1fr;
  row-gap: 30px;
  column-gap: 30px;
  grid-template-columns: 1fr 1fr;
}
</style>