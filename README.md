# 简体中文 | [繁體中文](./README_TW.md) | [English](./README_EN.md) | [日本語](./README_JP.md) | [Italiano](./README_IT.md) | [Português](./README_PT.md) <!-- omit in toc -->

[![wuhan2020 社区官网](https://img.shields.io/badge/wuhan2020-社区官网-green.svg?style=for-the-badge&colorB=red)](http://community.wuhan2020.org.cn/zh-cn)
[![wuhan2020 官方公告](https://img.shields.io/badge/wuhan2020-官方公告-green.svg?style=for-the-badge&colorB=red)](http://community.wuhan2020.org.cn/zh-cn/blog/wuhan2020-official-announcement.html)

### 志愿者入口        >>> [![点击加入 Slack 交流群组](https://img.shields.io/badge/slack-join-orange.svg)](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTQxMTU4MzgyNTYwLWIxMTMyNWI4NWE2YTk3NGRjZGJhMjUzNmJhMjg1MDQ3OTEzNDE5NGY4MWFhMjRlYWU4MmE3ZGQyOGU4N2YwMzY)


- [武汉新型冠状病毒防疫信息收集平台](#%e6%ad%a6%e6%b1%89%e6%96%b0%e5%9e%8b%e5%86%a0%e7%8a%b6%e7%97%85%e6%af%92%e9%98%b2%e7%96%ab%e4%bf%a1%e6%81%af%e6%94%b6%e9%9b%86%e5%b9%b3%e5%8f%b0)
  - [协作流程](#%e5%8d%8f%e4%bd%9c%e6%b5%81%e7%a8%8b)
  - [该平台主要开源项目](#%e8%af%a5%e5%b9%b3%e5%8f%b0%e4%b8%bb%e8%a6%81%e5%bc%80%e6%ba%90%e9%a1%b9%e7%9b%ae)
    - [数据同步](#%e6%95%b0%e6%8d%ae%e5%90%8c%e6%ad%a5)
    - [渐进式 Web 应用](#%e6%b8%90%e8%bf%9b%e5%bc%8f-web-%e5%ba%94%e7%94%a8)
    - [API 服务](#api-%e6%9c%8d%e5%8a%a1)
    - [地图可视化组件](#%e5%9c%b0%e5%9b%be%e5%8f%af%e8%a7%86%e5%8c%96%e7%bb%84%e4%bb%b6)
    - [石墨表格同步组件](#%e7%9f%b3%e5%a2%a8%e8%a1%a8%e6%a0%bc%e5%90%8c%e6%ad%a5%e7%bb%84%e4%bb%b6)
  - [数据提交](#%e6%95%b0%e6%8d%ae%e6%8f%90%e4%ba%a4)
    - [石墨文档地址：](#%e7%9f%b3%e5%a2%a8%e6%96%87%e6%a1%a3%e5%9c%b0%e5%9d%80)
  - [贡献指南](#%e8%b4%a1%e7%8c%ae%e6%8c%87%e5%8d%97)
  - [信息收集指南](#%e4%bf%a1%e6%81%af%e6%94%b6%e9%9b%86%e6%8c%87%e5%8d%97)
- [Slack交流群组](#slack%e4%ba%a4%e6%b5%81%e7%be%a4%e7%bb%84)
  - [Slack频道导航](#slack%e9%a2%91%e9%81%93%e5%af%bc%e8%88%aa)
- [FAQ常见问题 （持续更新，招募志愿者一起维护）](#faq%e5%b8%b8%e8%a7%81%e9%97%ae%e9%a2%98-%e6%8c%81%e7%bb%ad%e6%9b%b4%e6%96%b0%e6%8b%9b%e5%8b%9f%e5%bf%97%e6%84%bf%e8%80%85%e4%b8%80%e8%b5%b7%e7%bb%b4%e6%8a%a4)

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

## 合作的公益项目

### 阿里云疫情分析平台（完全免费）

- 基于阿里云日志服务、自动集成同步wuhan2020数据，提供一站式疫情分析可视化、报表订阅与告警、数据订阅或二次开发平台。完全免费。
- 公共演示项目：https://1340796328858956.cn-shanghai.fc.aliyuncs.com/2016-08-15/proxy/demo/slsconsole/?redirect=true&type=2020
- 疫情分析平台：https://sls.console.aliyun.com/lognext/app/ncp/setting
- 详细介绍：https://help.aliyun.com/document_detail/151625.html


# 我是志愿者，希望一起维护项目
## 我是数据提交志愿者，使用石墨文档

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

具体细节可以参见[这里](https://community.wuhan2020.org.cn/zh-cn/docs/dev/contributing.html)。

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


# Slack交流群组
点击加入[Slack 交流群组](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTQxMTU4MzgyNTYwLWIxMTMyNWI4NWE2YTk3NGRjZGJhMjUzNmJhMjg1MDQ3OTEzNDE5NGY4MWFhMjRlYWU4MmE3ZGQyOGU4N2YwMzY)

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

# 邮件列表

wuhan2020 邮件列表：[wuhan2020@googlegroups.com](https://groups.google.com/forum/#!forum/wuhan2020) ([订阅](mailto:wuhan2020+subscribe@googlegroups.com), [退订](mailto:wuhan2020+unsubscribe@googlegroups.com), [存档](https://groups.google.com/forum/#!forum/wuhan2020))

欢迎大家加入共同探讨各类技术或非技术类问题，让我们大家一起齐心协力，众志成城，共克时艰！

# FAQ常见问题

已经整理整个项目的FAQ，[请查看](https://community.wuhan2020.org.cn/zh-cn/docs/overview/faq.html)

信息组FAQ，[请查看](https://shimo.im/docs/JqX9CvrqphPV9T3J/)

请点击[石墨文档](https://shimo.im/docs/DdWvXvtvpxrqrJ83)
