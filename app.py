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

    name = st.text_input("الاسم بالكامل")

    national_id = st.text_input("الرقم القومي")

    birth_place = st.text_input("محل الميلاد")

    qualification = st.text_input("المؤهل")

    job = st.text_input("المهنة")

    age = st.number_input(
        "السن",
        min_value=1,
        max_value=120,
        value=30,
        key="age_form"
    )

    if st.button("إنشاء الاستمارة"):

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

        st.success("تم إنشاء البيانات")

        st.write("المهنة:", job)
        st.write("جهة العمل:", workplace)
        st.write("مصدر الدخل:", income_source)

        image = Image.open("Designer (1).png")

        draw = ImageDraw.Draw(image)

        # الاسم
        draw.text((620, 155), name, fill="black")

        # الرقم القومي
        draw.text((620, 195), national_id, fill="black")

        # محل الميلاد
        draw.text((620, 350), birth_place, fill="black")

        # المؤهل
        draw.text((520, 558), qualification, fill="black")

        # المهنة
        draw.text((720, 558), job, fill="black")

        # جهة العمل
        draw.text((620, 620), workplace, fill="black")

        # مصدر الدخل
        draw.text((450, 790), income_source, fill="black")

        image.save("result.png")

        st.image(
            "result.png",
            caption="معاينة الاستمارة",
            use_container_width=True
        )

        with open("result.png", "rb") as file:

            st.download_button(
                label="تحميل الاستمارة",
                data=file,
                file_name="axis_form.png",
                mime="image/png"
            )

# ===================================
# تعليمات Axis
# ===================================

elif page == "تعليمات Axis":

    st.title("📚 تعليمات Axis")

    st.markdown("""

### ربة منزل
- جهة العمل = شخص درجة أولى
- مصدر الدخل = أحد أقارب الدرجة الأولى

### طالب
- جهة العمل = شخص درجة أولى
- مصدر الدخل = أحد أقارب الدرجة الأولى

### عامل
- جهة العمل = حر
- مصدر الدخل = حر

### سائق
- جهة العمل = حر
- مصدر الدخل = حر

### فلاح
- جهة العمل = حر
- مصدر الدخل = حر

### أكبر من 60 سنة
- جهة العمل = معاش
- مصدر الدخل = معاش

""")

# ===================================
# العملاء عالية المخاطر
# ===================================

elif page == "العملاء عالية المخاطر":

    st.title("⚠ العملاء عالية المخاطر")

    st.markdown("""

- ضابط
- جيش
- شرطة
- سياسي
- دبلوماسي
- قاضي
- محام
- رجل دين
- تاجر ذهب
- ألماس
- مجوهرات
- كازينو
- قمار
- وكيل عقارات

""")
