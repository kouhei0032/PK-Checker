# リンカチェッカー (PK-Checker)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-%2334A853.svg?style=for-the-badge&logo=google-sheets&logoColor=white)

日々の食事における「リン(P)」と「カリウム(K)」の情報確認を行うためのアプリです。

## アプリリンク（App Link）
このアプリは以下のURLから利用できます。

[![Open in Streamlit](https://img.shields.io/badge/Open%20in%20Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://pk-checker.streamlit.app/)

## 背景　(Background)
1. 解決したい課題
透析治療を受けている患者にとって、日々の食事における「リン」「カリウム」「塩分」の摂取量管理は極めて重要です。過剰摂取は心不全や高カリウム血症などの深刻な合併症を引き起こすリスクがあるため、常に細心の注意を払う必要があります。しかし、既存の栄養計算アプリや食品成分表は以下のような課題を抱えています。

* 情報過多: 文部科学省の「日本食品標準成分表」には2,400項目以上のデータがあり、日常的に使う食材を探し出すのが困難。
* 状態による変動: 「ゆで」「乾」など、調理状態によって栄養価が激変するが、その選択を誤りやすい。
* 直感性の欠如: 数値だけでは、それが自分にとって「安全」か「危険」かを即座に判断しにくい。

2. プロジェクトの目的
本プロジェクト「リンカ検索」は、「迷わず、素早く、直感的に」栄養価を確認できるサポートツールの提供を目指して開発されました。
単にデータを表示するだけでなく、以下の3点に重きを置いています。

* データの最適化（キュレーション）: 膨大なマスターデータから、家庭でよく使われる食材や調理状態を厳選・整理し、検索ストレスを最小限に抑える。
* 視覚的なフィードバック: 独自のアルゴリズムに基づき、数値に応じて色（青・赤・標準）を変化させることで、一目でリスクを把握可能にする。
* アクセシビリティ: 外出先やキッチンでも片手で操作しやすいよう、モバイルフレンドリーなUIを設計。
