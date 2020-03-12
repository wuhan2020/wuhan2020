# [简体中文](./README.md) | [繁體中文](./README_TW.md) | [English](./README_EN.md) | [日本語](./README_JP.md) | [Italiano](./README_IT.md) | [Português](./README_PT.md) | 한국어 <!-- omit in toc -->

[![Github](https://img.shields.io/badge/wuhan2020-Community%20Website-green.svg?style=for-the-badge&colorB=red)](https://community.wuhan2020.org.cn/en-us/)
[![Github](https://img.shields.io/badge/wuhan2020-OFFICIAL%20ANNOUNCEMENT-green.svg?style=for-the-badge&colorB=red)](https://community.wuhan2020.org.cn/en-us/blog/wuhan2020-official-announcement.html)

### 자원 시작하기         >>> [![Get on Slack](https://img.shields.io/badge/slack-join-orange.svg)](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTQxMTU4MzgyNTYwLWIxMTMyNWI4NWE2YTk3NGRjZGJhMjUzNmJhMjg1MDQ3OTEzNDE5NGY4MWFhMjRlYWU4MmE3ZGQyOGU4N2YwMzY)

- [COVID-19 확산 방지를 위한 정보 취합 플랫폼](#COVID-19-확산-방지를-위한-정보-취합-플랫폼)
  - [협업 절차](#collaboration-process)
  - [주요 오픈소스 하위 프로젝트](#major-open-source-sub-projects)
    - [데이터 동기화](#data-synchronization)
    - [웹 프론트엔드 개발](#web-front-end-development)
    - [API 서비스](#api-service)
    - [지도 시각화 컴포넌트](#map-visualization-components)
    - [온라인 양식 편집 서비스(ShiMo) 동기화 컴포넌트](#online-form-editing-serviceshimo-synchronization-component)
  - [자료 제출](#data-submission)
    - [온라인 문서 서비스 Shimo 편집 링크：](#online-document-service-shimo-edit-link)
  - [기여 가이드](#contribution-guide)
  - [자료 및 정보 수집 가이드](#data-and-information-collection-guide)
- [슬랙 소통 그룹](#slack-communication-group)
  - [슬랙 채널 안내](#slack-channel-navigation)

# COVID-19 확산 방지를 위한 정보 취합 플랫폼
이 번역은  2020-03-10 13:49:00(KST)에 갱신되었습니다.

이 프로젝트는 병원, 호텔, 제조, 물류, 기부, 봉사, 예방, 치료 및 신뢰할 수 있는 출처의 국가 전염병 예방에 관한 모든 실시간 정보를 수집하여 영향을 받는 모든 사람, 조직이 서로 잘 의사 소통 할 수 있도록 도와줍니다. 중국 후베이 우한에서 시작된 신종 코로나 바이러스 (COVID-19) 발생에 맞서 효율적이고 효과적으로 싸울 수 있습니다. 모든 코드는 공개되며 수집 된 자료는 신중하게 검토 및 검증하여 공개됩니다.

이 저장소는 기본 데이터 웨어하우스로 작동합니다. 여기에 표시되는 모든 자료는 스크립트에 의해 자동으로 가져옵니다. **_이 저장소에 직접 자료를 제출하지 마십시오_** 데이터 제출에 대한 질문은 문서의 다른 섹션을 참조하십시오.


## 협업 절차

이 플랫폼은 다음과 같은 협업 절차를 따릅니다:

![img](https://yokii.cn/i/en.jpg)

모든 절차는 자동으로 처리되므로 데이터 및 정보에 대한 직접 검토 및 검증을 제외하고 수동 작업이 필요하지 않습니다.

##  주요 오픈소스 하위 프로젝트

### 데이터 동기화

- 코드 저장소: https://github.com/wuhan2020/data-sync

### 웹 프론트엔드 개발

- 코드 저장소：https://github.com/wuhan2020/WebApp
- 공식 프로젝트 사이트 : https://wuhan2020.kaiyuanshe.cn/

### API 서비스

- 코드 저장소：https://github.com/wuhan2020/api-server

### 지도 시각화 컴포넌트

- 코드 저장소：https://github.com/wuhan2020/map-viz

### 온라인 양식 편집 서비스(ShiMo) 동기화 컴포넌트

- 코드 저장소：https://github.com/wuhan2020/shimo-sheet2json

## 자료 제출

플랫폼에서 수집한 정보에는 다음 유형의 데이터가 포함됩니다. 별도로 분류하여 제출하십시오.

이 플랫폼은 온라인 문서 서비스 [Shimo](https://shimo.im/welcome)(Google Docs와 매우 유사함)를 사용하여 데이터를 수집 및 호스팅하며, CRON 스크립트가 저장소 및 데이터 웨어하우스에 동기화합니다. 저장소 및 데이터 웨어하우스의 파일을 직접 변경하지 마십시오.

참가자 수가 많으므로 기본적으로 모든 참여자에게 편집 권한이 부여되지 않습니다. 신청서를 제출하려면 [여기](https://shimo.im/forms/YVJkGrGCWwQPTpqY/fill)를 눌러주세요. 최대한 빨리 이메일로 응답해드리겠습니다.

### 온라인 문서 서비스 [Shimo](https://shimo.im/welcome) 편집 링크：

- [병원](https://shimo.im/sheets/q6WP3DpKKgVW63Pr/4WbFN/)
- [호텔](https://shimo.im/sheets/Hd9C3QytrJK3RWxG/z1rye/)
- [물류](https://shimo.im/sheets/RTHXp3ghtKXY3GcC/MODOC/)
- [제조](https://shimo.im/sheets/pchvJ6ddyRHHdXtv/MODOC/)
- [기부](https://shimo.im/sheets/W3gxW6cwkYTDY6DD/)
- [봉사](https://shimo.im/sheets/JgXjYCJJTRQxJ3GP/MODOC/)

## 기여 가이드

[여기](./CONTRIBUTING_EN.md)를 눌러주세요.

## 자료 및 정보 수집 가이드
[여기](./INFORMATION_GUIDE_EN.md)를 눌러주세요.

# 슬랙 소통 그룹

여기를 눌러[슬랙 소통 그룹](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTQxMTU4MzgyNTYwLWIxMTMyNWI4NWE2YTk3NGRjZGJhMjUzNmJhMjg1MDQ3OTEzNDE5NGY4MWFhMjRlYWU4MmE3ZGQyOGU4N2YwMzY)에 참여해주세요.

## 슬랙 채널 안내

(위 링크에 따라 슬랙 그룹에 먼저 가입해야합니다)

| 채널 이름               | 링크              |
|----------------------------|----------------------|
| 기본 채널               | [![Github](https://img.shields.io/badge/Slack%20Channel-%23anti--2019--ncov-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSS83MZUK)              |
| 일반 정보           | [![Github](https://img.shields.io/badge/Slack%20Channel-%23general-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSTGKFRCH)                       |
| 디자이너 팀             | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--designer-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT70SHJQ0)                |
| 제품 요구사항/관리 팀     | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--requirement--management-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT99VDWS2) |
| 프론트엔드 팀            | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--frontend-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT93L48H5)                |
| 백엔드 팀             | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--backend-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT93MCEJK)                 |
| 하위 프로젝트: 자료 동기화       | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--data--sync-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT4AV807P)              |
| 하위 프로젝트: 웹 프론트 페이지    | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--front--pages-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSTPXN533)            |
| 하위 프로젝트: 지도 시각화 | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--map--visualization-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT6HW3X8E)      |
| 하위 프로젝트: API 서버      | [![Github](https://img.shields.io/badge/Slack%20Channel-%23api--server-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT3V5CDKJ)                   |
| 자문 팀       | [![Github](https://img.shields.io/badge/Slack%20Channel-%23help--advisement-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT7AABP53)              |
| 해외 팀               | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--overseas-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CTAM5R65U)                |
| 슬랙 채널 운영 팀      | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--operation-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSX1X74M9)               |

# 전자우편 목록

wuhan2020 전자우편 목록: [wuhan2020@googlegroups.com](https://groups.google.com/forum/#!forum/wuhan2020) ([구독](mailto:wuhan2020+subscribe@googlegroups.com), [구독해지](mailto:wuhan2020+unsubscribe@googlegroups.com), [포럼](https://groups.google.com/forum/#!forum/wuhan2020))

모든 종류의 기술 및 비기술적 문제를 모색하기 위해 함께 모여 오신 것을 환영합니다. 모든 사람들이 함께 노력하여 어려움을 극복하고 바이러스와 싸우도록합시다!

# FAQ

자주 묻는 질문은 [여기](https://community.wuhan2020.org.cn/en-us/docs/overview/faq.html)를 눌러주세요.

자료 수집 팀에 대한 자주 묻는 질문은 [여기](https://shimo.im/docs은/JqX9CvrqphPV9T3J/)를 눌러주세요.


[Shimo 문서](https://shimo.im/docs/DdWvXvtvpxrqrJ83)를 눌러주세요.

---
번역: Go Namhyeon [@gnh1201](https://github.com/gnh1201)
