import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(
    page_title="Axis Wallet Assistant",
    page_icon="📋",
    layout="wide"
)

page = st.sidebar.radio(
    "القائمة",
    [
        "تحليل العميل",
        "إنشاء الاستمارة",
        "تعليمات Axis",
        "العملاء عالية المخاطر"
    ]
)

# ===================================
# تحليل العميل
# ===================================

if page == "تحليل العميل":

    st.title("📋 تحليل العميل")

    job = st.text_input("المهنة")

    age = st.number_input(
        "السن",
        min_value=1,
        max_value=120,
        value=30
    )

    if st.button("تحليل"):

        if age >= 60:
            workplace = "معاش"
            income_source = "معاش"

        elif job == "ربة منزل":
            workplace = "شخص درجة أولى"
            income_source = "أحد أقارب الدرجة الأولى"

        elif job in ["عامل", "سائق", "فلاح", "مزارع"]:
            workplace = "حر"
            income_source = "حر"

        else:
            workplace = job
            income_source = job

        st.success(f"جهة العمل: {workplace}")
        st.success(f"مصدر الدخل: {income_source}")


# ===================================
# إنشاء الاستمارة
# ===================================

elif page == "إنشاء الاستمارة":

    st.title("📄 إنشاء الاستمارة")

    
