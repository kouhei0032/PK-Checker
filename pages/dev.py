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
    <span class="no-wrap-title">‍👨‍💻 開発者について</span>
    """, unsafe_allow_html=True)

st.subheader("1. アプリ開発の想い")
st.write("""
本アプリのデータは、文部科学省：日本食品標準成分表（八訂）を利用しています。食品検索データはこちらのデータを
そのまま掲載しています。外食検索では、日本食品標準成分表（八訂）を元に一般的なレシピを用いて、AIが推計した
データを用いています。
""")

st.subheader("2. 食品検索について")
st.write("""
食品検索では日本食品標準成分表（八訂）のデータをピックアップして利用しています。そのままデータ利用すると
件数が膨大になるので、利用する方が選びやすいようにこちらでピックアップしています。またリンとカリウムの
含有量によって、数値の色を変化させていますが、下記のような条件で判定してます。

- 低リン: 100gあたり 100mg未満（青色）
- 中リン: 100gあたり 101〜149mg（黒色）
- 高リン: 100gあたり 150mg以上（赤色）
- 低カリウム: 100gあたり 150mg未満（青色）
- 中カリウム: 100gあたり 151〜299mg（黒色）
- 高カリウム: 100gあたり 300mg以上（赤色）
""")

st.caption("Developed by Kouhei Takahashi | 透析患者さんの食事管理応援プロジェクト")