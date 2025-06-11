<template>
  <div class="carousel-container">
    <el-carousel :interval="5000" arrow="always" indicator-position="outside">
      <el-carousel-item v-for="(item, index) in announcementList" :key="index">
        <el-card shadow="hover" class="announcement-card" :header="item.title" :body-style="{ padding: '10px' }">
          <div class="announcement-content">{{ item.content }}</div>
        </el-card>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
    export default {
        name: 'indexLuobo',
        data() {
            return {
                announcementList: [{
                    title: '公告1',
                    content: '尊敬的管理员，为了保障设备管理系统的正常运行和数据安全，请勿将账号和密码泄露给他人，并定期更换密码。如发现异常操作或者账号被盗，请及时联系系统管理员进行处理。'
                }, {
                    title: '公告2',
                    content: '各位管理员注意，为提高设备使用效率和延长设备寿命，请合理安排设备使用时间，避免设备连续长时间使用而导致过热、故障等问题的出现。同时，使用完毕后请及时关机并妥善保管设备，确保设备得到良好的保存和维护。。'
                }, {
                    title: '公告3',
                    content: '尊敬的管理员，为进一步规范设备管理系统的使用，现对设备管理流程进行调整。具体内容请见最新版《设备管理制度》，请各位管理员认真阅读并按要求执行，如有任何疑问可随时联系系统管理员。谢谢配合！'
                }]
            };
        }
    };
</script>

<style scoped>
    .carousel-container {
        margin-top: 90px;
        margin-left: 100px;
        width: 1100px;
        height: 100px;
    }
    
    .announcement-card {
        margin-bottom: 20px;
        height: 700px;
    }
    
    .announcement-content {
        white-space: pre-wrap;
    }
    
    .el-carousel__indicators {
        display: none;
    }
</style>