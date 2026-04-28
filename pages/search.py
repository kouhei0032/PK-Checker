import streamlit as st
import pandas as pd

# --- 設定 ---
# ご自身のスプレッドシートのURLをここに貼り付けてください
SHEET_URL = "https://docs.google.com/spreadsheets/d/1q5ACTKmnTL_2xkETX7rXajX7AG3d6I3n-DSj4QSx56Q/export?format=csv"


@st.cache_data(ttl=600)  # 10分間キャッシュを保持（頻繁な通信を避ける）
def load_data_from_gsheets(url):
    try:
        # スプレッドシートをCSVとして読み込む
        return pd.read_csv(url)
    except Exception as e:
        st.error(f"データの読み込みに失敗しました: {e}")
        return None


# データの読み込み
df = load_data_from_gsheets(SHEET_URL)

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
    <span class="no-wrap-title">🔍 リンカ検索"</span>
    """, unsafe_allow_html=True)

st.write("食品名を検索するとリンとカリウムの含有量を表示します。")

if df is not None:
    # 検索機能：食品表示名のリストを作成
    food_options = df["食品表示名"].dropna().unique().tolist()

    # 1. まずは自由入力の検索窓（これでキーボードを強制的に出す）
    search_term = st.text_input("🔍 キーワードで絞り込み", placeholder="例: 麦")

    # 2. 入力された文字でリストをフィルタリング
    if search_term:
        filtered_options = [opt for opt in food_options if search_term in opt]
    else:
        filtered_options = food_options

    # 3. 絞り込まれたリストから選択
    selected_name = st.selectbox(
        "食品名を選択",
        filtered_options,
        index=None,
        placeholder="候補から選んでください"
    )

    if selected_name:
        # 選択された食材の行を抽出
        item = df[df["食品表示名"] == selected_name].iloc[0]

        st.divider()

        # 重量の入力
        weight = st.number_input("食べる量 (g)", min_value=1, value=100, step=10)

        # 計算（100gあたりの数値を換算）
        # ※スプレッドシートのカラム名が「カリウム：K」である前提です
        k_val = item["カリウム：K"] * weight / 100
        p_val = item["リン：P"] * weight / 100
        s_val = item["塩分"] * weight / 100

        # 結果表示
        st.subheader(f"📊 {selected_name} ({weight}g) の推定値")

        col1, col2, col3 = st.columns(3)
        col1.metric("カリウム", f"{k_val:.0f} mg")
        col2.metric("リン", f"{p_val:.0f} mg")
        col3.metric("塩分", f"{s_val:.1f} g")

        # 備考や詳細情報
        with st.expander("詳細データ・備考"):
            st.write(f"**データソース:** {item['データソース']}")
            if pd.notna(item["備　　考"]):
                st.info(f"💡 備考: {item['備　　考']}")
    else:
        st.info("上の検索窓から食材を選んでください。")

st.caption("Developed by Kohei Takahashi")