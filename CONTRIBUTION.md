wuhan2020开源项目收集经过审核与确认过的武汉新型冠状病毒防疫相关信息，并利用开源和分布式协作优势实时更新并通报，望众程序员与开发者们可以齐心协力，共克时艰！

# 代码贡献指南
有任何疑问，欢迎提交 issue， 或者直接修改提交 PR！

## 提交 issue
遇到以下情况时，欢迎提交 `issue` ：

* Bug 反馈 
* 提交新需求
* 答疑交流

在提交 `issue` 时，请确定 `issue` 的类型，并在标题中注明：

* bug: 缺陷
* feature: 新功能
* documentation: 文档相关
* test: 测试用例相关


## 代码提交
### 1、克隆到本地仓库
1、先将该仓库 `fork` 到你自己的账号下面。

2、将自己账号下的该仓库 `clone` 到本地，如：
```bash
$ git clone git@github.com:XXX/wuhan2020.git
```

3、关联上游仓库
```bash
$ git remote add upstream git@github.com:wuhan2020/wuhan2020.git
```

### 2、本地开发
1、新建功能分支:
```bash
$ git checkout -b my-fix-branch master
```

2、接下来修改相应内容。

### 3、提交代码
#### 1、执行 `commit`。
```bash 
git add .
git commit -m "fix: update route, fix #1"
```

##### Commit 提交规范:
根据 [angular 规范](https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#commit-message-format) 简化为如下:
```
<type>: <subject>, <issue>
```
（1）type

提交 commit 的类型，包括以下几种:

* feat: 新功能
* fix: 修复问题
* docs: 修改文档
* style: 修改代码格式，不影响代码逻辑
* refactor: 重构代码，理论上不影响现有功能
* perf: 提升性能
* test: 增加修改测试用例
* chore: 修改工具相关（包括但不限于文档、代码生成等）
* deps: 升级依赖

（2）subject

用一句话清楚的描述这次提交做了什么。

（3）issue

关联相关 issue，如 fix #1, close #2, #3.


* 如果提交之后，又做了修改，可以使用 `--amend` 参数：
  ```bash
  $ git commit --amend -ams "fix #14, add homepage"   
  ```

#### 2、同步上游仓库变更，因为可能有其他人先于你提交到上游仓库：
```bash
$ git fetch upstream   
```
若上游仓库有变更，需要先进行 `rebase`:
```bash
$ git rebase upstream/master   
```

#### 3、推送新分支到自己的远程仓库
```bash
$ git push -f origin my-fix-branch:my-fix-branch
```

#### 4、提 `Merge Request`
* 在自己仓库的页面上提`merge request` 到上游仓库，填写`merge request`相关信息（从自己仓库的 `my-fix-branch` 分支合并到上游仓库的 `master` 分支、关联的 `issue` 、功能实现说明等）

* 如果其他人 `review` 之后，需要再进行更改，就修改代码，重跑测试，然后执行以下操作，该 MR 将会自动同步该 `commit` 。
```bash
$ git add . 
$ git commit --amend
$ git push -f origin my-fix-branch 
```

#### 5、当你的代码合并时出现冲突，你可以（可选）：
* 同步上游仓库变更，因为有其他人先于你提交到上游仓库
```bash
git fetch upstream
```
* 上游仓库有变更，需要先进行`rebase`:
```bash
git rebase upstream/master
```
* 手动解决冲突内容，之后重新提交：
```bash
git add my-fix-file
git rebase --continue
git push -f origin my-fix-branch
```

#### 6、当你的代码被合并进去以后，你可以：

* 切回到 `master` 分支：
```bash
git checkout master -f
```
* 保持本地 `master` 分支与上游分支同步：
```bash
git pull --ff upstream master
```
* 删除本地分支(可选):
```bash
# 切换回master分支：
git checkout master
# 同步上游仓库变更
git fetch upstream master
# 上游仓库有变更，需要进行rebase
git rebase upstream/master
# 删除本地分支
git branch -D my-fix-branch
# 删除远程分支
git push origin --delete my-fix-branch
```
* 删除远程分支(可选)：
```bash
git push origin --delete my-fix-branch
```

# csv 文件编辑指南
**逗号分隔值（Comma-Separated Values，CSV）**，其文件以纯文本形式存储表格数据（数字和文本），文件的每一行都是一个数据记录。每个记录由一个或多个字段组成，用**逗号( ```,``` )**分隔。

## CSV的格式规范
1. 每一行记录位于一个单独的行上，用**回车换行符CRLF**(也就是 ```\r\n``` )分割。
2. 文件中的最后一行记录可以有结尾回车换行符，也可以没有。
3. 第一行可以存在一个可选的标题头，格式和普通记录行的格式一样。标题头要包含文件记录字段对应的名称，应该有和记录字段一样的数量。（在MIME类型中，标题头行的存在与否可以通过MIME type中的可选”header”参数指明）
4. 在标题头行和普通行每行记录中，会存在一个或多个由**半角逗号(```,```)** 分隔的字段。整个文件中每行应包含相同数量的字段，空格也是字段的一部分，不应被忽略。**每一行记录最后一个字段后不能跟逗号**。（通常用逗号分隔，也有其他字符分隔的CSV，需事先约定）
5. 每个字段可用也可不用半角双引号(")括起来（不过有些程序，如Microsoft的Excel就根本不用双引号）。如果字段没有用引号括起来，那么该字段内部不能出现双引号字符。
6. 字段中若包含回车换行符、双引号或者逗号，该字段需要用**半角双引号(```"```)** 括起来。
7. 如果用半角双引号括字段，那么出现在字段内的双引号前必须加一个双引号进行转义。
8. 如果使用 VSCode 进行编辑，可以使用 **```Edit csv```** 插件进行本地测试。



# 项目机器人说明
项目中有机器人可以完成自动化流程：
* Contributors可以选择不同的任务，使用 **/self-assign** 领取任务。
* 完成任务后，提交 PR(Pull Request) ，使用 **/approve** 进行 PR review 与自动合入。



我们已经建立了[Slack交流群组](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTIzNjA2MDYwOTUxLWVjMjA4MjdhNGVmZmZlZTgxYjM1ZDY1NGVkZDVkNGI0NzhjZGVlYTM2Mjc5Mjk2YjgyYTk1NDJmNTkxODZlOTE)，欢迎大家加入共同探讨各类技术或非技术类问题！




