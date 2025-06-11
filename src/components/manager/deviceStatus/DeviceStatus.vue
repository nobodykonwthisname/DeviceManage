<template>
   <div>
     <div class="item" @click="handleSelect('闲置')">闲 置</div> 
    <div class="item" @click="handleSelect('在用')">在 用</div>
    <div class="item" @click="handleSelect('故障')">故 障</div>
   </div>
</template>

<style scoped>
    .item {
        width: 200px;
        height: 400px;
        font-size: 50px;
        color: white;
        float: left;
        margin-top: 100px;
        background-color: #D3DCE6;
        margin-left: 100px;
        border-radius: 5px;
        writing-mode: vertical-lr;
        /*从左向右 从右向左是 writing-mode: vertical-rl;*/
        writing-mode: tb-rl;
        /*IE浏览器的从左向右 从右向左是 writing-mode: tb-rl；*/
        text-align: center;
        display: flex;
        flex-direction: column;
        -webkit-display: flex;
        justify-content: center;
        box-shadow: 10px 10px 10px #d1d9e6, -10px -10px 10px #f9f9f9;
    }
    
    .item:hover {
        transform: scale(1.5, 1.2);
    }
</style>

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
        }
    }
</script>