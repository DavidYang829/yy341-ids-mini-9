import streamlit as st
from transformers import pipeline

# Load the language models for translation
translation_model_en_to_zh = pipeline("translation_en_to_zh", model="Helsinki-NLP/opus-mt-en-zh")
translation_model_zh_to_en = pipeline("translation_zh_to_en", model="Helsinki-NLP/opus-mt-zh-en")

# Define Streamlit app with enhanced aesthetics and custom styling
def main():
    # Set page title and add some styling
    st.set_page_config(
        page_title="Chinese and English translation application",
        page_icon="🌐",
        layout="wide",
        initial_sidebar_state="auto"
    )

    # Define left and right columns for input and translation
    left_column, right_column = st.columns(2)

    # Add header with image
    header_html = """
    <div style="background-color: #264653; padding: 20px; border-radius: 10px;">
        <h1 style="color: white; text-align: center; font-size: 36px;">🌐 中英文翻译应用</h1>
    </div>
    <br />
    """
    st.markdown(header_html, unsafe_allow_html=True)

    # Left column: Input Chinese text to translate to English
    with left_column:
        st.subheader("输入中文翻译成英语")
        chinese_input = st.text_area("请输入中文文本:", height=200)
        if st.button("翻译为英语", key="translate_chinese_to_english"):
            if chinese_input:
                translated_text = translation_model_zh_to_en(chinese_input)[0]['translation_text']
                st.markdown("<hr>", unsafe_allow_html=True)
                st.markdown("<h3>翻译结果:</h3>", unsafe_allow_html=True)
                st.write(translated_text)
                st.markdown("<hr>", unsafe_allow_html=True)
            else:
                st.warning("请输入一些中文文本。")

    # Right column: Input English text to translate to Chinese
    with right_column:
        st.subheader("Input English to translate into Chinese")
        english_input = st.text_area("Please enter English text:", height=200)
        if st.button("Translate intoto Chinese", key="translate_english_to_chinese"):
            if english_input:
                translated_text = translation_model_en_to_zh(english_input)[0]['translation_text']
                st.markdown("<hr>", unsafe_allow_html=True)
                st.markdown("<h3>Translate Result:</h3>", unsafe_allow_html=True)
                st.write(translated_text)
                st.markdown("<hr>", unsafe_allow_html=True)
            else:
                st.warning("Please enter some English text.")

if __name__ == "__main__":
    main()
