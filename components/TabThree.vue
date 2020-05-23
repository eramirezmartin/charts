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
      :calculate-widths="true"
      :disable-pagination="true"
      :hide-default-footer="true"
    >
      <template v-slot:item.issue_title="{ item }">
        <a :href="item.issue_link" target="_blank">
          {{ item.issue_title }}
        </a>
      </template>
      <template v-slot:item.issue_priority="{ item }">
        <v-chip :color="getColor(item.issue_priority, 'priority')" dark
          >{{ item.issue_priority }}
        </v-chip>
      </template>
      <template v-slot:item.issue_status="{ item }">
        <v-chip :color="getColor(item.issue_status, 'flow')" dark
          >{{ item.issue_status }}
        </v-chip>
      </template>
    </v-data-table>
  </v-card>
</template>
<script>
const priority = {
  Hotfix: 'red',
  Critical: 'orange',
  High: 'blue',
  Medium: 'green',
  Low: 'yellow'
}
const flow = {
  QA: 'red',
  Doing: 'dark blue',
  Ready: 'green',
  Analysis: 'brown',
  Waiting: 'purple',
  Open: 'grey'
}
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
    getColor(discussion, enumType) {
      if (enumType === 'priority') return priority[discussion]
      else if (enumType === 'flow') return flow[discussion]
    }
  }
}
</script>
