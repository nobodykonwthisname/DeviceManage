<template>
   <div style="width:100%">
    <el-table :data="compData.filter(data=>!search||data.numbering.includes(search))" style="width: 100%">
    <el-table-column label="编号" prop="numbering"></el-table-column>
    <el-table-column label="设备名" prop="nickname"></el-table-column>
    <el-table-column label="部门" prop="branch"></el-table-column>
    <el-table-column label="使用地" prop="place"></el-table-column>
    <el-table-column label="状态" prop="status"></el-table-column>
    <el-table-column label="操作" >
        <template slot-scope="scope">
            <el-button
          size="mini"
          type="primary"
          @click="giveback(scope.row)">归还</el-button>
          <el-button
          size="mini"
          type="danger"
          @click="details(scope.row)">报修</el-button>
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
<el-dialog title="申请报修" :visible.sync="dialogFormVisible" width="600px" height="500px">
    <el-form :model="form" ref="form">
        <el-form-item label="设备编号" :label-width="formLabelWidth" prop="numbering">
            <el-input v-model="form.numbering" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="设备名称" :label-width="formLabelWidth" prop="nickname">
            <el-input v-model="form.nickname" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="故障情况" :label-width="formLabelWidth" prop="count">
            <el-input v-model="form.sistuation" autocomplete="off"></el-input>
        </el-form-item>
    </el-form>
    <template #footer>
    <span class="dialog-footer">
      <el-button @click="cancel">取 消</el-button>
      <el-button type="primary" @click="repair"
        >报 修</el-button>
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
        props: ['uname'],
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
                    sistuation: '',
                },
            }
        },
        computed: {
            compData() {
                if (this.tableData) { // 检查 tableData 是否存在
                    const start = (this.currentPage - 1) * this.pageSize;
                    const end = this.currentPage * this.pageSize;
                    console.log('我是own里面的name', this.uname)
                    return this.tableData.filter(data => !this.search || data.numbering.includes(this.search)).slice(start, end);
                } else {
                    return [];
                }
            },

        },
        mounted() {
            this.total = this.tableData.length;
            this.fetchData(1);

        },
        methods: {
            fetchData(page) {
                axios.get(`/api/user/getReturnApplication?page=${page}&pageSize=${this.pageSize}`)
                    .then(response => {
                        this.tableData = response.data;
                        this.total = response.data.length;
                        this.currentPage = page;
                    })
                    .catch(error => {
                        console.error(error);
                    });
            },
            giveback(row) {
                this.$message({
                    message: '已申请归还，等待批准',
                    type: 'success'
                });
                const index = this.compData.indexOf(row);
                this.tableData.splice(index, 1);
            },
            repair(row) {
                this.dialogFormVisible = false
                this.$message({
                    message: '已申请报修，等待批准',
                    type: 'success'
                });
                const index = this.compData.indexOf(row);
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