import streamlit as st
import requests
import numpy as np
import cv2

BASE_URL = "https://vjaygdzonbzf.share.zrok.io"

# Mapping from database keys to desired labels
label_mapping = {
    "noun": "Danh từ",
    "verb": "Động từ",
    "adj": "Tính từ",
    "desc": "Mô tả",
    "example": "Ví dụ",
    "synonym": "Từ đồng nghĩa",
    "antonym": "Từ trái nghĩa",
    "img": "Hình ảnh"
}

# Fetch all words from the database via API
def get_all_words():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return [doc['word'] for doc in response.json()]
    return []

# Retrieve initial data from API for a specific word by word name
def get_initial_data(word):
    response = requests.get(f"{BASE_URL}/word/{word}")
    if response.status_code == 200:
        data = response.json()
        word_id = data.get("_id")
        word_data = data.get("word", "")
        voice_data = data.get("voice", "")
        status_data = data.get("status", 0)
        parts_of_speech = {k: v for k, v in data.items() if k not in [
            "_id", "word", "voice", "status"]}
        return word_id, word_data, voice_data, status_data, parts_of_speech
    return None, "", "", 0, {}

# Save the updated data back to API (update or create)
def save_data(word_id, word, voice, status, **kwargs):
    try:
        update_data = {
            "word": word,
            "voice": voice,
            "status": int(status)
        }
        update_data.update(kwargs)

        if word_id:  # Update if ID is available
            response = requests.put(f"{BASE_URL}/{word_id}", json=update_data)
        else:  # Create a new word if no ID is available
            response = requests.post(BASE_URL, json=update_data)

        return "Success" if response.status_code in [200, 201] else f"Failed: {response.status_code}"
    except Exception as e:
        return f"Failed: {str(e)}"

# Initialize session state for selected word
if "selected_word" not in st.session_state:
    st.session_state["selected_word"] = None

if "word_id" not in st.session_state:
    st.session_state["word_id"] = None

# Update the interface based on selected word
def update_interface(selected_word):
    if st.session_state["selected_word"] != selected_word:
        st.session_state["selected_word"] = selected_word
        word_id, word_data, voice_data, status_data, parts_of_speech = get_initial_data(selected_word)
        
        # Store the word_id in session state
        st.session_state["word_id"] = word_id

        col1, col2, col3 = st.columns(3)
        with col1:
            st.text_input('Từ', value=word_data, key="word_input")
        with col2:
            st.text_input('Phát Âm', value=voice_data, key="voice_input")
        with col3:
            st.text_input('Trạng thái', value=str(status_data), key="status_input")

        if isinstance(parts_of_speech, dict):
            tabs = st.tabs([label_mapping.get(pos, pos) for pos in parts_of_speech.keys()])

            for i, (pos, fields) in enumerate(parts_of_speech.items()):
                if isinstance(fields, dict):  # Check that fields is a dictionary
                    with tabs[i]:
                        col1, col2 = st.columns(2)
                        for field, value in fields.items():
                            field_label = label_mapping.get(field, field)
                            unique_key = f"{pos}_{field}_input"
                            if field != "img":
                                col1.text_input(f"{field_label}", value=value, key=unique_key)
                            else:
                                # col2.file_uploader(f"{field_label}", type=["png", "jpg"])
                                col2.image('data/example/walk.jpg')
                else:
                    st.error(f"Unexpected data format for {pos}: {fields}")
        else:
            st.error("Unexpected parts_of_speech format")

# Process vocabulary data and save it
def process_vocabulary():
    # Retrieve word_id from session state
    word_id = st.session_state.get("word_id")

    # Collect input data
    inputs = {
        "word": st.session_state["word_input"],
        "voice": st.session_state["voice_input"],
        "status": st.session_state["status_input"]
    }

    # Collect parts of speech data
    parts_of_speech_inputs = {}
    for pos in label_mapping.keys():
        pos_fields = {}
        for field in ["desc", "example", "synonym", "antonym", "img"]:
            unique_key = f"{pos}_{field}_input"
            if unique_key in st.session_state:
                pos_fields[field] = st.session_state[unique_key]
        if pos_fields:
            parts_of_speech_inputs[pos] = pos_fields

    # Save the data to the API
    status_message = save_data(word_id, **inputs, **parts_of_speech_inputs)
    return status_message

# Streamlit interface
st.title("Kiểm Tra Từ Vựng")

all_words = get_all_words()
selected_word = st.selectbox("Chọn từ", options=all_words)
if selected_word:
    update_interface(selected_word)

    if st.button("Submit"):
        status_message = process_vocabulary()
        st.success(status_message)