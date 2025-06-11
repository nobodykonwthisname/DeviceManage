<template>
  <el-container class="container">
    <el-header>
      <el-menu :default-active="activeIndex" class="menu" mode="horizontal" @select="handleSelect">
        <el-submenu index="1">
          <template slot="title">设备处理</template>
<el-menu-item index="2-1">设备申请</el-menu-item>
<el-menu-item index="2-2">归还报修</el-menu-item>
</el-submenu>
<el-menu-item index="2">处理进度</el-menu-item>
<el-menu-item index="3">信息反馈</el-menu-item>
<el-menu-item index="4">个人中心</el-menu-item>
</el-menu>
</el-header>

<el-main>
    <div v-if="activeIndex === '1-1'" class="index">
        <el-carousel :interval="4000" type="card" height="400px">
            <el-carousel-item v-for="(item, index) in picture" :key="index">
                <img :src="require(`@/static/${item}`)" alt="image" class="carousel-image" />
            </el-carousel-item>
        </el-carousel>
    </div>
    <div v-if="activeIndex === '2-1'" class="form-wrapper">
        <avaliableDevice></avaliableDevice>
    </div>
    <div v-if="activeIndex === '2-2'">
        <ownAndRepair :uname="username"></ownAndRepair>
    </div>
    <div v-if="activeIndex === '2'">
        <processingProgress :name="username"></processingProgress>
    </div>
    <div v-if="activeIndex === '3'">
        <InfomationFeedback></InfomationFeedback>
    </div>
    <div v-if="activeIndex === '4'">
        <personalDetail :name="username"></personalDetail>
    </div>
</el-main>
</el-container>
</template>

<script>
    import personalDetail from '../personal/personalDetail.vue'
    import InfomationFeedback from '../feedback/InfomationFeedback.vue'
    import processingProgress from '../processingProgress/processingProgress.vue'
    import avaliableDevice from '../equipmentProcessing/avaliableDevice.vue'
    import ownAndRepair from '../equipmentProcessing/ownAndRepair.vue'
    import {
        mapGetters
    } from 'vuex';
    export default {
        components: {
            personalDetail,
            InfomationFeedback,
            processingProgress,
            avaliableDevice,
            ownAndRepair
        },
        data() {
            return {
                activeIndex: '1-1',

                picture: [
                    'picture1.png',
                    'picture2.png',
                    'picture3.png'
                ]
            };
        },
        computed: {
            // 获取 Vuex 中保存的用户名信息
            ...mapGetters(['getUsername']),
            //
            username() {
                return this.getUsername; // 将获取到的 getUsername 值返回给 username 计算属性
            },

        },
        created() {

        },
        methods: {
            handleSelect(index) {
                this.activeIndex = index;
                console.log('258', this.username)
            },

        },
    };
</script>

<style scoped>
    .container {
        margin: 45px;
        width: 1400px;
        height: 700px;
        background-color: #f5f5f5;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
    
    .menu {
        background-color: #fff;
    }
    
    .menu::after {
        content: '';
        display: block;
        position: absolute;
        left: 50%;
        bottom: -10px;
        transform: translateX(-50%);
        width: 0;
        height: 0;
        border-top: 10px solid #fff;
        border-left: 10px solid transparent;
        border-right: 10px solid transparent;
    }
    
    .el-menu-demo .el-submenu__title {
        color: #666;
    }
    
    .el-menu-demo .el-submenu__title:hover {
        background-color: #f2f2f2;
    }
    
    .el-main {
        height: 300px;
    }
    
    .el-main>div {
        background-color: #fff;
        padding: 20px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
    
    .form-wrapper {
        display: flex;
        justify-content: center;
        /* 水平居中对齐 */
        align-items: center;
        /* 垂直居中对齐 */
    }
    
    .el-carousel__item h3 {
        color: #475669;
        font-size: 14px;
        opacity: 0.75;
        line-height: 200px;
        margin: 0;
    }
    
    .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
    }
    
    .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
    }
    
    .carousel-image {
        object-fit: cover;
        object-position: center;
        width: 100%;
        height: 100%;
    }
</style>