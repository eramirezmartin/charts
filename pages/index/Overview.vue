<template>
  <section v-if="analysis">
    <v-container :fluid="true">
      <v-row no-gutters>
        <v-col cols="3">
          <Selector :items="selectorItems" @change="updateChartData" />
        </v-col>
        <v-col v-if="current" cols="12" class="pl-auto">
          <h1 class="display-3 d-inline-block">
            {{ current.milestone }}
          </h1>
          <h2 class="d-inline-block">{{ current.dates }}</h2></v-col
        >
      </v-row>
    </v-container>
    <div v-if="current" class="py-auto text-center">
      <Statistics class="py-12" :data="current" />
      <v-container :fluid="true">
        <v-row no-gutters>
          <v-col cols="2"></v-col>
          <v-col cols="3" class:v-text-center>
            <Chart v-if="priorityData" :data="priorityData" />
          </v-col>
          <v-col cols="2"></v-col>
          <v-col cols="3"> <Chart v-if="typeData" :data="typeData" /> </v-col>
          <v-col cols="2"></v-col>
        </v-row>
        <v-row no-gutters></v-row>
        <v-col cols="12"></v-col>
        <v-row no-gutters class="mtb-auto">
          <v-col cols="12">
            <h2 class="d-inline-block">Historical Data</h2>
          </v-col>
        </v-row>
        <v-row no-gutters>
          <v-col cols="2"></v-col>
          <v-col cols="3" class:v-text-center>
            <LineChart :data="perMilestoneData" />
          </v-col>
          <v-col cols="2"></v-col>
          <v-col cols="3">
            <LineChart :data="closedMilestoneData" />
          </v-col>
          <v-col cols="2"></v-col>
        </v-row>
        <v-row no-gutters>
          <v-col cols="2"></v-col>
          <v-col cols="3" class:v-text-center>
            <LineChart :data="MergeMilestoneData" />
          </v-col>
          <v-col cols="2"></v-col>
          <v-col cols="3">
            <LineChart :data="originalMilestoneData" />
          </v-col>
          <v-col cols="2"></v-col>
        </v-row>
      </v-container>
    </div>
  </section>
</template>

<script>
import LineChart from '~/components/LineChart.vue'
import Chart from '~/components/Chart.vue'
import Selector from '~/components/Selector.vue'
import Statistics from '~/components/Statistics.vue'
import analysis from '~/static/milestone_analysis.json'

const chartColors = {
  red: 'rgb(255, 0, 0)',
  orange: 'rgb(255, 159, 64)',
  yellow: 'rgb(255, 205, 86)',
  green: 'rgb(75, 192, 192)',
  blue: 'rgb(54, 162, 235)',
  purple: 'rgb(153, 102, 255)',
  grey: 'rgb(201, 203, 207)'
}

export default {
  components: { LineChart, Selector, Statistics, Chart },
  asyncData() {
    return { analysis }
  },
  data() {
    return {
      current: null,
      priorityData: null,
      typeData: null,
      perMilestoneData: null,
      closedMilestoneData: null,
      originalMilestoneData: null,
      MergeMilestoneData: null,
      selectorItems: []
    }
  },
  created() {
    if (this.analysis && this.analysis.length) {
      this.formatSelectorData()
      this.perMilestoneData = this.getLineChartData(
        'milestone_planned_percentage',
        chartColors.red,
        '% Planned Issues'
      )
      this.closedMilestoneData = this.getLineChartData(
        'milestone_closed_issues',
        chartColors.blue,
        'Closed Issues'
      )
      this.MergeMilestoneData = this.getLineChartData(
        'milestone_merge_request',
        chartColors.yellow,
        'Merge Request'
      )
      this.originalMilestoneData = this.getLineChartData(
        'milestone_planned_issues',
        chartColors.green,
        'Planned Issues'
      )
    }
  },
  methods: {
    formatSelectorData() {
      this.selectorItems = this.analysis.map((item) => ({
        text: item.milestone,
        value: item.milestone
      }))
    },
    updateChartData(selectedItem) {
      if (selectedItem) {
        this.current = this.analysis.find(
          (item) => item.milestone === selectedItem
        )
      }
      this.priorityData = this.getPriorityData()
      this.typeData = this.getTypeData()
    },
    getPriorityData() {
      return {
        data: [
          this.current.p_high,
          this.current.p_low,
          this.current.p_medium,
          this.current.p_hotfix,
          this.current.p_critical
        ],
        labels: ['High', 'Low', 'Medium', 'Hotfix', 'Critical'],
        title: 'Issue Priority'
      }
    },
    getTypeData() {
      return {
        data: [
          this.current.tp_bug,
          this.current.tp_new_feature,
          this.current.tp_technical_debt,
          this.current.tp_discussion,
          this.current.tp_poc,
          this.current.tp_support
        ],
        labels: [
          'Bug',
          'New Feature',
          'Technical Debt',
          'Discussion',
          'POC',
          'Support'
        ],
        title: 'Issue Type'
      }
    },
    getLineChartData(serie, color, title) {
      return {
        data: this.analysis.map((item) => ({
          y: item[serie],
          x: item.milestone
        })),
        labels: this.analysis.map((item) => item.milestone),
        title,
        color
      }
    }
  }
}
</script>
