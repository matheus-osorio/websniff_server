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
  border: solid;
  border-color: white;
  background: #fff!important;
  box-shadow: 0 0 5px 0 #9f9f9f;
}

.text-center {
  text-align: center;
}

</style>