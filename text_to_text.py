import streamlit as st
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Title of the app
st.title("Language Translator: English ↔ South Indian Languages")

# Input text from the user
user_input = st.text_area("Enter text:")

# Dropdown for selecting translation direction
translation_direction = st.selectbox("Select Translation Direction:", ["English to South Indian", "South Indian to English"])

# Define South Indian languages and their codes
languages = {
    'Kannada': 'kn',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Malayalam': 'ml'
}

# If translating from English to South Indian languages
if translation_direction == "English to South Indian":
    target_language = st.selectbox("Select Target Language:", list(languages.keys()))
else:
    target_language = st.selectbox("Select Source Language:", list(languages.keys()))

# Button to perform translation
if st.button("Translate"):
    if user_input:
        if translation_direction == "English to South Indian":
            # Perform translation from English to selected South Indian language
            translated_text = translator.translate(user_input, dest=languages[target_language])
            st.success(f"Translated Text in {target_language}: {translated_text.text}")
        else:
            # Perform translation from selected South Indian language to English
            source_language_code = languages[target_language]
            translated_text = translator.translate(user_input, src=source_language_code, dest='en')
            st.success(f"Translated Text in English: {translated_text.text}")
    else:
        st.error("Please enter text to translate.")

# Run the app using: streamlit run app.py
