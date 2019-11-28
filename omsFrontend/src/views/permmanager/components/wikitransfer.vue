<template>
  <div>
    <div>
      <el-transfer
        v-model="value"
        :titles="['未选择', '已选择']"
        :button-texts="['向左走', '向右走']"
        :data="alldata"
        filterable
        @change="handleChange">
        <el-button
          slot="left-footer"
          type="info"
          class="transfer-footer"
          size="mini"
          @click="getData">重置</el-button>
      </el-transfer>
    </div>
  </div>
</template>

<script>
import {getWiki} from '@/api/wiki'
export default {
  props: {
      selectdata: {
        type: Array,
        default: () => ([])
      }
    },
  data() {
    return {
      alldata: [],
      value: this.selectdata,
      changedata: false
    }
  },
  watch: {
    // 监控rowdata值的变化，有变化立即刷新数据
    selectdata() {
      this.getData()
    }
  },

  created() {
    this.getData()
  },

  methods: {
    getData() {
      this.alldata = []
      this.value = this.selectdata
      getWiki().then(response => {
        this.alldata = []
        const results = response.data
        for (var i = 0, len = results.length; i < len; i++) {
          this.alldata.push({
            key: results[i].title
          })
        }
      })
    },
    handleChange(value, direction, movedKeys) {
      this.$emit('getDatas', value)
    }
  }
}
</script>

<style>
  .transfer-footer {
    margin-left: 20px;
    padding: 6px 5px;
  }
</style>
