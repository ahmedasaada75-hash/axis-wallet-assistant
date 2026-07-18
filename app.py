import streamlit as st

st.set_page_config(layout="wide")

page = st.sidebar.radio(
    "القائمة",
    [[
    "تحليل العميل",
    "إنشاء الاستمارة",
    "تعليمات Axis",
    "العملاء عالية المخاطر"
]
    ]
)


# =====================
# صفحة التحليل
# =====================
if page == "تحليل العميل":

    st.title("📋 Axis Wallet Assistant")

    name = st.text_input("الاسم")

    national_id = st.text_input("الرقم القومي")

    job = st.text_input("المهنة")

    age = st.number_input("السن", 1, 120)

    if st.button("تحليل العميل"):

        if age >= 60:
            workplace = "معاش"

        elif job == "ربة منزل":
            workplace = "شخص درجة أولى"

        elif job in ["عامل", "سائق", "فلاح"]:
            workplace = "حر"

        else:
            workplace = job

        st.success(f"جهة العمل: {workplace}")


# =====================
# صفحة إنشاء الاستمارة
# =====================
elif page == "إنشاء الاستمارة":

    from PIL import Image, ImageDraw

    st.title("📄 إنشاء الاستمارة")

    name = st.text_input("الاسم")
    national_id = st.text_input("الرقم القومي")
    job = st.text_input("المهنة")
    workplace = st.text_input("جهة العمل")
    work_address = st.text_input("عنوان العمل")
    birth_place = st.text_input("محل الميلاد")

    if st.button("إنشاء الاستمارة"):

        image = Image.open("Designer (1).png")
        draw = ImageDraw.Draw(image)

        draw.text((300, 150), name, fill="black")
        draw.text((300, 190), national_id, fill="black")
        draw.text((300, 230), job, fill="black")
        draw.text((300, 270), workplace, fill="black")
        draw.text((300, 310), work_address, fill="black")
        draw.text((300, 350), birth_place, fill="black")

        image.save("result.png")
        st.image("result.png")

        with open("result.png", "rb") as file:
            st.download_button(
                "تحميل الاستمارة",
                file,
                "axis_form.png"
            )

elif page == "تعليمات Axis":

    st.title("📚 تعليمات Axis")

    st.markdown("""
### مصدر الدخل

- كبار السن بدون وظيفة = معاش
- ربة منزل = أحد أقارب الدرجة الأولى
- طالب = أحد أقارب الدرجة الأولى
- خريج = أحد أقارب الدرجة الأولى

### الجنسية

- وجود 88 في الرقم القومي = جنسية أخرى

### محل الميلاد

- يكتب اسم المحافظة فقط
""")


# =====================
# صفحة المخاطر
# =====================
elif page == "العملاء عالية المخاطر":

    st.title("⚠ العملاء عالية المخاطر")

    st.markdown("""
- جيش
- عسكري
- ضابط
- قاضي
- محام
- رجل دين
- سياسي
- دبلوماسي
- تاجر ذهب
- ألماس
- مجوهرات
- كازينو
- قمار
- وكيل عقارات
""")
