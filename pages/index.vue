<template>
  <div>
    <label>Milestone:</label>
    <select v-on:change="updateChartData" v-model="current">
      <option
        v-for="(item, index) in analysis"
        :key="`milestone-${index}`"
        :value="item"
        >{{ item.milestone }}</option
      >
    </select>
    <Chart v-bind:data="priorityData" :height="200" />
    <Chart v-bind:data="typeData" :height="200" />
  </div>
</template>
<script>
import analysis from '~/static/milestone_analysis.json'
import Chart from '~/components/Chart.vue'

export default {
  components: { Chart },
  asyncData() {
    return { analysis }
  },
  data() {
    return {
      current: null,
      priorityData: null,
      typeData: null
    }
  },
  created() {
    this.current = this.analysis[this.analysis.length - 1]
    this.updateChartData()
  },
  methods: {
    updateChartData() {
      this.priorityData = {
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

      this.typeData = {
        data: [
          this.current.tp_bug,
          this.current.tp_new_feature,
          this.current.tp_technical_debt,
          this.current.tp_discussion,
          this.current.tp_poc,
          this.current.tp_support
        ],
        labels: ['High', 'Low', 'Medium', 'Hotfix', 'Critical', 'mongo'],
        title: this.current.milestone
      }
    }
  }
}
</script>
