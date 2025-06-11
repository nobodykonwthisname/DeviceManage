<template>
  <div class="feedback">
   <el-form ref="form" :model="form" label-width="100px" class="form-container">
  <el-form-item label="设备名称" class="label-left" style="margin-top: 10px; width: 100%;">
    <el-input v-model="form.deviceName"></el-input>
  </el-form-item>
  <el-form-item label="设备编号" class="label-left" style="width: 100%;">
    <el-input v-model="form.deviceNumber"></el-input>
  </el-form-item>
  <el-form-item label="设备类型" class="label-left" style="width: 100%;">
    <el-select v-model="form.deviceType" placeholder="请选择设备类型">
      <el-option label="手持终端" value="handheld"></el-option>
      <el-option label="路由器" value="router"></el-option>
      <el-option label="其他" value="other"></el-option>
    </el-select>
  </el-form-item>
  <el-form-item label="意见反馈" class="label-left" style="width: 100%;">
    <el-input
      type="textarea"
      :rows="10"
      placeholder="请输入您的反馈意见"
      v-model="form.feedback"
      :autosize="{ minRows: 10, maxRows: 10 }"
    ></el-input>
  </el-form-item>
</el-form>

    <el-button class="submit-btn" type="primary" size="medium" @click="onSubmit">提交反馈</el-button>
  </div>
</template>

<script>
    export default {
        data() {
            return {
                form: {
                    deviceName: "",
                    deviceNumber: "",
                    deviceType: "",
                    feedback: "",
                },
            };
        },
        methods: {
            onSubmit() {
                const feedbackTime = new Date().toLocaleString();
                const content = `设备名称：${this.form.deviceName}\n设备编号：${this.form.deviceNumber}\n设备类型：${this.form.deviceType}\n意见反馈：${this.form.feedback}`;
                const data = {
                    account: "example",
                    name: "张三",
                    content,
                    time: feedbackTime,
                };
                console.log(data);
                this.$message({
                    message: '反馈提交完毕',
                    type: 'success'
                });
                this.form = {
                    deviceName: "",
                    deviceNumber: "",
                    deviceType: "",
                    feedback: "",
                }
            },
        },
    };
</script>

<style scoped>
    .feedback {
        height: 700px;
        overflow-y: auto;
        margin-top: 10px;
        display: flex;
        overflow: hidden;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
    }
    
    .form-container {
        width: 80%;
        margin-left: 20px;
        margin-top: 10px;
        /* 或者其他合适的值 */
    }
    
    .label-left .el-form-item__label {
        text-align: left;
    }
    
    .el-input {
        width: 100%;
        margin-bottom: 20px;
    }
    
    .el-select {
        width: 100%;
    }
    
    .submit-btn {
        margin-top: 10px;
        align-self: center;
    }
</style>