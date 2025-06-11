const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({  
    transpileDependencies: true,
      devServer: {    
        proxy: {      
            '^/api': {        
                target: 'http://localhost:5000/', //接口的前缀
                ws: true, //代理websocked
                changeOrigin: true, //虚拟的站点需要更管origin
                pathRewrite: {          
                    '^/api': '/' //重写路径          
                }      
            }    
        }  
    }
})