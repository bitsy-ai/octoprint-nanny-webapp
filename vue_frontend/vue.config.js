const BundleTracker = require("webpack-bundle-tracker");
const ESLintPlugin = require('eslint-webpack-plugin');

const pages = {
    'vue_alerts_dropdown': {
        entry: './src/apps/alertsDropdown.js',
        chunks: ['chunk-vendors']
    }
}

module.exports = {
    pages: pages,
    filenameHashing: false,
    productionSourceMap: false,
    publicPath: process.env.NODE_ENV === 'production'
        ? ''
        : 'http://localhost:8080/',
    outputDir: '../print_nanny_webapp/static/vue/',
    css: {
        loaderOptions: {
            scss: {}
        }
    },
    chainWebpack: config => {
        config.module
        .rule('ts')
        .use('ts-loader')
          .loader('ts-loader')
          .tap(options => {
            // modify the ts options...
            return options
          })


        config.optimization
            .splitChunks({
                cacheGroups: {
                    vendor: {
                        test: /[\\/]node_modules[\\/]/,
                        name: "chunk-vendors",
                        chunks: "all",
                        priority: 1
                    },
                },
            });

        Object.keys(pages).forEach(page => {
            config.plugins.delete(`html-${page}`);
            config.plugins.delete(`preload-${page}`);
            config.plugins.delete(`prefetch-${page}`);
        })

        config
            .plugin('ESLintPlugin')
            .use(ESLintPlugin)
        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: '../vue_frontend/webpack-stats.json'}]);

        config.resolve.symlinks(false)
        config.resolve.alias
            .set('__STATIC__', 'static')

        config.devServer
            .public('http://localhost:8080')
            .host('localhost')
            .port(8080)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .headers({"Access-Control-Allow-Origin": ["*"]})

    }
};