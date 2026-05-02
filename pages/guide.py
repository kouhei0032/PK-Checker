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
    <span class="no-wrap-title">📘 公式ガイド</span>
    """, unsafe_allow_html=True)

st.subheader("1. アプリに記載されているデータ")
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

- 低リン: 100gあたり 100mg以下（青色）
- 中リン: 100gあたり 101〜1150mg（黒色）
- 高リン: 100gあたり 151mg以上（赤色）
- 低カリウム: 100gあたり 150mg以下（青色）
- 中カリウム: 100gあたり 151〜300mg（黒色）
- 高カリウム: 100gあたり 301mg以上（赤色）
""")

st.subheader("3. 外食検索について")
st.write("""
外食検索では日本食品標準成分表（八訂）のデータを元にAIが推計しています。またリンとカリウムの
含有量によって、数値の色を変化させています。

- 低リン: 1食あたり 200mg以下（青色）
- 中リン: 1食あたり 201〜350mg（黒色）
- 高リン: 1食あたり 351mg以上（赤色）

- 低カリウム: 1食あたり 400mg以下（青色）
- 中カリウム: 1食あたり 401〜600mg（黒色）
- 高カリウム: 1食あたり 601mg以上（赤色）
  
リンの吸収率は下記の分類ルールに基づき定義しています。

- 低: 穀類、豆類、野菜（植物性リン）：植物のリンは分解しにくいため吸収率が低めで20%～30%吸収されます
- 中: 肉類、魚類（タンパク質に含まれるリン）：動物性タンパク質由来のリンは40%～60%吸収されます
- 高: 加工食品の添加物（リン酸塩）、魚卵、乳製品、練物：添加物（無機リン）はほぼ100%吸収されます
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