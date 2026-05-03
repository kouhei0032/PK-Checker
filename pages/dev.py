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
「透析患者さんのQOL応援プロジェクト」は、現役の人工透析患者である私自身の経験から生まれた、非営利の活動です。
普段はシステムエンジニアとして働きながら、夜間週3日の透析を続けています。透析のない日の食事はどうしても外食に偏りがちになりますが、
その際「この料理にはどれくらいのリンやカリウムが含まれているんだろう？」と、心配になることもありました。

特に透析を導入した直後は、これまでの食生活をどう変えるべきか、戸惑う方も多いのではないでしょうか。
そんな時に、手軽にリン・カリウムの成分をチェックできるツールがあれば、食事選びがもっと前向きに、便利になると考え、このアプリを開発しました。

本アプリは、どなたでも無料でご利用いただけます。皆様の健やかな食事管理の一助となれば幸いです。
""")

st.subheader("2. 技術スタックと専門性について ")
st.write("""
本アプリは、現役のシステムエンジニアとしての知見を活かし、データの正確性とプライバシーへの配慮を最優先に開発しています。

- 言語・環境: Python / Streamlit を採用し、高速かつモダンなUIを実現
- データ管理: Google Sheets / Google Apps Script (GAS) を利用した、安全でメンテナンス性の高いデータベースを構築
- 業務経験: 日中はシステムエンジニアとして、大規模なデータ処理や効率的なアルゴリズム構築に従事。その経験を、複雑な栄養計算のロジックに反映させています。
""")

st.subheader("3. OFUSEで応援を送る")
st.write("本プロジェクトは非営利で運営しており、頂いたご支援は開発維持費や、"
         "データの調査にかかる実費、また活動に必要なインフラ費用の一部として大切に活用させていただきます。"
         "同じ悩みを持つ方々の力になれるよう開発を続けてまいりますので、温かい応援をいただけますと幸いです。")
# OFUSEボタンの自作
ofuse_url = "https://ofuse.me/o?uid=174869"

st.markdown(f"""
    <style>
    .ofuse-button {{
        display: inline-block;
        background-color: #FF4B4B; /* OFUSEに近い赤色 */
        color: white !important;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none !important;
        font-weight: bold;
        font-size: 16px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: 0.3s;
    }}
    .ofuse-button:hover {{
        background-color: #D63D3D;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transform: translateY(-1px);
    }}
    </style>

    <a href="{ofuse_url}" target="_blank" class="ofuse-button">
        OFUSEで応援を送る
    </a>
    <p style="font-size: 12px; color: #666; margin-top: 10px;">
        ※外部サイト（OFUSE）へ移動します。
    </p>
""", unsafe_allow_html=True)

st.subheader("4. お問い合わせ")
st.write("""
アプリへのご要望や不具合報告などがございましたら、下記のメールアドレスまでお気軽にご連絡ください。
皆様の声をもとに、より使いやすいアプリを目指して改善を続けてまいります。

ありがたいことに、銀行振込による寄付のご相談をいただくことがございます。
本プロジェクトは非営利で運営しており、振込でのご支援をご希望の場合は、個別に振込先口座をご案内させていただきます。
誠にお手数ですが、下記の **「公式メールアドレス」** より、メールにて銀行振込希望の旨をご連絡いただけますと幸いです。
お送りいただいたご支援は、サーバー維持費やデータの調査費用として、責任を持って大切に活用させていただきます。
""")

st.write("rinkari.navi@●●●.com")
st.caption("※返信にお時間をいただく場合がございます。あらかじめご了承ください。")

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

st.caption("Developed by Kouhei Takahashi | 透析患者さんのQOL応援プロジェクト")