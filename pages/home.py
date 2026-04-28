import streamlit as st

st.markdown("""
    <style>
    .no-wrap-title {
        white-space: nowrap;       /* 改行を禁止 */
        font-size: 2.25rem;        /* タイトルの大きさ */
        font-weight: 700;          /* 太字 */
        padding: 1.25rem 0;        /* 上下の余白 */
        line-height: 1.2;
        display: block;
    }
    </style>
    <span class="no-wrap-title">🥗 リンカチェッカー</span>
    """, unsafe_allow_html=True)

st.write("日々の献立管理における、リン(P)とカリウム(K)の計算をサポートします。")

st.info("""
### 💡 このアプリでできること
- **食材別の成分確認**: 文部科学省のデータベースに基づいた正確な計算。
- **摂取量の見える化**: 制限値を超えないためのスマートなチェック。
""")

# --- 追加：スマホ横幅いっぱいの検索ボタン風リンク ---
st.markdown("""
    <style>
    /* リンク全体の設定（下線を消す） */
    .link-container {
        text-decoration: none !important;
        display: block;
        width: 100%;
        margin-top: 10px;
    }

    /* 実際のボタンの見た目（中身のdivに設定） */
    .button-design {
        background-color: #007bff;
        color: white !important;
        text-align: center;
        padding: 15px 0;
        border-radius: 10px;
        font-weight: bold;
        font-size: 1.1rem;
        transition: 0.3s;
        /* ここでも下線が出ないよう念押し */
        text-decoration: none !important;
    }

    .button-design:hover {
        background-color: #0056b3;
    }

    /* Streamlitが強制的に引く下線を完全に消去 */
    .link-container * {
        text-decoration: none !important;
    }
    </style>

    <a href="/search" target="_self" class="link-container">
        <div class="button-design">
            🔍 リンカ検索をはじめる
        </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.caption("Developed by Kouhei Takahashi")