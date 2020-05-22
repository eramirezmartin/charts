<template>
  <div>
    <v-app>
      <Tabs :data="data" :mr="mr" :issues="issues" />
    </v-app>
  </div>
</template>
<script>
import data from '~/static/milestone_analysis.json'
import mr from '~/static/milestone_mr.json'
import issues from '~/static/milestone_issues.json'
import Tabs from '~/components/Tabs.vue'

export default {
  components: { Tabs },
  asyncData() {
    return { data, mr, issues }
  }
}
</script>
