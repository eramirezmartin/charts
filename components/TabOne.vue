<template>
  <section>
    <Selector :items="selectorItems" @change="updateChartData" />
    <Statistics v-if="current" :data="current" />
    <div class="d-flex">
      <v-flex class="pr-5">
        <Chart v-if="priorityData" :data="priorityData" :height="200" />
      </v-flex>
      <v-flex class="pl-5">
        <Chart v-if="typeData" :data="typeData" :height="200" />
      </v-flex>
    </div>
  </section>
</template>

<script>
import Chart from '~/components/Chart.vue'
import Selector from '~/components/Selector.vue'
import Statistics from '~/components/Statistics.vue'

export default {
  components: { Selector, Statistics, Chart },
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
        labels: ['High', 'Low', 'Medium', 'Hotfix', 'Critical', 'mongo'],
        title: this.current.milestone
      }
    }
  }
}
</script>
