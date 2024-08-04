import gradio as gr
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient("mongodb://127.0.0.1:9191")  # User's MongoDB URI
db = client["Datasys"]
collection = db["dictionary"]

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

# Fetch all words from the database
def get_all_words():
    return [doc['word'] for doc in collection.find({}, {"word": 1})]

# Retrieve initial data from MongoDB for a specific word
def get_initial_data(word):
    data = collection.find_one({"word": word})  # Find the document by word
    if data:
        word_data = data.get("word", "")
        voice_data = data.get("voice", "")
        status_data = data.get("status", 0)
        parts_of_speech = {k: v for k, v in data.items() if k not in ["_id", "word", "voice", "status"]}
        return word_data, voice_data, status_data, parts_of_speech
    return "", "", 0, {}

# Save the updated data back to MongoDB
def save_data(word, voice, status, **kwargs):
    try:
        update_data = {
            "word": word,
            "voice": voice,
            "status": int(status)
        }
        update_data.update(kwargs)
        
        collection.update_one(
            {"word": word},
            {"$set": update_data},
            upsert=True
        )
        return "Success"
    except Exception as e:
        return f"Failed: {str(e)}"

# Define the interface callback function
def update_interface(selected_word):
    word_data, voice_data, status_data, parts_of_speech = get_initial_data(selected_word)
    
    # Update input components
    inputs = [
        gr.Textbox(label='Từ', value=word_data),
        gr.Textbox(label='Phát Âm', value=voice_data),
        gr.Textbox(label='Trạng thái', value=str(status_data))
    ]

    parts_of_speech_inputs = []
    for pos, fields in parts_of_speech.items():
        label = label_mapping.get(pos, pos)
        for field, value in fields.items():
            field_label = label_mapping.get(field, field)
            if field != "img":
                parts_of_speech_inputs.append(gr.Textbox(label=f"{label} - {field_label}", value=value))
            else:
                parts_of_speech_inputs.append(gr.Image(label=f"{label} - {field_label}", value=value))

    return inputs + parts_of_speech_inputs

# Define the interface
def process_vocabulary(word, voice, status, *args):
    pos_data = {}
    i = 0
    for pos, fields in parts_of_speech.items(): # type: ignore
        pos_fields = {}
        for field in fields.keys():
            pos_fields[field] = args[i]
            i += 1
        pos_data[pos] = pos_fields
    
    # Save the data to MongoDB
    status = save_data(word, voice, status, **pos_data)
    return status

# Create the Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Kiểm Tra Từ Vựng")
    
    all_words = get_all_words()
    initial_word = all_words[0] if all_words else ""
    
    word_dropdown = gr.Dropdown(label="Chọn từ", choices=all_words, value=initial_word)
    
    initial_word_data = get_initial_data(initial_word)
    dynamic_components = update_interface(initial_word)
    
    submit_btn = gr.Button("Submit")

    # Display dynamic components
    inputs = []
    for inp in dynamic_components:
        inputs.append(inp)
    
    status_output = gr.Textbox(label='Trạng thái')

    # Update dynamic components on word selection
    def on_word_change(selected_word):
        new_components = update_interface(selected_word)
        return new_components

    word_dropdown.change(on_word_change, inputs=[word_dropdown], outputs=inputs)

    # Submit button functionality
    submit_btn.click(
        fn=process_vocabulary,
        inputs=[word_dropdown] + inputs,
        outputs=[status_output]
    )

demo.launch()
