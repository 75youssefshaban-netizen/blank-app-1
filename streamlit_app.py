import streamlit as st

st.set_page_config(page_title="تطبيق تلخيص المناهج الدراسية", page_icon="📚")

st.title("📚 تطبيق تلخيص المناهج الدراسية")
st.markdown("---")

option = st.radio("اختر طريقة إدخال المنهج أو الدرس:", ("إدخال نص", "رفع صورة للمنهج"))

text_input = ""
uploaded_image = None

if option == "إدخال نص":
    text_input = st.text_area("ضع نص الدرس أو المنهج هنا للتلخيص:", placeholder="اكتب أو الصق النص هنا...")
else:
    uploaded_image = st.file_uploader("قم بتحديث أو رفع صورة الدرس أو الكتاب:", type=["png", "jpg", "jpeg"])

if st.button("✨ تلخيص الدرس"):
    if option == "إدخال نص" and text_input.strip() != "":
        st.success("جاري تلخيص النص الدراسي...")
        st.write("### الملخص:")
        st.info("هنا سيظهر ملخص الدرس بناءً على النص الذي أدخلته.")
    elif option == "رفع صورة للمنهج" and uploaded_image is not None:
        st.success("تم رفع الصورة بنجاح! جاري قراءة محتوى الصورة وتلخيصه...")
        st.image(uploaded_image, caption="الصورة المرفوعة", use_column_width=True)
        st.write("### الملخص المستخرج من الصورة:")
        st.info("هنا سيظهر الملخص المستخرج من المادة البصرية للدرس.")
    else:
        st.warning("الرجاء إدخال نص أو رفع صورة أولاً قبل الضغط على زر التلخيص

