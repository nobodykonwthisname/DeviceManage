import axios from "axios";
import { getToken } from '@/api/setToken';
import { Message } from "element-ui";
const service = axios.create({
    baseURL: '/api',
    timeout: 3000
})

//添加请求拦截器
service.interceptors.request.use((config) => {
    //在请求之前做些什么（获取并设置token）
    config.headers['token'] = getToken('token')
    return config
}, (error) => {
    return Promise.reject(error)
})

//添加响应拦截器
service.interceptors.response.use((response) => {
    //对响应数据做什么
    //console.log(response)
    let { status, message } = response
    //console.log('service的' + status)
    if (status != 200) {
        Message({ message: message || 'error', type: 'warning' })
    }
    return response
}, (error) => {
    return Promise.reject(error)
})

export default service