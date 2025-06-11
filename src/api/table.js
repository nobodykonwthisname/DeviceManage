import { dataDelete, Add, updateData, getEquiment } from '@/api/api.js'

//删除操作封装（用户）
export function handleDelete(root, usename, pri, callFun, url) {
    root.$alert('你确定要进行此操作吗？', '提示', {
        confirmButtonText: '确定',
        callback: () => {
            dataDelete({
                    usename: usename,
                    pri: pri
                }, '/delete')
                .then(res => {
                    if (res.status === 200) {
                        root.$message({
                            message: '操作成功',
                            type: 'success'
                        })
                        callFun(root, url)
                    }
                }).catch((err) => {
                    console.log(err)
                })
        }
    })
}
//修改方法封装（用户）
export function updateUserData(root, callFun, url) {
    root.$refs.form.validate((valid) => {
        if (valid) {
            callFun(root, url)
            updateData(root.form, '/updateUser').then(res => {
                console.log(res)
                if (res.status === 200) {
                    callFun(root, url)
                    root.dialogFormVisible = false
                    root.$refs['form'].resetFields()
                    root.$message({
                        type: 'success',
                        message: res.data.msg
                    })
                }
            })
        } else {
            console.log("不合规")
        }
    })

}
//添加用户方法封装(用户)
export function addUserData(root, ruleForm, callFun, url) {
    root.$refs.ruleForm.validate((valid) => {
        if (valid) {
            console.log(ruleForm)
            Add(root.ruleForm, '/userDataAdd').then((res) => {
                if (res.data.status === 200) {
                    root.$message({
                        type: 'success',
                        message: res.data.msg
                    })
                    callFun(root, url)
                }
            })
        } else {
            console.log('error submit!!');
            return false;
        }
    });

}
export function addRegisteData(root, data, callFun, url) {
    Add(data, '/userActiveAdd').then((res) => {
        if (res.data.status === 200) {
            root.$message({
                type: 'success',
                message: res.data.msg
            })
            callFun(root, url)
        }
    })

}

//添加新设备信息
export function AddDevice(root, ruleForm) {
    console.log(ruleForm)
    root.$refs.ruleForm.validate((valid) => {
        if (valid) {
            console.log(ruleForm)
            Add(root.ruleForm, '/deviceDataAdd').then((res) => {
                if (res.data.status === 200) {
                    root.$message({
                        type: 'success',
                        message: res.data.msg
                    })
                }
            })
        } else {
            console.log('error submit!!');
            return false;
        }
    });
}
//删除申请表的操作（设备）
export function handleDeleteApplication(root, numbering, callFun, url) {
    console.log("这是handleDeleteApplication：" + numbering)
    dataDelete({
            numbering: numbering,
            pri: 2
        }, '/delete')
        .then(res => {
            if (res.status === 200) {
                root.$message({
                    message: '已拒绝',
                    type: 'success'
                })
                callFun(root, url)
            }
        }).catch((err) => {
            console.log(err)
            console.log("handleDeleteApplication错误：！！！！！！！！！！！！！！！！")
        })
}
//删除设备信息（设备）
export function handleDeleteDeviceDetail(root, numbering, pri, tabData, index) {
    root.$alert('你确定要进行此操作吗？', '提示', {
        confirmButtonText: '确定',
        callback: () => {
            dataDelete({
                    numbering: numbering,
                    pri: pri
                }, '/delete')
                .then(res => {
                    if (res.status === 200) {
                        root.$message({
                            message: '操作成功',
                            type: 'success'
                        })
                        console.log('删除设备成功')
                            //删除后更新数据
                        if (index !== -1) {
                            tabData.splice(index, 1)
                        }
                    }
                }).catch((err) => {
                    console.log(err)
                })
        }
    })
}

//修改设备状态信息（设备）
export function updateApplicationData(root, callFun, url) {
    root.$refs.form.validate((valid) => {
        if (valid) {
            callFun(root, url)
            updateData(root.form, '/updateApplication').then(res => {
                console.log(res)
                if (res.status === 200) {
                    callFun(root, url)
                    root.dialogFormVisible = false
                    root.$refs['form'].resetFields()
                    root.$message({
                        type: 'success',
                        message: res.data.msg
                    })
                }
            })
        } else {
            console.log("不合规")
        }
    })

}

//展示设备信息（设备）
export async function showEquiment(data) {
    var val;
    console.log('这是table的' + data)
    if (["集团派驻", '行政部', '财务部', '运营部'].includes(data)) {
        await getEquiment({ branch: data }, '/getEquipmentBranchData')
            .then(res => {
                if (res.status === 200) {
                    val = res.data
                }
            }).catch((err) => {
                console.log(err)
            });
        return val
    } else if (['手持终端', '打印机', '路由器'].includes(data)) {
        await getEquiment({ EquipmentType: data }, '/getEquipmentTypeData')
            .then(res => {
                if (res.status === 200) {
                    val = res.data
                }
            }).catch((err) => {
                console.log(err)
                console.log('我错啦???????????')
            })
        return val
    } else if (['闲置', '在用', '故障'].includes(data)) {
        await getEquiment({ status: data }, '/getEquipmentStatusData')
            .then(res => {
                if (res.status === 200) {
                    val = res.data
                }
            }).catch((err) => {
                console.log(err)
                console.log('我错啦???????????')
            })
        return val
    }
}