# [簡體中文](./README.md) | 繁體中文 | [English](./README_EN.md) | [日本語](./README_JP.md) | [Italiano](./README_IT.md) | [Português](./README_PT.md) <!-- omit in toc -->

[![wuhan2020 社群官網](https://img.shields.io/badge/wuhan2020-社区官网-green.svg?style=for-the-badge&colorB=red)](http://community.wuhan2020.org.cn/zh-cn)
[![wuhan2020 官方公告](https://img.shields.io/badge/wuhan2020-官方公告-green.svg?style=for-the-badge&colorB=red)](http://community.wuhan2020.org.cn/zh-cn/blog/wuhan2020-official-announcement.html)

### 志願者入口        >>> [![按一下加入 Slack 交流群組](https://img.shields.io/badge/slack-join-orange.svg)](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTQxMTU4MzgyNTYwLWIxMTMyNWI4NWE2YTk3NGRjZGJhMjUzNmJhMjg1MDQ3OTEzNDE5NGY4MWFhMjRlYWU4MmE3ZGQyOGU4N2YwMzY)


- [武漢新型冠狀病毒防疫資訊收集平台](#%e6%ad%a6%e6%b1%89%e6%96%b0%e5%9e%8b%e5%86%a0%e7%8a%b6%e7%97%85%e6%af%92%e9%98%b2%e7%96%ab%e4%bf%a1%e6%81%af%e6%94%b6%e9%9b%86%e5%b9%b3%e5%8f%b0)
  - [協作流程](#%e5%8d%8f%e4%bd%9c%e6%b5%81%e7%a8%8b)
  - [該平台主要開源專案](#%e8%af%a5%e5%b9%b3%e5%8f%b0%e4%b8%bb%e8%a6%81%e5%bc%80%e6%ba%90%e9%a1%b9%e7%9b%ae)
    - [資料同步](#%e6%95%b0%e6%8d%ae%e5%90%8c%e6%ad%a5)
    - [漸進式 Web 應用](#%e6%b8%90%e8%bf%9b%e5%bc%8f-web-%e5%ba%94%e7%94%a8)
    - [API 服務](#api-%e6%9c%8d%e5%8a%a1)
    - [地圖可視化組件](#%e5%9c%b0%e5%9b%be%e5%8f%af%e8%a7%86%e5%8c%96%e7%bb%84%e4%bb%b6)
    - [石墨表格同步組件](#%e7%9f%b3%e5%a2%a8%e8%a1%a8%e6%a0%bc%e5%90%8c%e6%ad%a5%e7%bb%84%e4%bb%b6)
  - [數據提交](#%e6%95%b0%e6%8d%ae%e6%8f%90%e4%ba%a4)
    - [石墨文檔網址：](#%e7%9f%b3%e5%a2%a8%e6%96%87%e6%a1%a3%e5%9c%b0%e5%9d%80)
  - [貢獻指南](#%e8%b4%a1%e7%8c%ae%e6%8c%87%e5%8d%97)
  - [資訊收集指南](#%e4%bf%a1%e6%81%af%e6%94%b6%e9%9b%86%e6%8c%87%e5%8d%97)
- [Slack交流群組](#slack%e4%ba%a4%e6%b5%81%e7%be%a4%e7%bb%84)
  - [Slack頻道導航](#slack%e9%a2%91%e9%81%93%e5%af%bc%e8%88%aa)
- [FAQ常見問題 （持續更新，招募志願者一起維護）](#faq%e5%b8%b8%e8%a7%81%e9%97%ae%e9%a2%98-%e6%8c%81%e7%bb%ad%e6%9b%b4%e6%96%b0%e6%8b%9b%e5%8b%9f%e5%bf%97%e6%84%bf%e8%80%85%e4%b8%80%e8%b5%b7%e7%bb%b4%e6%8a%a4)

# 武漢新型冠狀病毒防疫資訊收集平台

針對 2020 年初在武漢爆發的新型冠狀病毒疫情，本專案旨在收集各醫院、酒店、工廠、物流、捐贈、捐款、預防、治療、動態等資訊，統一收集，統一發布，以便各方之間進行資訊互通，有效調配社會資源。

該倉庫為資料主倉，所有資料均由腳本自動提交匯入，**_請不要在該倉庫中直接提交資料資訊_**，具體資料提交管道，請參考該檔案。

## 協作流程

本平台為方便大家協作，建構協作流程如下

![img](http://www.plantuml.com/plantuml/png/RP31Jkf068NtynIJkMiImf85uQxGdT4d6DfH6akRj5EDEqb4H2MO420HerOn4arQZT5e0NcPcIckU0NR3bqOtJKzttyotodQ55lKgUg0QbGdSDUfO2ENpMKXRxNPz4AyriBH2G1OeQO57PjODiGsHABx95gUQ9-npy5ylxwO7B7nc4sxB0WMaoQ2_zQ92XHJrub2DTEmeLtHgcPo6bwzy9kHw3M4UukMnTXHDPgat7F5zJkVzSN1B2gEcaeM8GPGCSLbR1EufT6AKqxOaaPNea_v5ZRkyA23036eHlTW6IlRn50Jxl_QAjmWrWwnqhgKshHCWwOORxR2H__B_GW7tjz2G0wGAKYTF4HivegQ7-yG316G6fbVUMpaNI8WHuXpQH41Cf8Ozyv5_stUUE378-vFUFqE0I39-2XrogVpIrwIop_n0gbwfY3zVfoq_Vdz8J_jyUTkE0mGA4QfKzM_0G00)

除資訊人工審核外，其他部分均為自動化完成，不需要人工介入。

## 該平台主要開放原始碼專案

### 資料同步

-	代碼倉庫： https://github.com/wuhan2020/data-sync

### 漸進式 Web 應用

- 代碼倉庫：https://github.com/wuhan2020/WebApp
- 正式環境：https://wuhan2020.kaiyuanshe.cn/

### API 服務

-	代碼倉庫：https://github.com/wuhan2020/api-server

### 地圖可視化組件

-	代碼倉庫：https://github.com/wuhan2020/map-viz

### 石墨表格同步組件

-	代碼倉庫：https://github.com/wuhan2020/shimo-sheet2json

# 我是志願者，希望一起維護專案
## 我是資料提交志願者，使用石墨文檔

本平台收集資訊包含如下幾類資料提交的資訊，請分別申報填寫。

本平台使用石墨文檔收集資料資訊，並由腳本定時資料同步到該倉庫，請不要在該倉庫中直接修改資料檔案。

由於參與人員較多，不開放所有人員的編輯權限，請在[此處](https://shimo.im/forms/YVJkGrGCWwQPTpqY/fill)填寫申請，會定向邀請到特定表單中進行資訊登錄。

### 石墨文檔網址：

- [醫院](https://shimo.im/sheets/q6WP3DpKKgVW63Pr/4WbFN/ )
- [酒店](https://shimo.im/sheets/Hd9C3QytrJK3RWxG/z1rye/)
- [物流](https://shimo.im/sheets/RTHXp3ghtKXY3GcC/MODOC/)
- [生產](https://shimo.im/sheets/pchvJ6ddyRHHdXtv/MODOC/)
- [捐贈](https://shimo.im/sheets/W3gxW6cwkYTDY6DD/)
- [義診](https://shimo.im/sheets/JgXjYCJJTRQxJ3GP/MODOC/)
- [在外武漢遊客住宿資訊](https://shimo.im/sheets/pdHRcXyKqJdqPyGJ/MODOC/)

具體細節可以參見[此處](https://community.wuhan2020.org.cn/zh-cn/docs/dev/contributing.html)。

## 我是開發相關志願者，使用GitHub

本平台現階段主要流程是使用GitHub flow以及GitHub project，透過issue和PR來進行處理。參與者需要有GitHub帳號。

**提交issue**

`issue`可以是需求，也可以是建議或bug等。在送出 `issue` 時，請確定 `issue` 的類型，並在標題中註明，專案的機器人將會自動打上對應的標籤。具體類型現在定義如下：

- hospital: 醫院相關資訊
- factory: 生產相關資訊
- logistical: 物流相關資訊
- hotel: 酒店相關資訊
- donation：捐款相關資訊
- clinic：義診相關資訊
- news：疫情新聞動態相關資訊
- doc: 文件相關
- bug： 缺陷回饋
- feature: 新的特性

**認領任務**

在 [Issue 列表](https://github.com/wuhan2020/wuhan2020/issues) 中挑選任務。然後在該 `issue` 中使用 `/self-assign`命令領取任務。專案的機器人將會自動將該`issue`的`Assignees`指定為自己。

具體如何提issue和PR，請參考[這裡](./CONTRIBUTING.md)。


# Slack交流群組
按一下加入[Slack 交流群組](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTQxMTU4MzgyNTYwLWIxMTMyNWI4NWE2YTk3NGRjZGJhMjUzNmJhMjg1MDQ3OTEzNDE5NGY4MWFhMjRlYWU4MmE3ZGQyOGU4N2YwMzY)

## Slack頻道導航

(需要先加入群組)

| 頻道名稱     | 連結      |
|------------| ----------|
| 預設頻道               | [![Github](https://img.shields.io/badge/Slack%20Channel-%23anti--2019--ncov-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSS83MZUK)              |
| 通用資訊發佈           | [![Github](https://img.shields.io/badge/Slack%20Channel-%23general-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSTGKFRCH)                       |
| 設計技能組             | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--designer-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT70SHJQ0)                |
| 產品需求管理技能組     | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--requirement--management-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT99VDWS2) |
| 前端技能組             | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--frontend-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT93L48H5)                |
| 後端技能組             | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--backend-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT93MCEJK)                 |
| 子專案: 資料同步       | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--data--sync-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT4AV807P)              |
| 子專案: Web前端展示    | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--front--pages-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSTPXN533)            |
| 子專案: 數據地圖可視化 | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--map--visualization-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT6HW3X8E)      |
| 子專案: API伺服器      | [![Github](https://img.shields.io/badge/Slack%20Channel-%23api--server-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT3V5CDKJ)                   |
| 採集給官方的建議       | [![Github](https://img.shields.io/badge/Slack%20Channel-%23help--advisement-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT7AABP53)              |
| 海外相關               | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--overseas-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CTAM5R65U)                |
| Slack頻道營運團隊      | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--operation-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSX1X74M9)               |

# 郵件列表

wuhan2020 郵件列表: [wuhan2020@googlegroups.com](https://groups.google.com/forum/#!forum/wuhan2020) ([訂閱](mailto:wuhan2020+subscribe@googlegroups.com), [退訂](mailto:wuhan2020+unsubscribe@googlegroups.com), [存檔](https://groups.google.com/forum/#!forum/wuhan2020))

歡迎大家加入共同探討各類技術或非技術類問題，讓我們大家一起齊心協力，眾志成城，共體時艱！

# FAQ常見問題

已經整理整個專案的FAQ，[請檢視](https://community.wuhan2020.org.cn/zh-cn/docs/overview/faq.html)

資訊組FAQ，[請檢視](https://shimo.im/docs/JqX9CvrqphPV9T3J/)

請點按 [石墨文檔](https://shimo.im/docs/DdWvXvtvpxrqrJ83)

---
Translator: [@jrthsr700tmax](https://github.com/jrthsr700tmax)
