var path = require('path');
var APP_DIR = path.resolve(__dirname, 'household/resources/assets');
var BUILD_DIR = path.resolve(__dirname, 'household/static/household/js');
var CSS_BUILD_DIR = path.resolve(__dirname,'household/static/household/css');

var ExtractTextPlugin = require('extract-text-webpack-plugin');
var WebpackNotifierPlugin = require('webpack-notifier');

module.exports = {
    entry: {
        build: [APP_DIR + '/js/app.js', APP_DIR + '/sass/app.scss'],
        landing: [APP_DIR + '/sass/landing.scss'],
    },
    output:  {
       path: BUILD_DIR, 
       filename:  '[name].js'
    },
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: ExtractTextPlugin.extract({
                    fallback : 'style-loader',
                    use: ['css-loader','sass-loader']
                })
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin({
            filename: '../css/[name].css',
            allChunks: true
        }),
        new ExtractTextPlugin({
            filename: '../css/[name].css',
            allChunks: true
        }),
        new WebpackNotifierPlugin()
    ]
}