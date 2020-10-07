<template>
  <div>
    <v-row
      class="modify"
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
              <v-img ref="img" />
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
                    v-model="item.username"
                    color="grey"
                    readonly
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
                    v-model="item.email"
                    placeholder="이메일을 입력해 주세요."
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
                    v-model="item.nickname"
                    placeholder="닉네임을 입력해 주세요."
                    color="grey"
                    :error-messages="nickerror ? nick_text : ''"
                    @blur="validNickname()"
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
                    v-model="item.address"
                    placeholder="관심 지역을 입력해 주세요."
                    color="grey"
                    :error-messages="addrerror ? addr_text : false"
                    readonly
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
            :color="'#0dCA78'"
            rounded
            x-large
            depressed
            dark
            style="width:240px;"
            :loading="loading"
            @click="modify"
          >
            <span style="font-size:18px; font-weight:500">수정완료</span>
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
        item: {

        },
        nick:'',
        nickerror:false,
        nick_text: '',
        addrerror:false,
        addr_text:  '',
        loading:false,
    }
  },
  mounted() {
    http.axios.get('/rest-auth/user/profile/').then(({data}) => {
      if(data.profile_image)
        this.$refs.img.src = 'http://j3a111.p.ssafy.io:8000'+data.profile_image;
      else
        this.$refs.img.src = "/user2.png";
      this.item = data;
      this.nick = data.nickname;
    })
  },
  methods: {
    validNickname() {
      if(this.item.nickname == this.nick) {
        this.nickerror = false;
        return;
      }

      http.axios.get(`/rest-auth/validate/nickname/?nickname=${this.item.nickname}`)
        .then(({data}) => {
          this.nickerror = false;
          this.nick_text = '사용할 수 있는 닉네임입니다.'
        })
        .catch((error) => {
          this.nickerror = true;
          this.nick_text = '사용할 수 없는 닉네임입니다.'
        })
    },
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
        this.item.address = address
        this.item.longitude = lng
        this.item.latitude = lat
    },
    validCheck() {
      return this.nickerror || this.addrerror;
    },
    modify() {
      if(this.validCheck()){
        return;
      }
      this.loading = true;
      var frm = new FormData();
      if(document.getElementById("file").files[0]) {
        frm.append("profile_image", document.getElementById("file").files[0]);
      }
      frm.append("latitude", this.item.latitude)
      frm.append("longitude", this.item.longitude)
      frm.append("address", this.item.address)
      frm.append("nickname", this.item.nickname)
      const token = this.$router.app.$store.getters.getToken
      console.log(token)
      http.axios.put('http://j3a111.p.ssafy.io:8000/rest-auth/user/update/', frm, {
        headers: {
          Authorization: token ? token : '',
          'accept': '*/*',
          'Content-Type': 'multipart/form-data'
        }
      }).then(({data}) => {
        alert("수정되었습니다.")
        this.loading = false;
        this.$router.push('/home')
      })
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
    .modify {
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
