[简体中文](./README.md) | [English](./README_EN.md) | 日本語 | [Italiano](./README_IT.md)

# 新型コロナウイルス関連肺炎（2019-nCoV）情報共有サイト
11:00（CST）1/31/2020時点で更新,最新のアップデートについては、中国語版と英語版を確認してください。

2020年初、武漢市に発生した新型コロナウイルス関連肺炎に対し、情報収集と目的として、各病院、ホテル、工場、物流、寄贈、寄付金、予防、治療、活動などを統一収集又は公表、お互いに情報共有、又は有効に社会資源を上手く利用する出来るように。　　　　　

本プロジェクトはデータウェアハウスをメインとして、すべてのデータはスクリプトを使用し自動導入されている。**_直接データウェアハウスに提出することはご遠慮ください_**，具体的な提出ルートは下に参照してください。

## 協力フローチャート

本プログラムでは皆さんが円滑に進めるために、以下のフローチャートを組み立てた。

![img](https://yokii.cn/i/en.jpg)

提供した情報は他人認証が必要以外、ほかの部分は全部自動化され、人為的な介入を行わず。

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

本プロジェクトは収集する情報は以下のように分類されている、別々に記入してください。

本プロジェクトは(shimo)ファイルを利用して、情報収集を行う、その上にすべてのデータはスクリプトを使用し自動導入されている。直接にファイルの改ざんなどはご遠慮ください。

参加人数が多いため、全ての人に編集権限を与えることができない。ここに[クリック](https://shimo.im/forms/YVJkGrGCWwQPTpqY/fill)申し込んだ後に、招待メールを送る。

### (shimo)ファイル編集リンク：

- [病院](https://shimo.im/sheets/q6WP3DpKKgVW63Pr/4WbFN/ )
- [ホテル](https://shimo.im/sheets/Hd9C3QytrJK3RWxG/z1rye/)
- [物流](https://shimo.im/sheets/RTHXp3ghtKXY3GcC/MODOC/)
- [生産](https://shimo.im/sheets/pchvJ6ddyRHHdXtv/MODOC/)
- [寄贈](https://shimo.im/sheets/W3gxW6cwkYTDY6DD/)
- [無料診療](https://shimo.im/sheets/JgXjYCJJTRQxJ3GP/MODOC/)
- [在外武漢観光客の宿泊先](https://shimo.im/sheets/pdHRcXyKqJdqPyGJ/MODOC/)

もし新しいファイルを開ければ、[新しいファイル申し込み]（https://shimo.im/forms/rcThp3vPqqrtvChV/fill ）を記入してください。


## 貢献ガイド

ここに[クリック](./CONTRIBUTING.md)してください。

## 情報収集ガイド
ここに[クリック](./INFORMATION_GUIDE.md)してください。


# Slack 交流グループ
ここにクリックすると参加できる[Slack 交流グループ](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTI2NTU1NzU3MTM2LWQ1YjIzMDllYjYzYTE1OTNhMWU4OTZkOGYzOGJhOWM2MzdlMjgwMmZiOWEzYTQwNmJkZDI4OWRmM2Q2ZDM1MTc)

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

初心者の方、専門家の方問わずに交流出来るように心からお待ちしております！こころをあわせて、一緒に難関を乗り越えよう！

# FAQ （更新中，ボランティア募集中）

よくある質問，[クリック](./FAQ.md)

情報グループFAQ，[クリック](https://shimo.im/docs/JqX9CvrqphPV9T3J/)

クリックしてください[shimoファイル](https://shimo.im/docs/DdWvXvtvpxrqrJ83)

翻訳者 Sakula Air, Yoki, 校正者 Yoki W.
