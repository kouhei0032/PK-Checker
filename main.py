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
    title="食品検索",
    icon="🔍"
)

# ブラウザに「これは日本語のページです」と明示的に伝える
st.markdown('<html lang="ja"></html>', unsafe_allow_html=True)

# 2. ナビゲーションの設定
pg = st.navigation([home_page, search_page])

# 4. 実行
pg.run()