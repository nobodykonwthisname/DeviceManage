import service from "@/service";

//登录接口
export function login(usename) {
    return service({
        method: 'post',
        url: '/login',
        data: usename
    })
}

//增：注册接口
export function register(data, aimurl) {
    return service({
        method: 'post',
        url: aimurl,
        data
    })
}
//管理员界面进行增加数据
//增：
export function Add(data, aimurl) {
    data = JSON.stringify(data)
    console.log('这还是修改Add的消息' + data)
    return service({
        method: 'post',
        url: aimurl,
        data
    })

}

//删：删除接口
export function dataDelete(data, aimurl) {
    return service({
        method: 'post',
        url: aimurl,
        data
    })

}
//改：修改信息
export function updateData(data, aimurl) {
    data = JSON.stringify(data)
    console.log('这还是修改api的消息' + data)
    return service({
        method: 'post',
        url: aimurl,
        data
    })
}
//查：展示数据
export function getData(root, url, params) {
    root.service.get(url, { params: params || {} })
        .then(res => {
            console.log(res)
            if (res.status === 200) {
                console.log('这里是getDATA', res)
                root.tableData = res.data
                root.total = res.data.length
            }
        })
        .catch(err => {
            throw err
        })
}
//展示设备信息
export function getEquiment(data, aimurl) {
    data = JSON.stringify(data)
    return service({
        method: 'post',
        url: aimurl,
        data
    })
}