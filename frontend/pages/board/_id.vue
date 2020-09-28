<template>
  <div>
    <!-- 배너 사진 -->
    <BannerImage />

    <!-- 내용물 -->
    <div class="container">
      <v-card
        outlined
        rounded="0"
        :min-width="500"
      >
        <v-list-item>
          <v-row
            justify="center"
            class="pa-5"
          >
            <v-col
              class="py-0"
              :cols="6"
            >
              <v-list-item-title class="headline" style="font-weight:800;">
                게시판 이름
              </v-list-item-title>
            </v-col>
            <v-col
              class="py-0"
              :cols="6"
            >
              <v-row
                align="end"
                justify="end"
                class="pr-3"
              >
                <div>
                  게시판 글쓰기 버튼 들어갈 자리
                </div>
              </v-row>
            </v-col>
            <div class="border_black py-2" />
          </v-row>
        </v-list-item>
        <v-list-item class="px-10">
          <v-list-item-content class="pa-0">
            <v-list-item-title><h3>제목</h3></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item class="px-8">
          <v-list-item-avatar>
            <v-img
              :src="'https://www.iconfinder.com/data/icons/female-avatars-vol-1/256/female-portrait-avatar-profile-woman-sexy-afro-2-512.png'"
            />
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title>유저 이름</v-list-item-title>
          </v-list-item-content>
          <v-list-item-icon class="pr-1">
            조회 7 | 추천 | 2020.09.28 05:07
          </v-list-item-icon>
        </v-list-item>
        <v-row>
          <v-col
            align="center"
            class="pa-0"
          >
            <div class="border_gray" />
          </v-col>
        </v-row>
        <v-row class="px-9 pa-3">
          <v-col>
            내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용내용
          </v-col>
        </v-row>
        <v-list-item class="px-8">
          <v-btn
            small
            rounded
            outlined
            color="rgb(236, 236, 236)"
            dark
          >
            <span
              style="color:#212121;"
            >
              목록보기
            </span>
          </v-btn>
          <v-list-item-content />
          <v-list-item-icon class="pr-1">
            <v-btn
              rounded
              outlined
              color="rgb(236, 236, 236)"
              dark
            >
              <v-icon
                class="mr-2"
                color="rgb(143, 143, 143)"
                dark
                style="font-size:20px;"
              >
                mdi-thumb-up-outline
              </v-icon>
              <span
                style="color:#212121;"
              >
                0
              </span>
            </v-btn>
          </v-list-item-icon>
        </v-list-item>
        <v-list-item class="px-10">
          <v-list-item-content class="pa-0">
            <v-list-item-title>
              <v-icon
                style="font-size:18px;"
              >
                mdi-comment-outline
              </v-icon><span style="font-size:16px; font-weight:700;">&nbsp;댓글 <span style="font-size:16px; color:orange;">1</span>개</span>
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-row>
          <v-col
            align="center"
            class="pa-0"
          >
            <div class="border_gray" />
          </v-col>
        </v-row>
        <div class="pa-8">
          <Review />
          <Review />
          <Review />
        </div>
        <v-row>
          <v-col
            align="center"
            class="pa-0"
          >
            <div class="border_gray" />
          </v-col>
        </v-row>
        <div
          class="pa-8"
        >
          <v-card
            outlined
            rounded="0"
            :min-width="500"
          >
            <v-list-item class="px-4 pt-2">
              <v-list-item-avatar>
                <v-img
                  :src="'https://www.iconfinder.com/data/icons/female-avatars-vol-1/256/female-portrait-avatar-profile-woman-sexy-afro-2-512.png'"
                />
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title><h4>유저 이름</h4></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-textarea
              class="px-4 ma-0"
              rows="1"
              flat
              solo
              no-resize
              height="100"
              label="이 곳에 작성해주세요 :D"
              hide-details
            />
            <v-list-item class="px-8">
              <span
                style="color:orange;"
              >
                주제와 무관한 댓글, 악플은 삭제 될 수 있습니다.
              </span>
              <v-list-item-content />
              <v-list-item-icon class="pr-1">
                <v-btn
                  rounded
                  outlined
                  color="rgb(236, 236, 236)"
                  dark
                >
                  <span
                    style="color:#212121;"
                  >
                    등록
                  </span>
                </v-btn>
              </v-list-item-icon>
            </v-list-item>
          </v-card>
        </div>
      </v-card>
    </div>
  </div>
</template>

<script>
import BannerImage from '@/components/Community/Banner.vue'
import Review from '@/components/Community/Review.vue'

export default {
  components: { BannerImage, Review }

}
</script>

<style scoped>
.border_black{
  width: 98%;
  border-bottom: 1px solid;
}

.border_gray{
  width: 92%;
  border-bottom: 1px solid rgb(236, 236, 236);
}

</style>
