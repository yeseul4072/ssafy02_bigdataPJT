<template>
  <div>
    <div class="MainHeader" style="background-color:white; ">
      <div class="HeaderGradient" />
      <v-container fluid class="cont">
        <div class="Logo">
          <section class="LogoLeft">
            <logo-icon />
          </section>
          <section class="LogoRight">
            <div class="ServiceName" @click="goToHome()">
              <h1 style="font-size:2.0rem">
                어린이ZIP
              </h1>
            </div>
            <div>
              <h5 style="color: gray;">
                "어린이집 정보, 한번에 찾자"
              </h5>
            </div>
          </section>
        </div>
        <div class="NavBar">
          <ul class="NavBarMenu">
            <v-col class="d-none d-md-block">
              <!-- 게시판 -->
              <li type="button" @click.stop="changeBoard()">
                <i class="far fa-clipboard NavIcon" />
              </li>
              <!-- 알림 -->
              <v-menu
                rounded="lg"
                offset-y
              >
                <template v-slot:activator="{ attrs, on }">
                  <li type="button">
                    <template v-if="newNoti!=0">
                      <v-badge color="red" :content="newNoti">
                        <i
                          v-bind="attrs"
                          class="far fa-bell NavIcon"
                          v-on="on"
                        />
                      </v-badge>
                    </template>
                    <i v-else class="far fa-bell NavIcon" />
                  </li>
                </template>

                <v-list>
                  <v-list-item
                    v-for="item in notiTap"
                    :key="item"
                    link
                  >
                    <v-list-item-title class="tapFont" v-text="item" />
                  </v-list-item>
                </v-list>
              </v-menu>

              <!-- 회원 -->
              <v-menu
                key="Large"
                rounded="lg"
                offset-y
              >
                <template v-slot:activator="{ attrs, on }">
                  <li type="button">
                    <i
                      v-bind="attrs"
                      class="far fa-user-circle NavIcon"
                      v-on="on"
                    />
                  </li>
                </template>

                <v-list>
                  <v-list-item
                    v-for="(item, index) in userTap"
                    :key="index"
                    link
                  >
                    <v-row>
                      <v-col cols="3" align="center">
                        <i :class="userIcon[index]" />
                      </v-col>
                      <v-col cols="2" align="center" />
                      <v-col cols="7" align="left" class="tapFont">
                        {{ item }}
                      </v-col>
                    </v-row>
                  </v-list-item>
                </v-list>
              </v-menu>
            </v-col>
            <!-- hamhurger -->
            <v-col class="d-block d-md-none">
              <v-icon @click.stop="drawer = !drawer">
                fas fa-bars
              </v-icon>
            </v-col>
          </ul>
        </div>
      </v-container>
      <div style="padding-top:125px">
        <v-divider />
      </div>
    </div>
    <div v-show="drawer">
      <v-navigation-drawer
        v-model="drawer"
        absolute
        right
        temporary
        style="position:fixed"
      >
        <v-list
          nav
          dense
        >
          <v-list-item-group
            v-model="group"
            active-class="deep-purple--text text--accent-4"
          >
            <v-list-item>
              <v-row>
                <v-col cols="3" align="center">
                  <i class="far fa-clipboard MNavIcon" />
                </v-col>
                <v-col cols="9" align="center" class="MNavFont">
                  게시판
                </v-col>
              </v-row>
            </v-list-item>

            <v-list-item>
              <v-row>
                <v-col cols="3" align="center">
                  <template v-if="newNoti!=0">
                    <v-badge color="red" :content="newNoti">
                      <i class="far fa-bell MNavIcon" />
                    </v-badge>
                  </template>
                  <i v-else class="far fa-bell MNavIcon" />
                </v-col>
                <v-col cols="9" align="center" class="MNavFont">
                  알림
                </v-col>
              </v-row>
            </v-list-item>

            <v-list-item>
              <v-row>
                <v-col cols="3" align="center">
                  <i class="far fa-user MNavIcon" />
                </v-col>
                <v-col cols="9" align="center" class="MNavFont">
                  회원정보
                </v-col>
              </v-row>
            </v-list-item>

            <v-list-item>
              <v-row>
                <v-col cols="3" align="center">
                  <i class="fas fa-power-off MNavIcon" />
                </v-col>
                <v-col cols="9" align="center" class="MNavFont">
                  로그아웃
                </v-col>
              </v-row>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
    </div>
  </div>
</template>

<script scoped>
import { mapGetters } from 'vuex'
import LogoIcon from '@/components/Common/Header/Logo.vue'
// import NavBoard from '@/components/Common/Header/NavBoard.vue'
export default {
  components: {
    LogoIcon
    // NavBoard
  },
  data () {
    return {
      newNoti: 4,
      userTap: ['회원정보', '로그아웃'],
      userIcon: ['far fa-user tapIcon', 'fas fa-power-off tapIcon'],
      notiTap: [...Array(4)].map((_, i) => `안녕하세요...글에 댓글이 달렸습니다. ${i}`),
      drawer: false,
      group: null
    }
  },
  computed: {
    ...mapGetters(['isLogin'])
  },
  watch: {
    group () {
      this.drawer = false
    }
  },
  methods: {
    goToRoot () {
      this.$router.push('/')
    },
    goToHome () {
      this.$router.push('/home')
    },
    changeBoard () {
      const cur = this.$store.state.Header.isBoard
      this.$store.commit('setIsBoard', !cur)
    }
  }
}
</script>

<style scoped>
.MainHeader {
  width: 100%;
  height: 125px;
  position: fixed;
  top: 0px;
  /* background: #fae57c; */
  z-index: 3;
}
.HeaderGradient {
  width: 100%;
  height: 100%;
  opacity: 0.3;
  /* background-image: linear-gradient(to bottom, #fdf4b3, #ffd400); */
  position: absolute;
}
.cont {
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-areas:
      ". logo logo logo navbar navbar navbar navbar navbar ."
      ". hr hr hr hr hr hr hr hr ."
      ". subNavbar subNavbar subNavbar subNavbar subNavbar subNavbar subNavbar subNavbar .";
  grid-template-columns: 3.75% repeat(8,11.5625%) 3.75%;
  grid-template-rows: 70% 5% 25%;
  padding: 30px 0 0;
  z-index: 4;
  position: absolute;
}
.Logo {
  grid-area: logo;
  display: inline-flex;
  width: 350px;
}
.LogoLeft {
  width: 33%;
  height: 120px;
}
.LogoRight {
  width: 67%;
  height: 120px;
}
.logoMob {
  cursor: pointer;
  width: 130px;
  height: 130px;
  transform-origin: left top;
  transform: scale(.58);
  cursor: pointer;
  pointer-events: auto;
}
.ServiceName {
  cursor: pointer;
}
.NavBar {
  grid-area: navbar;
  float: right;
  display: inline-flex;
}
.NavBarMenu {
  width: 100%;
  list-style: none;
  text-align: right;
}
.NavBarMenu li {
  display: inline;
  margin: 0 10px;
  padding: 10px 12px;
  font-size: 16px;
  background-color: transparent;
  border-radius: 4px;
  font-weight: 800;
}
.NavIcon {
  font-size: 2.3rem;
  color: #2E2E2E;
}
.MNavIcon {
  font-size: 1.7rem;
  color: #2E2E2E;
}
.MNavFont {
  font-size: 1.0rem;
  font-weight: 800;
}
.tapIcon {
  font-size: 1.3rem;
  color: #2E2E2E;
}
.tapFont {
  font-size: 1.0rem;
  font-weight: 800;
}
i:hover {
  color : gray;
}

</style>
