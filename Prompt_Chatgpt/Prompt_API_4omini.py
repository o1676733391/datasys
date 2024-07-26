import json
import os
from dotenv import load_dotenv
from openai import OpenAI
import time

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

with open('./300wordfirst.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

out_data = []
try:
    with open('./prompt_text.json', 'r', encoding='utf-8') as f:
        out_data = json.load(f)
except FileNotFoundError:
    out_data = []

for i in range(10, len(data)):
    print(i)
    word = data[i]['title']
    list_words_type = data[i]['categories']
    prompt = ""

    prompt += "chỉ trả lời theo mẫu:\n"\
        + "- Từ - Loại từ:\n"\
        + "1.Mô tả:...\n"\
        + "2.Ví dụ:...\n"\
        + "3.Từ đồng nghĩa:...\n"\
        + "4.Từ trái nghĩa:...\n"\
        + "nếu từ trái nghĩa, từ đồng nghĩa không có: 'n/a'\n"\
        + "trả lời với trẻ em:\n"\

    for word_type in list_words_type:
        prompt += f"- {word} - {word_type}:\n"\
            + "1.Mô tả bằng cách đơn giản nhất và ngắn gọn mà trẻ em hiểu được\n"\
            + "2.Ví dụ đơn giản mà trẻ em hiểu được và gần gũi với trẻ em\n"\
            + "3.Vài từ đồng nghĩa\n"\
            + "4.Vài từ trái nghĩa\n"\

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user",
             "content": prompt}
        ],
        temperature=0.3,
    )

    form = {
        "title": word,
        "categories": list_words_type,
        "prompt": completion.choices[0].message.content
    }
    out_data.append(form)
    time.sleep(0.5)


with open('./prompt_text.json', 'w', encoding='utf-8') as f:
    json.dump(out_data, f, ensure_ascii=False, indent=4)
    print("success")