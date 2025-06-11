<template>
    <el-row class="tac">
        <el-col :span="24">
            <el-menu default-active="2" class="el-menu-vertical-demo"  @open="handleOpen" @close="handleClose">
            <el-submenu index="1">
                    <template slot="title">
                            <i class="el-icon-location"></i>
                            <span>设备类型</span>
                    </template>

<el-menu-item-group @select="handleSelect">
    <!-- <template slot="title">分组一</template> -->
    <el-menu-item index="1-1" @click="handleSelect('手持终端')">手持终端</el-menu-item>
    <el-menu-item index="1-2" @click="handleSelect('打印机')">打印机</el-menu-item>
    <el-menu-item index="1-3" @click="handleSelect('路由器')">路由器</el-menu-item>
</el-menu-item-group>

</el-submenu>

<el-submenu index="2">
    <template slot="title">
        <i class="el-icon-menu"></i>
        <span>所属部门</span>
    </template>
    <el-menu-item-group>
        <!-- <template slot="title">分组一</template> -->
        <el-menu-item index="2-1" @click="handleSelect('集团派驻')">集团派驻</el-menu-item>
        <el-menu-item index="2-2" @click="handleSelect('财务部')">财务部</el-menu-item>
        <el-menu-item index="2-3" @click="handleSelect('运营部')">运营部</el-menu-item>
    </el-menu-item-group>

</el-submenu>

<el-menu-item index="3">
    <i class="el-icon-view"></i>
    <span slot="title" @click="RecordClick">维修记录</span>
</el-menu-item>

<el-menu-item index="4">
    <i class="el-icon-setting"></i>
    <span slot="title" @click="StatusClick">设备状态</span>
</el-menu-item>

<el-menu-item index="5">
    <i class="el-icon-s-data"></i>
    <span slot="title" @click="DeviceFixingAnalyse">故障分析</span>
</el-menu-item>

<el-menu-item index="6">
    <i class="el-icon-chat-round"></i>
    <span slot="title" @click="MessageClick">消息管理</span>
</el-menu-item>

<el-menu-item index="7">
    <i class="el-icon-s-custom"></i>
    <span slot="title" @click="UserClick">用户频道</span>
</el-menu-item>

</el-menu>
</el-col>
</el-row>
</template>

<script>
    export default {
        methods: {
            handleSelect(item) {
                console.log(item)
                this.$router.push({
                    path: '/MangeMent/CommonTabs',
                    query: {
                        item: item
                    }
                })
            },
            handleOpen(key, keyPath) {
                console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
            },
            UserClick() {
                this.$router.push('/MangeMent/MyTabs');
            },
            MessageClick() {
                this.$router.push('/MangeMent/MessageMent');
            },
            DeviceFixingAnalyse() {
                this.$router.push('/MangeMent/FixingAnalyse')
            },
            RecordClick() {
                this.$router.push('/MangeMent/MaintainRecord')
            },
            StatusClick() {
                this.$router.push('/MangeMent/DeviceStatus')
            }
        }
    }
</script>

<style scoped>
    .el-menu {
        background-color: #D3DCE6;
        color: #333;
        text-align: left;
        line-height: 60px;
    }
</style>