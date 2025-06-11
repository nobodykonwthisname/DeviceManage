import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        username: 'Guest'
    },
    mutations: {
        setUsername(state, name) {
            state.username = name;
        }
    },
    getters: {
        getUsername(state) {
            return state.username;
        }
    }
});

export default store;