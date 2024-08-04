import gradio as gr
from pymongo import MongoClient
from PIL import Image
# MongoDB connection setup
client = MongoClient("mongodb://127.0.0.1:9191")  # Update with your MongoDB URI
db = client["Datasys"]  # Use the correct case for your existing database
collection = db["dictionary"]  # Use the correct collection name

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

# Retrieve initial data from MongoDB
def get_initial_data(word):
    data = collection.find_one({"word": word})  # Replace with your query
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

# Load initial data for the interface
word_data, voice_data, status_data, parts_of_speech = get_initial_data()

# Create input components dynamically
inputs = [
    gr.Textbox(label='Từ', value=word_data),
    gr.Textbox(label='Phát Âm', value=voice_data),
    gr.Textbox(label='Trạng thái', value=str(status_data))
]

parts_of_speech_inputs = {}
for pos, fields in parts_of_speech.items():
    pos_inputs = []
    label = label_mapping.get(pos, pos)  # Use mapping for label if available
    for field, value in fields.items():
        field_label = label_mapping.get(field, field)
        if field_label != "Hình ảnh":
            pos_inputs.append(gr.Textbox(label=f"{label} - {field_label}", value=value))
        else:
            pos_inputs.append(gr.Image(label=f"{label} - {field_label}"))
    parts_of_speech_inputs[pos] = pos_inputs

outputs = [gr.Textbox(label='Trạng thái')]

# Define the interface
def process_vocabulary(word, voice, status, *args):
    pos_data = {}
    i = 0
    for pos, fields in parts_of_speech.items():
        pos_fields = {}
        for field in fields.keys():
            pos_fields[field] = args[i]
            i += 1
        pos_data[pos] = pos_fields
    
    # Save the data to MongoDB
    status = save_data(word, voice, status, **pos_data)
    return status

# Create the Gradio interface with Tabs
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Kiểm Tra Từ Vựng")
    
    with gr.Row():
        inputs[0].render()
        inputs[1].render()
        inputs[2].render()
    
    with gr.Tabs():
        for pos, pos_inputs in parts_of_speech_inputs.items():
            with gr.TabItem(label_mapping.get(pos, pos)):
                for inp in pos_inputs:
                    inp.render()
                
    submit_btn = gr.Button("Submit")
    submit_btn.click(
        fn=process_vocabulary,
        inputs=inputs + [inp for sublist in parts_of_speech_inputs.values() for inp in sublist],
        outputs=outputs
    )

demo.launch()
