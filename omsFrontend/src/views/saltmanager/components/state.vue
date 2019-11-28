<template>
  <div>
    <el-card>
      <div class="head-lavel">
        <div class="table-button">
          <el-button type="success">state服务</el-button>
          <el-button type="primary" icon="el-icon-plus" @click="addForm=true">新建</el-button>
        </div>
        <div class="table-search">
        </div>
      </div>
      <div>
        <el-table :data='tableData' border style="width: 100%">
          <el-table-column prop='name' label='名称'></el-table-column>
          <el-table-column prop='group' label='分组'></el-table-column>
          <el-table-column prop='cmd' label='state命令'></el-table-column>
          <el-table-column prop='desc' label='描述'></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button @click="deleteGroup(scope.row.id)" type="danger" size="small">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div class="table-pagination">
        <el-pagination
          small
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page.sync="currentPage"
          :page-sizes="pagesize"
          :page-size="listQuery.limit"
          :layout="pageformat"
          :total="tabletotal">
        </el-pagination>
      </div>
    </el-card>

    <el-dialog :visible.sync="addForm">
      <el-form :model="ruleForm" ref="ruleForm" label-width="100px">
        <el-form-item label="名称" prop="name">
          <el-input v-model="ruleForm.name"></el-input>
        </el-form-item>
        <el-form-item label="分组" prop="group">
          <el-select v-model="ruleForm.group" placeholder="请选择分组">
            <el-option v-for="item in groups" :key="item.name" :value="item.name"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="state命令" prop="cmd">
          <el-input v-model="ruleForm.cmd"></el-input>
        </el-form-item>
        <el-form-item label="描述" prop="desc">
          <el-input v-model="ruleForm.desc" type="textarea" :autosize="{ minRows: 5, maxRows: 10}"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import { getSaltStateGroup, getSaltState, postSaltState, deleteSaltState } from '@/api/salt'
import { LIMIT, pagesize, pageformat } from '@/config'

export default {
  components: {},

  data() {
    return {
      status: true,
      tableData: [],
      tabletotal: 0,
      currentPage: 1,
      pagesize: pagesize,
      pageformat: pageformat,
      listQuery: {
        limit: LIMIT,
        offset: ''
      },
      addForm: false,
      ruleForm: {
        name: '',
        group: '',
        cmd: '',
        desc: ''
      },
      groups: []
    }
  },
  created() {
    this.fetchData()
    this.fetchGroupData()
  },
  methods: {
    fetchData() {
      getSaltState(this.listQuery).then(response => {
        this.tableData = response.data.results
        this.tabletotal = response.data.count
      })
    },
    fetchGroupData() {
      getSaltStateGroup().then(response => {
        this.groups = response.data
      })
    },
    submitForm() {
      postSaltState(this.ruleForm).then(response => {
        this.$message({
          message: '恭喜你，新建成功',
          type: 'success'
        })
        this.fetchData()
        this.addForm = false
      }).catch(error => {
        this.$message.error('新建失败')
        console.log(error)
      })
    },
    deleteGroup(id) {
      deleteSaltState(id).then(response => {
        this.$message({
          message: '恭喜你，删除成功',
          type: 'success'
        })
        this.fetchData()
      }).catch(error => {
        this.$message.error('删除失败')
        console.log(error)
      })
    },
    searchClick() {
      this.fetchData()
    },
    handleSizeChange(val) {
      this.limit = val
      this.fetchData()
    },
    handleCurrentChange(val) {
      this.offset = (val - 1) * LIMIT
      this.fetchData()
    }
  }
}
</script>

<style lang="scss">
</style>
