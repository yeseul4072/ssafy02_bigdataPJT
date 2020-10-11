<template>
  <v-carousel
    cycle
    hide-delimiters
    show-arrows-on-hover
    delimiter-icon="mdi-minus"
    style="height:95%;"
  >
    <v-carousel-item
      v-for="(kinder, i) in kinders"
      :key="i"
    >
      <v-sheet
        color="white"
        light
      >
        <div style="font-size:1.5vw">
          <v-btn
            class="mx-2"
            fab
            dark
            depressed
            x-small
            color="#0CC476"
            style="pointer-events: none !important;"
          >
            <v-icon>
              fas fa-angle-right
            </v-icon>
          </v-btn>
          {{ title }}
        </div>
        <v-row>
          <v-col cols="6">
            <v-row>
              <v-col cols="12" style="padding:30px;">
                <v-row style="height:300px;">
                  <v-img class="cursor" style="height:100%;border-radius: 7px;-moz-border-radius: 7px;-khtml-border-radius: 7px;-webkit-border-radius: 7px;" :src="kinder.left.image" @click="linkKinder(kinder.left.id)" />
                </v-row>
                <v-row align="center">
                  <span class="mt-4 mb-1" style="font-size:1.5vw;font-wight:800;padding-left:6px">
                    {{ kinder.left.organization_name }}
                  </span>
                  &nbsp;&nbsp;
                  <span style="font-size:0.8vw;padding-left:6px;margin-top:15px;">
                    <i style="color:orange" class="fas fa-star" />
                    <span style="font-size:1.1vw;font-weight:800;">{{ kinder.left.score_avg.toFixed(1) }}</span>
                    <i style="color:#DEDEDE" class="fas fas fa-ellipsis-v" />
                    <span> {{ kinder.left.distance }} </span> Km
                    <i style="color:#DEDEDE" class="fas fa-ellipsis-v" />

                    <nuxt-link :to="'/kinder/'+1">전체리뷰 <span>{{ kinder.left.reviews_count }}</span></nuxt-link>
                  </span>
                </v-row>
                <v-row style="height:68px; overflow:hidden;">
                  <v-chip
                    v-for="(tag, i) in kinder.left.tags"
                    :key="i"
                    class="ma-1"
                    color="green accent-4"
                    text-color="#black"
                    outlined
                    small
                  >
                    <v-icon color="green accent-4" left>
                      mdi-server-plus
                    </v-icon>
                    {{ tag }}
                  </v-chip>
                </v-row>
              </v-col>
            </v-row>
          </v-col>
          <v-col cols="6">
            <v-row>
              <v-col cols="12" style="padding:30px;">
                <v-row style="height:300px;">
                  <v-img class="cursor" style="height:100%;border-radius: 7px;-moz-border-radius: 7px;-khtml-border-radius: 7px;-webkit-border-radius: 7px;" :src="kinder.right.image" @click="linkKinder(kinder.right.id)" />
                </v-row>
                <v-row align="center">
                  <span style="font-size:1.5vw;font-wight:800;padding-left:6px;margin-top:15px; margin-bottom:5px;">
                    {{ kinder.right.organization_name }}
                  </span>
                  &nbsp;&nbsp;
                  <span style="font-size:0.8vw;padding-left:6px;margin-top:15px;">
                    <i style="color:orange" class="fas fa-star" />
                    <span style="font-size:1.1vw;font-weight:800;">{{ kinder.right.score_avg.toFixed(1) }}</span>
                    <i style="color:#DEDEDE" class="fas fas fa-ellipsis-v" />
                    <span> {{ kinder.right.distance }} </span> Km
                    <i style="color:#DEDEDE" class="fas fa-ellipsis-v" />

                    <a>전체리뷰 <span>{{ kinder.right.reviews_count }}</span></a>
                  </span>
                </v-row>
                <v-row style="height:68px; overflow:hidden;">
                  <v-chip
                    v-for="(tag, i) in kinder.right.tags"
                    :key="i"
                    class="ma-1"
                    color="green accent-4"
                    text-color="#black"
                    outlined
                    small
                  >
                    <v-icon color="green accent-4" left>
                      mdi-server-plus
                    </v-icon>
                    {{ tag }}
                  </v-chip>
                </v-row>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  props: ['kinders', 'title'],
  data () {
    return {
      slides: [
        'First',
        'Second',
        'Third',
        'Fourth',
        'Fifth'
      ],
      colors: [
        'indigo',
        'warning',
        'pink darken-2',
        'red lighten-1',
        'deep-purple accent-4'
      ]
    }
  },
  methods: {
    linkKinder (id) {
      this.$router.push('/kinder/' + id)
    }
  }
}
</script>

<style scoped>
._1KCw5 {
    fill: #2adba3;
    margin-right: 5px ;
    transform: scaleX(-1);

}
.aW-AU {
    fill: #2adba3;
    margin-left: 5px;
}
.cursor {
  cursor: pointer;
}
a {
  text-decoration: none;
}
</style>
