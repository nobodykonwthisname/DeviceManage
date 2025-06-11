<template>
    <div>
        <el-button type="plain" style="float: right;">新增部门</el-button>
        <el-card class="box-card">
        <div  @click="branch1">
            集团派驻
        </div>
        </el-card>
        <el-card class="box-card">
        <div  >
            运营部
        </div>
        </el-card>
        <el-card class="box-card">
        <div  >
            财务部
        </div>
        </el-card>
      
    </div>   
</template>

<style>
    .box-card {
        width: 240px;
        height: 130px;
        float: left;
        margin: 20px;
        margin-top: 50px;
        margin-left: 50px;
    }
    
    .box-card:hover {
        transform: scale(1.5);
    }
</style>

<script>
    export default {
        name: 'FixingAnalyse',
        methods: {
            branch1() {
                //获取到数据used和maintenance
                //跳转到echartsShow路由
                this.$router.push('/MangeMent/echartsShow')
            }
        }
    }
</script>