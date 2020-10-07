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
            <span class="success--text" style="font-weight:700; font-size:40px;">어린이ZIP</span> 회원가입
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
                    v-model="id"
                    placeholder="아이디를 입력해 주세요."
                    color="grey"
                    :success-messages="!iderror ? id_text : ''"
                    :error-messages="iderror ? id_text : ''"
                    @blur="validID()"
                  />
                </td>
              </tr>
              <div class="empty" />
              <tr>
                <th>
                  비밀번호
                </th>
              </tr>
              <tr>
                <td>
                  <v-text-field
                    v-model="password"
                    placeholder="비밀번호를 입력해 주세요."
                    color="grey"
                    type="password"
                    :success-messages="!pwerror ? pw_text : ''"
                    :error-messages="pwerror ? pw_text : ''"
                    @blur="validPassword()"
                  />
                </td>
              </tr>
              <tr>
                <td>
                  <v-text-field
                    v-model="re_password"
                    placeholder="비밀번호를 다시 한번 입력해 주세요."
                    color="grey"
                    type="password"
                    :success-messages="!repwerror ? repw_text : ''"
                    :error-messages="repwerror ? repw_text : ''"
                    @input="validRePassword()"
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
                    v-model="nickname"
                    placeholder="닉네임을 입력해 주세요."
                    color="grey"
                    :success-messages="!nickerror ? nick_text : ''"
                    :error-messages="nickerror ? nick_text : ''"
                    @blur="validNickname()"
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
                    v-model="email"
                    placeholder="이메일을 입력해 주세요."
                    color="grey"
                    :success-messages="!emailerror ? email_text : ''"
                    :error-messages="emailerror ? email_text : ''"
                    @blur="validEmail()"
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
                    v-model="address"
                    placeholder="관심 지역을 입력해 주세요."
                    color="grey"
                    :success-messages="!addrerror ? addr_text : false"
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
            :color="!validCheck() ? '#0dCA78' : '#d4d4d4'"
            rounded
            x-large
            depressed
            dark
            style="width:240px;"
            :loading="loading"
            @click="signup"
          >
            <span style="font-size:18px; font-weight:500">가입완료</span>
          </v-btn>
        </v-row>

        <div style="margin-bottom:100px;" />
      </div>
    </v-row>
  </div>
</template>

<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></script>
<script type="text/JavaScript" src="http://dmaps.daum.net/map_js_init/postcode.v2.js"></script>
<script type="text/JavaScript" src="http://dapi.kakao.com/v2/maps/sdk.js?appkey=dff523ff715cfa66c3e0461e1f477834&autoload=false"></script>
<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=dff523ff715cfa66c3e0461e1f477834&libraries=services"></script>
<script>
import http from "@/util/http_common.js"
// import axios from "axios"
export default {
  data () {
    return {
        id:'',
        password:'',
        re_password:'',
        nickname:'',
        email:'',
        address: '',
        lat: '',
        lng: '',

        iderror: false,
        id_text: '',
        pwerror: false,
        pw_text: '',
        repwerror: false,
        repw_text: '',
        emailerror: false,
        email_text: '',
        nickerror:false,
        nick_text: '',
        addrerror:false,
        addr_text:  '',
        loading:false,
    }
  },
  mounted() {
    this.$refs.img.src = "/user2.png";
  },
  methods: {
    validCheck() {
      return this.iderror || this.nickerror || this.emailerror || this.pwerror || this.repwerror || this.addrerror || !this.id_text || !this.nick_text || !this.email_text || !this.pw_text || !this.repw_text || !this.addr_text;
    },
    validID() {
      http.axios.get(`/rest-auth/validate/username/?username=${this.id}`)
        .then(({data}) => {
          this.iderror = false;
          this.id_text = '사용할 수 있는 아이디입니다.';
        })
        .catch((error) => {
          this.iderror = true;
          this.id_text = '사용할 수 없는 아이디입니다.';
        })
    },
    validPassword() {
      http.axios.get(`/rest-auth/validate/password/?password=${this.password}`)
        .then(({data}) => {
          this.pwerror = false;
          this.pw_text = '사용할 수 있는 비밀번호입니다.';
        })
        .catch((error) => {
          this.pwerror = true;
          this.pw_text = '사용할 수 없는 비밀번호입니다.';
        })
    },
    validRePassword() {
      if(this.password == this.re_password) {
        this.repwerror = false;
        this.repw_text = '비밀번호가 일치합니다.'
      }else {
        this.repwerror = true;
        this.repw_text = '비밀번호가 일치하지 않습니다.'
      }
    },
    validNickname() {
      http.axios.get(`/rest-auth/validate/nickname/?nickname=${this.nickname}`)
        .then(({data}) => {
          this.nickerror = false;
          this.nick_text = '사용할 수 있는 닉네임입니다.'
        })
        .catch((error) => {
          this.nickerror = true;
          this.nick_text = '사용할 수 없는 닉네임입니다.'
        })
    },
    validEmail() {
      http.axios.get(`/rest-auth/validate/email/?email=${this.email}`)
        .then(({data}) => {
          this.emailerror = false;
          this.email_text = '사용할 수 있는 이메일입니다.'
        })
        .catch((error) => {
          this.emailerror = true;
          this.email_text = '사용할 수 없는 이메일입니다.'
        })
    },
    validAddr() {
      if(this.lat && this.lng) {
        this.addrerror = false;
        this.addr_text = '올바른 주소입니다.'
      }else {
        this.addrerror = true;
        this.addr_text = '올바르지 않은 주소입니다.'
      }
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
        this.address = address
        this.lng = lng
        this.lat = lat
        this.validAddr()
    },
    signup() {
      if(this.id == ''){
        this.iderror = true;
        this.id_text = '아이디를 입력해주세요.';
        return;
      }
      else if(this.password == ''){
        this.pwerror = true;
        this.pw_text = '비밀번호를 입력해주세요.';
        return;
      }
      else if(this.re_password == ''){
        this.repwerror = true;
        this.repw_text = '비밀번호를 재확인해주세요.';
        return;
      }
      else if(this.nickname == ''){
        this.nickerror = true;
        this.nick_text = '닉네임을 입력해주세요.';
        return;
      }
      else if(this.email == ''){
        this.emailerror = true;
        this.email_text = '이메일을 입력해주세요.';
        return;
      }
      else if(this.address == ''){
        this.addrerror = true;
        this.addr_text = '주소를 입력해주세요.';
        return;
      }
      else if(this.validCheck()){
        return;
      }
      this.loading = true;
      var frm = new FormData();
      if(document.getElementById("file").files[0]) {
        frm.append("profile_image", document.getElementById("file").files[0]);
      }
      frm.append("username", this.id)
      frm.append("email", this.email)
      frm.append("password1", this.password)
      frm.append("password2", this.re_password)
      frm.append("latitude", this.lat)
      frm.append("longitude", this.lng)
      frm.append("address", this.address)
      frm.append("nickname", this.nickname)
      frm.append("is_director", 'False')
      console.log(frm)
      http.axios.post('http://j3a111.p.ssafy.io:8000/rest-auth/registration/', frm, {
        headers: {
          'accept': '*/*',
          'Content-Type': 'multipart/form-data'
        }
      }).then(({data}) => {
        alert(data.detail)
        this.loading = false;
        this.$router.push('/login')
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
