# 简体中文 | [English](./README_EN.md) | [日本語](./README_JP.md) | [Italiano](./README_IT.md)

[![Github](https://img.shields.io/badge/wuhan2020-官方公告-green.svg?style=for-the-badge&colorB=red)](https://wuhan2020.github.io/) [![Github](https://img.shields.io/badge/wuhan2020-OFFICIAL%20ANNOUNCEMENT-green.svg?style=for-the-badge&colorB=red)](WUHAN2020_OFFICIAL_ANNOUNCEMENT.md)

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

### API 服务

- 代码仓库：https://github.com/wuhan2020/api-server

### 地图可视化组件

- 代码仓库：https://github.com/wuhan2020/map-viz

### 石墨表格同步组件

- 代码仓库：https://github.com/wuhan2020/shimo-sheet2json

## 数据提交

本平台收集信息包含如下几类数据提交的信息，请分别申报填写。

本平台使用石墨文档收集数据信息，并由脚本定时同步数据到该仓库，请不要在该仓库中直接修改数据文件。

由于参与人员较多，不开放所有人员的编辑权限，请在[这里](https://shimo.im/forms/YVJkGrGCWwQPTpqY/fill)填写申请，会定向邀请到特定表单中进行信息录入。

### 石墨文档地址：

- [医院](https://shimo.im/sheets/q6WP3DpKKgVW63Pr/4WbFN/ )
- [酒店](https://shimo.im/sheets/Hd9C3QytrJK3RWxG/z1rye/)
- [物流](https://shimo.im/sheets/RTHXp3ghtKXY3GcC/MODOC/)
- [生产](https://shimo.im/sheets/pchvJ6ddyRHHdXtv/MODOC/)
- [捐赠](https://shimo.im/sheets/W3gxW6cwkYTDY6DD/)
- [义诊](https://shimo.im/sheets/JgXjYCJJTRQxJ3GP/MODOC/)
- [在外武汉游客住宿信息](https://shimo.im/sheets/pdHRcXyKqJdqPyGJ/MODOC/)

如果你想新开表单，请填写[新开表单申请]（https://shimo.im/forms/rcThp3vPqqrtvChV/fill ）


## 贡献指南

请点击[这里](./CONTRIBUTING.md)

## 信息收集指南
请点击[这里](./INFORMATION_GUIDE.md)


# Slack交流群组
点击加入[Slack 交流群组](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTI2NTU1NzU3MTM2LWQ1YjIzMDllYjYzYTE1OTNhMWU4OTZkOGYzOGJhOWM2MzdlMjgwMmZiOWEzYTQwNmJkZDI4OWRmM2Q2ZDM1MTc)

## Slack频道导航

(需要先加入群组)

| 频道名     | 链接      |
|-----------|----------|
| 默认频道               | [![Github](https://img.shields.io/badge/Slack%20Channel-%23anti--2019--ncov-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSS83MZUK)              |
| 通用信息发布           | [![Github](https://img.shields.io/badge/Slack%20Channel-%23general-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSTGKFRCH)                       |
| 设计技能组             | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--designer-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT70SHJQ0)                |
| 产品需求管理技能组     | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--requirement--management-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT99VDWS2) |
| 前端技能组             | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--frontend-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT93L48H5)                |
| 后端技能组             | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--backend-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT93MCEJK)                 |
| 子项目: 数据同步       | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--data--sync-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT4AV807P)              |
| 子项目: Web前端展示    | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--front--pages-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSTPXN533)            |
| 子项目: 数据地图可视化 | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--map--visualization-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT6HW3X8E)      |
| 子项目: API服务器      | [![Github](https://img.shields.io/badge/Slack%20Channel-%23api--server-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT3V5CDKJ)                   |
| 采集给官方的建议       | [![Github](https://img.shields.io/badge/Slack%20Channel-%23help--advisement-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT7AABP53)              |
| 海外相关               | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--overseas-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CTAM5R65U)                |
| Slack频道运营团队      | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--operation-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSX1X74M9)               |

欢迎大家加入共同探讨各类技术或非技术类问题，让我们大家一起齐心协力，众志成城，共克时艰！

# FAQ常见问题 （持续更新，招募志愿者一起维护）

已经整理整个项目的FAQ，[请查看](./FAQ.md)

信息组FAQ，[请查看](https://shimo.im/docs/JqX9CvrqphPV9T3J/)

请点击[石墨文档](https://shimo.im/docs/DdWvXvtvpxrqrJ83)
