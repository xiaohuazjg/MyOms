<template>
  <div>
    <el-card>
      <div class="head-lavel">
        <div class="table-search">
          <el-input
            v-model="searchdata"
            placeholder="搜索 ..."
            @keyup.enter.native="searchClick">
            <i
              slot="suffix"
              class="el-icon-search el-input__icon"
              @click="searchClick"/>
          </el-input>
        </div>
      </div>
      <div>
        <el-table
          :data="tableData"
          border
          style="width: 100%">
          <el-table-column
            prop="username"
            label="用户名"
            sortable="custom"/>
          <el-table-column
            prop="email"
            label="Email"/>
          <el-table-column
            prop="skype"
            label="Skype"/>
        </el-table>
      </div>
      <div class="table-pagination">
        <el-pagination
          :current-page.sync="currentPage"
          :page-sizes="pagesize"
          :page-size="listQuery.limit"
          :layout="pageformat"
          :total="tabletotal"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"/>
      </div>
    </el-card>
  </div>
</template>

<script>
  import {getUser} from '@/api/user'
  import {LIMIT, pagesize, pageformat} from '@/config'

  export default {
    props: {
      rowdata: {
        type: Object,
        default: () => ({})
      }
    },
    data() {
      return {
        tableData: [],
        tabletotal: 0,
        searchdata: '',
        currentPage: 1,
        pagesize: pagesize,
        pageformat: pageformat,
        listQuery: {
          limit: LIMIT,
          offset: '',
          groups__name: '',
          search: ''
        }
      }
    },
    watch: {
      // 监控rowdata值的变化，有变化立即刷新数据
      rowdata() {
        this.fetchData()
      }
    },

    created() {
      this.fetchData()
    },

    methods: {
      fetchData() {
        this.listQuery.groups__name = this.rowdata.name
        getUser(this.listQuery).then(response => {
          this.tableData = response.data.results
          this.tabletotal = response.data.count
        })
      },
      searchClick() {
        this.listQuery.search = this.searchdata
        this.fetchData()
      },
      handleSizeChange(val) {
        this.listQuery.limit = val
        this.fetchData()
      },
      handleCurrentChange(val) {
        this.listQuery.offset = (val - 1) * LIMIT
        this.fetchData()
      }
    }
  }
</script>

<style lang='scss'>

</style>
