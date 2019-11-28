<template>
  <div class="components-container" style='height:100vh'>
    <el-row :gutter="20">
      <el-col :span="10">
        <el-card>
          <div slot="header">
            <span>执行state</span>
          </div>
          <el-form :model="ruleForm" ref="ruleForm" label-width="70px">
            <el-form-item label="选择主机" prop="hosts">
              <sesect-hosts :selecthost="selecthosts" @gethosts="getHosts"></sesect-hosts>
            </el-form-item>
            <hr class="heng"/>
            <el-form-item v-for="item in stateDates" :key="item.id" :label="item.name">
              <el-button v-for="state in item.state" :key="state.id" size="mini" @click="ruleForm.statejob=state.name">
                {{state.name}}
              </el-button>
            </el-form-item>
            <hr class="heng"/>
            <el-form-item>
              <el-button type="primary" @click="submitForm()">执行</el-button>
            </el-form-item>
          </el-form>
        </el-card>
      </el-col>

      <el-col :span="14">
        <el-card>
          <div class="table-button">
            <a class="jobname">历史记录</a>
          </div>
          <div class="table-search">
            <el-input
              placeholder="search"
              v-model="listQuery.search"
              @keyup.enter.native="searchClick">
              <i class="el-icon-search el-input__icon" slot="suffix" @click="searchClick"></i>
            </el-input>
          </div>
          <div>
            <el-table :data='tableData' style="width: 100%">
              <el-table-column prop='statejob' label='名称'></el-table-column>
              <el-table-column prop='status' label='状态' sortable>
                <template slot-scope="scope">
                  <div slot="reference">
                    <el-button plain size="mini" :type="STATE_STATUS[scope.row.status].type"
                               :icon="STATE_STATUS[scope.row.status].icon">
                      {{STATE_STATUS[scope.row.status].text}}
                    </el-button>
                  </div>
                </template>
              </el-table-column>
              <el-table-column prop='action_user' label='执行主机'>
                <template slot-scope="scope">
                  <div slot="reference" class="name-wrapper" style="text-align: center">
                    <el-tag v-for="item in scope.row.hosts.split('|')" :key="item.id" size="mini" style="margin-right: 3px">
                      {{item}}
                    </el-tag>
                  </div>
                </template>
              </el-table-column>
              <el-table-column prop='action_user' label='发布人'></el-table-column>
              <el-table-column prop='create_time' label='创建时间' sortable>
                <template slot-scope="scope">
                  <div slot="reference">
                    {{scope.row.create_time | formatTime}}
                  </div>
                </template>
              </el-table-column>
              <el-table-column label="操作">
                <template slot-scope="scope">
                  <el-button @click="showJobResult(scope.row.result)" type="success" size="mini"
                             :disabled="!scope.row.result">结果
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
          <div class="table-footer">

            <div class="table-button">
            </div>
            <div class="table-pagination">
              <el-pagination
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page.sync="currentPage"
                :page-sizes="pagesize"
                :page-size="listQuery.limit"
                :layout="pageformat"
                :total="tabletotal">
              </el-pagination>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-dialog :visible.sync="showresult">
      <div>
        <div class="runlog" v-for="item in job_results" :key="item.id">
          <p class="host">{{ item.host }}</p>
          <pre>{{ item.data }}</pre>
        </div>
      </div>
    </el-dialog>
  </div>
</template>
<script>
import { getStatesStatusBygroup, getSaltStateJob, getUpdateStatesStatus, postSaltStateJob } from '@/api/salt'
import { LIMIT, pagesize, pageformat } from '@/config'
import sesectHosts from '../components/hosttransfer.vue'

export default {
  components: { sesectHosts },
  data() {
    return {
      selectcmd: '',
      route_path: this.$route.path.split('/'),
      ruleForm: {
        statejob: '',
        hosts: '',
        action_user: localStorage.getItem('username')
      },
      currentPage: 1,
      listQuery: {
        limit: LIMIT,
        offset: '',
        search: ''
      },
      pagesize: pagesize,
      pageformat: pageformat,
      tableData: [],
      tabletotal: 0,
      STATE_STATUS: {
        deploy: { text: '执行中', type: 'primary', icon: 'el-icon-loading' },
        success: { text: '执行成功', type: 'success', icon: 'el-icon-success' },
        failed: { text: '执行失败', type: 'danger', icon: 'el-icon-error' }
      },
      showresult: false,
      job_results: [],
      check_job_status: '',
      stateDates: [],
      selecthosts: []
    }
  },
  created() {
    this.fetchStateData()
    this.fetchJobData()
  },
  methods: {
    fetchStateData() {
      getStatesStatusBygroup().then(response => {
        this.stateDates = response.data
      })
    },
    fetchJobData() {
      getSaltStateJob(this.listQuery).then(response => {
        this.tableData = response.data.results
        this.tabletotal = response.data.count
        const job_status = this.tableData.map(function(item) {
          return item.status
        })
        if (job_status.indexOf('deploy') > -1) {
          this.check_job_status = setInterval(() => {
            getUpdateStatesStatus().then(response => {
              if (response.data.count === 0) {
                clearInterval(this.check_job_status)
                this.fetchJobData()
              } else {
                console.log('check job_status 3/s')
              }
            })
          }, 3000)
        } else {
          console.log('setInterval_id:' + this.check_job_status)
          clearInterval(this.check_job_status)
        }
      })
    },
    submitForm() {
      postSaltStateJob(this.ruleForm).then(response => {
        this.fetchJobData()
      })
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      this.fetchJobData()
    },
    handleCurrentChange(val) {
      this.listQuery.offset = (val - 1) * LIMIT
      this.fetchJobData()
    },
    showJobResult(row) {
      this.showresult = true
      const data = (new Function('return ' + row))()
      const a = []
      Object.keys(data).map(function(k) {
        a.push({ 'host': k, 'data': data[k] })
      })
      this.job_results = a
    },
    searchClick() {
      this.fetchJobData()
    },
    getHosts(data) {
      this.ruleForm.hosts = data.join()
    }
  }
}
</script>

<style lang='scss'>
</style>
