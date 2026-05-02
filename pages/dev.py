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
    <span class="no-wrap-title">‍👨‍💻 開発について</span>
    """, unsafe_allow_html=True)

st.subheader("1. アプリ開発の想い")
st.write("""
「透析患者さんの食事管理応援プロジェクト」は、現役の人工透析患者である私自身の経験から生まれた、非営利の活動です。
普段はシステムエンジニアとして働きながら、夜間週3日の透析を続けています。透析のない日の食事はどうしても外食に偏りがちになりますが、
その際「この料理にはどれくらいのリンやカリウムが含まれているんだろう？」と、常に不安がつきまとっていました。

特に透析を導入した直後は、これまでの食生活をどう変えるべきか、戸惑う方も多いのではないでしょうか。
そんな時に、手軽にリン・カリウムの成分をチェックできるツールがあれば、食事選びがもっと前向きに、便利になると考え、このアプリを開発しました。

本アプリは、どなたでも無料でご利用いただけます。皆様の健やかな食事管理の一助となれば幸いです。
""")

# --- スマホ横幅いっぱいの戻るボタン風リンク ---
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

    <a href="/" target="_self" class="link-container">
        <div class="button-design">
            🥗 もどる
        </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.caption("Developed by Kouhei Takahashi | 透析患者さんの食事管理応援プロジェクト")