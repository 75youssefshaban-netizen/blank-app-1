import streamlit as st

st.set_page_config(page_title="Study App", page_icon="📖")

st.title("📚 Study Summarizer App")
st.markdown("**Developed by:** Youssef")
st.markdown("---")

option = st.radio("Choose input method:", ("Text Input", "Upload Image"))

text_input = ""
uploaded_image = None

if option == "Text Input":
    text_input = st.text_area("Enter your study text here:")
else:
    uploaded_image = st.file_uploader("Upload your study image here:", type=["png", "jpg", "jpeg"])

if st.button("✨ Summarize Lesson"):
    if option == "Text Input" and text_input.strip() != "":
        st.success("Processing text successfully!")
        st.write("### Summary:")
        st.info("Here is the generated summary based on your text.")
    elif option == "Upload Image" and uploaded_image is not None:
        st.success("Image uploaded successfully! Processing...")
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        st.write("### Summary from Image:")
        st.info("Here is the extracted summary from the visual material.")
    else:
        st.warning("Please enter text or upload an image first!")
        

