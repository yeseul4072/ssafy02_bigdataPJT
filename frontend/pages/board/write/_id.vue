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
        <v-row
          class="pt-3 pl-8"
          align="center"
          justify="center"
        >
          <v-col>
            <h2>게시판 분류</h2>
            <div class="border_gray pt-3 mr-8" />
          </v-col>
        </v-row>
        <div
          class="pt-3 pl-8"
        >
          <h3>
            제목
          </h3>
        </div>
        <div
          class="pl-8 pr-8"
        >
          <v-text-field
            class="pa-0"
            :rules="rules"
            hide-details="auto"
          />
        </div>
        <div
          class="pt-10 pl-8"
        >
          <h3>
            내용
          </h3>
        </div>
        <div
          class="pl-8 pr-8 pt-0 pb-4"
        >
          <v-card
            class="pl-3 pt-1"
            outlined
            rounded="0"
            :min-width="500"
          >
            <v-textarea
              class="mb-3"
              rows="1"
              flat
              solo
              no-resize
              height="300"
              label="이 곳에 작성해주세요 :D"
              hide-details
            />
          </v-card>
        </div>
        <v-row
          class="pl-11 pr-11 pt-0 pb-8"
        >
          <v-col
            class="pa-0"
          >
            <v-btn depressed>
              작성 취소
            </v-btn>
          </v-col>
          <v-col
            class="pa-0"
            align="end"
          >
            <v-btn
              depressed
              color="#2adba3"
            >
              작성 완료
            </v-btn>
          </v-col>
        </v-row>
      </v-card>
    </div>
  </div>
</template>

<script>
import BannerImage from '@/components/Community/Banner.vue'

export default {
  components: { BannerImage },
  data () {
    return {
      rules: [
        value => !!value || '필수로 입력해야합니다.'
      ]
    }
  }
}
</script>

<style scoped>
.border_gray{
  border-bottom: 1px solid rgb(236, 236, 236);
}
</style>
