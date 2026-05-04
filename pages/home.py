import streamlit as st
import base64
from pathlib import Path

# st.markdown("""
#     <style>
#     .no-wrap-title {
#         white-space: nowrap;       /* 改行を禁止 */
#         font-size: 2.25rem;        /* タイトルの大きさ */
#         font-weight: 700;          /* 太字 */
#         padding: 1.25rem 0;        /* 上下の余白 */
#         line-height: 1.2;
#         display: block;
#     }
#     </style>
#     <span class="no-wrap-title">🥗 リンカリナビ</span>
#     """, unsafe_allow_html=True)

# 画像をBase64に変換する関数
def get_image_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# ロゴ画像のパス（staticフォルダの中にある場合）
# home.pyの場所を基準に、一つ上の階層の static/logo.png を指す
current_dir = Path(__file__).parent  # pages フォルダ
root_dir = current_dir.parent         # プロジェクトのルート
logo_path = root_dir / "static" / "logo.png"

if logo_path.exists():
    img_base64 = get_image_base64(logo_path)

    st.markdown(f"""
        <style>
        .no-wrap-title {{
            display: flex;
            align-items: center;
            white-space: nowrap;
            font-size: 2.25rem;
            font-weight: 700;
            padding: 1.25rem 0;
            line-height: 1.2;
        }}
        .title-logo-img {{
            height: 1.5em; /* 文字の大きさに合わせる */
            margin-right: 15px;
        }}
        </style>
        <div class="no-wrap-title">
            <img src="data:image/png;base64,{img_base64}" class="title-logo-img">
            リンカリナビ
        </div>
        """, unsafe_allow_html=True)
else:
    st.error("ロゴ画像が見つかりません。パスを確認してください。")

st.write("透析導入となった方の日々の食事管理における、リン(P)とカリウム(K)の情報検索をサポートするWebアプリです。"
         "食事をするとき時に気軽にリンとカリウムを検索できるアプリを目指しています。無料でご利用いただけます")

# --- スマホ横幅いっぱいの検索ボタン風リンク ---
st.markdown("""
    <style>
    .button-design {
        display: flex;             /* 追記：中身を中央に寄せる */
        align-items: center;       /* 追記：上下中央 */
        justify-content: center;    /* 追記：左右中央 */
        height: 60px;              /* 追記：高さを固定して揃える */
        color: white !important;
        text-align: center;
        border-radius: 10px;
        font-weight: bold;
        font-size: 1.1rem;
        transition: 0.3s;
        text-decoration: none !important;
        width: 100%;               /* 追記：親要素(column)いっぱいに広げる */
    }

    /* 食品検索用の色（青） */
    .btn-food {
        background-color: #007bff;
    }
    .btn-food:hover {
        background-color: #0056b3;
    }

    /* 外食検索用の色（オレンジ） */
    .btn-out {
        background-color: #ffa500;
    }
    .btn-out:hover {
        background-color: #e86c00;
    }
    
    /* データについての色（明るい緑） */
    .btn-data {
        background-color: #28a745;  /* 鮮やかな緑 */
    }
    .btn-data:hover {
        background-color: #218838;  /* ホバー時に少し暗く */
    }
    
    /* 私についての色（グレー） */
    .btn-dev {
        background-color: #ff6b6b;  /* 温かみのある赤 */
    }
    .btn-dev:hover {
        background-color: #fa5252;  /* ホバー時に少し暗く */
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlitの機能で2列に分割
col1, col2 = st.columns(2)

#1行目
with col1:
    # クラスを button-design と btn-food の両方指定
    st.markdown('<a href="/food_search" target="_self" class="button-design btn-food">🔍 食品検索</a>', unsafe_allow_html=True)

with col2:
    st.markdown('<a href="/menu_search" target="_self" class="button-design btn-out">🍴 外食検索</a>', unsafe_allow_html=True)

#2行目
col3, col4 = st.columns(2)

with col3:
    st.markdown('<a href="/guide" target="_self" class="button-design btn-data">📘 公式ガイド</a>', unsafe_allow_html=True)

with col4:
    st.markdown('<a href="/dev" target="_self" class="button-design btn-dev">👨‍💻 開発について</a>', unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

st.info("""
### 💡 アプリについて
- **食材別の成分確認**: 文部科学省のデータに基づいた計算。日本食品標準成分表（八訂）
- **外食時の成分確認**: 文部科学省のデータに基づいたAI推測。
- **摂取量の見える化**: 制限値を超えないためのスマートなチェック。
""")

st.info("""
### 🎨 色の目安について：リンとカリウムの含有量に基づいて色分けしています
- **青色**: リン・カリウムが控えめな食材（安心してお召し上がりいただけます）
- **黒色**: リン・カリウムが一般的な食材（通常の量であれば問題ありません）
- **赤色**: リン・カリウムが多めな食材（食べる量や調理法に注意しましょう）
""")

st.warning("""
**⚠️ ご利用上の注意**

本アプリの数値は文部科学省のデータベースに基づく「推定値」であり、食事管理の参考として提供するものです。
個々の病状や健康状態により必要な制限は異なります。必ず主治医や管理栄養士の指導に従ってください。
""")

st.caption("Developed by Kouhei Takahashi | 透析患者さんのQOL応援プロジェクト")