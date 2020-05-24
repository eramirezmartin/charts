<template>
  <section class="d-flex flex-wrap">
    <v-flex>
      <h3 class="display-3">{{ data.milestone_planned_percentage }}</h3>
      <p class="body-1">% milestone</p>
    </v-flex>
    <v-flex>
      <h3 class="display-3">{{ data.milestone_closed_issues }}</h3>
      <p class="body-1">milestone_closed_issues</p>
    </v-flex>
    <v-flex>
      <h3 class="display-3">{{ data.milestone_merge_request }}</h3>
      <p class="body-1">milestone_merge_request</p>
    </v-flex>
    <v-flex>
      <h3 class="display-3">{{ data.milestone_planned_issues }}</h3>
      <p class="body-1">milestone_planned_issues</p>
    </v-flex>
    <v-flex>
      <h3 class="display-3">{{ data.milestone_added_issues }}</h3>
      <p class="body-1">milestone_added_issues</p>
    </v-flex>
  </section>
</template>
<script>
export default {
  props: {
    data: {
      type: Object,
      required: true
    }
  }
}
</script>
<style scoped>
h3,
p {
  text-align: center;
  font-weight: normal;
}
</style>
