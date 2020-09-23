<template>
  <div class="body-container">
    <!-- 타이틀 바 -->
    <v-row
      align="center"
      style="margin-left:5px;"
    >
      <v-col
        :cols="2"
      >
        <!-- 세로 -->
        <v-row
          align="center"
        >
          <span style="font-size:1.5rem; font-weight:800;">커뮤니티</span>
        </v-row>
      </v-col>
      <v-col>
        <ul>
          <li
            v-for="i in tabs"
            :key="i"
            @click="changeTab(i)"
          >
            <div
              class="index-hover"
            >
              {{ title[i-1] }}<div />
            </div>
          </li>
        </ul>
      </v-col>
    </v-row>
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
    background-color: #f3f3f3;
  margin-top: 20px;
  padding-left: 50px;
  padding-right: 50px;
  min-width: 500px;
}
ul {
  list-style:none;
  margin-left: 30px;
  margin-bottom : 10px;
  padding:0;
  font-size: 17px;
}

li {
  margin: 0;
  padding: 0;
  border : 0;
  float: left;
}
.index-hover{
  margin-right:20px;
  font-size: 1rem;
  font-weight: 600;
}
.index-hover:hover{
  color: #ff5faa;
  cursor: pointer;
  text-decoration: underline;
}

</style>
