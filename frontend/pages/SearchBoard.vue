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
              <v-text
                @click="selected=index"
              >
                {{ item.text }}
              </v-text>
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
                    :board-count="item.boardCount"
                    :text="text"
                  />
                </v-col>
              </template>
            </v-data-iterator>
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
          <v-container>
            <v-row justify="center">
              <v-col cols="8">
                <v-pagination v-model="page" class="my-4" :length="pageCnt" />
              </v-col>
            </v-row>
          </v-container>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchBoardDetail from '@/components/Community/Search/SearchBoardDetail.vue'
export default {
  components: { SearchBoardDetail },
  data () {
    return {
      selected: 0,
      text: '',
      count: 0,
      page: 1,
      pageCnt: 10,
      itemsPerPage: 5,
      searchList: [
        {
          text: '게시판 제목'
        },
        {
          text: '게시판 설명'
        }
      ],
      boardList: [
        {
          id: 1,
          title: '안녕하세요! 여러분께 화이트데이 사탕을 가져왔어요! ( + 풀이 슬라이드 )',
          content: '여러분께 화이트 데이 사탕을 가지고 왔어요! 아래 문제를 화이트데이가 끝나기 전까지 풀어 주시면 제가 사탕 기프티콘을 드릴게요! https://www.acmicpc.net/proble... https://www.acmicpc.net/proble... https://www.acmicpc.net/proble... P. S. 1. 데이터가 중간에 추가 될 수 있어요, 그래도 데이터가 추가되기 전에 맞은 경우에는 사탕을 드릴게요! P. S. 2. 한 문제라도 풀어주시면 저는 기뻐요! 여러분들을 위한 사탕도 준비할 게요! P. S. 3. 이상한 방법으로 사탕을 얻으려고 시도 하면 제가 사탕을 안 줄지도 몰라요!',
          boardCount: 1
        },
        {
          id: 1,
          title: '안녕하세요!',
          content: '드디어 인사드릴 수 있어 기쁩니다.요즘 매일같이 이곳에 들락거리며,  "틀렸습니다" 와 더 친해지고 있네요.운영자님의 노고에 감사드리며, 모두들 화이팅 입니다! ',
          boardCount: 2
        },
        {
          id: 1,
          title: '안녕하세요. 현재 군대에서 문제 풀고있네요.',
          content: '안녕하세요.2012, 2013 ICPC 에 참가한 고려대학교 전명우입니다.다름이 아니라 얼마 전 있었던 인터넷예선 풀이를 제 블로그에 작성해서 같이 공유하고자 글을 쓰게 되었습니다.http://blog.myungwoo.krIOI 풀이도 작성했고, 기타 자잘한 문제 소개, 해법도 있습니다.감사합니다!',
          boardCount: 3
        },
        {
          id: 1,
          title: '안녕 여러분',
          content: 'JAVA 공부하면서 문제풀이할 곳을 찾다가 들어오게 되었습니다.   같은 문제라도 다른방식으로 접근해서 푸는분들을 보면서요 컴퓨터 언어를 언어라고 하는 이유를 많이 느낍니다  어제 기초 문제인 셀프넘버 풀면서 많이 느꼇어요 안녕하세요랑 안녕하십니까랑 같은 의미를 전달하지만 다른 형태를 가지고 있는 것처럼요 아무쪼록 열심히 하겠습니다. 잘부탁드립니당',
          boardCount: 4
        },
        {
          id: 1,
          title: '안녕 여러분',
          content: '반갑습니다 여러분',
          boardCount: 5
        },
        {
          id: 1,
          title: '안녕 여러분',
          content: '반갑습니다 여러분',
          boardCount: 6
        },
        {
          id: 1,
          title: '안녕 여러분',
          content: '반갑습니다 여러분',
          boardCount: 7
        }
      ]
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
