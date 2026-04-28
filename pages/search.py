import streamlit as st
import pandas as pd

# --- 設定 ---
# ご自身のスプレッドシートのURLをここに貼り付けてください
SHEET_URL = "https://docs.google.com/spreadsheets/d/1q5ACTKmnTL_2xkETX7rXajX7AG3d6I3n-DSj4QSx56Q/export?format=csv"

# --- 関数 ---
# 1. 状態に応じた色を判定する関数
def get_status_color(value, low_threshold=None, high_threshold=None):
    """
    値に応じて色（CSSカラーコード）を返す
    - low_threshold 以下なら青
    - high_threshold 以上なら赤
    - それ以外はデフォルト色
    """
    if low_threshold is not None and value <= low_threshold:
        return "#007BFF"  # 青色
    if high_threshold is not None and value >= high_threshold:
        return "#FF4B4B"  # 赤色
    return "#31333F"      # 標準の黒に近いグレー

# 2. カスタム表示用関数
def display_custom_metric(label, value, unit, color):
    """HTMLを使用して色付きのメトリックを表示"""
    st.markdown(
        f"""
        <div style="font-size: 14px; color: #61636A; margin-bottom: 4px;">{label}</div>
        <div style="font-size: 24px; font-weight: 600; color: {color};">
            {value} <span style="font-size: 16px;">{unit}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

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
    <span class="no-wrap-title">🔍 リンカ検索</span>
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

        st.subheader(f"📊 {selected_name} ({weight}g) の推定値")
        col1, col2, col3 = st.columns(3)

        # 各項目の判定（例: カリウムは2000以上なら赤、リンは50以下なら青/200以上なら赤）
        k_color = get_status_color(k_val, low_threshold=50, high_threshold=200)
        p_color = get_status_color(p_val, low_threshold=50, high_threshold=200)
        s_color = get_status_color(s_val, low_threshold=50, high_threshold=200)

        with col1:
            display_custom_metric("カリウム", f"{k_val:.0f}", "mg", k_color)

        with col2:
            display_custom_metric("リン", f"{p_val:.0f}", "mg", p_color)

        with col3:
            display_custom_metric("塩分", f"{s_val:.1f}", "g", s_color)

        st.markdown("<br>", unsafe_allow_html=True)

        # 備考や詳細情報
        with st.expander("詳細データ・備考"):
            st.write(f"**データソース:** {item['データソース']}")
            if pd.notna(item["備　　考"]):
                st.info(f"💡 備考: {item['備　　考']}")
    else:
        st.info("上の検索窓から食材を選んでください。")

st.caption("Developed by Kouhei Takahashi")