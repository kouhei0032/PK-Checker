# リンカチェッカー (PK-Checker)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-%2334A853.svg?style=for-the-badge&logo=google-sheets&logoColor=white)

日々の食事における「リン(P)」と「カリウム(K)」の情報確認を行うためのアプリです。

## アプリリンク（App Link）
このアプリは以下のURLから利用できます。

[![Open in Streamlit](https://img.shields.io/badge/Open%20in%20Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://pk-checker.streamlit.app/)

## 背景 (Background)

### 1. 解決したい課題
透析治療を受けている患者にとって、日々の食事における「リン」「カリウム」「塩分」の摂取量管理は極めて重要です。過剰摂取は心不全や高カリウム血症などの深刻な合併症を引き起こすリスクがあるため、常に細心の注意を払う必要があります。しかし、既存の食品成分表には以下の課題があります。

* **情報過多**: 「日本食品標準成分表」の2,400項目以上から、日常的な食材を探すのが困難。
* **状態による変動**: 「ゆで」「乾」といった調理状態による数値の変化を誤認しやすい。
* **直感性の欠如**: 数値だけでは、自分にとって「安全」か「危険」かを即座に判断しにくい。

### 2. プロジェクトの目的
本プロジェクト**「リンカ検索」**は、「迷わず、素早く、直感的に」栄養価を確認できるサポートツールの提供を目指して開発されました。単にデータを表示するだけでなく、以下の3点に重きを置いています。

* **データの最適化（キュレーション）**: 家庭でよく使われる食材を厳選し、検索ストレスを最小化。
* **視覚的なフィードバック**: 数値に応じて色を変化させ、一目でリスクを把握可能に。
* **アクセシビリティ**: 外出先でも操作しやすいモバイルフレンドリーなUI設計。

## 🗂 データベース (Database)
本プロジェクトでは、データの更新性と保守性を高めるため、Googleスプレッドシートをデータベースとして活用しています。

[![Database](https://img.shields.io/badge/Food_Database-34A853?style=for-the-badge&logo=google-sheets&logoColor=white)](https://docs.google.com/spreadsheets/d/1q5ACTKmnTL_2xkETX7rXajX7AG3d6I3n-DSj4QSx56Q/edit?gid=0#gid=0)
  - 収録数：約47品目（順次拡充中）
  - 特徴：調理状態（ゆで・乾）による分類、使用頻度フラグ（高・中・低）の付与
