<template>
  <v-card>
    <v-card-title>
      Devel Issues
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
      <template v-slot:item.issue_title="{ item }"
        ><a :href="item.issue_link" target="_blank">
          {{ item.issue_title }}</a
        ></template
      >
      <template v-slot:item.issue_priority="{ item }">
        <v-chip :color="getColor(item.issue_priority)" dark>{{
          item.issue_priority
        }}</v-chip>
      </template>
    </v-data-table>
  </v-card>
</template>
<script>
export default {
  props: {
    analysis: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      search: '',
      headers: [
        { text: 'Priority', value: 'issue_priority' },
        { text: 'Project', value: 'issue_project', align: 'left' },
        { text: 'Title', value: 'issue_title', url: 'mr_link' },
        { text: 'Issue Type', value: 'issue_type' },
        { text: 'Status', value: 'issue_status' },
        { text: 'Assigend', value: 'issue_assigned' }
      ]
    }
  },
  methods: {
    getColor(discussion) {
      if (discussion === 'Hotfix') return 'red'
      else if (discussion === 'Critical') return 'orange'
      else if (discussion === 'High') return 'blue'
      else if (discussion === 'Medium') return 'green'
      else if (discussion === 'Low') return 'yellow'
    }
  }
}
</script>
