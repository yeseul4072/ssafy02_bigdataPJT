<template>
  <v-carousel
    cycle
    hide-delimiters
    show-arrows-on-hover
    delimiter-icon="mdi-minus"
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
            x-small
            color="#f7d64d"
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
                <v-row>
                  <v-img style="border-radius: 7px;-moz-border-radius: 7px;-khtml-border-radius: 7px;-webkit-border-radius: 7px;" :src="require('../../assets/'+kinder.url)" />
                </v-row>
                <v-row>
                  <div style="width:100%;font-size:2vh;padding-left:6px;margin-top:15px; margin-bottom:5px;">
                    {{ kinder.name }}
                  </div>
                </v-row>
                <v-row>
                  <v-chip
                    v-for="(tag, i) in kinder.tags"
                    :key="i"
                    class="ma-1"
                    color="#ff9800"
                    text-color="#black"
                    outlined
                  >
                    <v-icon color="#ff9800" left>
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
                <v-row>
                  <v-img style="max-width:50%;border-radius: 7px;-moz-border-radius: 7px;-khtml-border-radius: 7px;-webkit-border-radius: 7px;" :src="require('../../assets/'+kinder.url)" />
                </v-row>
                <v-row>
                  <div style="width:100%;font-size:2vh;padding-left:6px;margin-top:15px; margin-bottom:5px;">
                    {{ kinder.name }}
                  </div>
                </v-row>
                <v-row>
                  <v-chip
                    v-for="(tag, i) in kinder.tags"
                    :key="i"
                    class="ma-1"
                    color="#ff9800"
                    text-color="#black"
                    outlined
                  >
                    <v-icon color="#ff9800" left>
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

  }
}
</script>

<style scoped>

</style>
