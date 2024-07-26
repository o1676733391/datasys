import gradio as gr
from PIL import Image

# Load the initial image
initial_image_path = "walk.jpg"
initial_image = Image.open(initial_image_path)

# Load the initial audio
initial_audio_path = "run-11239.mp3"

# Function to check and correct word descriptions, types, images, and audio


def correct_word(word, word_type, synonym, antonym, description, image, audio):
    corrected_word = word.title()  # Capitalize the word
    corrected_type = word_type.lower()  # Ensure type is in lowercase
    corrected_description = description.strip()  # Remove leading/trailing spaces

    # Assuming the image correction involves some validation, this is just a placeholder
    if isinstance(image, Image.Image):
        corrected_image = image.resize(
            (1024, 1024))  # Resize image to 1024x1024
    else:
        corrected_image = None  # Handle invalid images

    corrected_audio = audio  # Just passing through the audio

    return corrected_word, corrected_type, synonym, antonym, corrected_description, corrected_image, corrected_audio


# Define the Gradio Blocks interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Checking & Correcting Words with Image Resize")
    gr.Markdown("This is a simple web for checking and correcting word descriptions and types. Images will be resized to 1024x1024 pixels.")

    with gr.Column():
            gr.Markdown('')
            word = gr.Textbox(label='Word', value='đi', interactive=False)
            word_type = gr.Textbox(
                label='Type', value='động từ', interactive=False)
            synonym = gr.Textbox(
                label='Synonym', value='123,34,12,121431241,12312312,4', interactive=False)
            antonym = gr.Textbox(label='Antonym', value='', interactive=False)
            description = gr.Textbox(
                label='Description', value='(người, động vật) tự di chuyển từ chỗ này đến chỗ khác bằng những bước chân nhấc lên, đặt xuống liên tiếp', interactive=False)

            audio = gr.Audio(
                label='Audio', value=initial_audio_path, type='filepath', interactive=False)
            # with gr.Row():
            #     image = gr.Image(
            #         label='Image', value=initial_image_path, type='filepath', interactive=False)
    with gr.Row():
        gr.Markdown("# Correcting word:")
    with gr.Row():
        with gr.Column():
            corrected_word = gr.Textbox(label='Word')
            corrected_type = gr.Textbox(label='Type')
            corrected_synonym = gr.Textbox(label='Synonym')
            corrected_antonym = gr.Textbox(label='Antonym')
            corrected_description = gr.Textbox(label='Description')
            corrected_audio = gr.Audio(label='Audio')
        with gr.Column():
            with gr.Row():
                corrected_image = gr.Image(label='Image', type='pil',value=initial_image)
                corrected_image = gr.Image(label='Image', type='pil',value=initial_image)
                corrected_image = gr.Image(label='Image', type='pil',value=initial_image)
            prompt_command = gr.TextArea(label='Image prompt',lines=3)
            btn = gr.Button("Regenerate")

    def on_submit(word, word_type, synonym, antonym, description, image, audio):
        corrected_word_val, corrected_type_val, corrected_synonym_val, corrected_antonym_val, corrected_description_val, resized_image, corrected_audio_val = correct_word(
            word, word_type, synonym, antonym, description, image, audio)
        corrected_word.update(value=corrected_word_val)
        corrected_type.update(value=corrected_type_val)
        corrected_synonym.update(value=corrected_synonym_val)
        corrected_antonym.update(value=corrected_antonym_val)
        corrected_description.update(value=corrected_description_val)
        corrected_image.update(value=resized_image)
        corrected_audio.update(value=corrected_audio_val)

    # btn.click(on_submit, [word, word_type, synonym,antonym, description, image, audio])

# Launch the interface
demo.launch()