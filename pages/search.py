import streamlit as st

st.set_page_config(page_title="search", page_icon="📚")

st.title("🔍 リンカ検索")
st.write("日々の献立管理における、リン(P)とカリウム(K)の計算をサポートします。")

st.info("""
### 💡 このアプリでできること
- **食材別の成分確認**: 文部科学省のデータベースに基づいた正確な計算。
- **摂取量の見える化**: 制限値を超えないためのスマートなチェック。
""")

st.write("Developed by Kohei Takahashi")