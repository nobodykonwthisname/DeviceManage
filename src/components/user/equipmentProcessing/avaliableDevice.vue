<template>
  <div style="width:100%;height:500px">
     <el-table  :data="tableData.filter(data=>!search||data.numbering.includes(search))" style="width: 100%" >
    <el-table-column label="编号" prop="numbering"></el-table-column>
    <el-table-column label="设备名" prop="nickname"></el-table-column>
    <el-table-column label="部门" prop="branch"></el-table-column>
    <el-table-column label="所在地" prop="place"></el-table-column>
    <el-table-column label="状态" prop="status"></el-table-column>
<el-table-column label="操作">
    <template slot-scope="scope">
        <el-button
          size="mini"
          type="primary"
          @click="details(scope.row)">申请</el-button>
      </template>
</el-table-column>
<el-table-column align="right">
    <template slot="header" slot-scope="scope">
        <div class="inputAndSearch">
            <el-input
          v-model="search"
          size="mini" @click="inputCheck(scope)"
          placeholder="输入编号"/>
        </div>
      </template>

</el-table-column>
</el-table>
<el-dialog title="申请详情" :visible.sync="dialogFormVisible" width="600px" height="500px">
    <el-form :model="form" ref="form">
        <el-form-item label="申请部门" :label-width="formLabelWidth" prop="branch">
            <el-input v-model="form.branch" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="设备位置" :label-width="formLabelWidth" prop="branch">
            <el-input v-model="form.place" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="设备编号" :label-width="formLabelWidth" prop="numbering">
            <el-input v-model="form.numbering" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="设备名称" :label-width="formLabelWidth" prop="nickname">
            <el-input v-model="form.nickname" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="使用时间（天）" :label-width="formLabelWidth" prop="count">
            <el-input v-model="form.count" autocomplete="off"></el-input>
        </el-form-item>
    </el-form>
    <template #footer>
    <span class="dialog-footer">
      <el-button @click="cancel">取 消</el-button>
      <el-button type="primary" @click="apply"
        >申 请</el-button>
    </span>
  </template>
</el-dialog>
<el-pagination v-model="currentPage" :page-size="pageSize" :total="total" @current-change="fetchData">
</el-pagination>
</div>
</template>

<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                tableData: [],
                search: '',
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
                if (this.tableData) { // 检查 tableData 是否存在
                    const start = (this.currentPage - 1) * this.pageSize;
                    const end = this.currentPage * this.pageSize;
                    return this.tableData.filter(data => !this.search || data.numbering.includes(this.search)).slice(start, end);
                } else {
                    return [];
                }
            }
        },
        mounted() {
            this.total = this.tableData.length;
            this.fetchData(1);
        },
        methods: {
            fetchData(page) {
                axios.get(`/api/user/getUnusedApplication?page=${page}&pageSize=${this.pageSize}`)
                    .then(response => {
                        this.tableData = response.data;
                        this.total = response.data.length;
                        this.currentPage = page;
                    })
                    .catch(error => {
                        console.error(error);
                    });
            },
            apply(row) {
                this.dialogFormVisible = false
                this.$message({
                    message: '申请成功，等待管理员批准',
                    type: "success"
                })
                const index = this.tableData.indexOf(row);
                this.tableData.splice(index, 1);
            },
            details(row) {
                this.dialogFormVisible = true
                this.form = row
            },
            cancel() {
                this.dialogFormVisible = false
            }
        }
    }
</script>

<style scoped>

</style>