import openai
import json

# Đọc file JSON
with open('prompt_text.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Thiết lập API key cho OpenAI
openai.api_key = 'YOUR_API_KEY'

# Hàm để tạo ảnh từ từ khóa
def create_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

# Lặp qua từng mục trong JSON và tạo ảnh
for entry in data:
    title = entry['title']
    prompt = f"Tạo ảnh phù hợp với từ '{title}' cho trẻ em dễ hiểu"
    image_url = create_image(prompt)
    print(f"Title: {title}\nImage URL: {image_url}\n")
