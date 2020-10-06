<template>
  <div class="board-component-body">
    <!-- 리스트 뿌리기 -->
    <div class="bc-list-body">
      <!-- 상단 title -->
      <div class="divider">
        <v-row
          align="center"
          class="cm-bc-t1"
        >
          <v-col
            align="start"
            class="pa-0"
          >
            <v-row>
              <span>
                {{ board.title }}
              </span>
              <span v-if="board.title !== '공지사항' && board.title !== 'FAQ' && board.title !== '1:1문의'" class="pl-2">
                <v-icon
                  v-if="!board.favorite_yn"
                  class="cm-bc-icon"
                  @click="bmBoard"
                >
                  mdi-star-outline
                </v-icon>
                <v-icon
                  v-else
                  class="cm-bc-icon"
                  color="yellow"
                  @click="bmBoard"
                >
                  mdi-star
                </v-icon>
                <v-btn
                  class="cm-bc-icon"
                  depressed
                  fab
                  dark
                  x-small
                  color="success"
                  @click="goToWrite"
                >
                  <v-icon>
                    mdi-pencil
                  </v-icon>
                </v-btn>
              </span>
            </v-row>
          </v-col>
          <v-col
            class="pa-0"
            md="5"
            align="end"
          >
            <v-text-field
              v-model="text"
              outlined
              dense
              style="width:98%; padding-top:20px;"
              label="검색"
            />
          </v-col>
        </v-row>
      </div>
      <div
        v-if="articles.length != 0 && articles.results.length > 0"
      >
        <v-data-iterator
          :items="articles.results"
          :items-per-page.sync="itemsPerPage"
          hide-default-footer="hide-default-footer"
          no-data-text="게시글이 존재하지 않습니다."
          align="center"
        >
          <template
            v-slot:default="props"
          >
            <v-card
              rounded="0"
              outlined
              style="width:80%"
            >
              <v-col
                v-for="(item, index) in props.items"
                :key="index"
                class="pa-0"
                @click="goToBoardDetail(item.id)"
              >
                <BoardDetail :article="item" />
              </v-col>
            </v-card>
          </template>
        </v-data-iterator>
        <v-container>
          <v-row justify="center">
            <v-col cols="8">
              <v-pagination v-model="page" class="my-4" :length="pageCnt" />
            </v-col>
          </v-row>
        </v-container>
      </div>
      <div v-else>
        <v-row style="width:100%;">
          <v-col cols="12">
            <v-row align="start" justify="center">
              <v-icon style="font-size:150px; color:rgba(0, 0, 0, 0.54); margin:30px 0 20px 0">
                mdi-emoticon-cry-outline
              </v-icon>
            </v-row>
            <v-row align="start" justify="center">
              <div style="font-size:20px; margin-bottom:20px;">
                게시글이 존재하지 않습니다 :(
              </div>
            </v-row>
          </v-col>
        </v-row>
      </div>
    </div>
  </div>
</template>

<script>
import http from '@/util/http_common.js'
import BoardDetail from '@/components/Community/BoardDetail.vue'
export default {
  components: { BoardDetail },
  props: ['board', 'articles'],
  data () {
    return {
      page: 1,
      pageCnt: 0,
      itemsPerPage: 10,
      text: ''
    }
  },
  watch: {
    text () {
      http.axios.get(`/community/${this.board.id}/article?page=${this.page}&title=${this.text}`)
        .then(({ data }) => {
          this.pageCnt = parseInt((data.articles.count - 1) / this.itemsPerPage + 1)
          this.$emit('call-board', data.board)
          this.$emit('call-articles', data.articles)
        })
    },
    page () {
      http.axios.get(`/community/${this.board.id}/article?page=${this.page}&title=${this.text}`)
        .then(({ data }) => {
          this.pageCnt = parseInt((data.articles.count - 1) / this.itemsPerPage + 1)
          this.$emit('call-board', data.board)
          this.$emit('call-articles', data.articles)
        })
    }
  },
  mounted () {
    this.pageCnt = parseInt((this.articles.count - 1) / this.itemsPerPage + 1)
  },
  methods: {
    goToBoardDetail (id) {
      this.$router.push(`/board/${this.board.id}?title=${this.board.title}&id=${id}`)
    },
    bmBoard () {
      http.axios.post(`/community/${this.board.id}/favorite/`)
        .then(({ data }) => {
          this.board.favorite_yn = !this.board.favorite_yn
        })
    },
    goToWrite () {
      this.$router.push(`/board/write/${this.board.id}?title=${this.board.title}`)
    }
  }
}
</script>
<style scoped>
.board-component-body{
  padding-bottom: 20px;
  margin-bottom:20px;
}
.cm-bc-t1{
  margin-top: 5px !important;
  font-size: 1.5rem;
  font-weight: 600;
}
.cm-bc-icon{
  margin-bottom:5px;
}
.cm-bc-icon:hover{
  cursor: pointer;
}

.divider {
  margin:auto;
  width: 78%;
}

.bc-list-body{
  margin-left: 50px;
  margin-right: 50px;
}

</style>
