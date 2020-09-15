<template>
  <div>
    <v-carousel
      cycle
      hide-delimiter-background
      show-arrows-on-hover
      delimiter-icon="mdi-minus"
      height="600"
    >
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
      >
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <div>
            <div id="launcher_sub_title1" v-html="item.mainTitle" />
            <div id="launcher_sub_title2" v-html="item.subTitle" />
          </div>
        </v-row>
      </v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
export default {
  data () {
    return {
      items: [
        {
          src: 'https://drscdn.500px.org/photo/230496623/q%3D80_m%3D2000_k%3D1/v2?sig=e8c3249d5d980df53d985511f65d7624ed39d3f2f3c0404d6c78fdf18ee482a9',
          mainTitle: 'No.1 어린이집 추천 플랫폼, 어린이ZIP',
          subTitle: '보건복지부, 한국사회보장정보원에서 제공하는 정보로<br>우리 아이 어린이집 한눈에!'
        },
        {
          src: 'https://images.unsplash.com/photo-1559251606-c623743a6d76?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80',
          mainTitle: '어린이집, 헤매지 말고 어린이ZIP하자!',
          subTitle: '어린이집 정보를 찾고, 알아보기 위해<br>아직도 헤매고 있지 않나요?'
        },
        {
          src: 'https://drscdn.500px.org/photo/88868969/q%3D80_m%3D2000/v2?sig=5dc5a8d0b90ceb70ff06c7f73f669a0cc2272ee3112921fe8eeed44d22c15fa0',
          mainTitle: '어린이집 추천 플랫폼 1위<br>지금까지 이런 플랫폼은 없었다',
          subTitle: '대한민국 모든 부모님들이 선택한<br>어린이집 추천 플랫폼 어린이ZIP을 만나보세요!'
        }
      ]
    }
  }
}
</script>

<style>
#launcher_sub_title1{
  text-align: center;
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 15px;
}
#launcher_sub_title2{
  text-align: center;
  font-weight: 100;
  font-size: 1.3rem;
  margin-top: 15px;
}
</style>
