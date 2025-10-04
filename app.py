import streamlit as st

st.set_page_config(page_title="外交シミュレーション作成ツール", page_icon="🧭", layout="centered")

st.title("外交シミュレーション作成ツール")
st.caption("まずはUIだけ動かしてみましょう（v0.1）")

st.subheader("ステップ1：シミュレーションの基本設定")

purpose = st.radio("シミュレーションの目的", ["高校・大学での教育", "企業・団体の研修", "政策決定演習"])
participants = st.number_input("参加人数（例：20）", min_value=1, max_value=200, value=20, step=1)
sim_scope = st.selectbox("シミュレーション形態", ["国内アクター", "国際アクター"])
duration = st.selectbox("実施時間（分）", [90, 180, 360], index=0)
ai_events = st.checkbox("AI目的イベント生成をONにする")

if st.button("次へ進む"):
    st.success("入力を受け取りました！")
    st.write({
        "目的": purpose,
        "参加人数": participants,
        "形態": sim_scope,
        "実施時間(分)": duration,
        "AIイベント生成": ai_events
    })
