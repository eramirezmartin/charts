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
        <v-chip :color="priorityColor[item.issue_priority]" dark
          >{{ item.issue_priority }}
        </v-chip>
      </template>
      <template v-slot:item.issue_status="{ item }">
        <v-chip :color="flowColor[item.issue_status]" dark
          >{{ item.issue_status }}
        </v-chip>
      </template>
    </v-data-table>
  </v-card>
</template>
<script>
import analysis from '~/static/milestone_issues.json'
export default {
  asyncData() {
    return { analysis }
  },
  data() {
    return {
      search: '',
      priorityColor: {
        Hotfix: 'red',
        Critical: 'orange',
        High: 'blue',
        Medium: 'green',
        Low: 'yellow'
      },
      flowColor: {
        QA: 'red',
        Doing: 'dark blue',
        Ready: 'green',
        Analysis: 'brown',
        Waiting: 'purple',
        Open: 'grey'
      },
      headers: [
        { text: 'Priority', value: 'issue_priority' },
        { text: 'Project', value: 'issue_project', align: 'left' },
        { text: 'Title', value: 'issue_title', url: 'mr_link' },
        { text: 'Issue Type', value: 'issue_type' },
        { text: 'Status', value: 'issue_status' },
        { text: 'Assigend', value: 'issue_assigned' }
      ]
    }
  }
}
</script>
