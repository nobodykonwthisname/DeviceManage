import Vue from 'vue'
import App from './App.vue'
//引入路由组件
import VueRouter from 'vue-router'
import router from './router'
//引入ElementUI组件库 
import ElementUI from 'element-ui';
//引入ElementUI全部样式 
import 'element-ui/lib/theme-chalk/index.css';
//引入store
import store from './components/user/store/store.js'
import service from './service';
// 引入echarts
import * as echarts from 'echarts'
Vue.prototype.$echarts = echarts

Vue.prototype.service = service

Vue.config.productionTip = false
    //使用ElementUI 
Vue.use(ElementUI)
Vue.use(VueRouter)

new Vue({
    el: "#app",
    render: h => h(App),
    store, // 将 store 与根 Vue 实例关联
    router: router,

})