<template>
  <footer>
　　<ul class="footer-menu">
      <li class="nav-list-item"><router-link to="/">Home</router-link></li>
      <li class="nav-list-item"><router-link to="/about">About</router-link></li>
    </ul>
    <p>© All rights reserved by Gota Shirato.</p>
  </footer>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  * {
    margin:0; padding:0;
  }
  header {
    width: 100%;
    height: 200px;
    padding: 5px 0;
    text-align: center;
    color: #a52a2a;
    background-image: url("sampleimg2.jpg");
    background-position: center bottom;
    background-size: cover;
  }
  header .headline{
      line-height: 100px;
      font-size: 30px;
      text-decoration: underline;
  }
  .nav-list {
      line-height: 100px;
      list-style: none;
      font-weight: bold;
  }
  .nav-list-item {
    list-style: none;
    display: inline-block;
    margin: 0 20px;
  }
  footer{
      width: 100%;
      height: 100px;
      background-color: #174a5c;
      color: white;
      text-align: center;
  }
  ul.footer-menu li {
  display: inline;
  }
</style>
