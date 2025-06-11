<template>
  <div class="user-profile">
    <div class="sidebar">
      <el-menu :default-active="$route.path" class="el-menu-vertical-demo" @select="handleSelect">
        <el-menu-item index="/userMainInterface/InfoDisplay">信息展示</el-menu-item>
        <el-menu-item index="/userMainInterface/InfoEdit">信息修改</el-menu-item>
        <el-menu-item index="/SignIn">退出</el-menu-item>
      </el-menu>
    </div>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
    export default {
        methods: {
            handleSelect(index) {
                this.$router.push(index);
            },
        },
    };
</script>

<style scoped>
    body {
        font-family: "Helvetica Neue", Arial, sans-serif;
    }
    
    .info-display .card-content {
        padding: 20px;
    }
    
    .info-edit {
        max-width: 600px;
        margin: 0 auto;
    }
    
    .el-form-item__label {
        font-size: 14px;
        color: #666;
    }
    
    .user-profile {
        display: flex;
        height: 100%;
    }
    
    .sidebar {
        width: 200px;
        background-color: #f2f2f2;
    }
    
    .content {
        flex: 1;
        height: 500px;
        padding: 20px;
    }
    
    .el-menu-vertical-demo {
        height: 539px;
    }
</style>