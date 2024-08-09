import json

data_hanviet = []
data_vocab = []
data_output = []

with open('./hanviet.json', 'r', encoding='utf-8') as f:
    data_hanviet = json.load(f)
with open('./vocab_not_null.json', 'r', encoding='utf-8') as f:
    data_vocab = json.load(f)

try:
    with open('./vocab_filter.json', 'r', encoding='utf-8') as f:
        data_output = json.load(f)
except FileNotFoundError:
    data_output = []

dsHanViet = []
for word in data_hanviet["words"]:
    dsHanViet.append(word["hanviet"])

for word in data_vocab:
    if word["title"] not in dsHanViet:
        data_output.append(word)

with open('./vocab_filter.json', 'w', encoding='utf-8') as f:
    json.dump(data_output, f, ensure_ascii=False, indent=4)
    print("success")
