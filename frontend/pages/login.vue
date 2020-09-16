<template>
  <div class="login">
    <div class="login-box">
      <a href="/" class="logo" />

      <div class="login-box-wrap">
        <h1 style="text-align:center;">
          어린이ZIP
        </h1>
      </div>
    </div>
    <div class="banner" />
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
    .login{
        display: flex;
        min-width: 1200px;
    }
    .banner {
        position: relative;
        padding: 48px;
        width: 100%;
        min-height: 100vh;
        max-width: 768px;
        /* background: url(/bg.png) center center / cover no-repeat; */
        background-image: linear-gradient(45deg, rgb(13,202,120), rgb(11,203,156)); min-height:100%;
        display: flex;
    }
    .login-box {
        display: flex;
        flex-direction: column;
        background-color: rgb(255, 255, 255);
        width: calc(100% - 768px);
        min-height: 100vh;
    }
    .login-box-wrap {
        width: 480px;
        margin: auto;
    }
    .logo {
      margin-top:1%;
      margin-left:3%;
      background: url(/Vue.png) center center / cover no-repeat;

      height:50px;
      width:50px;
    }
</style>
