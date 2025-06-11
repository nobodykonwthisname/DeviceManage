<template>
    <el-card>
    <el-table :data="compData" style="width: 100%">
        <el-table-column prop="name" label="姓名" width="180">
        </el-table-column>
        <el-table-column prop="branch" label="单位">
        </el-table-column>
        <el-table-column prop="phonenumber" label="联系电话">
        </el-table-column>
        <el-table-column prop="email" label="email">
        </el-table-column>
        <el-table-column prop="tel" label="部门电话">
        </el-table-column>
        <el-table-column prop="address" label="地址">
        </el-table-column>

        <el-table-column label="操作">
            <!--eslint-disable-next-line-->
            <template slot-scope="scope">
                    <el-button
                    size="mini"
                    @click="handleEdit(scope.row)">编辑</el-button>
                    <el-button
                    size="mini"
                    type="danger"
                    @click="handleDelete(scope.row)">删除</el-button>
                    </template>
</el-table-column>
</el-table>
<el-dialog title="用户信息编辑" :visible.sync="dialogFormVisible" width="600px" height="500px">
    <el-form :model="form" ref="form" :rules="rules">
        <el-form-item label="姓名" :label-width="formLabelWidth" prop="name">
            <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="性别" :label-width="formLabelWidth" prop="sex">
            <el-radio v-model="form.sex" label="1">男</el-radio>
            <el-radio v-model="form.sex" label="2">女</el-radio>
        </el-form-item>
        <el-form-item label="部门" :label-width="formLabelWidth" prop="branch">
            <el-select v-model="form.branch" placeholder="请选择活动区域">
                <el-option label="集团派驻" value="集团派驻"></el-option>
                <el-option label="运营部" value="运营部"></el-option>
                <el-option label="行政部" value="行政部"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="邮箱" :label-width="formLabelWidth" prop="email">
            <el-input v-model="form.email" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="电话" :label-width="formLabelWidth" prop="phonenumber">
            <el-input v-model="form.phonenumber" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="年龄" :label-width="formLabelWidth" prop="age">
            <el-input v-model="form.age" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="住址" :label-width="formLabelWidth" prop="address">
            <el-input v-model="form.address" autocomplete="off"></el-input>
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
<!-- 分页功能-->
<el-pagination :page-size="3" :page-sizes="[3,5]" @current-change="handleCurrentChange" background layout="prev, pager, next" :total="15">
</el-pagination>

</el-card>

</template>
<script>
    import {
        getData
    } from '@/api/api.js'
    import {
        handleDelete,
        updateUserData
    } from '@/api/table.js'
    export default {
        data() {
            return {
                tableData: [],
                currentPage: 1,
                pageSize: 0,
                total: 0,
                form: {
                    name: '',
                    branch: '',
                    sex: '1',
                    phonenumber: '',
                    age: '',
                    address: ''
                },
                dialogFormVisible: false,
                formLabelWidth: '80px',
                rules: {
                    name: [{
                        required: true,
                        message: '请输入姓名'
                    }],
                    branch: [{
                        required: true,
                        message: '请选择部门'
                    }],
                    email: [{
                        required: true,
                        message: '请输入邮箱'
                    }],
                    phonenumber: [{
                        required: true,
                        message: '请输入联系方式'
                    }],
                    age: [{
                        required: true,
                        message: '请输入年龄'
                    }],
                    address: [{
                        required: true,
                        message: '请输入地址'
                    }]
                }
            }
        },
        computed: {
            compData() {
                return this.tableData.slice((this.currentPage - 1) * 5, this.currentPage * 5)
            }
        },
        methods: {
            handleEdit(row) {
                this.dialogFormVisible = true
                this.form = row
            },
            handleCurrentChange(val) {
                this.currentPage = val
            },
            handleDelete(row) {
                console.log(row)
                handleDelete(this, row.usename, 0, getData, '/getUsersData')
            },
            dialogEdit(row) {
                console.log(row)
                console.log('这是dialog' + this.form.name)
                updateUserData(this, getData, '/getUsersData')
            }
        },
        mounted() {
            getData(this, '/getUsersData')
        }
    }
</script>

<style scoped>
    el-radio {
        float: left;
    }
</style>