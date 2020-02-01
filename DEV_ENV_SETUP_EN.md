# Github Repo processing
## Git Repository Download Addresses
- Major point wuhan2020：https://github.com/wuhan2020/wuhan2020.git  -- wuhan（branch prefix start with）
- api project： https://github.com/wuhan2020/api-server.git -- api
- REST-api project： https://github.com/wuhan2020/rest-api.git  -- rest
- map visualization： https://github.com/wuhan2020/map-viz.git -- map
- web application： https://github.com/wuhan2020/WebApp.git  -- web
- data simulation：https://github.com/wuhan2020/data-sync.git  -- data
- Json data storage：https://github.com/wuhan2020/shimo-sheet2json.git --json

# Developer/QA git clone process:
* `git clone *** `

#### copy various repos to local，create branches according issues with your own name and project name, start with fixed prefix，for an example：
* `用Python爬取最新疫情数据`, `allocated to centurion-crawler` with utilizing  `wuhan-pythonspider-centurion`

* `对于页面展示的建议`, `allocated to zhuangbiaowei` with utilizing `web-pagepresentation-zhuangbiaowei` 

#### after to modification on local branch，push your change to remote branch to master or upstream. The authorize has right to decide use it or modify or merge
* `git branch {branch-name} `
* `git branch -a`
* `git checkout {branch-name}`
* `git push --set-upstream origin {branch-name}`
* `git commit -m "message"`
* `git push`

**Make sure your pull request has right or authorization to be merged to master, if it cannot be, please contact author of project, make sure it is not blocked**

