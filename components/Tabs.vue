<template>
  <v-card>
    <v-tabs v-model="tab" background-color="primary" dark>
      <v-tab v-for="(item, i) in items" :key="item.tab" :href="`#tab-${i}`">
        {{ item.tab }}
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab" class="pt-10 pb-10 pl-10 pr-10">
      <v-tab-item value="tab-0">
        <TabOne :analysis="data" />
      </v-tab-item>
      <v-tab-item value="tab-1">
        <TabTwo :analysis="mr" />
      </v-tab-item>
      <v-tab-item value="tab-2">
        <TabThree />
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>
<script>
import TabOne from '~/components/TabOne.vue'
import TabTwo from '~/components/TabTwo.vue'
import TabThree from '~/components/TabThree.vue'

export default {
  components: { TabOne, TabTwo, TabThree },
  props: {
    data: {
      type: Array,
      required: true
    },
    mr: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      current: null,
      priorityData: null,
      typeData: null,
      tab: null,
      items: [
        { tab: 'One', content: 'Tab 1 Content' },
        { tab: 'Two', content: 'Tab 2 Content' },
        { tab: 'Three', content: 'Tab 3 Content' }
      ]
    }
  }
}
</script>
