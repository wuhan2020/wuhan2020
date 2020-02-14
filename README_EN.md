# [简体中文](./README.md) | [繁體中文](./README_TW.md) | English | [日本語](./README_JP.md) | [Italiano](./README_IT.md) | [Português](./README_PT.md) <!-- omit in toc -->

[![Github](https://img.shields.io/badge/wuhan2020-Community%20Website-green.svg?style=for-the-badge&colorB=red)](https://community.wuhan2020.org.cn/en-us/)
[![Github](https://img.shields.io/badge/wuhan2020-OFFICIAL%20ANNOUNCEMENT-green.svg?style=for-the-badge&colorB=red)](https://community.wuhan2020.org.cn/en-us/blog/wuhan2020-official-announcement.html)

### Volunteer entrance         >>> [![Get on Slack](https://img.shields.io/badge/slack-join-orange.svg)](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTQxMTU4MzgyNTYwLWIxMTMyNWI4NWE2YTk3NGRjZGJhMjUzNmJhMjg1MDQ3OTEzNDE5NGY4MWFhMjRlYWU4MmE3ZGQyOGU4N2YwMzY)

- [Information Collection Platform for Wuhan Covid-19 Epidemic Prevention](#information-collection-platform-for-wuhan-Covid-19-epidemic-prevention)
  - [Collaboration process](#collaboration-process)
  - [Major Open Source Sub-Projects](#major-open-source-sub-projects)
    - [Data Synchronization](#data-synchronization)
    - [Web Front-end Development](#web-front-end-development)
    - [API Service](#api-service)
    - [Map Visualization Components](#map-visualization-components)
    - [Online Form Editing Service(ShiMo) Synchronization Component](#online-form-editing-serviceshimo-synchronization-component)
  - [Data Submission](#data-submission)
    - [Online Document Service Shimo Edit Link：](#online-document-service-shimo-edit-link)
  - [Contribution Guide](#contribution-guide)
  - [Data and Information Collection Guide](#data-and-information-collection-guide)
- [Slack Communication Group](#slack-communication-group)
  - [Slack Channel Navigation](#slack-channel-navigation)

# Information Collection Platform for Wuhan Covid-19 Epidemic Prevention
This translation updates to 18:30(CST), 1/30/2020.

This project aims at collecting and gathering information of hospitals, hotels, factories, logistics, donations, contributions, prevention, treatment and any live information regarding national epidemic prevention from reliable sources to help all affected people, organizations better communicate and coordinate with each other to efficiently and effectively fight against the Novel Coronavirus (Covid-19) outbreak that started in Wuhan, Hubei, China. All of the code will be open-source and the data collected will be carefully reviewed/validated and available to the public.

This repo works as the main data warehouse. All data you see here is imported automatically by scripts. **_ Please do NOT submit data directly to this repo_**. Please refer to other sections of this document for questions about data submission.


## Collaboration process

This platform has the following collaboration process:

![img](https://yokii.cn/i/en.jpg)

All of the parts are processed automatically and won't require manual work except for the manual reviews and validations on the data/information.

##  Major Open Source Sub-Projects

### Data Synchronization

- Codebase: https://github.com/wuhan2020/data-sync

### Web Front-end Development

- Codebase：https://github.com/wuhan2020/wuhan2020.github.io
- Production environment：https://wuhan2020.github.io/

### API Service

- Codebase：https://github.com/wuhan2020/api-server

### Map Visualization Components

- Codebase：https://github.com/wuhan2020/map-viz

### Online Form Editing Service(ShiMo) Synchronization Component

- Codebase：https://github.com/wuhan2020/shimo-sheet2json

## Data Submission

The information collected by the platform includes the following types of data, please categorize and submit separately.

This platform uses the online document service [Shimo](https://shimo.im/welcome) (which is very similar to Google Docs) to collect and host data, and there is a cron script synchronizes the data to the data repo/warehouse. Please do NOT modify the data files directly in the repo/warehouse.

Due to the large number of participants, the editing permission of all personnel are not granted by default，please click [here](https://shimo.im/forms/YVJkGrGCWwQPTpqY/fill)to submit your application，we will send you an email for entry ASAP.

### Online Document Service [Shimo](https://shimo.im/welcome) Edit Link：

- [HOSPITAL](https://shimo.im/sheets/q6WP3DpKKgVW63Pr/4WbFN/)
- [HOTEL](https://shimo.im/sheets/Hd9C3QytrJK3RWxG/z1rye/)
- [LOGISTICS](https://shimo.im/sheets/RTHXp3ghtKXY3GcC/MODOC/)
- [MANUFACTURE](https://shimo.im/sheets/pchvJ6ddyRHHdXtv/MODOC/)
- [DONATION](https://shimo.im/sheets/W3gxW6cwkYTDY6DD/)
- [FREE/VOLUNTEER CLINICS](https://shimo.im/sheets/JgXjYCJJTRQxJ3GP/MODOC/)

## Contribution Guide

Please click [here](./CONTRIBUTING_EN.md)

## Data and Information Collection Guide
Please click [here](./INFORMATION_GUIDE_EN.md)

# Slack Communication Group

Click here to join the [Slack Communication Group](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTQxMTU4MzgyNTYwLWIxMTMyNWI4NWE2YTk3NGRjZGJhMjUzNmJhMjg1MDQ3OTEzNDE5NGY4MWFhMjRlYWU4MmE3ZGQyOGU4N2YwMzY)

## Slack Channel Navigation

(It requires you to join the Slack Group first following the above link)

| Channel Name               | Pointer              |
|----------------------------|----------------------|
| Default Channel               | [![Github](https://img.shields.io/badge/Slack%20Channel-%23anti--2019--ncov-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSS83MZUK)              |
| General Info           | [![Github](https://img.shields.io/badge/Slack%20Channel-%23general-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSTGKFRCH)                       |
| Team of Designers             | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--designer-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT70SHJQ0)                |
| Team of Product Requirements/Management     | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--requirement--management-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT99VDWS2) |
| Team of Frondend Folks            | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--frontend-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT93L48H5)                |
| Team of Backend Folks             | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--backend-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT93MCEJK)                 |
| Sub Project: Data Sync       | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--data--sync-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT4AV807P)              |
| Sub Project: Web Front pages    | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--front--pages-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSTPXN533)            |
| Sub Project: Map Visualizations | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--map--visualization-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT6HW3X8E)      |
| Sub Project: API Server      | [![Github](https://img.shields.io/badge/Slack%20Channel-%23api--server-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT3V5CDKJ)                   |
| Collect Advise to the Officials       | [![Github](https://img.shields.io/badge/Slack%20Channel-%23help--advisement-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT7AABP53)              |
| Team of Oversea Folks               | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--overseas-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CTAM5R65U)                |
| Team of Slack Channel Operations      | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--operation-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSX1X74M9)               |

# E-mail List

wuhan2020 e-mail list: [wuhan2020@googlegroups.com](https://groups.google.com/forum/#!forum/wuhan2020) ([subscribe](mailto:wuhan2020+subscribe@googlegroups.com), [unsubscribe](mailto:wuhan2020+unsubscribe@googlegroups.com), [archive](https://groups.google.com/forum/#!forum/wuhan2020))

Welcome to join together to explore all kinds of technical and non-technical issues, let's all work together and united to overcome the difficulties and fight against the virus!

# FAQ

Selected FAQ，[click here](https://community.wuhan2020.org.cn/en-us/docs/overview/faq.html).

FAQ for Info Collection Team, [click here](https://shimo.im/docs/JqX9CvrqphPV9T3J/).

Follow [Shimo Document](https://shimo.im/docs/DdWvXvtvpxrqrJ83)

---
Translator: [@CNYoki](https://github.com/CNYoki) , Proofreader: [@Atena1118](https://github.com/Atena1118) [@JoeZijunZhou](https://github.com/JoeZijunZhou)
