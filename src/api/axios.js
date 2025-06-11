// // 引入 封装的api 
import api from './api.js';

//下面是简写的形式
// getXXX 自定义的接口名字


// export const getXXX = (params) => api.get(`/apigb/v1/component`, { params})
// export const postXXX = (params) => api.post(`/apigb/v1/component/update-info`, params)


// // 下面是详细的写法
export const getServer = (params) => api({
    url: 'http://127.0.0.1:5000', // 请求地址
    method: 'post', // 请求方式
    data: params, // (一般post请求，我们习惯使用 data属性来传参)
    params: params //(一般get请求，我们习惯使用params属性来传参）
        //     // 注意：data，和 params 两个属性传参使用，并不是固定的，也可以调换使用。
})
export default getServer