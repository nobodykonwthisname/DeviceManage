<template>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm">
   <el-form-item label="用户姓名" prop="name">
        <el-input v-model="ruleForm.name"></el-input>
    </el-form-item>
    <el-form-item label="用户账号" prop="usename">
        <el-input v-model="ruleForm.usename"></el-input>
    </el-form-item>
     <el-form-item label="用户密码" prop="password">
        <el-input v-model="ruleForm.password"></el-input>
    </el-form-item>
        <el-form-item label="用户年龄" prop="age">
        <el-input v-model="ruleForm.age"></el-input>
    </el-form-item>
        <el-form-item label="用户性别" prop="sex">
        <el-radio v-model="ruleForm.sex" label="1">男</el-radio>
            <el-radio v-model="ruleForm.sex" label="2">女</el-radio>
    </el-form-item>
      <el-form-item label="所属部门" prop="branch" style="width: 100%;">
        <el-select v-model="ruleForm.branch" placeholder="请选择所属部门">
                <el-option label="集团派驻" value="集团派驻"></el-option>
                <el-option label="运营部" value="运营部"></el-option>
                <el-option label="行政部" value="行政部"></el-option>
            </el-select>
    </el-form-item>
        <el-form-item label="用户电话" prop="phonenumber">
        <el-input v-model="ruleForm.phonenumber"></el-input>
    </el-form-item>
     <el-form-item label="用户邮箱" prop="email">
        <el-input v-model="ruleForm.email"></el-input>
    </el-form-item>
       
    <el-form-item>
        <el-button type="primary" @click="submitForm(ruleForm)">立即添加</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
    </el-form-item>
</el-form>
</template>
<script>
    import {
        getData,
    } from '@/api/api.js'
    import {
        addUserData
    } from '@/api/table.js'
    export default {
        data() {
            return {
                ruleForm: {
                    name: '',
                    usename: '',
                    branch: '',
                    sex: '1',
                    phonenumber: '',
                    age: '',
                    address: ''
                },
                rules: {
                    name: [{
                        required: true,
                        message: '请输入用户姓名'
                    }],
                    usename: [{
                        required: true,
                        message: '请输入用户账号'
                    }],
                    branch: [{
                        required: true,
                        message: '请选择所属部门',
                        trigger: 'change'
                    }],
                    email: [{
                        required: true,
                        message: '请输入用户邮箱'
                    }],
                    phonenumber: [{
                        required: true,
                        message: '请输入联系方式'
                    }],
                    age: [{
                        required: true,
                        message: '请输入用户年龄'
                    }],
                    address: [{
                        required: true,
                        message: '请输入用户地址'
                    }]
                }
            };
        },
        methods: {
            submitForm(ruleForm) {
                addUserData(this, ruleForm, getData, '/getUsersData')
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        }
    }
</script>

<style scoped>
    el-input {
        width: 200px;
    }
</style>