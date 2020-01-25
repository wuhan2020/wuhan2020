<!-- TOC -->

- [贡献指南](#贡献指南)
  - [GitHub 操作流程](#github-操作流程)
    - [0、提交 issue](#0提交-issue)
    - [1、认领任务](#1认领任务)
    - [2、Fork 本仓库](#2fork-本仓库)
    - [3、Clone 仓库](#3clone-仓库)
    - [4、新建 `branch`](#4新建-branch)
    - [5、修改内容，并提交](#5修改内容并提交)
    - [6、同步上游仓库变更](#6同步上游仓库变更)
    - [7、推送新分支到自己的远程仓库](#7推送新分支到自己的远程仓库)
    - [8、提 `Pull Request`](#8提-pull-request)
    - [9、如果你的代码合并时出现冲突时，你可以：](#9如果你的代码合并时出现冲突时你可以)
    - [10、当你的代码被合并进去以后，你可以：](#10当你的代码被合并进去以后你可以)
  - [CSV 文件编辑指南](#csv-文件编辑指南)
  - [CSV 的格式规范](#csv-的格式规范)
  - [项目机器人说明](#项目机器人说明)
  - [Slack 交流群组](#slack-交流群组)

<!-- /TOC -->

# 贡献指南
这篇指南会尽可能清楚地描述如何为 **wuhan2020** 贡献一份自己的力量。欢迎提交 issue， 或者直接修改提交 PR！

## GitHub 操作流程
### 0、提交 issue
有任何想法或问题，欢迎到 [这里](https://github.com/wuhan2020/wuhan2020/issues) 提交 `issue`，参与项目的志愿者将会及时沟通交流。

在提交 `issue` 时，请确定 `issue` 的类型，并在标题中注明，项目的机器人将会自动打上对应的标签：

* hospital: 医院相关信息
* factory: 生产相关信息
* logistical: 物流相关信息
* hotel: 酒店相关信息
* donation：捐款相关信息
* clinic：义诊相关信息
* news：疫情新闻动态相关信息
* doc: 文档相关
* bug： 缺陷反馈
* feature: 新的特性

### 1、认领任务
> **衷心地希望大家能为本项目添砖加瓦，齐心协力，共克时艰！**

在 [Issue 列表](https://github.com/wuhan2020/wuhan2020/issues) 中挑选任务。然后在该 `issue` 中使用 `/self-assign`命令领取任务。项目的机器人将会自动将该`issue`的`Assignees`指定为自己。
```
/self-assign
```
示意图如下：

![self-assign 示意图](./static/self-assign.png)


### 2、Fork 本仓库

访问 [wuhan2020 仓库的主页](https://github.com/wuhan2020/wuhan2020)，并 Fork 到自己的账号下。

![Fork 仓库](./static/fork-repo.png)

> 注：以下内容是在命令行终端里面操作，需要安装 [Git](https://git-scm.com/).

### 3、Clone 仓库
回到自己的 GitHub 主页，并找到刚刚 Fork 过来的 *wuhan2020* 仓库，进入仓库主页, 将该仓库 `clone` 到本地，如：
```bash
# 将下面的 XXX 替换成你自己的用户名
git clone git@github.com:XXX/wuhan2020.git
cd wuhan2020
```

### 4、新建 `branch`
> 非紧急修复，不建议在 master 分支进行开发修改。

根据该分支的用途，起一个恰当的分支名称，新建分支，如：
```bash
git checkout -b my-fix-branch master
```

### 5、修改内容，并提交
对相应文件做出修改，修改完成后，提交：
```bash 
git add .
git commit -m "hotel: update HOTEL.csv, fix #1"
```

提交时，尽量：

(1) 用一句话清楚的描述这次提交做了什么。

(3) 关联相关 `issue`，如 `fix #1` 、`close #2`、`#3`


如果 `commit` 之后，又做了修改，可以使用 `--amend` 参数：
```bash
git add .
git commit --amend -sm "hotel: update HOTEL.csv, fix #1" 
```

### 6、同步上游仓库变更
同步上游仓库变更(即 [wuhan2020/wuhan2020](https://github.com/wuhan2020/wuhan2020) )，因为可能有其他人先于你提交到上游仓库：

```bash
$ git remote add upstream git@github.com:wuhan2020/wuhan2020.git
$ git fetch upstream   
```

若上游仓库有变更，需要先进行 `rebase`:
```bash
$ git rebase upstream/master   
```

### 7、推送新分支到自己的远程仓库
```bash
$ git push -f origin my-fix-branch:my-fix-branch
```

### 8、提 `Pull Request`
在自己仓库的页面上提`pull request` 到上游仓库。如下图所示。

![pull-request](./static/pull-request.png)

![open-pr](./static/open-pr.png)
如果其他人 `review` 之后，需要再进行更改，就修改相关内容，然后执行以下操作，该 PR 将会自动同步该 `commit` 。

```bash
git add . 
git commit --amend
git push -f origin my-fix-branch 
```


### 9、如果你的代码合并时出现冲突时，你可以：
> 注：如果未出现冲突，则无需进行以下操作

* 先同步上游仓库变更
```bash
git fetch upstream
```
* 进行`rebase`:
```bash
git rebase upstream/master
```
* 手动解决冲突内容，之后重新提交：
```bash
git add my-fix-file
git rebase --continue
git push -f origin my-fix-branch
```


### 10、当你的代码被合并进去以后，你可以：

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
git branch -D my-fix-branch
```

* 删除远程分支(可选)：
```bash
git push origin --delete my-fix-branch
```
--- 

## CSV 文件编辑指南
**逗号分隔值（Comma-Separated Values，CSV）**，其文件以纯文本形式存储表格数据（数字和文本），文件的每一行都是一个数据记录。每个记录由一个或多个字段组成，用**逗号( ```,``` )**分隔。

## CSV 的格式规范
1. 每一行记录位于一个单独的行上，用**回车换行符CRLF**(也就是 ```\r\n``` )分割。
2. 文件中的最后一行记录可以有结尾回车换行符，也可以没有。
3. 第一行可以存在一个可选的标题头，格式和普通记录行的格式一样。标题头要包含文件记录字段对应的名称，应该有和记录字段一样的数量。（在MIME类型中，标题头行的存在与否可以通过MIME type中的可选”header”参数指明）
4. 在标题头行和普通行每行记录中，会存在一个或多个由**半角逗号(```,```)** 分隔的字段。整个文件中每行应包含相同数量的字段，空格也是字段的一部分，不应被忽略。**每一行记录最后一个字段后不能跟逗号**。（通常用逗号分隔，也有其他字符分隔的CSV，需事先约定）
5. 每个字段可用也可不用半角双引号(")括起来（不过有些程序，如Microsoft的Excel就根本不用双引号）。如果字段没有用引号括起来，那么该字段内部不能出现双引号字符。
6. 字段中若包含回车换行符、双引号或者逗号，该字段需要用**半角双引号(```"```)** 括起来。
7. 如果用半角双引号括字段，那么出现在字段内的双引号前必须加一个双引号进行转义。
8. 如果使用 VSCode 进行编辑，可以使用 **```Edit csv```** 插件进行本地测试。

---

## 项目机器人说明
本项目已接入 Github 机器人：`Menbotics`，该机器人可以：

* **`Issue` 自动打标签**：具体见 [0、提交 issue](#0提交-issue)
* **任务认领**：具体见 [1、认领任务](#1认领任务)
* **代码自动合并**：有 PR(Pull Request) 提交上来之后，有代码合并权限的人员使用 `/approve` 让机器人自动合入代码。

机器人配置见 [hypertrons.json](./.github/hypertrons.json)，如在该配置文件中可以看到具体有哪些人员有代码合并权限。


## Slack 交流群组
此外，我们已经建立了 [Slack交流群组](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTIzNjA2MDYwOTUxLWVjMjA4MjdhNGVmZmZlZTgxYjM1ZDY1NGVkZDVkNGI0NzhjZGVlYTM2Mjc5Mjk2YjgyYTk1NDJmNTkxODZlOTE)，欢迎大家加入共同探讨各类技术或非技术类问题，让我们大家 一起齐心协力，众志成城，共克时艰！




