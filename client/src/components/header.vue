<template>
  <header>
    <h1 class="headline">
      <a>Gota Shirato</a>
    </h1>
    <ul class="nav-list">
      <li class="nav-list-item"><router-link to="/">Home</router-link></li>
      <li class="nav-list-item"><router-link to="/about">About</router-link></li>
    </ul>
  </header>
</template>

<style scoped>
  * {
    margin:0; padding:0;
  }
  header {
    height: 100px;
    width: 100%;
    padding: 15px 0;
    background-color: #337079;
    color: white;
  }
  header .headline{
      line-height: 100px;
      float: left;
      font-size: 30px;
      margin-left: 100px;
  }
  .nav-list {
      line-height: 100px;
      float: left;
      margin-left: 30px;
      list-style: none;
  }
  .nav-list-item {
    list-style: none;
    display: inline-block;
    margin: 0 20px;
  }
</style>
