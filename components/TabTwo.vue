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
    <v-data-table :headers="headers" :items="data" :search="search">
      <template v-slot:item.mr_up_votes="{ item }">
        <v-chip :color="getColor(item.mr_up_votes)" dark>{{
          item.mr_up_votes
        }}</v-chip>
      </template>
    </v-data-table>
  </v-card>
</template>
<script>
export default {
  props: {
    mr_analysis: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      search: '',
      headers: [
        { text: 'Project', value: 'mr_project', align: 'left' },
        { text: 'Title', value: 'mr_title' },
        { text: 'Up Votes', value: 'mr_up_votes' },
        { text: 'Down Votes', value: 'mr_down_votes' },
        { text: 'Pending Discussion', value: 'mr_pending_discussion' },
        { text: 'Last Update', value: 'mr_updated' }
      ],
      data: this.mr_analysis
    }
  },
  methods: {
    getColor(title) {
      if (title > 1) return 'red'
      else if (title > 1) return 'deepOrange'
      else return 'green'
    }
  }
}
</script>
