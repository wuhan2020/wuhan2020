# [简体中文](./README.md) | [繁體中文](./README_TW.md) | [English](./README_EN.md) | 日本語 | [Italiano](./README_IT.md) | [Português](./README_PT.md) <!-- omit in toc -->

[![wuhan2020 コミュニティ公式ウェブサイト](https://img.shields.io/badge/wuhan2020-コミュニティ公式ウェブサイト-green.svg?style=for-the-badge&colorB=red)](http://community.wuhan2020.org.cn/ja-jp)
[![wuhan2020 公式発表](https://img.shields.io/badge/wuhan2020-公式発表-green.svg?style=for-the-badge&colorB=red)](http://community.wuhan2020.org.cn/ja-jp/blog/wuhan2020-official-announcement.html)

### 志愿者入口        >>> [![[ここをリックすると参加できます Slack 交流グループ]](https://img.shields.io/badge/slack-join-orange.svg)](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTQxMTU4MzgyNTYwLWIxMTMyNWI4NWE2YTk3NGRjZGJhMjUzNmJhMjg1MDQ3OTEzNDE5NGY4MWFhMjRlYWU4MmE3ZGQyOGU4N2YwMzY)

- [新型コロナウイルス関連肺炎（Covid-19）情報共有サイト](#%e6%96%b0%e5%9e%8b%e3%82%b3%e3%83%ad%e3%83%8a%e3%82%a6%e3%82%a4%e3%83%ab%e3%82%b9%e9%96%a2%e9%80%a3%e8%82%ba%e7%82%8eCovid-19%e6%83%85%e5%a0%b1%e5%85%b1%e6%9c%89%e3%82%b5%e3%82%a4%e3%83%88)
  - [協力フローチャート](#%e5%8d%94%e5%8a%9b%e3%83%95%e3%83%ad%e3%83%bc%e3%83%81%e3%83%a3%e3%83%bc%e3%83%88)
  - [メインオープンソース](#%e3%83%a1%e3%82%a4%e3%83%b3%e3%82%aa%e3%83%bc%e3%83%97%e3%83%b3%e3%82%bd%e3%83%bc%e3%82%b9)
    - [データ同期](#%e3%83%87%e3%83%bc%e3%82%bf%e5%90%8c%e6%9c%9f)
    - [webフロントエンド開発](#web%e3%83%95%e3%83%ad%e3%83%b3%e3%83%88%e3%82%a8%e3%83%b3%e3%83%89%e9%96%8b%e7%99%ba)
    - [API サービス](#api-%e3%82%b5%e3%83%bc%e3%83%93%e3%82%b9)
    - [ストーリーマップコンポーネント](#%e3%82%b9%e3%83%88%e3%83%bc%e3%83%aa%e3%83%bc%e3%83%9e%e3%83%83%e3%83%97%e3%82%b3%e3%83%b3%e3%83%9d%e3%83%bc%e3%83%8d%e3%83%b3%e3%83%88)
    - [(shimo)ファイル同期コンポーネント](#shimo%e3%83%95%e3%82%a1%e3%82%a4%e3%83%ab%e5%90%8c%e6%9c%9f%e3%82%b3%e3%83%b3%e3%83%9d%e3%83%bc%e3%83%8d%e3%83%b3%e3%83%88)
  - [情報提供](#%e6%83%85%e5%a0%b1%e6%8f%90%e4%be%9b)
    - [(shimo)ファイル編集リンク：](#shimo%e3%83%95%e3%82%a1%e3%82%a4%e3%83%ab%e7%b7%a8%e9%9b%86%e3%83%aa%e3%83%b3%e3%82%af)
  - [貢献ガイド](#%e8%b2%a2%e7%8c%ae%e3%82%ac%e3%82%a4%e3%83%89)
  - [情報収集ガイド](#%e6%83%85%e5%a0%b1%e5%8f%8e%e9%9b%86%e3%82%ac%e3%82%a4%e3%83%89)
- [Slack 交流グループ](#slack-%e4%ba%a4%e6%b5%81%e3%82%b0%e3%83%ab%e3%83%bc%e3%83%97)
  - [Slackチャンネルナビゲーション](#slack%e3%83%81%e3%83%a3%e3%83%b3%e3%83%8d%e3%83%ab%e3%83%8a%e3%83%93%e3%82%b2%e3%83%bc%e3%82%b7%e3%83%a7%e3%83%b3)
- [FAQ （更新中，ボランティア募集中）](#faq-%e6%9b%b4%e6%96%b0%e4%b8%ad%e3%83%9c%e3%83%a9%e3%83%b3%e3%83%86%e3%82%a3%e3%82%a2%e5%8b%9f%e9%9b%86%e4%b8%ad)

# 新型コロナウイルス関連肺炎（Covid-19）情報共有サイト
11:00（CST）1/31/2020時点で更新,最新のアップデートについては、中国語版と英語版を確認してください。

2020年初、武漢市に発生した新型コロナウイルス関連肺炎に対し、各病院、ホテル、工場、物流、寄贈、寄付金、予防、治療、活動などを統一収集又は公表、お互いに情報共有、又は有効に社会資源を上手く利用する出来るようにすることを目的としています。中国湖北省武漢より発生した新型コロナウイルス（Covid-19）と効率的に戦っていきます。すべてのコードはオープンソースであり、収集されたデータは慎重にレビュー・検証されたうえで、一般に公開されます。

本プロジェクトはデータウェアハウスをメインとして、すべてのデータはスクリプトを使用し自動導入されています。**_直接データウェアハウスに提出することはご遠慮ください_**，具体的な提出ルートは以下を参照してください。

## 協力フローチャート

本プログラムでは皆さんが円滑に進めるために、以下のフローチャートを組み立てました。

![img](https://yokii.cn/i/en.jpg)

提供された情報は、データの検証やレビューを除いてすべて自動的に処理されるため、手動での作業は必要ありません。

## メインオープンソース

### データ同期

- コードリポジトリ： https://github.com/wuhan2020/data-sync

### webフロントエンド開発

- コードリポジトリ：https://github.com/wuhan2020/WebApp
- 応用サイト：https://wuhan2020.kaiyuanshe.cn/

### API サービス

- コードリポジトリ：https://github.com/wuhan2020/api-server

### ストーリーマップコンポーネント

- コードリポジトリ：https://github.com/wuhan2020/map-viz

### (shimo)ファイル同期コンポーネント

- コードリポジトリ：https://github.com/wuhan2020/shimo-sheet2json

## 情報提供

本プロジェクトで収集する情報は以下のように分類されています。それぞれに記入してください。

本プロジェクトは(shimo)ファイルを利用して、情報収集を行います。そして、すべてのデータはスクリプトを使用し自動導入されてます。直接ファイルを書き換えることはご遠慮ください。

参加人数が多いため、全ての人に編集権限を与えることができません。ここを[クリック](https://shimo.im/forms/YVJkGrGCWwQPTpqY/fill)して申し込むと、招待メールが送られます。

### (shimo)ファイル編集リンク：

- [病院](https://shimo.im/sheets/q6WP3DpKKgVW63Pr/4WbFN/ )
- [ホテル](https://shimo.im/sheets/Hd9C3QytrJK3RWxG/z1rye/)
- [物流](https://shimo.im/sheets/RTHXp3ghtKXY3GcC/MODOC/)
- [生産](https://shimo.im/sheets/pchvJ6ddyRHHdXtv/MODOC/)
- [寄贈](https://shimo.im/sheets/W3gxW6cwkYTDY6DD/)
- [無料診療](https://shimo.im/sheets/JgXjYCJJTRQxJ3GP/MODOC/)
- [在外武漢観光客の宿泊先](https://shimo.im/sheets/pdHRcXyKqJdqPyGJ/MODOC/)

もし新しいファイルを作りたい場合、[新規ファイル申し込み]（https://shimo.im/forms/rcThp3vPqqrtvChV/fill ）を記入してください。


## 貢献ガイド

ここを[クリック](./CONTRIBUTING.md)してください。

## 情報収集ガイド

ここを[クリック](https://community.wuhan2020.org.cn/ja-jp/docs/dev/contributing.html)してください。

# Slack 交流グループ
ここをリックすると参加できます[Slack 交流グループ](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTQxMTU4MzgyNTYwLWIxMTMyNWI4NWE2YTk3NGRjZGJhMjUzNmJhMjg1MDQ3OTEzNDE5NGY4MWFhMjRlYWU4MmE3ZGQyOGU4N2YwMzY)

## Slackチャンネルナビゲーション
(最初にグループに参加する必要があります)

| お名前     | リンク     |
|-----------|----------|
| デフォルトチャンネル        | [![Github](https://img.shields.io/badge/Slack%20Channel-%23anti--2019--ncov-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSS83MZUK)              |
| 一般情報リリース       | [![Github](https://img.shields.io/badge/Slack%20Channel-%23general-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSTGKFRCH)                       |
| デザインスキルグループ | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--designer-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT70SHJQ0)                |
| 製品要件管理チーム     | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--requirement--management-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT99VDWS2) |
| フロントエンド開発チーム| [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--frontend-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT93L48H5)                |
| バックエンド開発チーム  | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--backend-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT93MCEJK)                 |
| サブプロジェクト：データ同期| [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--data--sync-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT4AV807P)              |
| サブプロジェクト：Webフロントエンド | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--front--pages-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSTPXN533)            |
| サブプロジェクト：データマップの視覚化 | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--map--visualization-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT6HW3X8E)      |
| サブプロジェクト：APIサーバー| [![Github](https://img.shields.io/badge/Slack%20Channel-%23api--server-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT3V5CDKJ)                   |
| 提案       | [![Github](https://img.shields.io/badge/Slack%20Channel-%23help--advisement-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT7AABP53)              |
| 中国本土外              | [![Github](https://img.shields.io/badge/Slack%20Channel-%23team--overseas-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CTAM5R65U)                |
| Slackチャネル運用チーム      | [![Github](https://img.shields.io/badge/Slack%20Channel-%23proj--operation-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CSX1X74M9)               |

初心者の方も経験者の方も貢献出来るように心からお待ちしております！こころをあわせて、一緒に危機を乗り越えましょう！

# FAQ （更新中，ボランティア募集中）

よくある質問，[クリック](https://community.wuhan2020.org.cn/ja-jp/docs/overview/faq.html)

情報グループFAQ，[クリック](https://shimo.im/docs/JqX9CvrqphPV9T3J/)

クリックしてください[shimoファイル](https://shimo.im/docs/DdWvXvtvpxrqrJ83)

翻訳者 Sakula Air, Yoki 校正者 Yoki W, [RRF](https://github.com/RRFHOUDEN)
