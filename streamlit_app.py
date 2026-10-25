import streamlit as st

st.title("📚 تطبيق تلخيص المناهج الدراسية")

# مكان لكتابة أو لصق الدرس
lesson_text = st.text_area("ضع نص الدرس أو المنهج هنا للتلخيص:", height=250)

if st.button("تلخيص الدرس ✨"):
    if lesson_text:
        st.success("تم استقبال النص بنجاح!")
        st.subheader("📝 الملخص:")
        st.write(lesson_text)
    else:
        st.warning("الرجاء إدخال نص الدرس أولاً.")

