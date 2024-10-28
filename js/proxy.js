import express from 'express';
import { createProxyMiddleware } from 'http-proxy-middleware';

const app = express();

// 這裡設置代理代理到遠端伺服器
app.use('/api', createProxyMiddleware({
    target: 'https://stats.moe.gov.tw',
    changeOrigin: true,
    pathRewrite: {
        '^/api': '', // 去除"/api"前綴
    },
}));

app.listen(3000, () => {
    console.log('代理伺服器運行於 http://localhost:30010');
});