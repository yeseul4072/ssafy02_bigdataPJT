<template>
  <div>
    <!-- 배너 사진 -->
    <BannerImage />
    <!-- 리스트 내용물 -->
    <div>
      <BoardComponent :board-type="index" :title="title" :articles="articles" />
    </div>
  </div>
</template>

<script>
import http from '@/util/http_common.js'
import BannerImage from '@/components/Community/Banner.vue'
import BoardComponent from '@/components/Community/BoardComponent.vue'
export default {
  components: { BoardComponent, BannerImage },
  asyncData ({ params }) {
    return http.axios.get(`/community/${params.id}/article/`)
      .then(({ data }) => {
        console.log(data)
        return {
          index: 10,
          title: '게시물 이름',
          articles: data
        }
      })
  },
  validate ({ params }) {
    // validation 체크 파라미터 값이 숫자가 아니면 page falut 에러 반환하게
    return /^\d+$/.test(params.id)
  },
  data () {
    return {
    }
  },
  mounted () {

  },
  methods: {

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
