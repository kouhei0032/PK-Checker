import streamlit as st
import pandas as pd

# --- 設定 ---
# スプレッドシートのURL
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
    <span class="no-wrap-title">🔍 食品検索</span>
    """, unsafe_allow_html=True)

st.write("食品名を検索するとリンとカリウムの含有量を表示します。")

if df is not None:
    # 検索機能：食品表示名のリストを作成
    food_options = df["食品表示名"].dropna().unique().tolist()

    # 1. まずは自由入力の検索窓（これでキーボードを強制的に出す）
    # search_term = st.text_input("🔍 キーワードで絞り込み", placeholder="例: 麦")

    # 2. 入力された文字でリストをフィルタリング
    # if search_term:
    #     filtered_options = [opt for opt in food_options if search_term in opt]
    # else:
    #     filtered_options = food_options

    # 3. 絞り込まれたリストから選択
    selected_name = st.selectbox(
        "食品名を選択",
        food_options,
        index=None,
        placeholder="候補から選んでください"
    )

    if selected_name:
        # 選択された食材の行を抽出
        item = df[df["食品表示名"] == selected_name].iloc[0]

        st.divider()

        # 重量の入力
        weight = st.number_input("食べる量 (g)", min_value=1, value=100, step=10)

        # 1. まず「100gあたりの基本値」を取得（判定用）
        # 数値以外のデータ（Trなど）が含まれる可能性があるため float に変換
        raw_k = pd.to_numeric(item["カリウム：K"], errors='coerce')
        raw_p = pd.to_numeric(item["リン：P"], errors='coerce')
        raw_s = pd.to_numeric(item["塩分"], errors='coerce')

        # 2. 「実際に食べる量」に合わせて計算（表示用）
        k_display = raw_k * weight / 100
        p_display = raw_p * weight / 100
        s_display = raw_s * weight / 100

        # 3. 色の判定は「100gあたりの基本値（raw_...）」で行う！
        # しきい値も100gあたりの基準に合わせます
        k_color = get_status_color(raw_k, low_threshold=150, high_threshold=301)
        p_color = get_status_color(raw_p, low_threshold=100, high_threshold=151)
        s_color = get_status_color(raw_s, low_threshold=0.1, high_threshold=1.1)

        # 4. 表示
        st.subheader(f"📊 {selected_name} ({weight}g) の推定値")

        st.markdown("<br>", unsafe_allow_html=True)

        # --- アドバイス表示の修正版（優先順位順） ---
        # 1. どちらか一方でも「赤（高い）」がある場合を最優先でチェック
        if k_color == "#FF4B4B" or p_color == "#FF4B4B":
            st.warning(
                "⚠️ カリウムまたはリンが高めです。料理に利用する際は、分量を調整するか「茹でこぼし」などの調理法を工夫してください。")

        # 2. 両方とも「青（低い）」場合（最高評価）
        elif k_color == "#007BFF" and p_color == "#007BFF":
            st.success("✅ リン・カリウム共に控えめで、料理に利用するのにオススメの食材です！")

        # 3. 「赤」がなく、かつどちらか一方でも「青（低い）」がある場合
        # （2番を通過しているので、ここでは「片方だけが青」の状態が判定されます）
        elif k_color == "#007BFF" or p_color == "#007BFF":
            st.success("✅ リン・カリウムの少なくとも一方が控えめです。料理に利用するのにオススメの食材です！")

        # 4. それ以外（両方とも「黒（標準）」の場合）
        else:
            st.info("💡 標準的な含有量です。他の食材とのバランスを考えて活用しましょう。")

        # --------------------------------------------

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            # 表示するのは計算後の値(k_display)、色は基本値ベース(k_color)
            display_custom_metric("リン", f"{p_display:.0f}", "mg", p_color)

        with col2:
            display_custom_metric("カリウム", f"{k_display:.0f}", "mg", k_color)

        with col3:
            display_custom_metric("塩分", f"{s_display:.1f}", "g", s_color)

        st.markdown("<br>", unsafe_allow_html=True)

        # 備考や詳細情報
        with st.expander("詳細データ・備考", expanded=True):
            st.write(f"**データソース:** {item['データソース']}")
            st.write(f"**食品詳細名:** {item['食品詳細名']}")
            if pd.notna(item["備考"]):
                st.info(f"💡 備考: {item['備考']}")
    else:
        st.info("食材を選択すると日本食品標準成分表（八訂）に基づいたデータが表示されます。")


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