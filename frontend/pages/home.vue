<template>
  <div class="HomeWrapper">
    <v-container fluid>
      <search-bar />
      <v-row no-gutters>
        <v-row style="width:100%;height:70px">
          <v-col cols="12">
            <div style="font-size:2vw">
              이런 어린이집 어때요?
            </div>
          </v-col>
        </v-row>
        <v-row style="width:100%;height:500px;margin-bottom:50px;">
          <v-col cols="12">
            <kinder-box :kinders="kinders1" class="card" title="천사동에 3~4살 아이가 가장 많은 어린이집" />
          </v-col>
        </v-row>
        <v-row style="width:100%;height:500px;">
          <v-col cols="12">
            <kinder-box :kinders="kinders1" class="card" title="천사동에 야간운영을 하는 어린이집" />
          </v-col>
        </v-row>
      </v-row>
      <v-row style="height:800px;margin-top:50px;">
        <v-col cols="6" style="height:100%">
          <div class="card" style="height:100%">
            <v-row>
              <v-col cols="12">
                <div style="font-size:2vw">
                  우리 아이
                </div>
              </v-col>
            </v-row>
            <v-row
              v-for="(item, index) in posts"
              :key="index"
              style="height:18%;"
            >
              <v-col cols="12">
                <post-box />
              </v-col>
            </v-row>
          </div>
        </v-col>
        <v-col cols="6" style="height:100%">
          <div class="card" style="height:100%">
            <v-row style="height:10%;">
              <v-col cols="12">
                <v-row>
                  <v-col cols="6" style="font-size:2vw;">
                    지금 뜨는 리뷰
                  </v-col>
                  <v-col cols="6" style="text-align:right">
                    <v-btn icon @click="changeReview(-1)">
                      <v-icon>fas fa-angle-left</v-icon>
                    </v-btn>
                    <v-btn icon @click="changeReview(1)">
                      <v-icon>fas fa-angle-right</v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
            <v-row style="height:90%">
              <review-box :review="reviews[reviewIdx]" />
            </v-row>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import SearchBar from '@/components/Home/Search.vue'
import KinderBox from '@/components/Home/Kinder.vue'
import PostBox from '@/components/Home/Post.vue'
import ReviewBox from '@/components/Home/Review.vue'
export default {
  components: {
    SearchBar,
    KinderBox,
    PostBox,
    ReviewBox
  },
  data () {
    return {
      kinders1: [
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', '안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          tel: '(02)3789-5971',
          stars: 4.3,
          grade: 'A',
          review_cnt: 120,
          distance: 1.5
        },
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', '안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          tel: '(02)3789-5971',
          stars: 4.3,
          grade: 'A',
          review_cnt: 120,
          distance: 2.2
        },
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', '안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          tel: '(02)3789-5971',
          stars: 4.3,
          grade: 'A',
          review_cnt: 120,
          distance: 3.3
        },
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', '안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          tel: '(02)3789-5971',
          stars: 4.3,
          grade: 'A',
          review_cnt: 120,
          distance: 1.2
        },
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', '안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          tel: '(02)3789-5971',
          stars: 4.3,
          grade: 'A',
          review_cnt: 120,
          distance: 1.5
        },
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          tel: '(02)3789-5971',
          stars: 4.3,
          grade: 'A',
          review_cnt: 120,
          distance: 1.7
        }
      ],
      kinders2: [

      ],
      posts: [
        {
          title: '오늘은 날이 좋더라구요',
          user: {
            name: '우승아빠'
          },
          viewcnt: 266,
          likecnt: 50
        },
        {
          title: '오늘은 날이 좋더라구요',
          user: {
            name: '우승아빠'
          },
          viewcnt: 266,
          likecnt: 50
        }, {
          title: '오늘은 날이 좋더라구요',
          user: {
            name: '우승아빠'
          },
          viewcnt: 266,
          likecnt: 50
        },
        {
          title: '오늘은 날이 좋더라구요',
          user: {
            name: '우승아빠'
          },
          viewcnt: 266,
          likecnt: 50
        },
        {
          title: '오늘은 날이 좋더라구요',
          user: {
            name: '우승아빠'
          },
          viewcnt: 266,
          likecnt: 50
        }

      ],
      reviews: [
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          title: '믿고 맡길 수 있는 어린이집',
          stars: 5,
          pros: '1원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.',
          cons: '1원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.'
        },
        {
          name: '둘리어린이집',
          tags: ['국공립', '방과후 통합', '야간연장', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          title: '사건사고 많은 어린이집',
          stars: 2,
          pros: '2원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.',
          cons: '2원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.'
        },
        {
          name: '포차어린이집',
          tags: ['국공립', '방과후 통합', '야간연장', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          title: '원장선생님이 술마시다 걸림',
          stars: 1,
          pros: '3원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.',
          cons: '3원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.'
        },
        {
          name: '바둑어린이집',
          tags: ['국공립', '방과후 통합', '야간연장', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg',
          title: '세상에 이런 어린이집이?',
          stars: 4.5,
          pros: '4원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.',
          cons: '4원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. \n원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. \n매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.'
        }
      ],
      reviewIdx: 0
    }
  },
  computed: {
    ...mapGetters(['isLogin'])
  },
  watch: {

  },
  methods: {
    changelogin () {
      const cur = this.$store.state.User.isLogin
      this.$store.commit('setIsLogin', !cur)
    },
    changeReview (num) {
      const len = this.reviews.length
      this.reviewIdx = ((this.reviewIdx + num) + len) % len
    }
  }
}
</script>

<style scoed>
.HomeWrapper{
  margin: 0 8vw;
  font-weight: 600;
  font-size: 1.2vw;
  }
.card{
  border-radius: 4px;
  padding: 15px;
  border : thin solid #E6E6E6;
}
</style>
