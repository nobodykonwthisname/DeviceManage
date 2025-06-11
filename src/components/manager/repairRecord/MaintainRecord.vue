<template>
    <div class="block">
  <el-timeline>
    <el-timeline-item timestamp="2018/4/12" placement="top" class="record">
      <el-card>
        <h4>王小虎对编号ly1117小米路由器设备进行了维修，该设备维修次数现为19，使用次数为3</h4>
        <p>王小虎 提交于 2018/4/12 20:46</p>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2018/4/3" placement="top" class="record">
      <el-card>
        <h4>王小虎对编号ly1116小米路由器设备进行了维修，该设备维修次数现为18，使用次数为3</h4>
        <p>王小虎 提交于 2018/4/3 20:46</p>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2018/4/2" placement="top" class="record">
      <el-card>
        <h4>王小虎对编号ly1115小米路由器设备进行了维修，该设备维修次数现为17，使用次数为3</h4>
        <p>王小虎 提交于 2018/4/2 20:46</p>
      </el-card>
    </el-timeline-item>
  </el-timeline>
</div>
</template>

<script>
    export default {
        name: 'MaintainRecord'
    }
</script>

<style scoped>
    .record {
        width: 700px;
    }
</style>