import streamlit as st
import pandas as pd

# サンプル選手データ（簡略化）
players_data = [
    {"名前": "白石 翼", "ポジション": "MF", "年齢": 25, "国籍": "日本", "能力": 68, "所属クラブ": "ストライバーFC"},
    {"名前": "佐々木 海斗", "ポジション": "FW", "年齢": 22, "国籍": "日本", "能力": 72, "所属クラブ": "ストライバーFC"},
    {"名前": "高橋 悠斗", "ポジション": "FW", "年齢": 30, "国籍": "フランス", "能力": 75, "所属クラブ": "ストライバーFC"},
]

players_df = pd.DataFrame(players_data)

st.title("💰 移籍オファー画面")

# 選手選択
selected_player = st.selectbox("📋 移籍させたい選手を選んでください", players_df["名前"])

player_info = players_df[players_df["名前"] == selected_player].iloc[0]
st.write("### 🎯 選手情報")
st.write(f"**ポジション**：{player_info['ポジション']}")
st.write(f"**能力値**：{player_info['能力']}")
st.write(f"**現在クラブ**：{player_info['所属クラブ']}")

# オファー設定
st.write("---")
st.write("### 📝 オファー内容の入力")

new_club = st.text_input("移籍先クラブ名", "ソレイユFC")
offer_fee = st.slider("移籍金（万）", min_value=100, max_value=10000, value=2000, step=100)
contract_years = st.slider("契約年数", 1, 5, 3)

if st.button("🚀 オファーを送信"):
    st.success(f"✅ {selected_player} に対し {new_club} からのオファー（{offer_fee}万円 / {contract_years}年契約）を送信しました。")
