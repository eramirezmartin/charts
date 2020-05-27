<template>
  <v-card>
    <v-tabs v-model="tab" background-color="black" dark>
      <v-tab v-for="(item, index) in items" :key="`tab-${index}`" :to="item.to">
        {{ item.name }}
      </v-tab>
    </v-tabs>
  </v-card>
</template>
<script>
export default {
  data() {
    return {
      tab: 'tab-0',
      items: [
        {
          to: '/Overview',
          name: 'Milestone Report',
          content: 'Tab 1 Content'
        },
        {
          to: '/Merge',
          name: 'Devel MR',
          content: 'Tab 2 Content'
        },
        {
          to: '/Issues',
          name: 'Devel Issues',
          content: 'Tab 3 Content'
        }
      ]
    }
  }
}
</script>
