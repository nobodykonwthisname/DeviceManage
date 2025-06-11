<template> 
    <div class="content-box">
            <div class="login">
                <br><br>
                <form action="">
                    <h2>注 册</h2>
                    <input type="text" name="usename" v-model="usename" placeholder="输入账户">
                     <input type="password" name="password" v-model="password" placeholder=" 输入密码">
                    <input type="email" name="email" v-model="email" required placeholder=" 输入邮箱">
                </form>
                <br><br>
                <button class="register-btn" @click="register">立即注册</button>
            </div>
            <div class="login">
                <br><br><br><br>
                <h2>欢 迎 您 ！</h2>
                <p>让 我 们 在 这 里 开 启 我 们 的 旅 程 吧<br> <br> 紧 紧 跟 随 我 的 步 伐 ！</p>
                <br>
                <button class="login_btn" @click="login">立即登录</button>
            </div>
    </div>
</template>

<script>
    import {
        register
    } from '@/api/api.js'
    export default {
        name: 'SignIn',
        data() {
            return {
                usename: "",
                password: "",
                email: ""
            }
        },
        methods: {
            //第一个register是该组件的register的功能函数
            register() {
                //第二个register是注册接口
                register({
                    usename: this.usename,
                    password: this.password,
                    email: this.email
                }, '/register').then((res) => {
                    this.$message({
                        message: '注册成功，等待管理员激活账户信息',
                        type: 'success'
                    })
                    setTimeout(() => {
                        location.reload();
                    }, 1000);
                    console.log(res)
                }).catch((err) => {
                    console.log(err)
                })
            },
            login() {
                this.$router.push('/SignIn')
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
</style>