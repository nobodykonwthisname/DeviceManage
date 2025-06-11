<template>
  <div class="info-edit">
    <el-form ref="editForm" :model="userInfo" label-position="left" label-width="80px">
      <el-form-item label="姓名" prop="name">
        <el-input v-model="userInfo.name"></el-input>
      </el-form-item>
      <el-form-item label="性别" prop="gender">
        <el-radio-group v-model="userInfo.gender">
          <el-radio label="男">男</el-radio>
          <el-radio label="女">女</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="年龄" prop="age">
        <el-input v-model.number="userInfo.age" type="number"></el-input>
      </el-form-item>
      <el-form-item label="电话" prop="phone">
        <el-input v-model="userInfo.phone"></el-input>
      </el-form-item>
      <el-form-item label="邮箱" prop="email">
        <el-input v-model="userInfo.email"></el-input>
      </el-form-item>
      <el-form-item label="地址" prop="address">
        <el-input v-model="userInfo.address"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleSubmit">保存</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
    export default {
        data() {
            return {
                userInfo: {
                    name: "张三",
                    gender: "男",
                    age: 20,
                    email: 'example@example.com',
                    phone: "13888888888",
                    address: "北京市海淀区",
                },
            };
        },
        methods: {
            handleSubmit() {
                this.$refs.editForm.validate(valid => {
                    if (valid) {
                        // 提交表单数据到后端
                        console.log(this.userInfo);

                        // 返回上一级路由
                        this.$router.go(-1);
                    } else {
                        console.log("表单校验失败！");
                        return false;
                    }
                });
            },
        },
    };
</script>

<style scoped>
    .info-edit {
        max-width: 600px;
        margin: 0 auto;
    }
</style>