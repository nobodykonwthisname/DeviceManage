<template>
<el-card>
    <el-table :data="tabData.filter(data=>!search||data.numbering.includes(search))" style="width: 100%" >
    <el-table-column label="编号" prop="numbering"></el-table-column>
    <el-table-column label="设备名" prop="nickname"></el-table-column>
    <el-table-column label="部门" prop="branch"></el-table-column>
    <el-table-column label="使用地" prop="place"></el-table-column>
    <el-table-column label="数量" prop="count"></el-table-column>
    <el-table-column label="状态" prop="status"></el-table-column>
    <el-table-column align="right">
    <template slot="header" slot-scope="scope">
        <div class="inputAndSearch">
            <el-input
          v-model="search"
          size="mini" @click="inputCheck(scope)"
          placeholder="输入编号"/>
          <el-button type="primary" @click="addDevice" size="small" >新增</el-button>
        </div>
      </template>
<template slot-scope="scope">
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.row)">Delete</el-button>
      </template>
</el-table-column>
</el-table>
<el-dialog title="设备信息添加" :visible.sync="dialogFormVisible" width="600px" height="500px">
    <el-form :model="ruleForm" ref="ruleForm" :rules="rules">
        <el-form-item label="设备编号" :label-width="formLabelWidth" prop="numbering">
            <el-input v-model="ruleForm.numbering" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="设备名称" :label-width="formLabelWidth" prop="nickname">
            <el-input v-model="ruleForm.nickname" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="设备类型" :label-width="formLabelWidth" prop="type">
            <el-input v-model="ruleForm.type" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="所属部门" :label-width="formLabelWidth" prop="branch">
            <el-select v-model="ruleForm.branch" placeholder="请选择该新设备归属部门">
                <el-option label="集团派驻" value="集团派驻"></el-option>
                <el-option label="运营部" value="运营部"></el-option>
                <el-option label="行政部" value="行政部"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="放置场所" :label-width="formLabelWidth" prop="place">
            <el-input v-model="ruleForm.place" autocomplete="off"></el-input>
        </el-form-item>
    </el-form>
    <template #footer>
    <span class="dialog-footer">
      <el-button @click="dialogFormVisible = false">取 消</el-button>
      <el-button type="primary" @click="dialogEdit"
        >确 定</el-button
      >
    </span>
  </template>
</el-dialog>
<!-- 使用 props 中的值渲染分页组件 -->
<el-pagination :current-page="currentPage" :page-size="5" :total="total" @current-change="handleCurrentChange(page)" layout="prev, pager, next">
</el-pagination>

</el-card>
</template>

<script>
    import {
        showEquiment
    } from '@/api/table.js'
    import {
        handleDeleteDeviceDetail,
        AddDevice
    } from '@/api/table.js'
    export default {
        name: 'CommonTabs',
        data() {
            return {
                item: '',
                tabData: [],
                search: '',
                filteredData: [],
                currentPage: 1,
                total: 5,
                dialogFormVisible: false,
                formLabelWidth: '80px',
                ruleForm: {
                    numbering: '',
                    nickname: '',
                    type: '',
                    branch: '',
                    place: '',
                },
                rules: {
                    numbering: [{
                        required: true,
                    }],
                    nickname: [{
                        required: true,
                    }],
                    type: [{
                        required: true,
                    }],
                    branch: [{
                        required: true,
                    }],
                    place: [{
                        required: true,

                    }]
                }
            }
        },
        methods: {
            inputCheck(scope) {
                console.log(scope)
            },
            //新增设备信息
            addDevice() {
                this.dialogFormVisible = true
            },
            //删除设备信息
            handleDelete(row, index) {
                handleDeleteDeviceDetail(this, row.numbering, 3, this.tabData, index)
            },

            dialogEdit(ruleForm) {
                //添加新设备信息
                console.log(ruleForm)
                AddDevice(this, ruleForm)
                this.dialogFormVisible = false
            },
            getTabData(item) {
                let val = showEquiment(item)
                val.then(result => {
                    console.log('这是nav里面的result' + result)
                    this.tabData = result
                })
            },
            handleCurrentChange(page) {
                this.currentPage = page
            }

        },

        created() {
            if (this.$route.query.item) {
                this.getTabData(this.$route.query.item)
            }
        },
        mounted() {
            this.getTabData(this.$route.query.item)
        },
        watch: {
            '$route.query.item' (newValue, oldValue) {
                console.log('我是newval：', newValue)
                console.log('Data changed from ' + oldValue + ' to ' + newValue);
                this.getTabData(newValue)
            },
            filterTabData(newVal) {
                this.filteredData = newVal
            }
        },
    }
</script>
<style scoped>
    .inputAndSearch {
        display: flex;
        align-items: center;
    }
    
    .inputAndSearch .el-input {
        flex: 1;
        margin-right: 10px;
        width: 300px;
        height: 30px;
        box-sizing: border-box;
    }
    
    .inputAndSearch .el-button {
        height: 30px;
        padding: 0 15px;
        box-sizing: border-box;
    }
</style>