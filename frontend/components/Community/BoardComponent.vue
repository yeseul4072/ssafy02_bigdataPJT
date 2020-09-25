<template>
  <div class="board-component-body">
    <!-- 리스트 뿌리기 -->
    <div class="bc-list-body">
      <div
        v-if="boardList.length > 0"
      >
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
              {{ title }}
              <v-icon
                class="cm-bc-icon"
              >
                mdi-star-outline
              </v-icon>
              <v-btn
                class="cm-bc-icon"
                depressed
                fab
                dark
                x-small
                color="success"
              >
                <v-icon>
                  mdi-pencil
                </v-icon>
              </v-btn>
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
        <v-data-iterator
          :items="boardList"
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
              >
                <BoardDetail :board="item" />
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
import BoardDetail from '@/components/Community/BoardDetail.vue'
export default {
  components: { BoardDetail },
  props: ['boardType', 'title'],
  data () {
    return {
      page: 1,
      pageCnt: 10,
      itemsPerPage: 15,
      boardList: [
        {
          id: 1,
          title: '안녕하세요! 여러분께 화이트데이 사탕을 가져왔어요! ( + 풀이 슬라이드 )',
          content: '여러분께 화이트 데이 사탕을 가지고 왔어요! 아래 문제를 화이트데이가 끝나기 전까지 풀어 주시면 제가 사탕 기프티콘을 드릴게요! https://www.acmicpc.net/proble... https://www.acmicpc.net/proble... https://www.acmicpc.net/proble... P. S. 1. 데이터가 중간에 추가 될 수 있어요, 그래도 데이터가 추가되기 전에 맞은 경우에는 사탕을 드릴게요! P. S. 2. 한 문제라도 풀어주시면 저는 기뻐요! 여러분들을 위한 사탕도 준비할 게요! P. S. 3. 이상한 방법으로 사탕을 얻으려고 시도 하면 제가 사탕을 안 줄지도 몰라요!',
          boardCount: 1,
          likeCount: 1,
          dateTime: '2020-02-10',
          writer: '미용쓰기'
        },
        {
          id: 1,
          title: '안녕하세요!',
          content: '드디어 인사드릴 수 있어 기쁩니다.요즘 매일같이 이곳에 들락거리며,  "틀렸습니다" 와 더 친해지고 있네요.운영자님의 노고에 감사드리며, 모두들 화이팅 입니다! ',
          boardCount: 2,
          likeCount: 2,
          dateTime: '2020-02-10',
          writer: '미용쓰기'
        },
        {
          id: 1,
          title: '안녕하세요. 현재 군대에서 문제 풀고있네요.',
          content: '안녕하세요.2012, 2013 ICPC 에 참가한 고려대학교 전명우입니다.다름이 아니라 얼마 전 있었던 인터넷예선 풀이를 제 블로그에 작성해서 같이 공유하고자 글을 쓰게 되었습니다.http://blog.myungwoo.krIOI 풀이도 작성했고, 기타 자잘한 문제 소개, 해법도 있습니다.감사합니다!',
          boardCount: 3,
          likeCount: 3,
          dateTime: '2020-02-10',
          writer: '미용쓰기'
        },
        {
          id: 1,
          title: '안녕 여러분',
          content: 'JAVA 공부하면서 문제풀이할 곳을 찾다가 들어오게 되었습니다.   같은 문제라도 다른방식으로 접근해서 푸는분들을 보면서요 컴퓨터 언어를 언어라고 하는 이유를 많이 느낍니다  어제 기초 문제인 셀프넘버 풀면서 많이 느꼇어요 안녕하세요랑 안녕하십니까랑 같은 의미를 전달하지만 다른 형태를 가지고 있는 것처럼요 아무쪼록 열심히 하겠습니다. 잘부탁드립니당',
          boardCount: 4,
          likeCount: 4,
          dateTime: '2020-02-10',
          writer: '미용쓰기'
        },
        {
          id: 1,
          title: '안녕 여러분',
          content: '반갑습니다 여러분',
          boardCount: 5,
          likeCount: 5,
          dateTime: '2020-02-10',
          writer: '미용쓰기'
        },
        {
          id: 1,
          title: '안녕 여러분',
          content: '반갑습니다 여러분',
          boardCount: 6,
          likeCount: 6,
          dateTime: '2020-02-10',
          writer: '미용쓰기'
        },
        {
          id: 1,
          title: '안녕 여러분',
          content: '반갑습니다 여러분',
          boardCount: 7,
          likeCount: 7,
          dateTime: '2020-02-10',
          writer: '미용쓰기'
        }
      ]
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
