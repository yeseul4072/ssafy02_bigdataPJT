<template>
  <div>
    <!-- 타이틀 바 -->
    <!-- <v-col
      class="pa-0"
      align="center"
    >
      <div class="body-container">
        <v-row
          align="center"
        >
          <v-col
            :cols="3"
          >
            <v-row
              align="center"
            >
              <v-icon style="margin-right:10px;">
                mdi-charity
              </v-icon>
              <span style="font-size:1.5rem; font-weight:800;">커뮤니티</span>
            </v-row>
          </v-col>

          <v-col
            :cols="8"
          >
            <v-row>
              <v-col
                v-for="i in tabs"
                :key="i"
                class="pa-0"
                align="center"
                :cols="2"
                @click="changeTab(i)"
              >
                <div
                  class="index-hover"
                >
                  {{ title[i-1] }}<div />
                </div>
              </v-col>
            </v-row>
          </v-col>
          <v-col
            class="pa-0"
            align="end"
            :cols="1"
          >
            <v-btn
              class="cm-bc-icon"
              depressed
              fab
              dark
              small
              color="primary"
            >
              <v-icon>
                mdi-magnify
              </v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </div>
    </v-col> -->
    <!-- 배너 사진 -->
    <BannerImage />
    <!-- 리스트 내용물 -->
    <div>
      <BoardComponent :board-type="index" :title="title[index-1]" />
    </div>
  </div>
</template>

<script>
import BannerImage from '@/components/Community/Banner.vue'
import BoardComponent from '@/components/Community/BoardComponent.vue'
export default {
  components: { BoardComponent, BannerImage },
  data () {
    return {
      tab: null,
      tabs: 4,
      title: ['전체글보기', '공지사항', 'FAQ', '1:1 문의'],
      index: 1
    }
  },
  methods: {
    changeTab (type) {
      this.index = type
    }
  }
}
</script>

<style scoped>
.body-container{
  width: 70%;
  margin-top: 5px;
  min-width: 500px;
}
ul {
  list-style:none;
  margin-left: 30px;
  margin-bottom : 10px;
  padding:0;
  font-size: 17px;
}

.index-hover{
  margin-right:20px;
  font-size: 1rem;
  font-weight: 600;
}
.index-hover:hover{
  border-bottom: 1px solid #ff5faa;
  cursor: pointer;
}
</style>
