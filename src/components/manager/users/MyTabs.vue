<template>
  <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="用户管理" name="first"> 
        <MyDetails/>
    </el-tab-pane>
    <el-tab-pane label="添加用户" name="second">
        <MyAdd/>
    </el-tab-pane>
   <!--  <el-tab-pane label="角色管理" name="third">角色管理</el-tab-pane>
    <el-tab-pane label="定时任务补偿" name="fourth">定时任务补偿</el-tab-pane> -->
  </el-tabs>
</template>
<script>
    import MyAdd from './MyAdd'
    import MyDetails from './MyDetails'
    export default {
        name: 'MyTabs',
        data() {
            return {
                activeName: 'first'
            };
        },
        components: {
            MyDetails,
            MyAdd

        },
        methods: {
            ShowUserData() {
                confirm("创建好了")
            },
            handleClick() {}
        }
    };
</script>