<template>
  <div>
    <div><img src="oa.png" width="292" height="70" /></div>
    <v-app>
      <Tabs />
      <main class="pa-10"><router-view /></main>
    </v-app>
  </div>
</template>
<script>
import Tabs from '~/components/Tabs.vue'

export default {
  components: { Tabs }
}
</script>
