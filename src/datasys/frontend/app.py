import gradio as gr
from PIL import Image

# Load the image
initial_image_path = "datasys\\data\\example\\walk.jpg"
initial_image = Image.open(initial_image_path)

# Load the audio
initial_audio_path = "datasys\\data\\example\\run-11239.mp3"

# Define the Blocks interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:  # theme
    gr.Markdown("# Checking Words & Adding Images")
    with gr.Column():
        gr.Markdown('')
        with gr.Row():
            with gr.Column():
                word = gr.Textbox(label='Word', value='đi', interactive=False)
                word_type = gr.Textbox(
                    label='Type', value='động từ', interactive=False)
            with gr.Column():
                synonym = gr.Textbox(
                    label='Synonym', value='123', interactive=False)
                antonym = gr.Textbox(
                    label='Antonym', value='123', interactive=False)
            with gr.Column():
                audio = gr.Audio(
                    label='Audio', value=initial_audio_path, type='filepath', interactive=False)

        description = gr.Textbox(
            label='Description', value='(người, động vật) tự di chuyển từ chỗ này đến chỗ khác bằng những bước chân nhấc lên, đặt xuống liên tiếp', interactive=False)
        # with gr.Row():
        #     image = gr.Image(
        #         label='Image', value=initial_image_path, type='filepath', interactive=False)
    with gr.Column():
        gr.Markdown("# Correcting word:")
        with gr.Row():
            with gr.Column():
                corrected_word = gr.Textbox(label='Word', value='đi')
                corrected_type = gr.Dropdown(['động từ', 'danh từ', 'tính từ'], label='Type')
            with gr.Column():

                corrected_synonym = gr.Textbox(label='Synonym')
                corrected_antonym = gr.Textbox(label='Antonym')
            with gr.Column():
                corrected_audio = gr.Audio(label='Audio')
        corrected_description = gr.TextArea(
            label='Description', value='(người, động vật) tự di chuyển từ chỗ này đến chỗ khác bằng những bước chân nhấc lên, đặt xuống liên tiếp', lines=2,interactive=True)
        with gr.Row():
            with gr.Column():
                prompt_command = gr.TextArea(label='Image prompt', lines=5)
                # btn_send_prompt = gr.Button('Send prompt', variant='secondary')

            with gr.Column():
                corrected_image = gr.Image(
                    label='Image', type='pil', value=initial_image)
                btn_regen = gr.Button("Regenerate", variant='primary')

    gr.Button('Next word', variant='primary')
# Launch the interface
demo.launch()
