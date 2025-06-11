 import Vue from 'vue'
 import Vuex from 'vuex'
 Vue.use(Vuex);
 // 用Vuex.Store对象用来记录token
 const store = new Vuex.Store({

     state: {
         // 存储token
         token: "",
         userName: "" // 可选
     },
     getters: {
         getToken(state) {
             return state.token || localStorage.getItem("token") || "";
         }
     },
     mutations: {
         // 修改token，并将token存入localStorage
         setToken(state, token) {
             state.token = token;
             localStorage.setItem('token', token);
             console.log('store、localstorage保存token成功！');
         },
         delToken(state) {
             state.token = "";
             localStorage.removeItem("token");
         },
         // 可选
         setUserInfo(state, userName) {
             state.userName = userName;
         }
     },

     actions: {
         // removeToken: (context) => {
         // context.commit('setToken')
         // }
     },
 });

 export default store;