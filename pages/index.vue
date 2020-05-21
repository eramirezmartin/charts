<template>
  <div>
    <Tabs :data="data" />
  </div>
</template>
<script>
import data from '~/static/milestone_analysis.json'
import Tabs from '~/components/Tabs.vue'

export default {
  components: { Tabs },
  asyncData() {
    return { data }
  }
}
</script>
