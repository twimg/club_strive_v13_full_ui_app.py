import streamlit as st
import pandas as pd
import random
import datetime

# データの初期化
teams = ['ストライバーFC', 'レグルスSC', 'アルマーレFC', 'ブラッドフォールズ', 'シルフィード東京', 'バルデナールFC']

# 試合シミュレーション関数
def simulate_match(home, away):
    home_score = random.randint(0, 3)
    away_score = random.randint(0, 3)
    home_pos = random.randint(45, 60)
    away_pos = 100 - home_pos
    home_shots = random.randint(5, 12)
    away_shots = random.randint(5, 12)
    return {
        'match_id': random.randint(1000, 9999),
        'date': datetime.date.today(),
        'home_team': home,
        'away_team': away,
        'home_score': home_score,
        'away_score': away_score,
        'home_possession': home_pos,
        'away_possession': away_pos,
        'home_shots': home_shots,
        'away_shots': away_shots
    }

# UI
st.title("⚽ 即時試合シミュレーター")

home = st.selectbox("ホームチーム", teams)
away = st.selectbox("アウェイチーム", [team for team in teams if team != home])

if st.button("試合を開始！"):
    result = simulate_match(home, away)
    st.success(f"試合終了: {result['home_team']} {result['home_score']} - {result['away_score']} {result['away_team']}")
    st.write(f"📅 日付: {result['date']}")
    st.write(f"🔢 ポゼッション: {result['home_team']} {result['home_possession']}% / {result['away_team']} {result['away_possession']}%")
    st.write(f"🎯 シュート数: {result['home_team']} {result['home_shots']}本 / {result['away_team']} {result['away_shots']}本")
    
    # 表として表示
    df = pd.DataFrame([result])
    st.dataframe(df)
