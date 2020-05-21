<template>
  <section>
    <Selector :items="selectorItems" />
    <Chart v-bind:data="priorityData" :height="200" />
    <Chart v-bind:data="typeData" :height="200" />
  </section>
</template>

<script>
import Chart from '~/components/Chart.vue'
import Selector from '~/components/Selector.vue'

export default {
  components: { Selector, Chart },
  props: {
    analysis: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      current: null,
      priorityData: null,
      typeData: null,
      selectorItems: []
    }
  },
  created() {
    if (this.analysis && this.analysis.length) {
      this.current = this.analysis[this.analysis.length - 1]
      this.updateChartData()
      this.formatSelectorData()
    }
  },
  methods: {
    formatSelectorData() {
      this.selectorItems = this.analysis.map((item) => ({
        text: item.milestone,
        value: item.milestone
      }))
    },
    updateChartData() {
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
        labels: ['High', 'Low', 'Medium', 'Hotfix', 'Critical', 'mongo'],
        title: this.current.milestone
      }
    }
  }
}
</script>
