<template>
  <v-select
    v-model="selected"
    :items="items"
    label="Milestone"
    class="flex-grow-0"
    @change="onChange"
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
    selected: null
  }),
  created() {
    if (this.items && this.items.length) {
      this.selected = this.items[this.items.length - 1].value
    }
    this.onChange()
  },
  methods: {
    onChange() {
      this.$emit('change', this.selected)
    }
  }
}
</script>
