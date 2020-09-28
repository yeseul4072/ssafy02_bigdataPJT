<template>
  <v-navigation-drawer
    v-model="draw"
    absolute
    right
    temporary
    style="z-index:100;"
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
              <template v-if="noti!=0">
                <v-badge color="red" :content="noti">
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
</template>

<script scoped>
export default {
  props: ['draw', 'noti'],
  data () {
    return {
      group: null
    }
  },
  watch: {
    group () {
      this.draw = false
      this.$emit('childs-event')
    }
  }
}
</script>

<style>
.MNavIcon {
  font-size: 1.7rem;
  color: #2E2E2E;
}
.MNavFont {
  font-size: 1.0rem;
  font-weight: 600;
}
</style>
