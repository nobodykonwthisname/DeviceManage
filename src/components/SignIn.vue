<template> 
   <div class="content-box">
            <div class="login">
               <br><br><br><br>
                <h2>你 好 !</h2>
                <p>豫 章 设 备 系 统 欢 迎 您 的 加 入 <br> <br> 一 起 加 入 我 们 吧！</p>
                <br>
                <button class="login_btn" @click="register">立即注册</button>
            </div>
            <div class="login">
                <br><br>
                <form action="">
                    <h2>登 入</h2>
                    <input type="text" name="usename" v-model="usename" placeholder=" 输入账户">
                    <input type="password" name="password" v-model="password" placeholder=" 输入密码">
                </form>
                <br><br>
                <button class="register-btn" @click="login">立即登录</button>
            </div>
    </div>
</template>
<meta http-equiv="Access-Control-Allow-Origin" content="*" />
<script>
    import {
        login
    } from '@/api/api.js'
    export default {
        name: 'SignIn',
        data() {
            return {
                usename: "",
                password: "",
            }
        },
        methods: {
            register() {
                this.$router.push('/SignUp')
            },
            //第一个login是该组件的功能函数
            login() {
                //第二个login是api里面的登录接口
                login({
                        usename: this.usename,
                        password: this.password
                    }).then((res) => {
                        if (res.data.status == 200 && res.data.role == 'manager')
                            this.$router.push('/MangeMent')
                        else {
                            console.log(this.usename)
                            this.$router.push({
                                path: '/userMainInterface',
                                query: {
                                    usename: this.usename
                                }
                            })
                        }
                        const token = res.data.token
                        if (token) {
                            localStorage.setItem('token', token)
                            console.log('这是token的数据！！！！！！！！！！！', token)
                        }
                        this.$message({
                            message: 'login success',
                            type: 'success'
                        })
                        console.log('登录成功')
                    })
                    .catch((err) => {
                        this.$message.error('账号或密码错误')
                        this.$router.push('/SignIn')
                        console.log(err)
                    })
            }
        }
    }
</script>


<style scoped>
    body {
        padding: 0;
        margin: 0;
        background-color: #ECF0F3;
    }
    
    .content-box {
        margin: 150px auto;
        width: 750px;
        height: 400px;
        display: flex;
        border-radius: 12px;
        box-shadow: 10px 10px 10px #d1d9e6, -10px -10px 10px #f9f9f9;
        ;
    }
    
    .register {
        height: 400px;
        width: 350px;
        text-align: center;
        background-color: #ECF0F3;
        z-index: 50;
    }
    /*  .register-right {
        z-index: 10;
        left: calc(100% - 600px);
    } */
    
    .login {
        height: 400px;
        width: 400px;
        text-align: center;
        box-shadow: -2px 0 0 #DEE4EB;
        background-color: #ECF0F3;
        z-index: 200;
    }
    
    button {
        width: 100px;
        height: 30px;
        border-radius: 25px;
        background-color: #4B70E2;
        border-style: none;
        color: white;
    }
    
    input {
        width: 200px;
        height: 25px;
        margin-top: 20px;
        border: none;
        border-radius: 5px;
        box-shadow: inset 2px 2px 4px #d1d9e6, inset -2px -2px 4px #f9f9f9;
        caret-color: red;
    }
    
    p {
        font-weight: 10;
        font-size: smaller;
    }
    
    @keyframes shake {
        0%,
        100% {
            transform: translateX(0);
        }
        10%,
        30%,
        50%,
        70%,
        90% {
            transform: translateX(-10px);
        }
        20%,
        40%,
        60%,
        80% {
            transform: translateX(10px);
        }
    }
    
    .shake {
        animation: shake .5s;
    }
</style>