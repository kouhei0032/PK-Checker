import streamlit as st

st.markdown("""
    <style>
    .no-wrap {
        white-space: nowrap;
        font-size: 2.25rem; /* st.titleに近いサイズ */
        font-weight: 700;
        margin-bottom: 1.5rem;
    }
    </style>
    <div class="no-wrap">🥗 リンカチェッカー</div>
    """, unsafe_content_safe=True)

st.write("日々の献立管理における、リン(P)とカリウム(K)の計算をサポートします。")

st.info("""
### 💡 このアプリでできること
- **食材別の成分確認**: 文部科学省のデータベースに基づいた正確な計算。
- **摂取量の見える化**: 制限値を超えないためのスマートなチェック。
""")

st.caption("Developed by Kohei Takahashi")