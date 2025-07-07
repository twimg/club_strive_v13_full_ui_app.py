import streamlit as st
import pandas as pd

# 仮データ読み込み
df = pd.read_csv("transfer_offers.csv")

st.title("💸 移籍交渉センター")

for i, row in df.iterrows():
    st.subheader(f"選手: {row['選手名']}（{row['ポジション']}）")
    st.write(f"移籍先: {row['移籍先クラブ']}")
    st.write(f"提示額: 💰 {row['移籍金']} / 年俸: {row['年俸']} / 契約年数: {row['契約年数']}年")
    st.write(f"選手希望: {row['選手希望度']}｜クラブ意向: {row['クラブ意向']}｜状態: {row['交渉ステータス']}")

    if row['交渉ステータス'] == '交渉中':
        col1, col2, col3 = st.columns(3)
        if col1.button(f"承諾 - {row['選手名']}", key=f"a{i}"):
            df.at[i, '交渉ステータス'] = '承諾済'
        if col2.button(f"拒否 - {row['選手名']}", key=f"r{i}"):
            df.at[i, '交渉ステータス'] = '拒否済'
        if col3.button(f"再交渉 - {row['選手名']}", key=f"re{i}"):
            df.at[i, '交渉ステータス'] = '再交渉提案中'

st.write("📝 交渉状況")
st.dataframe(df)
