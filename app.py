
# Club Strive - v13 Demo (Full UI)
import streamlit as st
import pandas as pd

# サンプルデータ（実際はCSVから読み込み）
players = pd.DataFrame([
    [1, "木村 隼人", "DF", 27, "日本", 66, 78, "リーダー", "タックルマスター", "ストライバーFC"],
    [2, "白石 翼", "MF", 23, "日本", 70, 85, "頭脳派", "チャンスクリエイター", "ストライバーFC"],
    [3, "鈴木 圭", "FW", 19, "日本", 61, 92, "早熟型", "トリックスター", "ストライバーFC"]
], columns=["id", "名前", "ポジション", "年齢", "国籍", "能力", "潜在能力", "性格", "プレースタイル", "所属クラブ"])

# ページ構成
st.set_page_config(page_title="Club Strive", layout="wide")
st.title("⚽ Club Strive - v13 Demo")

# サイドバーでメニュー選択
menu = st.sidebar.selectbox("メニューを選んでください", ["ホーム", "選手一覧", "試合", "スカウト", "財務", "ユース"])

# ホーム
if menu == "ホーム":
    st.header("ホーム")
    st.image("https://i.imgur.com/uwQFqBN.png", caption="スタジアム")  # 任意の画像リンクに変更

# 選手一覧
elif menu == "選手一覧":
    st.header("選手一覧")
    st.dataframe(players)

# 試合
elif menu == "試合":
    st.header("試合進行")
    st.write("本日の対戦：ストライバーFC vs レイジングFC")
    st.success("試合中...（簡易シミュレーション）")

# スカウト
elif menu == "スカウト":
    st.header("スカウト")
    st.image("https://i.imgur.com/hQgYF9H.png", caption="スカウト中の選手")
    st.write("名前: 川島 大一")
    st.write("年齢: 17")
    st.write("評価: ★★★★☆")

# 財務
elif menu == "財務":
    st.header("財務情報")
    st.metric("現在の予算", "4億50万")
    st.metric("スポンサー収入", "+350万")

# ユース
elif menu == "ユース":
    st.header("ユースチーム")
    st.write("若手選手を育成中...")
    st.info("ユース方針：バランス型")

# フッター
st.markdown("---")
st.caption("© 2025 Club Strive Project")
