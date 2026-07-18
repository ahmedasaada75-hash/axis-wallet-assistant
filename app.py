import streamlit as st

st.set_page_config(
    page_title="Axis Wallet Assistant",
    page_icon="📋",
    layout="centered"
)

st.title("📋 Axis Wallet Assistant")

st.write("أدخل بيانات العميل")

name = st.text_input("الاسم بالكامل")

national_id = st.text_input("الرقم القومي")

birth_place = st.text_input("محل الميلاد")

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

    st.success("تم تجهيز البيانات")

    st.markdown("## الاستمارة")

    st.text_area(
        "الناتج",
        value=f"""
الاسم: {name}

الرقم القومي: {national_id}

محل الميلاد: {birth_place}

المهنة: {job}

جهة العمل: {workplace}

مصدر الدخل: {income_source}
""",
        height=250
    )

    st.markdown("### ملخص")

    st.write("الاسم:", name)
    st.write("الرقم القومي:", national_id)
    st.write("محل الميلاد:", birth_place)
    st.write("المهنة:", job)
    st.write("جهة العمل:", workplace)
    st.write("مصدر الدخل:", income_source)
