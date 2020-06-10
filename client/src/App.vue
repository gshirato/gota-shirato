<template>

  <div id="app">
    <myheader></myheader>

    <router-view/>
  </div>

</template>

<script>
import myheader from './components/header'

export default {
  components: {
    myheader
  }
}
</script>
