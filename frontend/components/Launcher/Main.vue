<template>
  <div class="l4_main">
    <div>
      <div class="display-2" style="margin-bottom: 20px;">
        <p class="dp-2">
          No.1 어린이집 추천 플랫폼, 어린이ZIP
        </p>
      </div>
      <div style="text-align:center; margin-top: 20px;">
        <div class="text-center">
          <v-btn
            x-large
            :rounded="true"
            :outlined="true"
            :min-width="250"
          >
            <nuxt-link to="/Home" style="color:black; text-decoration: none;">
              지금 시작해 보세요 :)
            </nuxt-link>
          </v-btn>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {

  }
}
</script>

<style scoped>
.l4_main{
  display: flex;
  align-items: center;
  justify-content: center;
  width:100%;
  height:400px;
}

.dp-2{
  color: #F257A0;
}

.dp-1{
  font-size:17px;
}
</style>
