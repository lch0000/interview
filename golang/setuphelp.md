### golang在win7环境下安装
1. win7下go最高支持到1.20
2. 安装完之后设置GOROOT和GOPATH环境变量
3. vscode需要自动安装一些插件
'''
Tools environment: GOPATH=C:\Users\NUC\go
Installing 8 tools at C:\Users\NUC\go\bin in module mode.
  gotests
  gomodifytags
  impl
  goplay
  dlv
  staticcheck
  gopls  # 版本需要降级到v0.15.3才可以
  go-outline
'''
参考 https://goproxy.cn/ 中的GO111MODULE和GOPROXY完成配置
4. 通过go.mod来配置某一个项目下的依赖关系
5. vscode里可以通过go install看到安装了哪些必须得支持包