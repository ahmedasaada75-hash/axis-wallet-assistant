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

# =====================================
# تحليل العميل
# =====================================

if page == "تحليل العميل":

    st.title("📋 Axis Wallet Assistant")

    name = st.text_input("الاسم")

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

        elif job in ["عامل", "سائق", "فلاح", "مزارع"]:
            workplace = "حر"

        elif "بكالوريوس" in job:
            workplace = "شخص درجة أولى"

        elif "ليسانس" in job:
            workplace = "شخص درجة أولى"

        elif "طالب" in job:
            workplace = "شخص درجة أولى"

        else:
            workplace = job

        st.success(f"جهة العمل: {workplace}")

# =====================================
# إنشاء الاستمارة
# =====================================

elif page == "إنشاء الاستمارة":

    st.title("📄 إنشاء الاستمارة")

    name = st.text_input("الاسم بالكامل")

    national_id = st.text_input("الرقم القومي")

    job = st.text_input("المهنة")

    mobile = st.text_input("رقم المحمول")

    if st.button("إنشاء الاستمارة"):

        try:

            image = Image.open("Designer (1).png")

            draw = ImageDraw.Draw(image)

            draw.text((250, 150), name, fill="black")
            draw.text((250, 190), national_id, fill="black")
            draw.text((250, 230), job, fill="black")
            draw.text((250, 270), mobile, fill="black")

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

        except Exception as e:

            st.error(f"خطأ: {e}")

# =====================================
# تعليمات Axis
# =====================================

elif page == "تعليمات Axis":

    st.title("📚 تعليمات Axis")

    st.markdown("""

### مصدر الدخل

- ربة منزل = شخص درجة أولى
- طالب = شخص درجة أولى
- حاصل على مؤهل فقط = شخص درجة أولى
- أكبر من 60 سنة بدون وظيفة = معاش

### العمل الحر

- عامل = حر
- سائق = حر
- فلاح = حر
- مزارع = حر

### الجنسية

- وجود 88 في الرقم القومي = جنسية أخرى

""")

# =====================================
# العملاء عالية المخاطر
# =====================================

elif page == "العملاء عالية المخاطر":

    st.title("⚠ العملاء عالية المخاطر")

    st.markdown("""

- ضابط
- جيش
- شرطة
- قاضي
- محام
- رجل دين
- سياسي
- دبلوماسي
- تاجر ذهب
- مجوهرات
- ألماس
- كازينو
- قمار
- وكيل عقارات

""")
