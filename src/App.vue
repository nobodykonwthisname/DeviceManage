<template>
  <div id="app">
    <router-view>
      <SignIn/>
    </router-view>
  </div>
</template>

<script>
    //引入插件

    import SignIn from './components/SignIn';
    export default {
        name: "App",
        components: {
            SignIn
        },

    }
</script>