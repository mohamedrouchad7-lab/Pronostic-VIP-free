import streamlit as st
import pandas as pd
from scipy.stats import poisson

st.title("⚽ تطبيق التوقعات Pronostic VIP")

st.write("مرحباً بك! هاد التطبيق غيساعدك تحسب توقعات الماتشات.")

home_exp = st.number_input("متوسط أهداف الفريق المستضيف", value=1.5)
away_exp = st.number_input("متوسط أهداف الفريق الضيف", value=1.0)

if st.button('حساب الاحتمالات'):
    prob_home = 0
    prob_draw = 0
    prob_away = 0
    for i in range(10):
        for j in range(10):
            p = poisson.pmf(i, home_exp) * poisson.pmf(j, away_exp)
            if i > j: prob_home += p
            elif i == j: prob_draw += p
            else: prob_away += p
    
    st.success(f"فوز الأرض: {prob_home:.1%}")
    st.info(f"تعادل: {prob_draw:.1%}")
    st.warning(f"فوز الضيف: {prob_away:.1%}")
          
