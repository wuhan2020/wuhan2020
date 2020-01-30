# 武汉新型冠状病毒防疫信息收集平台

针对 2020 年初在武汉爆发的新型冠状病毒疫情，本项目旨在收集各医院、酒店、工厂、物流、捐赠、捐款、预防、治疗、动态等信息，统一收集，统一发布，以便各方之间进行信息互通，有效调配社会资源。

该仓库为数据主仓，所有数据由脚本自动提交导入，**_请不要在该仓库中直接提交数据信息_**，具体数据提交渠道，请参考该文档。

## 协作流程

本平台为方便大家协作，构建如下协作流程

![img](http://www.plantuml.com/plantuml/png/RP31Jkf068NtynIJkMiImf85uQxGdT4d6DfH6akRj5EDEqb4H2MO420HerOn4arQZT5e0NcPcIckU0NR3bqOtJKzttyotodQ55lKgUg0QbGdSDUfO2ENpMKXRxNPz4AyriBH2G1OeQO57PjODiGsHABx95gUQ9-npy5ylxwO7B7nc4sxB0WMaoQ2_zQ92XHJrub2DTEmeLtHgcPo6bwzy9kHw3M4UukMnTXHDPgat7F5zJkVzSN1B2gEcaeM8GPGCSLbR1EufT6AKqxOaaPNea_v5ZRkyA23036eHlTW6IlRn50Jxl_QAjmWrWwnqhgKshHCWwOORxR2H__B_GW7tjz2G0wGAKYTF4HivegQ7-yG316G6fbVUMpaNI8WHuXpQH41Cf8Ozyv5_stUUE378-vFUFqE0I39-2XrogVpIrwIop_n0gbwfY3zVfoq_Vdz8J_jyUTkE0mGA4QfKzM_0G00)

除信息人工审核外，其他部分均为自动化完成，不应需要人工介入。

## 该平台主要开源项目

### 数据同步

- 代码仓库： https://github.com/wuhan2020/data-sync

### 渐进式 Web 应用

- 代码仓库：https://github.com/wuhan2020/WebApp
- 正式环境：https://wuhan2020.kaiyuanshe.cn/
- 后端服务：https://github.com/wuhan2020/rest-api

### API 服务

- 代码仓库：https://github.com/wuhan2020/api-server

### 地图可视化组件

- 代码仓库：https://github.com/wuhan2020/map-viz

### 石墨表格同步组件

- 代码仓库：https://github.com/wuhan2020/shimo-sheet2json

# 我是志愿者，希望一起维护项目
## 我是数据提交志愿者，使用石墨文档（可通过微信群交流）

本平台收集信息包含如下几类数据提交的信息，请分别申报填写。

本平台使用石墨文档收集数据信息，并由脚本定时同步数据到该仓库，请不要在该仓库中直接修改数据文件。

由于参与人员较多，不开放所有人员的编辑权限，请在[这里](https://shimo.im/forms/YVJkGrGCWwQPTpqY/fill)填写申请，会定向邀请到特定表单中进行信息录入。

### 石墨文档地址：

- [医院](https://shimo.im/sheets/k399pHyt6HKvW6xR/MODOC/)
- [酒店](https://shimo.im/sheets/Hd9C3QytrJK3RWxG/z1rye/)
- [物流](https://shimo.im/sheets/RTHXp3ghtKXY3GcC/MODOC/)
- [生产](https://shimo.im/sheets/pchvJ6ddyRHHdXtv/MODOC/)
- [捐赠](https://shimo.im/sheets/W3gxW6cwkYTDY6DD/)
- [义诊](https://shimo.im/sheets/JgXjYCJJTRQxJ3GP/MODOC/)
- [在外武汉游客住宿信息](https://shimo.im/sheets/pdHRcXyKqJdqPyGJ/MODOC/)

具体细节包括微信群二维码可以参见[这里](./INFORMATION_GUIDE.md)。

## 我是开发相关志愿者，使用GitHub

本平台现阶段主要流程是使用GitHub flow以及GitHub project，通过issue和PR来进行处理。参与者需要有GitHub账号。

**提交issue**

`issue`可以是需求，也可以是建议或者bug等。在提交 `issue` 时，请确定 `issue` 的类型，并在标题中注明，项目的机器人将会自动打上对应的标签。具体类型现在定义如下：

- hospital: 医院相关信息
- factory: 生产相关信息
- logistical: 物流相关信息
- hotel: 酒店相关信息
- donation：捐款相关信息
- clinic：义诊相关信息
- news：疫情新闻动态相关信息
- doc: 文档相关
- bug： 缺陷反馈
- feature: 新的特性

**认领任务**

在 [Issue 列表](https://github.com/wuhan2020/wuhan2020/issues) 中挑选任务。然后在该 `issue` 中使用 `/self-assign`命令领取任务。项目的机器人将会自动将该`issue`的`Assignees`指定为自己。

具体如何提issue和PR，请参考[这里](./CONTRIBUTING.md)。


# Slack 交流群组
点击加入[Slack 交流群组](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTI2NTU1NzU3MTM2LWQ1YjIzMDllYjYzYTE1OTNhMWU4OTZkOGYzOGJhOWM2MzdlMjgwMmZiOWEzYTQwNmJkZDI4OWRmM2Q2ZDM1MTc)

欢迎大家加入共同探讨各类技术或非技术类问题，让我们大家一起齐心协力，众志成城，共克时艰！

# FAQ常见问题

已经整理整个项目的FAQ，[请查看](./FAQ.md)

信息组FAQ，[请查看](https://shimo.im/docs/JqX9CvrqphPV9T3J/)

请点击[石墨文档](https://shimo.im/docs/DdWvXvtvpxrqrJ83)
