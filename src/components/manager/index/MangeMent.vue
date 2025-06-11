<template>
    <el-container>
       <div id="aside">
                    <el-col :span="12">
                    <!--账户头像-->
                    <div class="demo-basic--circle">
                        <div class="block"><el-avatar :size="90" :src="(`@/static/picture.jpg`)" style="margin:36px;"></el-avatar></div>
                    </div>
                    </el-col>  
                    <NavMenu/>
            </div>
            <el-container>
                    <el-header>
                        <el-breadcrumb separator="/"><br><br/>
                                <el-breadcrumb-item style="float: right;">
                                    <button class="el-icon-switch-button" @click="logout()"></button>
                                </el-breadcrumb-item>
                        </el-breadcrumb>
                    </el-header>
            <el-main>
                 <router-view></router-view>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
    import NavMenu from './NavMenu.vue';
    export default {
        name: 'MangerMent',
        components: {
            NavMenu,
        },
        methods: {
            //退出按钮
            logout() {
                this.$router.push('/SignIn');
            }
        }
    }
</script>

<style>
    #aside {
        width: 200px;
        height: auto!important;
        min-height: 600px;
        height: 600px;
        background-color: #D3DCE6;
    }
    
    .demo-basic--circle {
        width: 199.2px;
        height: 150px;
    }
    
    button {
        background-color: #D2DCE6;
        border: none;
    }
    
    .el-header {
        background-color: #D3DCE6;
        color: #333;
        text-align: center;
        line-height: 60px;
    }
    
    .el-footer {
        background-color: #B3C0D1;
        color: #333;
        text-align: center;
        line-height: 60px;
    }
    
    .el-aside {
        height: auto;
        background-color: #D3DCE6;
        color: #333;
        text-align: center;
        line-height: 200px;
    }
    
    .el-main {
        height: 660px;
        background-color: #E9EEF3;
        color: #333;
        text-align: center;
        line-height: 90px;
    }
    
    body>.el-container {
        margin-bottom: 40px;
    }
    
    .el-container:nth-child(5) .el-aside,
    .el-container:nth-child(6) .el-aside {
        line-height: 260px;
    }
    
    .el-container:nth-child(7) .el-aside {
        line-height: 320px;
    }
</style>