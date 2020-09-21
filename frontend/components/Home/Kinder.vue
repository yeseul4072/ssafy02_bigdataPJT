<template>
  <v-carousel
    cycle
    hide-delimiters
    show-arrows-on-hover
    delimiter-icon="mdi-minus"
    height="40vh"
  >
    <v-carousel-item
      v-for="(kinder, i) in kinders"
      :key="i"
    >
      <v-sheet
        color="white"
        light
        height="100%"
      >
        <v-row style="height:100%;">
          <v-col cols="4">
            <!-- <v-img :src="require('@/assets/kinder_temp.jpg')" /> -->
            <v-img style="height:100%;border-radius: 7px;-moz-border-radius: 7px;-khtml-border-radius: 7px;-webkit-border-radius: 7px;" :src="require('../../assets/'+kinder.url)" />
          </v-col>
          <v-col cols="2">
            <v-row>
              <div style="width:100%;font-size:2vh;padding-left:6px;">
                {{ kinder.name }}
              </div>
            </v-row>
            <v-row
              v-for="(tag, i) in kinder.tags"
              :key="i"
            >
              <div style="width:100%;">
                <v-chip
                  class="ma-2"
                  color="#F781F3"
                  outlined
                >
                  <v-icon left>
                    mdi-server-plus
                  </v-icon>
                  {{ tag }}
                </v-chip>
              </div>
            </v-row>
          </v-col>
          <v-col cols="4">
            <v-img style="height:100%;border-radius: 7px;-moz-border-radius: 7px;-khtml-border-radius: 7px;-webkit-border-radius: 7px;" :src="require('../../assets/'+kinder.url)" />
          </v-col>
          <v-col cols="2">
            <v-row>
              <div style="width:100%;font-size:2vh;padding-left:6px;">
                {{ kinder.name }}
              </div>
            </v-row>
            <v-row
              v-for="(tag, i) in kinder.tags"
              :key="i"
            >
              <div style="width:100%;">
                <v-chip
                  class="ma-2"
                  color="#F781F3"
                  outlined
                >
                  <v-icon left>
                    mdi-server-plus
                  </v-icon>
                  {{ tag }}
                </v-chip>
              </div>
            </v-row>
          </v-col>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  props: {
    kinders: {
      type: Array,
      default () {
        return []
      }
    }
  },
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

<style>

</style>
