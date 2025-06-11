//该文件专门用于创建整个应用的路由器
import VueRouter from 'vue-router'
//引入组件
import SignIn from "../components/SignIn"
import SignUp from '../components/SignUp'
import MangeMent from '../components/manager/index/MangeMent'
import MyTabs from '../components/manager/users/MyTabs'
import MessageMent from '../components/manager/meaasage/MessageMent'
import FixingAnalyse from '../components/manager/fixing/FixingAnalyse'
import MaintainRecord from '../components/manager/repairRecord/MaintainRecord'
import DeviceStatus from '../components/manager/deviceStatus/DeviceStatus'
import CommonTabs from '../components/manager/commonTem/CommonTabs'
import echartsShow from '../components/manager/fixing/echartsShow'
//用户界面的组件引入
import userMainInterface from '../components/user/index/userMainInterface'
import InfoDisplay from '../components/user/personal/InfoDisplay'
import InfoEdit from '../components/user/personal/InfoEdit'
import indexLuobo from '../components/manager/index/indexLuobo.vue'
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(err => err)
}

//创建并暴露一个路由器
export default new VueRouter({
    routes: [{
            path: '/',
            redirect: '/SignIn',
            component: SignIn
        },
        {
            path: '/SignUp',
            component: SignUp
        },
        {
            path: '/SignIn',
            component: SignIn
        },
        {
            path: '/MangeMent',
            component: MangeMent,
            children: [{
                    path: '',
                    component: indexLuobo,

                }, {
                    path: 'CommonTabs',
                    component: CommonTabs
                }, {
                    path: 'MyTabs',
                    component: MyTabs
                },
                {
                    path: 'MessageMent',
                    component: MessageMent
                },
                {
                    path: 'FixingAnalyse',
                    component: FixingAnalyse
                },
                {
                    path: 'echartsShow',
                    component: echartsShow
                },
                {
                    path: 'MaintainRecord',
                    component: MaintainRecord
                },
                {
                    path: 'DeviceStatus',
                    component: DeviceStatus
                }
            ]
        },
        {
            path: '/userMainInterface',
            component: userMainInterface,
            children: [{
                    path: '',
                    component: InfoDisplay
                },
                {
                    path: 'InfoDisplay',
                    component: InfoDisplay
                }, {
                    path: 'InfoEdit',
                    component: InfoEdit
                },


            ]
        }
    ]
})