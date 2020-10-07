<template>
  <div>
    <v-row
      class="signup"
      align="center"
    >
      <div style="margin-top:100px;">
&nbsp;
      </div>
      <div style="width:100%;">
        <v-row
          justify="center"
        >
          <a href="/" class="logo" />
        </v-row>
        <v-row
          justify="center"
        >
          <h1 style="font-size:40px; font-weight:400;">
            <span class="success--text" style="font-weight:700; font-size:40px;">어린이ZIP</span> 회원정보
          </h1>
        </v-row>
        <v-row
          justify="center"
          style="margin-top:20px;"
        >
          <input
            v-show="false"
            id="file"
            ref="file"
            type="file"
            accept="image/png, image/jpeg, image/bmp"
            @change="changeImg"
          >

          <v-badge
            color="transparent"
            bottom
            offset-x="65"
            offset-y="65"
          >
            <template v-slot:badge>
              <v-btn
                fab
                depressed
                color="#e4e4e4"
                outlined
                style="background-color:white;"
                @click="clickImg()"
              >
                <v-icon color="#e4e4e4">
                  mdi-camera
                </v-icon>
              </v-btn>
            </template>
            <v-avatar width="184" height="184">
              <v-img ref="img" :src="user && user.profile_image ? user.profile_image : '/user2.png'" />
            </v-avatar>
          </v-badge>
        </v-row>
        <v-row justify="center">
          <v-card
            class="form"
            tile
            hover
            outlined
            style="box-shadow:none;"
            :ripple="false"
          >
            <table width="100%">
              <tr width="100%">
                <th width="100%">
                  아이디
                </th>
              </tr>
              <tr width="100%;">
                <td width="100%">
                  <v-text-field
                    v-model="user.username"
                    placeholder="아이디를 입력해 주세요."
                    color="grey"
                    readonly
                  />
                </td>
              </tr>
              <div class="empty" />
              <tr>
                <th>
                  닉네임
                </th>
              </tr>
              <tr width="100%">
                <td width="100%">
                  <v-text-field
                    v-model="user.nickname"
                    placeholder="닉네임을 입력해 주세요."
                    color="grey"
                  />
                </td>
              </tr>
              <div class="empty" />
              <tr>
                <th>
                  이메일
                </th>
              </tr>
              <tr>
                <td>
                  <v-text-field
                    v-model="user.email"
                    placeholder="이메일을 입력해 주세요."
                    color="grey"
                  />
                </td>
              </tr>
              <div class="empty" />
              <tr>
                <th>
                  관심 지역
                </th>
              </tr>
              <tr>
                <td>
                  <v-text-field
                    v-model="user.address"
                    placeholder="관심 지역을 입력해 주세요."
                    color="grey"
                    @click="openDaumZipAddress"
                  />
                </td>
              </tr>
            </table>
          </v-card>
        </v-row>
        <v-row
          justify="center"
          style="margin-top:20px;"
        >
          <v-btn
            color="#0dCA78"
            rounded
            x-large
            depressed
            dark
            style="width:240px;"
            @click="modify"
          >
            <span style="font-size:16px; font-weight:400">수정완료</span>
          </v-btn>
        </v-row>

        <div style="margin-bottom:100px;" />
      </div>
    </v-row>
  </div>
</template>

<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></script>
<script type="text/JavaScript" src="http://dmaps.daum.net/map_js_init/postcode.v2.js"></script>
<!--<script type="text/JavaScript" src="http://dapi.kakao.com/v2/maps/sdk.js?appkey=dff523ff715cfa66c3e0461e1f477834&autoload=false"></script>-->
<!--<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=dff523ff715cfa66c3e0461e1f477834&libraries=services"></script>-->
<script>
import http from "@/util/http_common.js"
// import axios from "axios"
export default {
  data () {
    return {
        user: {},
    }
  },
  mounted() {
      http.axios.get('/rest-auth/user/profile/').then(({data}) => {
          this.user = data
      })
  },
  methods: {
    clickImg() {
        $("#file").click();
    },
    changeImg(e){
      var self = this
      var file = document.getElementById("file").files[0]
      var reader  = new FileReader();

      reader.onloadend = function () {
        self.$refs.img.src = reader.result;
      }

      if (file) {
        reader.readAsDataURL(file);
      }
    },

    openDaumZipAddress() {
        var setAddress = this.setAddress;
        new daum.Postcode({
            oncomplete(data) {
                var geocoder = new kakao.maps.services.Geocoder();

                var callback = function(result, status) {
                    if (status === kakao.maps.services.Status.OK) {
                        setAddress(data.address, result[0].x, result[0].y);
                    }
                };
                geocoder.addressSearch(data.address, callback);
            }
        }).open();
    },

    setAddress(address, lng, lat) {
        this.user.address = address
        this.user.lng = lng
        this.user.lat = lat
    },
    modify() {
    //   var frm = new FormData();
    //   console.log(document.getElementById("file").files[0])
    //   frm.append("profile_image", document.getElementById("file").files[0]);
    //   frm.append("username", this.id)
    //   frm.append("email", this.email)
    //   frm.append("password1", this.password)
    //   frm.append("password2", this.re_password)
    //   frm.append("latitude", this.lat)
    //   frm.append("longitude", this.lng)
    //   frm.append("address", this.address)
    //   frm.append("nickname", this.nickname)
    //   frm.append("is_director", 'False')
    //   console.log(frm)
    //   http.axios.post('http://j3a111.p.ssafy.io:8000/rest-auth/registration/', frm, {
    //     headers: {
    //       'accept': '*/*',
    //       'Content-Type': 'multipart/form-data'
    //     }
    //   }).then(({data}) => {
    //     console.log(data)
    //   })
    }
  }
}
</script>

<style scoped>
    @import url(//fonts.googleapis.com/earlyaccess/notosanskr.css);
    * {
        font-family: "Noto Sans KR", sans-serif !important;
        font-size:16px;
    }
    .empty{
        height:15px;
    }
    tr{
        height:40px;
    }
    th{
        font-size:14px;
        font-weight: 700;
        text-align:left;
    }
    .v-badge__badge .v-icon {
        color: inherit;
        font-size: 36px;
        margin: 0 -2px;
    }
    .v-badge__badge{
        border-color: #666666 !important;
    }
    .logo {
      background: url(/Vue.png) center center / cover no-repeat;
      margin-bottom:5px;
      height:50px;
      width:50px;
    }
    .signup {
        background-color: #f9f9f9;
        width:100%;
        margin:0;
    }

    .form {
      margin: 20px 0px;
      width: 600px;
      padding:24px 36px;
    }

    .v-text-field{
        padding:0;
        margin:0;
    }
</style>
