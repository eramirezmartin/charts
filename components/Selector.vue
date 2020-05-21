<template>
  <v-select
    v-model="selected"
    :items="items"
    label="Select"
    return-object
  ></v-select>
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
