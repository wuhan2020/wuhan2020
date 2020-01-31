# Github Repo 流程
## Git Repository 下载地址
- 主要下载地址：https://github.com/wuhan2020/wuhan2020.git  -- wuhan（分支开始名称）
- api项目下载地址： https://github.com/wuhan2020/api-server.git -- api
- REST-api下载地址： https://github.com/wuhan2020/rest-api.git  -- rest
- 地图可视化下载地址： https://github.com/wuhan2020/map-viz.git -- map
- web应用下载地址： https://github.com/wuhan2020/WebApp.git  -- web
- 数据同步服务：https://github.com/wuhan2020/data-sync.git  -- data
- Json数据储存服务：https://github.com/wuhan2020/shimo-sheet2json.git --json

# 开发程序员/测试 下载流程
* `git clone *** ` 

#### 拷贝不同repo到本地，最好每个issue创建自己不同branch，以项目名称开头创建分支，例如：
* `用Python爬取最新疫情数据`, `分配给centurion-crawler` 使用 `wuhan-pythonspider-centurion`

* `对于页面展示的建议`, `分配给zhuangbiaowei` 使用 `web-pagepresentation-zhuangbiaowei`

#### 在本地branch进行更改后，push到远程分支master或者upstream. 由管理员统一整理决定更改或接受修改。 
* `git branch {branch-name} `
* `git branch -a`
* `git checkout {branch-name}`
* `git push --set-upstream origin {branch-name}`
* `git commit -m "message"`
* `git push`

**保证你的pull request有作者提供足够的权限能够合并入master分支**

