import streamlit as st

st.set_page_config(
    page_title="Axis Wallet Assistant",
    page_icon="📋",
    layout="centered"
)

st.title("📋 Axis Wallet Assistant")

name = st.text_input("الاسم بالكامل")

national_id = st.text_input("الرقم القومي")

birth_place = st.text_input("محل الميلاد")

job = st.text_input("المهنة")

company_name = st.text_input(
    "جهة العمل (اتركها فارغة إذا غير موجودة)"
)

age = st.number_input(
    "السن",
    min_value=1,
    max_value=120,
    value=30
)

if st.button("تجهيز الاستمارة"):

    final_job = job

    # بالمعاش
    if age >= 60 and "بالمعاش" in job:

        final_job = job.replace("بالمعاش", "").strip()

        workplace = "معاش"
        income_source = "معاش"

    # ربة منزل
    elif job == "ربة منزل":

        workplace = "شخص درجة أولى"
        income_source = "أحد أقارب الدرجة الأولى"

    # حاصل على مؤهل فقط
    elif (
        "بكالوريوس" in job
        or "ليسانس" in job
        or "دبلوم" in job
        or "حاصل على مؤهل" in job
    ):

        workplace = "شخص درجة أولى"
        income_source = "أحد أقارب الدرجة الأولى"

    # الأعمال الحرة
    elif job in [
        "عامل",
        "عامل زراعي",
        "فلاح",
        "مزارع",
        "نجار",
        "سباك",
        "حداد",
        "سائق"
    ]:

        workplace = "عمل حر"
        income_source = "عمل حر"

    # فوق 60 ومفيش جهة عمل
    elif age >= 60 and company_name.strip() == "":

        workplace = "عمل حر"
        income_source = "عمل حر"

    # وظيفة ومعها جهة عمل
    elif company_name.strip() != "":

        workplace = company_name
        income_source = company_name

    else:

        workplace = "عمل حر"
        income_source = "عمل حر"

    st.success("✅ تم تجهيز البيانات")

    st.text_area(
        "الاستمارة النهائية",
        value=f"""
الاسم: {name}

الرقم القومي: {national_id}

محل الميلاد: {birth_place}

المهنة: {final_job}

جهة العمل: {workplace}

مصدر الدخل: {income_source}
""",
        height=300
    )
