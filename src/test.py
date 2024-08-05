import gradio as gr
import requests
from PIL import Image

BASE_URL = "https://vjaygdzonbzf.share.zrok.io"  # Replace with your actual base URL

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

# Fetch a specific word's data from the API
def get_initial_data():
    response = requests.get(f"{BASE_URL}/word/tổ chức")  # Replace with your desired word
    if response.status_code == 200:
        data = response.json()
        word_data = data.get("word", "")
        voice_data = data.get("voice", "")
        status_data = data.get("status", 0)
        parts_of_speech = {k: v for k, v in data.items() if k not in ["_id", "word", "voice", "status"]}
        return word_data, voice_data, status_data, parts_of_speech
    return "", "", 0, {}

# Save the updated data back to the API
def save_data(word, voice, status, **kwargs):
    try:
        response = requests.get(f"{BASE_URL}/word/{word}")
        if response.status_code == 200:
            data = response.json()
            word_id = data['_id']
            update_data = {
                "word": word,
                "voice": voice,
                "status": int(status)
            }
            update_data.update(kwargs)
            response = requests.put(f"{BASE_URL}/{word_id}", json=update_data)
        else:
            update_data = {
                "word": word,
                "voice": voice,
                "status": int(status)
            }
            update_data.update(kwargs)
            response = requests.post(f"{BASE_URL}", json=update_data)
        return "Success" if response.status_code in [200, 201] else f"Failed: {response.status_code}"
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
    
    # Save the data to the API
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
