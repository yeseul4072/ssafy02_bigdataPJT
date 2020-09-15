<template>
  <v-container class="justify-center wrap" fluid fill-height>
    <v-row fill-height>
      <v-col cols="0.25" />
      <v-col cols="1" align="center">
        <v-img :src="require('../../assets/logo_foot.png')" height="70px" width="70px" />
      </v-col>
      <v-col cols="5">
        <v-row>
          <ul class="footLink">
            <li class="point br1" style="padding-left: 0;">
              <a href="javascript:void(0);" style="color: red !important;">개인정보 처리방침</a>
            </li>
            <li class="br1">
              <a href="javascript:void(0);">이용약관</a>
            </li>
            <li class="br1">
              <a href="javascript:void(0);">Help</a>
            </li>
            <li class="br1">
              <a href="javascript:void(0);">Contact</a>
            </li>
            <li>
              <a href="javascript:void(0);">About</a>
            </li>
          </ul>
        </v-row>
        <v-row>
          서울특별시 강남구 테헤란로 212 (역삼동 718-5번지) FAX. 0501-070-0000 고객상담센터 020-737-2020
        </v-row>
        <v-row>
          Copyright © 2020 ChildrenZIP Inc. All rights reserved.
        </v-row>
      </v-col>
      <v-col cols="2">
        <ul class="sns">
          <li class="icon">
            <a href="javascript:void(0);"><v-img :src="require('../../assets/foot_ic_facebook.png')" /></a>
          </li>
          <li class="icon">
            <a href="javascript:void(0);"><v-img :src="require('../../assets/foot_ic_blog.png')" /></a>
          </li>
          <li class="icon">
            <a href="javascript:void(0);"><v-img :src="require('../../assets/foot_ic_insta.png')" /></a>
          </li>
          <li class="icon">
            <a href="javascript:void(0);"><v-img :src="require('../../assets/foot_ic_youtube.png')" /></a>
          </li>
        </ul>
      </v-col>
      <v-col cols="0.25" />
    </v-row>
  </v-container>
</template>

<script>
export default {

}
</script>

<style scoped>
.wrap{
  height: 180px;
  background-color:#333;
  font-weight: 600;
  color: #999 ;
}
ul{
  list-style: none;
  display: block;
  padding: 0;
}
li {
  display: list-item;
  font-size: 14px;
  float: left;
  padding: 0 20px;
  margin-bottom: 15px;
}
.br1 {
  border-right: 1px solid #999;
}
a {
  color: #999 !important;
  text-decoration: none;
}
.icon {
  display: list-item;
  font-size: 14px;
  float: left;
  padding: 0 7px;
}
</style>
