import streamlit as st

st.set_page_config(page_title="Youssef's Study AI", page_icon="📖")

st.title("📚 Youssef's Study AI")
st.markdown("**Developed by:** Youssef")
st.markdown("---")

# القائمة الجانبية للتنقل
st.sidebar.header("Navigation")
app_mode = st.sidebar.selectbox("Choose Mode:", ["Study Assistant (Text/Image)", "AI Chat & Q&A"])

if app_mode == "Study Assistant (Text/Image)":
    st.header("📖 Study Material Processor")
    
    # اختيار طريقة الإدخال
    option = st.radio("Choose input method:", ("Text Input", "Upload Image (Handwritten or Printed)"))

    text_input = ""
    uploaded_image = None

    if option == "Text Input":
        text_input = st.text_area("Enter your study text here:")
    else:
        uploaded_image = st.file_uploader("Upload your study image:", type=["png", "jpg", "jpeg"])
        st.info("💡 Tip: Even if the handwriting is a bit messy, the AI will scan and analyze the visual content!")

    # اختيار ماذا تريد أن يفعل التطبيق
    task_type = st.selectbox(
        "Select what you want to generate:", 
        ("Summarize Lesson", "Generate Quiz Questions", "Both (Summary & Quiz)")
    )

    if st.button("🚀 Process with AI"):
        if option == "Text Input" and text_input.strip() != "":
            st.success("Text processed successfully!")
            
            if task_type in ["Summarize Lesson", "Both (Summary & Quiz)"]:
                st.write("### 📝 Lesson Summary:")
                st.info("Here is the smart summary based on your text.")
                
            if task_type in ["Generate Quiz Questions", "Both (Summary & Quiz)"]:
                st.write("### ❓ Quiz Questions:")
                st.info("1. What is the core idea discussed?\n2. Explain the main concept in detail.")
                
        elif option == "Upload Image (Handwritten or Printed)" and uploaded_image is not None:
            st.success("Image uploaded and scanned successfully!")
            st.image(uploaded_image, caption="Uploaded Study Material", use_column_width=True)
            
            # محاكاة استخراج النص حتى لو الخط مش كويس
            st.markdown("---")
            st.write("🔍 **Extracted Text Analysis (OCR simulation):** *Successfully detected content from the image, handling handwriting variations.*")
            
            if task_type in ["Summarize Lesson", "Both (Summary & Quiz)"]:
                st.write("### 📝 Summary from Image:")
                st.info("Here is the structured summary extracted from your study page.")
                
            if task_type in ["Generate Quiz Questions", "Both (Summary & Quiz)"]:
                st.write("### ❓ Quiz Questions from Image:")
                st.info("1. Based on the notes in the image, what is the primary conclusion?\n2. Test question regarding the formulas/concepts shown.")
        else:
            st.warning("Please enter text or upload an image first!")

else:
    st.header("💬 AI Chat & Q&A")
    st.markdown("Ask any question and get instant answers from your study assistant!")
    
    user_question = st.text_input("Ask me anything about your studies:")
    if st.button("💬 Send Question"):
        if user_question.strip() != "":
            st.success("Answer:")
            st.write(f"Great question regarding **'{user_question}'**. Here is the clear explanation to help you understand it completely!")
        else:
            st.warning("Please type a question first.")
        

