<template>
  <div class="bullet-border">
  <h2 class="text-center">{{data.title}}</h2>
  <h1 class="text-center">{{data.content}}</h1>
  </div>
</template>

<script>
export default {
  props: ['data']

}
</script>

<style>
.bullet-border {
  padding: 20px;
  border-style: solid;
  border-color: lightgrey;
  border-width: 1px;
  border-radius: 5px;
}

.text-center {
  text-align: center;
}

</style>