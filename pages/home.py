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

st.caption("Developed by Kohei Takahashi")