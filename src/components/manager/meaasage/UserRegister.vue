<template>
  <el-card>
    <el-table :data="compData"  style="width: 100%">
        <el-table-column prop="name" label="用户名" width="180">
        </el-table-column>
        <el-table-column prop="usename" label="账户" width="180">
        </el-table-column>
        <el-table-column prop="password" label="密码">
        </el-table-column>
        <el-table-column prop="branch" label="单位">
        </el-table-column>
        
        <el-table-column label="操作">
            <!--eslint-disable-next-line-->
        <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleEdit(scope.row)">同意</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.row)">拒绝</el-button>
      </template>
</el-table-column>


</el-table>
<!-- 分页功能-->
<el-pagination :page-size='pageSize' @current-change="handleCurrentChange" background layout="prev, pager, next" :total="50">
</el-pagination>
</el-card>
</template>

<script>
    import {
        getData,
    } from '@/api/api.js'
    import {
        handleDelete,
        addRegisteData
    } from '@/api/table.js'
    export default {
        data() {
            return {
                tableData: [],
                currentPage: 1,
                pageSize: 10,
                total: 0,
                form: {
                    name: '',
                    branch: '',
                    sex: '1',
                    phonenumber: '',
                    age: '',
                    address: ''
                },
            }
        },
        computed: {
            compData() {
                return this.tableData.slice((this.currentPage - 1) * 5, this.currentPage * 5)
            }
        },
        mounted() {
            getData(this, '/getRegistersData')
        },
        methods: {
            handleEdit(row) {
                handleDelete(this, row.usename, 1, getData, '/getRegistersData')
                addRegisteData(this, row, getData, '/getRegistersData')
            },
            handleDelete(row) {
                console.log(row)
                handleDelete(this, row.usename, 1, getData, '/getRegistersData')
            },
            handleCurrentChange(val) {
                this.currentPage = val
            },
        }
    }
</script>

<style scoped>

</style>