<template>
  <v-col cols="12">
    <v-card
      style="width:100%;height:100%;"
    >
      <v-card-title style="height:40%">
        <v-row style="width:100%;height:200px;overflow: hidden;">
          <v-col cols="6">
            <v-img class="cursor" style="height:176px;border-radius: 7px;-moz-border-radius: 7px;-khtml-border-radius: 7px;-webkit-border-radius: 7px;" :src="review.kindergarten.image_url" @click="linkKinder" />
          </v-col>
          <v-col cols="6" style="padding-left:0;">
            <v-row style="font-weight:800;">
              &nbsp;&nbsp;&nbsp;{{ review.kindergarten.organization_name }}
            </v-row>
            <v-chip
              v-for="(tag, i) in review.tags"
              :key="i"
              class="ma-1"
              color="green accent-4"
              text-color="black"
              outlined
              small
            >
              <v-icon color="green accent-4" left x-small>
                mdi-server-plus
              </v-icon>
              {{ tag }}
            </v-chip>
          </v-col>
        </v-row>
        <v-row style="width:100%;height:10%;font-weight:800;">
          &nbsp;"{{ review.title }}"
          &nbsp;
          <v-rating
            :value="review.avg_score"
            color="orange"
            background-color="orange lighten-3"
            dense
            half-increments
            readonly
            size="14"
          />
        </v-row>
      </v-card-title>

      <v-divider />

      <v-card-title style="height:10%">
        <v-chip class="success white--text">
          장점
        </v-chip>
      </v-card-title>

      <v-card-text style="height:13vh;overflow:hidden;">
        <!-- https://www.npmjs.com/package/vue-line-clamp -->
        <div v-html="review.pros.replace(/(?:\r\n|\r|\n)/g, '<br />')" />
      </v-card-text>
      <v-divider />
      <v-card-title style="height:10%">
        <v-chip class="pink white--text">
          단점
        </v-chip>
      </v-card-title>

      <v-card-text style="height:13vh;overflow:hidden;">
        <div v-html="review.cons.replace(/(?:\r\n|\r|\n)/g, '<br />')" />
      </v-card-text>
    </v-card>
  </v-col>
</template>

<script>
export default {
  props: {
    review: {
      type: Object,
      default () {
        return {}
      }
    }
  },
  data: () => ({

  }),
  mounted () {
  },
  methods: {
    linkKinder () {
      this.$router.push('/kinder/' + this.review.kindergarten.id)
    }
  }
}
</script>

<style scoped>
.cursor {
  cursor: pointer;
}
</style>
