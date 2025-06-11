<template>
   <div id="FeedBack">
    <ul>
        <li v-for="item in FeedbackData" :key="item.id">
            <div id="name">{{item.name}}&nbsp;&nbsp;&nbsp;{{item.time}}</div>
            
            <br>
            <div id="content">{{item.content}}</div>
        </li>
        
    </ul>
   </div>
</template>
<style>
    .FeedBack {
        width: 1300px;
        height: 500px;
        background-color: white;
    }
</style>

<script>
    import {
        getData
    } from '@/api/api.js'
    export default {
        data() {
            return {
                FeedbackData: [{
                    'name': '张老五',
                    'usename': 'zhanglaowu',
                    'time': '2023/02/06 20:00:01',
                    'content': '该设备管理系统的数据库采用MySQL关系型数据库，因其开源、易于安装、可扩展性好等优点被广泛应用于Web应用程序的数据存储。在数据库设计上，采用了实体-关系模型（ER模型）进行建模，通过对设备、用户、操作记录等核心实体的分析，建立了相应的数据表及其之间的关系。同时，为提高查询效率，对常用的查询进行了索引优化。'
                }, {
                    'name': '王老三',
                    'usename': 'wanglaosan',
                    'time': '2023/02/06 20:00:01',
                    'content': '该设备管理系统的数据库采用MySQL关系型数据库，因其开源、易于安装、可扩展性好等优点被广泛应用于Web应用程序的数据存储。在数据库设计上，采用了实体-关系模型（ER模型）进行建模，通过对设备、用户、操作记录等核心实体的分析，建立了相应的数据表及其之间的关系。同时，为提高查询效率，对常用的查询进行了索引优化。'
                }, {
                    'name': '李全蛋',
                    'usename': 'liquandan',
                    'time': '2023/02/06 20:00:01',
                    'content': '该设备管理系统的数据库采用MySQL关系型数据库，因其开源、易于安装、可扩展性好等优点被广泛应用于Web应用程序的数据存储。在数据库设计上，采用了实体-关系模型（ER模型）进行建模，通过对设备、用户、操作记录等核心实体的分析，建立了相应的数据表及其之间的关系。同时，为提高查询效率，对常用的查询进行了索引优化。'
                }]


            }
        },
        mounted() {
            getData(this, '/getUsersData')
        }
    }
</script>

<style>
    li {
        list-style-type: none;
    }
    
    #name {
        float: left;
    }
    
    #content {
        text-indent: 35px;
        width: 1000px;
        line-height: 25px;
        text-align: left;
    }
</style>