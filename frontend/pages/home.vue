<template>
  <div class="HomeWrapper">
    <search-bar />
    <div v-if="isLogin">
      로그인상태
    </div>
    <v-container fluid>
      <v-row no-gutters style="height:80vh;">
        <v-row style="width:100%;height:10%;">
          <v-col cols="12">
            <div style="font-size:2vw">
              이런 어린이집 어때요?
            </div>
          </v-col>
        </v-row>
        <v-row style="width:100%;height:5%;">
          <v-col cols="12">
            <div style="font-size:1.5vw">
              천사동에 3~4살 아기가 가장 많은 어린이집
            </div>
          </v-col>
        </v-row>
        <v-row style="width:100%;height:40;">
          <v-col cols="12">
            <kinder-box :kinders="kinders1" />
          </v-col>
        </v-row>
        <v-row style="width:100%;height:5%;">
          <v-col cols="12">
            <div style="font-size:1.5vw">
              천사동에 야간운영을 하는 어린이집
            </div>
          </v-col>
        </v-row>
        <v-row style="width:100%;height:40%;">
          <v-col cols="12">
            <kinder-box :kinders="kinders1" />
          </v-col>
        </v-row>
      </v-row>
      <v-row style="width:100%;height:25vh;" />
      <v-row style="height:80vh;">
        <v-col cols="6">
          <v-row style="height:10%;">
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
              컴포넌트
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="6">
          <v-row style="height:10%;">
            <v-col cols="12">
              <div style="font-size:2vw">
                지금 뜨는 리뷰
              </div>
            </v-col>
          </v-row>
          <v-row style="height:90%">
            <v-row style="width:100%;height:40%">
              <v-col cols="12">
                <kinder-box :kinders="kinders1" />
              </v-col>
            </v-row>
            <v-row style="width:10$" />
            <v-row style="width:100%;height:50%">
              <v-col cols="12">
                내용
              </v-col>
            </v-row>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import SearchBar from '@/components/Home/Search.vue'
import KinderBox from '@/components/Home/Kinder.vue'
export default {
  components: {
    SearchBar,
    KinderBox
  },
  data () {
    return {
      kinders1: [
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg'
        },
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg'
        },
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg'
        },
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg'
        },
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg'
        },
        {
          name: '대봉어린이집',
          tags: ['국공립', '야간연장', '방과후 통합', ' 안전교육', '통학차량', 'CCTV 운영'],
          url: 'kinder_temp.jpg'
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
          image_url: '@/assets/kinder_temp.jpg',
          title: '믿고 맡길 수 있는 어린이집',
          stars: 5,
          pros: '원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. 원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. 매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.',
          cons: '원장선생님이 교육에 대한 열의가 굉장하시다고 느꼈다. 원비 대비 하는 활동이나 교육프로그램이 많고 다양해서 아이가 항상 유치원 가기를 즐거워한다. 또한 현장학습이나 생일파티때 따로 음식을 준비하지 않아도 원에서 준비해 주신다. 매주 학습이 어떻게 이루어졌는지 그주의 활동을 정리해 보내주신다.'
        }
      ]
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
</style>
