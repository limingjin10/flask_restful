# Flask Restful 最佳实践

## GitBook 操作指南

初始化
```bash
npm install -g gitbook-cli
npm install --save gitbook-plugin-todo
npm install --save gitbook-plugin-mermaid-full
cd docs
gitbook init
```

开启服务
```bash
gitbook serve
```

访问 [http://localhost:4000](http://localhost:4000)


## 生成pdf

下载依赖(Mac环境)

https://calibre-ebook.com/download_osx

```bash
ln -s /Applications/calibre.app/Contents/MacOS/ebook-convert /usr/local/bin
```

生成pdf
```bash
gitbook pdf . flask_restful.pdf
```
