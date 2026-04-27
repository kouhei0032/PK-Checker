import streamlit as st

st.set_page_config(page_title="PK-Checker", page_icon="🥗")

# 1. ページの定義
# ホーム画面用の中身は pages/home.py に移動させます
home_page = st.Page(
    "pages/home.py",
    title="ホーム",
    icon="🏠",
    default=True
)

search_page = st.Page(
    "pages/search.py",
    title="リンカ検索",
    icon="🔍"
)

# 2. ナビゲーションの設定
pg = st.navigation([home_page, search_page])

# 4. 実行
pg.run()