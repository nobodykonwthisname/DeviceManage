<template>
  <div>
    <div ref="chart1" style="width:80%;height:556px;padding-left: 80px ;"></div>
  </div>
</template>
<script>
    export default {
        data() {
            return {
                used: [90, 92, 101, 50, 60, 40, 55, 23, 90, 48.61, 62, 65, 64, 67],
                maintence: [60, 61, 81, 35, 45, 33, 20, 10, 60, 10, 11, 12, 13, 14, 15]
            }
        },
        mounted() {
            this.getEchartData1()
        },
        methods: {
            //折线图展示
            getEchartData1() {
                var myChart
                const chart1 = this.$refs.chart1
                if (chart1) {
                    const myChart = this.$echarts.init(chart1)
                    const option = {
                        //标题
                        title: {
                            text: '使用次数'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },
                        legend: {
                            data: ['维修次数', '使用次数']
                        },
                        grid: {
                            left: '3%',
                            right: '4%',
                            bottom: '3%',
                            containLabel: true
                        },
                        toolbox: {
                            feature: {
                                saveAsImage: {}
                            }
                        },
                        xAxis: {
                            type: 'category',
                            boundaryGap: false,
                            data: ['手持终端', '打印机', '路由器', '投影仪', '电脑', '摄像头', '交换机', '录像机', '机柜', '饮水机', 'AP', 'AC', '鼠标', '键盘', '电灯']
                        },
                        yAxis: {
                            type: 'value',
                            /*  data: [50, 100, 150, 200] */
                        },
                        series: [{
                            name: '维修次数',
                            type: 'line',

                            data: this.maintence
                        }, {
                            name: '使用次数',
                            type: 'line',

                            data: this.used
                        }, ]

                    }
                    myChart.setOption(option)
                    window.addEventListener("resize", function() {
                        myChart.resize()
                    })
                }
                this.$on('hook:destroyed', () => {
                    window.removeEventListener("resize", function() {
                        myChart.resize();
                    });
                })
            },


        },
        watch: {},
        created() {}
    }
</script>