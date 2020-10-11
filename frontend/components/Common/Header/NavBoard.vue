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
            @click="moveToCommunity(item.id)"
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
            <v-col
              v-for="(boards, i) in bookmarkBoard"
              :key="i"
              cols="4"
            >
              <v-list-item
                v-for="(item, j) in boards"
                :key="j"
                v-ripple="false"
                dense
                @click="moveToCommunity(item.id)"
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
import http from '@/util/http_common.js'
export default {
  // props: ['is-show'],
  data () {
    return {
      item: 5,
      items: [
        {
          title: '공지사항',
          id: 1
        },
        {
          title: 'FAQ',
          id: 2
        },
        {
          title: '1:1문의',
          id: 3
        }
      ],
      bookmarkBoard: []
    }
  },
  watch: {

  },
  mounted () {
    http.axios.get('/community/favorite/boards/')
      .then(({ data }) => {
        if (data.length === 0) {
          this.bookmarkBoard = []
          this.bookmarkBoard.push([{
            title: '북마크 추가',
            id: 0
          }])
        } else {
          for (let i = 0; i < 15; i = i + 5) {
            this.bookmarkBoard.push(data.slice(i, i + 5))
          }
          let row = parseInt(data.length / 5)
          row = row >= 3 ? 2 : row
          const col = data.length % 5
          this.bookmarkBoard[row][col] = {
            title: '북마크 추가',
            id: 0
          }
        }
      })
  },
  methods: {
    validation () {
      this.dialog = true
    },
    moveToCommunity (id) {
      if (id === 0) {
        this.$router.push('/searchboard')
      } else {
        this.$router.push(`/community/${id}`)
      }
    },
    test () {
      this.$on('open-contact-form', () => {
      })
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
