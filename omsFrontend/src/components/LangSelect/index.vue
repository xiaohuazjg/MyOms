<template>
  <el-dropdown
    trigger="click"
    class="international"
    @command="handleSetLanguage">
    <div class="navbar-icon">
      <icon
        name="globe-asia"
        scale="1.5"
        spin/>
    </div>
    <el-dropdown-menu slot="dropdown">
      <el-dropdown-item
        :disabled="language==='zh'"
        command="zh">中文</el-dropdown-item>
      <el-dropdown-item
        :disabled="language==='en'"
        command="en">English</el-dropdown-item>
    </el-dropdown-menu>
  </el-dropdown>
</template>

<script>
export default {
  computed: {
    language() {
      return this.$store.getters.language
    }
  },
  methods: {
    handleSetLanguage(lang) {
      this.$i18n.locale = lang
      this.$store.dispatch('setLanguage', lang)
      this.$message({
        message: 'Switch Language Success',
        type: 'success'
      })
    }
  }
}
</script>
