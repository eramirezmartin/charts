<template>
  <v-app>
    <v-select
      v-model="selected"
      :items="items"
      label="Select"
      data-app
    ></v-select>
  </v-app>
</template>
<script>
export default {
  props: {
    items: {
      type: Array,
      required: true
    }
  },
  data: () => ({
    selected: {}
  }),
  methods: {
    onChange() {
      this.$emit('onChange', this.selected)
    }
  }
}
</script>
