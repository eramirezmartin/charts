<template>
  <section class="d-flex flex-wrap">
    <v-flex>
      <h3 class="display-3">{{ data.milestone_planned_percentage }}</h3>
      <p class="body-1">% Planned Milestone</p>
    </v-flex>
    <v-flex>
      <h3 class="display-3">{{ data.milestone_closed_issues }}</h3>
      <p class="body-1">Closed Issues</p>
    </v-flex>
    <v-flex>
      <h3 class="display-3">{{ data.milestone_merge_request }}</h3>
      <p class="body-1">Merge Request</p>
    </v-flex>
    <v-flex>
      <h3 class="display-3">{{ data.milestone_planned_issues }}</h3>
      <p class="body-1">Planned Issues</p>
    </v-flex>
    <v-flex>
      <h3 class="display-3">{{ data.milestone_added_issues }}</h3>
      <p class="body-1">Added Issues</p>
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
