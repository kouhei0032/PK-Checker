import streamlit as st

st.set_page_config(page_title="リンカリナビ", page_icon="🥗")

# 1. ページの定義
# ホーム画面用の中身は pages/home.py に移動させます
home_page = st.Page(
    "pages/home.py",
    title="ホーム",
    icon="🏠",
    default=True
)

food_search_page = st.Page(
    "pages/food_search.py",
    title="食品検索",
    icon="🔍"
)

menu_search_page = st.Page(
    "pages/menu_search.py",
    title="外食検索",
    icon="🍴"
)

guide_page = st.Page(
    "pages/guide.py",
    title="公式ガイド",
    icon="📘"
)

dev_page = st.Page(
    "pages/dev.py",
    title="開発について",
    icon="👨‍💻"
)

# ブラウザに「これは日本語のページです」と明示的に伝える
st.markdown('<html lang="ja"></html>', unsafe_allow_html=True)

# 2. ナビゲーションの設定
pg = st.navigation([home_page, food_search_page, menu_search_page, guide_page,dev_page])

# 4. 実行
pg.run()