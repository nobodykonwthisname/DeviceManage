<template>
  <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="用户注册消息" name="first"> 
        <UserRegister/>
    </el-tab-pane>
    <el-tab-pane label="用户申请消息" name="second">
        <UserApplication/>
    </el-tab-pane>
    <el-tab-pane label="用户反馈消息" name="third">
        <FeedBack/>
    </el-tab-pane>
  </el-tabs>
</template>
<script>
    import UserRegister from './UserRegister'
    import UserApplication from './UserApplication'
    import FeedBack from '../feedback/FeedBack'
    export default {
        name: 'MessageMent',
        data() {
            return {
                activeName: 'first'
            };
        },
        components: {
            FeedBack,
            UserApplication,
            UserRegister

        },
        methods: {
            handleClick() {

            }
        }
    };
</script>