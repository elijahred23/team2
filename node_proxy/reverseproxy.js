// Dependencies
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
var config = require('config.json')('./reverseproxyconfig.json');

// Config
const { routes } = require('./config.json');

const app = express();

var stuff;

//custom matching npm


for (route of routes) {
    app.use(route.route,
            createProxyMiddleware({
                target: route.address,
                pathRewrite: (path, req) => {
                //if(route.route)
                    stuff = path.split('/').slice(2).join('/').toString();
                    return path.split('/').slice(2).join('/'); // Could use replace, but take care of the leading '/'
                },
                //autoRewrite: true,
                hostRewrite: () => {
                    stuff = route.address.split('/')[2]
                    return stuff;
                },
                changeOrigin: true
            })  
    );
}

app.listen(80, () => {
    console.log('Proxy listening on port 80');
    //console.log(stuff);
    /**  do {
        if(stuff != undefined){
            console.log(stuff);
            stuff = undefined
        }
      } while (true);*/
   
});

console.log()

/**createProxyMiddleware({
            target: route.address,
            pathRewrite: (path, req) => {
		//if(route.route)
		        stuff = path.split('/').slice(2).join('/').toString();
                return path.split('/').slice(2).join('/'); // Could use replace, but take care of the leading '/'
            },
	    changeOrigin: true
        }) */

/**
 * createProxyMiddleware({
            target: route.address,
            pathRewrite: {
                '^/api/old-path': '/api/new-path', // rewrite path
              }
            },
	    changeOrigin: true
        })
 */
/*
        onProxyReq: function(request) {
            //path.split('/')
            request.setHeader("origin", "http://localhost:8000");
          }, */