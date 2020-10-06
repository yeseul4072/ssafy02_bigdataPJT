<template>
  <v-container class="justify-center wrap" fluid fill-height>
    <v-row fill-height>
      <v-col cols="1" />
      <v-col cols="1" align="center">
        <v-img :src="require('../../assets/logo_foot.png')" height="70px" width="70px" />
      </v-col>
      <v-col cols="6">
        <v-row>
          <ul class="footLink">
            <li class="point br1" style="padding-left: 0;">
              <v-dialog
                v-model="policy"
                width="600px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <span
                    style="color: red !important;"
                    v-bind="attrs"
                    @click="policy=!policy"
                    v-on="on"
                  >
                    개인정보 처리방침
                  </span>
                </template>
                <v-card>
                  <v-card-title class="d-flex">
                    <v-row>
                      <v-col cols="12" align="end">
                        <v-btn
                          class="mx-2"
                          fab
                          x-small
                          :outlined="false"
                          :depressed="true"
                          color="rgba(0, 153, 204, 0)"
                          @click="policy=false"
                        >
                          <v-icon dark>
                            mdi-close
                          </v-icon>
                        </v-btn>
                      </v-col>
                      <v-col cols="12">
                        <span class="headline">어린이ZIP 개인정보 처리방침</span>
                      </v-col>
                    </v-row>
                  </v-card-title>
                  <v-card-text style="word-break:keep-all">
                    <private-policy />
                  </v-card-text>
                </v-card>
              </v-dialog>
            </li>
            <li class="br1">
              <v-dialog
                v-model="terms"
                width="600px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <span
                    v-bind="attrs"
                    @click="terms=!terms"
                    v-on="on"
                  >
                    이용약관
                  </span>
                </template>
                <v-card>
                  <v-card-title class="d-flex">
                    <v-row>
                      <v-col cols="12" align="end">
                        <v-btn
                          class="mx-2"
                          fab
                          x-small
                          :outlined="false"
                          :depressed="true"
                          color="rgba(0, 153, 204, 0)"
                          @click="terms=false"
                        >
                          <v-icon dark>
                            mdi-close
                          </v-icon>
                        </v-btn>
                      </v-col>
                      <v-col cols="12">
                        <span class="headline">어린이ZIP 이용약관</span>
                      </v-col>
                    </v-row>
                  </v-card-title>
                  <v-card-text style="word-break:keep-all">
                    <terms />
                  </v-card-text>
                </v-card>
              </v-dialog>
            </li>
            <li class="br1">
              <nuxt-link to="/community/2">
                Help
              </nuxt-link>
            </li>
            <li class="br1">
              <nuxt-link to="/community/3">
                Contact
              </nuxt-link>
            </li>
            <li>
              <nuxt-link to="/community/1">
                About
              </nuxt-link>
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
      <v-col cols="3" class="d-flex justify-center">
        <ul class="sns" style="margin-top:15px;">
          <li class="icon">
            <a href="https://www.facebook.com/"><v-img :src="require('../../assets/foot_ic_facebook.png')" /></a>
          </li>
          <li class="icon">
            <a href="https://section.blog.naver.com/BlogHome.nhn?directoryNo=0&currentPage=1&groupId=0"><v-img :src="require('../../assets/foot_ic_blog.png')" /></a>
          </li>
          <li class="icon">
            <a href="https://www.instagram.com/?hl=ko"><v-img :src="require('../../assets/foot_ic_insta.png')" /></a>
          </li>
          <li class="icon">
            <a href="https://www.youtube.com/"><v-img :src="require('../../assets/foot_ic_youtube.png')" /></a>
          </li>
        </ul>
      </v-col>
      <v-col cols="1" />
    </v-row>
  </v-container>
</template>

<script>
import PrivatePolicy from '@/components/Common/Footer/Policy.vue'
import Terms from '@/components/Common/Footer/Terms.vue'
export default {
  components: {
    PrivatePolicy,
    Terms
  },
  data () {
    return {
      policy: false,
      terms: false
    }
  }
}
</script>

<style scoped>
.wrap{
  height: 180px;
  background-color:#333;
  font-weight: 600;
  color: #999 ;
  font-size: 1vw;
}
ul{
  list-style: none;
  display: block;
  padding: 0 !important;
}
li {
  display: list-item;
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
