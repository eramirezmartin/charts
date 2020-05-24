<template>
  <section v-if="analysis">
    <v-container :fluid="true">
      <v-row no-gutters>
        <v-col cols="2">
          <Selector :items="selectorItems" @change="updateChartData" />
        </v-col>
        <v-col v-if="current" cols="10" class="text-center">
          <h1 class="display-3 pb-12 d-inline-block">
            {{ current.milestone }}
          </h1>
          <h2 class="d-inline-block pl-5">{{ current.dates }}</h2></v-col
        >
      </v-row>
    </v-container>
    <div v-if="current" class="py-12 text-center">
      <Statistics class="py-12" :data="current" />
      <div class="d-flex flex-wrap flex-md-nowrap justify-space-between">
        <v-flex>
          <Chart v-if="priorityData" :data="priorityData" />
        </v-flex>
        <v-flex>
          <Chart v-if="typeData" :data="typeData" />
        </v-flex>
      </div>
      <div class="d-flex flex-wrap flex-md-nowrap justify-space-between">
        <v-flex><LineChart :data="lineMilestoneData"/></v-flex>
        <v-flex><LineChart :data="lineMilestoneData"/></v-flex>
      </div>
      <div class="d-flex flex-wrap flex-md-nowrap justify-space-between">
        <v-flex><LineChart :data="lineMilestoneData"/></v-flex>
        <v-flex><LineChart :data="lineMilestoneData"/></v-flex>
      </div>
    </div>
  </section>
</template>

<script>
import LineChart from '~/components/LineChart.vue'
import Chart from '~/components/Chart.vue'
import Selector from '~/components/Selector.vue'
import Statistics from '~/components/Statistics.vue'
import analysis from '~/static/milestone_analysis.json'

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
      lineMilestoneData: null,
      selectorItems: []
    }
  },
  created() {
    if (this.analysis && this.analysis.length) {
      this.formatSelectorData()
      this.lineMilestoneData = this.getLineChartData()
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
        title: this.current.milestone
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
        labels: ['High', 'Low', 'Medium', 'Hotfix', 'Critical', '- TODO'],
        title: this.current.milestone
      }
    },
    getLineChartData() {
      return {
        data: this.analysis.map((item) => ({
          y: item.milestone_planned_percentage,
          x: item.milestone
        })),
        labels: this.analysis.map((item) => item.milestone),
        title: '% milestone'
      }
    }
  }
}
</script>
