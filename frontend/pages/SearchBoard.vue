<template>
  <div class="body-container">
    <!-- 여기는 검색 하는 부분 -->
    <div class="search-box">
      <div class="search-box-title">
        <h2 class="search-box-title-text">
          게시판 검색
        </h2>
        <v-text-field
          v-model="text"
          style="width:500px;"
          outlined
          dense
          label="검색어"
        />
      </div>
    </div>
    <!-- 여기는 검색 결과 출력하는 부분 -->
    <div class="search-box-list">
      <div class="search-box-list-left">
        <div
          id="search-box-left-title"
          style="font-size:1rem; color:#555555;"
        >
          검색 결과
        </div>
        <ul
          class="search-box-nav"
          style="margin-top:15px;"
        >
          <li
            v-for="(item, index) in searchList"
            :key="index"
            style="padding-top:5px;"
          >
            <div>
              <span
                @click="selected=index; goSearch(1);"
              >
                {{ item.text }}
              </span>
              <v-hover v-slot:default="{ hover }">
                <v-icon
                  v-if="selected == index || hover"
                  style="font-size: 15px;"
                >
                  mdi-check-bold
                </v-icon>
              </v-hover>
            </div>
          </li>
        </ul>
      </div>
      <div class="search-box-list-right">
        <div style="width:100% !important;">
          <div style="font-size:0.8em; color:#555555;">
            검색 결과 {{ count }}개
          </div>
          <div
            v-if="boardList.length > 0"
          >
            <v-data-iterator
              :items="boardList"
              :items-per-page.sync="itemsPerPage"
              hide-default-footer="hide-default-footer"
              no-data-text="게시글이 존재하지 않습니다."
            >
              <template v-slot:default="props">
                <v-col v-for="(item, index) in props.items" :key="index">
                  <SearchBoardDetail
                    :id="item.id"
                    :title="item.title"
                    :content="item.content"
                    :board-count="item.article_count"
                    :text="text"
                  />
                </v-col>
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
                    게시판이 존재하지 않습니다 :(<br>
                    여러분이 한번 만들어보세요!
                    <v-dialog
                      v-model="dialog"
                      persistent
                      max-width="350"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn
                          class="cm-bc-icon"
                          depressed
                          fab
                          dark
                          x-small
                          color="success"
                          v-bind="attrs"
                          v-on="on"
                        >
                          <v-icon>
                            mdi-pencil
                          </v-icon>
                        </v-btn>
                      </template>
                      <v-card>
                        <v-card-title class="headline">
                          게시판 만들기
                        </v-card-title>
                        <v-card-text>
                          <div>
                            게시판이 없나요? 그렇다면 여러분이 원하는 게시판을 만들어보세요!
                          </div>
                          <div class="mt-5">
                            <v-text-field
                              v-model="title"
                              class="pa-0"
                              :rules="rules"
                              hide-details="auto"
                              label="이름"
                            />
                          </div>
                          <div class="mt-5">
                            <v-text-field
                              v-model="content"
                              class="pa-0"
                              hide-details="auto"
                              label="간단한 설명"
                            />
                          </div>
                        </v-card-text>
                        <v-card-actions>
                          <v-spacer />
                          <v-btn
                            color="red darken-1"
                            text
                            @click="dialog = false"
                          >
                            취소
                          </v-btn>
                          <v-btn
                            color="green darken-1"
                            text
                            @click="dialog = false; createBoard()"
                          >
                            만들기
                          </v-btn>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>
                  </div>
                </v-row>
              </v-col>
            </v-row>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import http from '@/util/http_common.js'
import SearchBoardDetail from '@/components/Community/Search/SearchBoardDetail.vue'
export default {
  components: { SearchBoardDetail },
  data () {
    return {
      selected: 0,
      text: '',
      count: 0,
      page: 1,
      pageCnt: 0,
      itemsPerPage: 10,
      searchList: [
        {
          text: '게시판 제목',
          type: 'title'
        },
        {
          text: '게시판 설명',
          tyep: 'content'
        }
      ],
      boardList: [
        {
          article_count: 0,
          content: '',
          favorite_yn: 0,
          id: 0,
          title: ''
        }
      ],
      dialog: false,
      rules: [
        value => !!value || '필수로 입력해야합니다.'
      ],
      title: '',
      content: ''
    }
  },
  watch: {
    text () {
      this.goSearch(1)
    },
    page () {
      this.goSearch(this.page)
    }
  },
  mounted () {
    http.axios.get(`/community/?page=${this.page}`)
      .then(({ data }) => {
        this.boardList = data.results
        this.count = data.count
        this.pageCnt = parseInt((data.count - 1) / this.itemsPerPage + 1)
      })
  },
  methods: {
    goSearch (page) {
      if (this.selected === 0) {
        http.axios.get(`/community?page=${page}&title=${this.text}`)
          .then(({ data }) => {
            this.boardList = data.results
            this.count = data.count
            this.pageCnt = parseInt((data.count - 1) / this.itemsPerPage + 1)
          })
      } else {
        http.axios.get(`/community?page=${page}&content=${this.text}`)
          .then(({ data }) => {
            this.boardList = data.results
            this.count = data.count
            this.pageCnt = parseInt((data.count - 1) / this.itemsPerPage + 1)
          })
      }
    },
    createBoard () {
      http.axios.post('/community/', {
        title: this.title,
        content: this.content
      })
        .then(({ data }) => {
          this.goSearch(1)
        })
    }
  }
}
</script>

<style scoped>
.search-box{
  background-color: rgb(251, 251, 251);
  border-bottom: 1px solid #eee;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 200px;
}
.search-box-title{
  margin: auto;
}
.search-box-title-text{
  text-align:center;
  padding-top: 20px;
  padding-bottom:20px;
  color:#585f69;
}

.search-box-title-div{
    margin: auto;
}
.centered-input input {
  text-align: center;
}
.body-center{
  display: table;
  text-align:center !important;
}
.search-box-list{
  display: flex;
  padding-top: 50px;
}
.search-box-list-right{
  position: relative;
  padding-left: 20px;
  width: 100%;
  min-width: 400px;
  max-width: 1000px;
  min-height: 50vh !important;
  display: flex;
}
.search-box-list-left{
  border-right: 1px solid #eee;
  position: relative;
  display: flex;
  flex-direction: column;
  padding-left: 10%;
  background-color: rgb(255, 255, 255);
  width: 20%;
  min-width: 200px;
}

.search-box-nav{
  margin: 0;
  padding: 0;
  list-style:none;
  font-size: 0.8rem;
}

.search-pagination{
  width: 100%;
  text-align:center !important;
}
</style>
