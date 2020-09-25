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
                <v-row style="height:60%">
                  <v-img style="height:100%;border-radius: 7px;-moz-border-radius: 7px;-khtml-border-radius: 7px;-webkit-border-radius: 7px;" :src="require('../../assets/'+kinder.url)" />
                </v-row>
                <v-row :align="center">
                  <span style="font-size:1.8vw;font-wight:800;padding-left:6px;margin-top:15px; margin-bottom:5px;">
                    {{ kinder.name }}
                  </span>
                  &nbsp;&nbsp;
                  <span style="font-size:0.8vw;padding-left:6px;margin-top:27px;">
                    <span> {{ kinder.distance }} </span> Km
                    <i style="color:#DEDEDE" class="fas fas fa-ellipsis-v" />

                    <span style="font-size:1.1vw;font-weight:800;">{{ kinder.stars }}</span>/5
                    <v-rating
                      :value="kinder.stars"
                      color="orange"
                      background-color="orange lighten-3"
                      dense
                      half-increments
                      readonly
                      size="1.0vw"
                      style="display:inline-block;"
                    />
                    <i style="color:#DEDEDE" class="fas fa-ellipsis-v" />

                    <a>전체리뷰 <span>{{ kinder.review_cnt }}</span></a>
                    <!-- <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="8"
                      height="19"
                      viewBox="0 0 8 19"
                      class="aW-AU"
                      role="presentation"
                    ><path d="M4.8 15.89a10.68 10.68 0 0 1-.05-.05l.05.05zm-1.14-1.93c-.25-.54-.48-1.12-.68-1.75a.3.3 0 0 0 .12-.04c.78-.48 1.41-1.01 1.6-1.55.2-.54.03-1.33-.29-2.16a.31.31 0 0 0-.46-.14c-.66.4-1.2.85-1.47 1.3 0-.34-.04-.65-.15-.89-.01-.55.03-1.07.12-1.57.87.1 1.68.06 2.16-.23.47-.29.87-.99 1.18-1.81a.2.2 0 0 0-.17-.26c-.88-.1-1.7-.06-2.18.23l-.03-.04.03.04c-.2.12-.4.33-.58.59a7.65 7.65 0 0 1 1.39-2.25l.28.02.5.03c.38 0 .67-.08.9-.28A4.8 4.8 0 0 0 7 .9a.2.2 0 0 0-.2-.2c-.7-.01-1.97.33-2.43.71-.24.21-.36.51-.4.96l-.02.4c0 .22-.01.33-.03.44a8.13 8.13 0 0 0-.96 1.35c0-.1 0-.19-.03-.27-.11-.5-.62-1.07-1.27-1.6a.18.18 0 0 0-.28.07C1 3.5.78 4.23.9 4.73c.1.5.62 1.07 1.27 1.58a.2.2 0 0 0 .05.03 8.22 8.22 0 0 0-.29 1.87 5.53 5.53 0 0 0-1.47-.89c-.13-.06-.27.01-.3.14-.2.87-.23 1.68.03 2.17l-.05.02.05-.02c.26.5.97.96 1.83 1.33.06.03.14.02.2 0l.02.11c.2.84.45 1.6.74 2.31a4.77 4.77 0 0 0-2.38-.11c-.16.02-.26.17-.2.3.33.92.79 1.7 1.33 2l-.02.05.02-.05c.54.31 1.46.33 2.47.18l.22.32c.63.87 1.3 1.55 1.98 2.04a5.8 5.8 0 0 0 .66.42 2 2 0 0 0 .3.14c.17.03.3.03.4-.02.24-.13.32-.45.16-.72-.1-.17-.3-.32-.7-.56l-.5-.3a12.12 12.12 0 0 1-.72-.46.21.21 0 0 0 .02-.03c.45-.92.7-1.8.56-2.4-.14-.6-.78-1.25-1.6-1.85a.2.2 0 0 0-.3.09 4.6 4.6 0 0 0-.58 2.25 4.23 4.23 0 0 0-.44-.71z" /></svg>
                    <span style="color:#2adba3;">평가등급 : {{ kinder.grade }}</span>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="8"
                      height="19"
                      viewBox="0 0 8 19"
                      class="_1KCw5"
                      role="presentation"
                    ><path d="M4.8 15.89a10.68 10.68 0 0 1-.05-.05l.05.05zm-1.14-1.93c-.25-.54-.48-1.12-.68-1.75a.3.3 0 0 0 .12-.04c.78-.48 1.41-1.01 1.6-1.55.2-.54.03-1.33-.29-2.16a.31.31 0 0 0-.46-.14c-.66.4-1.2.85-1.47 1.3 0-.34-.04-.65-.15-.89-.01-.55.03-1.07.12-1.57.87.1 1.68.06 2.16-.23.47-.29.87-.99 1.18-1.81a.2.2 0 0 0-.17-.26c-.88-.1-1.7-.06-2.18.23l-.03-.04.03.04c-.2.12-.4.33-.58.59a7.65 7.65 0 0 1 1.39-2.25l.28.02.5.03c.38 0 .67-.08.9-.28A4.8 4.8 0 0 0 7 .9a.2.2 0 0 0-.2-.2c-.7-.01-1.97.33-2.43.71-.24.21-.36.51-.4.96l-.02.4c0 .22-.01.33-.03.44a8.13 8.13 0 0 0-.96 1.35c0-.1 0-.19-.03-.27-.11-.5-.62-1.07-1.27-1.6a.18.18 0 0 0-.28.07C1 3.5.78 4.23.9 4.73c.1.5.62 1.07 1.27 1.58a.2.2 0 0 0 .05.03 8.22 8.22 0 0 0-.29 1.87 5.53 5.53 0 0 0-1.47-.89c-.13-.06-.27.01-.3.14-.2.87-.23 1.68.03 2.17l-.05.02.05-.02c.26.5.97.96 1.83 1.33.06.03.14.02.2 0l.02.11c.2.84.45 1.6.74 2.31a4.77 4.77 0 0 0-2.38-.11c-.16.02-.26.17-.2.3.33.92.79 1.7 1.33 2l-.02.05.02-.05c.54.31 1.46.33 2.47.18l.22.32c.63.87 1.3 1.55 1.98 2.04a5.8 5.8 0 0 0 .66.42 2 2 0 0 0 .3.14c.17.03.3.03.4-.02.24-.13.32-.45.16-.72-.1-.17-.3-.32-.7-.56l-.5-.3a12.12 12.12 0 0 1-.72-.46.21.21 0 0 0 .02-.03c.45-.92.7-1.8.56-2.4-.14-.6-.78-1.25-1.6-1.85a.2.2 0 0 0-.3.09 4.6 4.6 0 0 0-.58 2.25 4.23 4.23 0 0 0-.44-.71z" /></svg> -->
                  </span>
                </v-row>
                <v-row>
                  <v-chip
                    v-for="(tag, i) in kinder.tags"
                    :key="i"
                    class="ma-1"
                    color="#ff9800"
                    text-color="#black"
                    outlined
                    small
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
                <v-row style="height:60%">
                  <v-img style="height:100%;border-radius: 7px;-moz-border-radius: 7px;-khtml-border-radius: 7px;-webkit-border-radius: 7px;" :src="require('../../assets/'+kinder.url)" />
                </v-row>
                <v-row :align="center">
                  <span style="font-size:1.8vw;font-wight:800;padding-left:6px;margin-top:15px; margin-bottom:5px;">
                    {{ kinder.name }}
                  </span>
                  &nbsp;&nbsp;
                  <span style="font-size:0.8vw;padding-left:6px;margin-top:27px;">
                    <span> {{ kinder.distance }} </span> Km
                    <i style="color:#DEDEDE" class="fas fas fa-ellipsis-v" />

                    <span style="font-size:1.1vw;font-weight:800;">{{ kinder.stars }}</span>/5
                    <v-rating
                      :value="kinder.stars"
                      color="orange"
                      background-color="orange lighten-3"
                      dense
                      half-increments
                      readonly
                      size="1.0vw"
                      style="display:inline-block;"
                    />
                    <i style="color:#DEDEDE" class="fas fa-ellipsis-v" />

                    <a>전체리뷰 <span>{{ kinder.review_cnt }}</span></a>
                    <!-- <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="8"
                      height="19"
                      viewBox="0 0 8 19"
                      class="aW-AU"
                      role="presentation"
                    ><path d="M4.8 15.89a10.68 10.68 0 0 1-.05-.05l.05.05zm-1.14-1.93c-.25-.54-.48-1.12-.68-1.75a.3.3 0 0 0 .12-.04c.78-.48 1.41-1.01 1.6-1.55.2-.54.03-1.33-.29-2.16a.31.31 0 0 0-.46-.14c-.66.4-1.2.85-1.47 1.3 0-.34-.04-.65-.15-.89-.01-.55.03-1.07.12-1.57.87.1 1.68.06 2.16-.23.47-.29.87-.99 1.18-1.81a.2.2 0 0 0-.17-.26c-.88-.1-1.7-.06-2.18.23l-.03-.04.03.04c-.2.12-.4.33-.58.59a7.65 7.65 0 0 1 1.39-2.25l.28.02.5.03c.38 0 .67-.08.9-.28A4.8 4.8 0 0 0 7 .9a.2.2 0 0 0-.2-.2c-.7-.01-1.97.33-2.43.71-.24.21-.36.51-.4.96l-.02.4c0 .22-.01.33-.03.44a8.13 8.13 0 0 0-.96 1.35c0-.1 0-.19-.03-.27-.11-.5-.62-1.07-1.27-1.6a.18.18 0 0 0-.28.07C1 3.5.78 4.23.9 4.73c.1.5.62 1.07 1.27 1.58a.2.2 0 0 0 .05.03 8.22 8.22 0 0 0-.29 1.87 5.53 5.53 0 0 0-1.47-.89c-.13-.06-.27.01-.3.14-.2.87-.23 1.68.03 2.17l-.05.02.05-.02c.26.5.97.96 1.83 1.33.06.03.14.02.2 0l.02.11c.2.84.45 1.6.74 2.31a4.77 4.77 0 0 0-2.38-.11c-.16.02-.26.17-.2.3.33.92.79 1.7 1.33 2l-.02.05.02-.05c.54.31 1.46.33 2.47.18l.22.32c.63.87 1.3 1.55 1.98 2.04a5.8 5.8 0 0 0 .66.42 2 2 0 0 0 .3.14c.17.03.3.03.4-.02.24-.13.32-.45.16-.72-.1-.17-.3-.32-.7-.56l-.5-.3a12.12 12.12 0 0 1-.72-.46.21.21 0 0 0 .02-.03c.45-.92.7-1.8.56-2.4-.14-.6-.78-1.25-1.6-1.85a.2.2 0 0 0-.3.09 4.6 4.6 0 0 0-.58 2.25 4.23 4.23 0 0 0-.44-.71z" /></svg>
                    <span style="color:#2adba3;">평가등급 : {{ kinder.grade }}</span>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="8"
                      height="19"
                      viewBox="0 0 8 19"
                      class="_1KCw5"
                      role="presentation"
                    ><path d="M4.8 15.89a10.68 10.68 0 0 1-.05-.05l.05.05zm-1.14-1.93c-.25-.54-.48-1.12-.68-1.75a.3.3 0 0 0 .12-.04c.78-.48 1.41-1.01 1.6-1.55.2-.54.03-1.33-.29-2.16a.31.31 0 0 0-.46-.14c-.66.4-1.2.85-1.47 1.3 0-.34-.04-.65-.15-.89-.01-.55.03-1.07.12-1.57.87.1 1.68.06 2.16-.23.47-.29.87-.99 1.18-1.81a.2.2 0 0 0-.17-.26c-.88-.1-1.7-.06-2.18.23l-.03-.04.03.04c-.2.12-.4.33-.58.59a7.65 7.65 0 0 1 1.39-2.25l.28.02.5.03c.38 0 .67-.08.9-.28A4.8 4.8 0 0 0 7 .9a.2.2 0 0 0-.2-.2c-.7-.01-1.97.33-2.43.71-.24.21-.36.51-.4.96l-.02.4c0 .22-.01.33-.03.44a8.13 8.13 0 0 0-.96 1.35c0-.1 0-.19-.03-.27-.11-.5-.62-1.07-1.27-1.6a.18.18 0 0 0-.28.07C1 3.5.78 4.23.9 4.73c.1.5.62 1.07 1.27 1.58a.2.2 0 0 0 .05.03 8.22 8.22 0 0 0-.29 1.87 5.53 5.53 0 0 0-1.47-.89c-.13-.06-.27.01-.3.14-.2.87-.23 1.68.03 2.17l-.05.02.05-.02c.26.5.97.96 1.83 1.33.06.03.14.02.2 0l.02.11c.2.84.45 1.6.74 2.31a4.77 4.77 0 0 0-2.38-.11c-.16.02-.26.17-.2.3.33.92.79 1.7 1.33 2l-.02.05.02-.05c.54.31 1.46.33 2.47.18l.22.32c.63.87 1.3 1.55 1.98 2.04a5.8 5.8 0 0 0 .66.42 2 2 0 0 0 .3.14c.17.03.3.03.4-.02.24-.13.32-.45.16-.72-.1-.17-.3-.32-.7-.56l-.5-.3a12.12 12.12 0 0 1-.72-.46.21.21 0 0 0 .02-.03c.45-.92.7-1.8.56-2.4-.14-.6-.78-1.25-1.6-1.85a.2.2 0 0 0-.3.09 4.6 4.6 0 0 0-.58 2.25 4.23 4.23 0 0 0-.44-.71z" /></svg> -->
                  </span>
                </v-row>
                <v-row>
                  <v-chip
                    v-for="(tag, i) in kinder.tags"
                    :key="i"
                    class="ma-1"
                    color="#ff9800"
                    text-color="#black"
                    outlined
                    small
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
._1KCw5 {
    fill: #2adba3;
    margin-right: 5px ;
    transform: scaleX(-1);

}
.aW-AU {
    fill: #2adba3;
    margin-left: 5px;
}
</style>
