<template>
  <v-card>
    <v-card-title>
      Devel Merge Request
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="analysis"
      :search="search"
      :disable-pagination="true"
      :hide-default-footer="true"
    >
      <template v-slot:item.mr_up_votes="{ item }">
        <v-chip
          :color="
            getColor(
              item.mr_up_votes,
              item.mr_pending_discussion,
              item.mr_down_votes
            )
          "
          dark
          >{{ item.mr_up_votes }}
        </v-chip>
      </template>
      <template v-slot:item.mr_title="{ item }"
        ><a :href="item.mr_link" target="_blank">
          {{ item.mr_title }}</a
        ></template
      >
      <template v-slot:item.mr_pending_discussion="{ item }">
        <v-chip :color="item.mr_pending_discussion ? 'orange' : 'white'" dark>{{
          item.mr_pending_discussion
        }}</v-chip>
      </template>
    </v-data-table>
  </v-card>
</template>
<script>
import analysis from '~/static/milestone_mr.json'
export default {
  asyncData() {
    return { analysis }
  },
  data() {
    return {
      search: '',
      headers: [
        { text: 'Up Votes', value: 'mr_up_votes' },
        { text: 'Project', value: 'mr_project', align: 'left' },
        { text: 'Title', value: 'mr_title', url: 'mr_link' },
        { text: 'Down Votes', value: 'mr_down_votes' },
        { text: 'Pending Discussion', value: 'mr_pending_discussion' },
        { text: 'Last Update', value: 'mr_updated' }
      ]
    }
  },
  methods: {
    getColor(up, discussion, down) {
      if (up >= 2 && !discussion) return 'green'
      else if (up > 0 || discussion) return 'orange'
      else if (down > 1) return 'red'
    }
  }
}
</script>
