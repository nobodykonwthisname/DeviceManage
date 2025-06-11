<template>
  <div>
    <el-tabs>
      <el-tab-pane label="设备申请">
        <el-table :data="applyData" style="width: 100%">
          <el-table-column prop="numbering" label="设备编号"></el-table-column>
          <el-table-column prop="nickname" label="设备名称"></el-table-column>
          <el-table-column prop="place" label="使用场所"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button type="danger" size="mini" @click="handleCancel(scope.row)">撤销</el-button>
            </template>
</el-table-column>
</el-table>
<el-pagination v-model="currentPage" :page-size="pageSize" :total="applyDatatotal" @current-change="fetchData">
</el-pagination>
</el-tab-pane>
<el-tab-pane label="设备归还">
    <el-table :data="giveBackData" style="width: 100%">
        <el-table-column prop="numbering" label="设备编号"></el-table-column>
        <el-table-column prop="nickname" label="设备名称"></el-table-column>
        <el-table-column prop="place" label="使用场所"></el-table-column>
        <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button type="danger" size="mini" @click="handleCancel(scope.row)">撤销</el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-pagination v-model="currentPage" :page-size="pageSize" :total="giveBackDatatotal" @current-change="fetchData">
    </el-pagination>
</el-tab-pane>
<el-tab-pane label="设备报修">
    <el-table :data="repairsData" style="width: 100%">
        <el-table-column prop="numbering" label="设备编号"></el-table-column>
        <el-table-column prop="nickname" label="设备名称"></el-table-column>
        <el-table-column prop="situation" label="故障情况"></el-table-column>
        <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button type="danger" size="mini" @click="handleCancel(scope.row)">撤销</el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-pagination v-model="currentPage" :page-size="pageSize" :total="repairsDatatotal" @current-change="fetchData">
    </el-pagination>
</el-tab-pane>
</el-tabs>
</div>
</template>

<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                applyData: [],
                giveBackData: [],
                repairsData: [],
                currentPage: 1,
                pageSize: 5,
                applyDatatotal: 1,
                giveBackDatatotal: 1,
                repairsDatatotal: 1
                    // 类似的归还和报修处理数据...
            };
        },
        methods: {
            fetchData() {

            },
            handleCancel(row) {
                this.$confirm('确定要撤销该申请吗？', '提示', {
                        confirmButtonText: '确定',
                        cancelButtonText: '取消',
                        type: 'warning'
                    })
                    .then(() => {
                        // 发送撤销请求，并更新数据
                        const index = this.applyData.indexOf(row);
                        this.applyData.splice(index, 1);
                        this.$message.success('操作已撤销');
                        console.log(row)
                        console.log(index)
                    })
                    .catch(() => {});
            },
        },
        mounted() {
            console.log('这是processingProgress')
            axios.get('/api/user/getApplicationData').then(response => {
                this.applyData = response.data;

            }).catch(error => {
                console.error(error);
            });
            axios.get('/api/user/getOwnData').then(response => {
                this.giveBackData = response.data;
                console.log('1232212', response.data)
            }).catch(error => {
                console.error(error);
            });
            axios.get('/api/user/getRepairsData').then(response => {
                console.log('789987789987', response.data)
                this.repairsData = response.data;
            }).catch(error => {
                console.error(error);
            });
        }
    };
</script>