import streamlit as st

st.set_page_config(
    page_title="Axis Assistant",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Axis Wallet Assistant")

st.markdown("---")

name = st.text_input("الاسم بالكامل")

national_id = st.text_input("الرقم القومي")

birth_place = st.text_input("محل الميلاد")

qualification = st.text_input("المؤهل")

job = st.text_input("المهنة")

age = st.number_input(
    "السن",
    min_value=1,
    max_value=120,
    value=30
)

if st.button("تجهيز الاستمارة"):

    if age >= 60:
        workplace = "معاش"
        income_source = "معاش"

    elif job == "ربة منزل":
        workplace = "شخص درجة أولى"
        income_source = "أحد أقارب الدرجة الأولى"

    elif job == "طالب":
        workplace = "شخص درجة أولى"
        income_source = "أحد أقارب الدرجة الأولى"

    elif "بكالوريوس" in job:
        workplace = "شخص درجة أولى"
        income_source = "أحد أقارب الدرجة الأولى"

    elif "ليسانس" in job:
        workplace = "شخص درجة أولى"
        income_source = "أحد أقارب الدرجة الأولى"

    elif job in [
        "عامل",
        "سائق",
        "فلاح",
        "مزارع"
    ]:
        workplace = "حر"
        income_source = "حر"

    else:
        workplace = job
        income_source = job

    st.success("تم تجهيز الاستمارة")

    st.markdown("## 📄 الاستمارة النهائية")

    st.text_area(
        "",
        value=f"""
الاسم : {name}

الرقم القومي : {national_id}

محل الميلاد : {birth_place}

المؤهل : {qualification}

المهنة : {job}

جهة العمل : {workplace}

مصدر الدخل : {income_source}
""",
        height=350
    )

    st.markdown("---")

    st.write("✅ الاسم:", name)
    st.write("✅ الرقم القومي:", national_id)
    st.write("✅ محل الميلاد:", birth_place)
    st.write("✅ المؤهل:", qualification)
    st.write("✅ المهنة:", job)
    st.write("✅ جهة العمل:", workplace)
    st.write("✅ مصدر الدخل:", income_source)
