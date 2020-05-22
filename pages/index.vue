<template>
  <div>
    <Tabs :data="data" :mr="mr" />
  </div>
</template>
<script>
import data from '~/static/milestone_analysis.json'
import mr from '~/static/milestone_mr.json'
import Tabs from '~/components/Tabs.vue'

export default {
  components: { Tabs },
  asyncData() {
    return { data, mr }
  }
}
</script>
