<template>
  <div class="user-info">
    <el-form ref="form" :model="form" label-width="100px">
      <el-form-item label="姓名">
        <span class="form-value">{{ form.name }}</span>
      </el-form-item>
      <el-form-item label="账号">
        <span class="form-value">{{ form.username }}</span>
      </el-form-item>
      <el-form-item label="性别">
        <span class="form-value">{{ form.gender }}</span>
      </el-form-item>
      <el-form-item label="年龄">
        <span class="form-value">{{ form.age }}</span>
      </el-form-item>
      <el-form-item label="邮箱">
        <span class="form-value">{{ form.email }}</span>
      </el-form-item>
      <el-form-item label="电话">
        <span class="form-value">{{ form.phone }}</span>
      </el-form-item>
      <el-form-item label="地址">
        <span class="form-value">{{ form.address }}</span>
      </el-form-item>
      
    </el-form>
  </div>
</template>

<script>
    export default {
        data() {
            return {
                form: {
                    name: '张三',
                    password: '123456',
                    email: 'example@example.com',
                    phone: '12345678901',
                    address: '北京市朝阳区',
                    username: 'zhangsan',
                    gender: '男',
                    age: 20
                },


            }
        },

    }
</script>

<style scoped>
    .user-info {
        height: 500px;
        overflow-y: auto;
        margin-left: 80px;
    }
    
    .el-form {
        width: 400px;
        margin: 0;
        float: left;
    }
    
    .el-form-item__label {
        display: inline-block;
        width: 100px;
        padding-right: 10px;
        text-align: right;
        font-weight: bold;
    }
    
    .form-value {
        display: inline-block;
        margin-left: 12px;
        vertical-align: middle;
        font-weight: normal;
    }
    
    .pwd-container {
        position: relative;
    }
    
    .pwd-container .el-button {
        position: absolute;
        right: 0;
        top: 50%;
        transform: translateY(-50%);
    }
</style>