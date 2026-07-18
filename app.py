import streamlit as st

st.set_page_config(
    page_title="Axis Wallet Assistant",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Axis Wallet Assistant")

st.subheader("بيانات العميل")

name = st.text_input("الاسم بالكامل")

national_id = st.text_input("الرقم القومي")

job = st.text_input("المهنة")

age = st.number_input(
    "السن",
    min_value=1,
    max_value=120,
    value=30
)

if st.button("تحليل العميل"):

    if age >= 60:
        workplace = "معاش"

    elif job == "ربة منزل":
        workplace = "شخص درجة أولى"

    elif job in ["عامل", "سائق", "فلاح"]:
        workplace = "حر"

    else:
        workplace = job

    st.success("تم تحليل البيانات")

    st.write("جهة العمل:", workplace)
