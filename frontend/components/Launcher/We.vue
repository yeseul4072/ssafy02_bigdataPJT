<template>
  <div>
    <v-carousel
      cycle
      hide-delimiter-background
      show-arrows-on-hover
      delimiter-icon="mdi-minus"
      height="500"
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
            <div id="launcher_sub_title1">
              {{ item.mainTitle }}
            </div>
            <div id="launcher_sub_title2">
              {{ item.subTitle }}
            </div>
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
          src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
          mainTitle: 'mainTitle1',
          subTitle: 'subTitle1'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
          mainTitle: 'mainTitle2',
          subTitle: 'subTitle2'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
          mainTitle: 'mainTitle3',
          subTitle: 'subTitle3'
        }
      ]
    }
  }
}
</script>

<style>
#launcher_sub_title1{
  font-size: 3rem;
}
#launcher_sub_title2{
  text-align: center;
  font-size: 1rem;
}
</style>
