<template>
  <div class="components-container" style='height:100vh'>
    <el-row :gutter="20">
      <el-col :span="10">
        <salt-state-group></salt-state-group>
      </el-col>
      <el-col :span="14">
        <salt-state></salt-state>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import saltState from './components/state.vue'
import saltStateGroup from './components/stategroup.vue'

export default {
  components: { saltState, saltStateGroup },

  data() {
    return {}
  },
  created() {
  },
  methods: {}
}
</script>

<style lang="scss">
</style>
