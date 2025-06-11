<template>
  <el-card>
    <el-table :data="compData" style="width: 100%">
        <el-table-column prop="name" label="申请人" width="180">
        </el-table-column>
        <el-table-column prop="branch" label="申请单位">
        </el-table-column>
        <el-table-column prop="numbering" label="设备编号">
        </el-table-column>
        <el-table-column prop="nickname" label="设备名称">
        </el-table-column>
        <el-table-column prop="count" label="使用时间（天）">
        </el-table-column>
        <el-table-column label="操作">
            <!--eslint-disable-next-line-->
        <template slot-scope="scope">
        <el-button
          size="mini"
          @click="details(scope.row)">详情</el-button>
      </template>
</el-table-column>
</el-table>
<el-dialog title="申请详情" :visible.sync="dialogFormVisible" width="600px" height="500px">
    <el-form :model="form" ref="form">
        <el-form-item label="申请人" :label-width="formLabelWidth" prop="name">
            <el-input v-model="form.name" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="申请部门" :label-width="formLabelWidth" prop="branch">
            <el-input v-model="form.branch" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="使用场所" :label-width="formLabelWidth" prop="branch">
            <el-input v-model="form.place" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="设备编号" :label-width="formLabelWidth" prop="numbering">
            <el-input v-model="form.numbering" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="设备名称" :label-width="formLabelWidth" prop="nickname">
            <el-input v-model="form.nickname" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="使用时间（天）" :label-width="formLabelWidth" prop="count">
            <el-input v-model="form.count" autocomplete="off" disabled></el-input>
        </el-form-item>
    </el-form>
    <template #footer>
    <span class="dialog-footer">
      <el-button @click="reject">拒 绝</el-button>
      <el-button type="primary" @click="dialogEdit"
        >同 意</el-button
      >
    </span>
  </template>
</el-dialog>
<!-- 分页功能-->
<el-pagination :page-size='pageSize' @current-change="handleCurrentChange" background layout="prev, pager, next" :total="5">
</el-pagination>
</el-card>
</template>

<script>
    import {
        getData,
    } from '@/api/api.js'
    import {
        //updateApplicationData,
        handleDeleteApplication
    } from '@/api/table.js'
    export default {
        data() {
            return {
                tableData: [],
                currentPage: 1,
                pageSize: 5,
                total: 0,
                dialogFormVisible: false,
                formLabelWidth: '80px',
                form: {
                    name: '',
                    branch: '',
                    numbering: '',
                    place: '',
                    nickname: '',
                    count: '',
                },
            }
        },
        computed: {
            compData() {
                return this.tableData.slice((this.currentPage - 1) * 5, this.currentPage * 5)
            }
        },
        mounted() {
            getData(this, '/getApplicationData')
        },
        methods: {
            reject(row) {
                console.log(row)
                this.dialogFormVisible = false
                handleDeleteApplication(this, this.form.numbering, getData, '/getApplicationData')
            },
            details(row) {
                this.dialogFormVisible = true
                this.form = row
            },
            handleCurrentChange(val) {
                this.currentPage = val
            },
            dialogEdit(row) {
                console.log(row)
                this.dialogFormVisible = false
                const index = this.compData.indexOf(row);
                this.tableData.splice(index, 1);
                this.$message({
                        message: '已同意',
                        type: 'success'
                    })
                    //更新状态
                    /* if (updateApplicationData(this, getData, '/getApplicationData'))
                //删除该申请表
                    handleDeleteApplication(this, row.numbering, getData, '/getApplicationData')
 */
            }
        }
    }
</script>

<style scoped>

</style>