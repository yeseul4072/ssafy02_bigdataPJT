<template>
  <v-container fluid class="cont" style="z-index:98; background-color:white;">
    <v-divider />
    <div ref="boardBox" class="wrap justify-center d-flex">
      <v-row class="w700">
        <v-col cols="0.5" />
        <v-divider
          class="mx-4"
          vertical
        />
        <v-col cols="2" style="max-width: 230px">
          <v-subheader><h2>중요 게시판</h2></v-subheader>
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            v-ripple="false"
            dense
            @click="moveToCommunity(1)"
          >
            {{ item.title }}
          </v-list-item>
        </v-col>
        <v-divider
          class="mx-4"
          vertical
        />
        <v-col cols="7" style="max-width: 780px">
          <v-subheader><h2>나만의 게시판</h2></v-subheader>
          <v-row>
            <v-col cols="4">
              <v-list-item
                v-for="(item, i) in items2"
                :key="i"
                v-ripple="false"
                dense
                @click="moveToCommunity(1)"
              >
                {{ item.title }}
              </v-list-item>
            </v-col>
            <v-col cols="4">
              <v-list-item
                v-for="(item, i) in items2"
                :key="i"
                v-ripple="false"
                dense
                @click="moveToCommunity(1)"
              >
                {{ item.title }}
              </v-list-item>
            </v-col>
            <v-col cols="4">
              <v-list-item
                v-for="(item, i) in items2"
                :key="i"
                v-ripple="false"
                dense
                @click="moveToCommunity(1)"
              >
                {{ item.title }}
              </v-list-item>
            </v-col>
          </v-row>
        </v-col>
        <v-divider
          class="mx-4"
          vertical
        />
        <v-col cols="0.5" />
      </v-row>
      <hr>
    </div>
    <v-divider />
  </v-container>
</template>

<script>
export default {
  // props: ['is-show'],
  data () {
    return {
      item: 5,
      items: [
        {
          title: '공지사항'
        },
        {
          title: 'FAQ'
        },
        {
          title: '1:1문의'
        }
      ],
      items2: [
        {
          title: '수다게시판'
        },
        {
          title: '우리 아이'
        },
        {
          title: '육아 질문'
        },
        {
          title: '정보 공유/후기'
        },
        {
          title: '같이해요/같이사요'
        }
      ],
      items3: [
        {
          title: '수다게시판'
        },
        {
          title: '우리 아이'
        },
        {
          title: '육아 질문'
        },
        {
          title: '정보 공유/후기'
        },
        {
          title: '게시판 찾기'
        }
      ],
      lenItems3 () {
        return this.items3.length - 1
      }
    }
  },
  watch: {
    // isShow (val) {
    //   if (val === true) { this.$emit('child-event', this.$refs.boardBox.clientHeight) } else { this.$emit('child-event', 0) }
    // }
  },
  mounted () {
  },
  methods: {
    validation () {
      this.dialog = true
    },
    moveToCommunity (id) {
      this.$router.push(`/community/${id}`)
    }
  }

}
</script>

<style scoped>
.warp {
  box-sizing: border-box;
  font-size: 0;
  text-align: center;
  white-space: nowrap;
  overflow: hidden;
  overflow-x: auto;
}
.cont {
  padding-bottom: 0;
}
.col {
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}
.w700{
  font-weight: 700;
}
.v-list-item{
  cursor: pointer;
}
.v-list-item:hover{
  background-color: #D8D8D8;
}

</style>
