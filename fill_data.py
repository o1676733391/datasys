import re
import json
from tqdm import tqdm

# NOTE: desc, example, synonym, antonym


def regex_process(paragraph):
    pattern = re.compile(r"(\d\.\s)|(.*:\s)")
    cleaned_data = pattern.sub("", paragraph)

    # list and remove empty string
    list_cleaned_data = [data for data in cleaned_data.splitlines() if data != ""]
    return list_cleaned_data


def formular(list_promt):
    formular_data = {}
    categories_list = ["desc", "example", "synonym", "antonym"]

    for index_data in range(len(list_promt)):
        formular_data[categories_list[index_data]] = list_promt[index_data]
    formular_data["img"] = "n/a"
    return formular_data


def regex_raw_data(raw_data):
    regex_data = {"word": raw_data["title"], "voice": "n/a"}

    regex_data_process_list = regex_process(raw_data["prompt"])
    raw_data_categories = raw_data["categories"]

    # convert categories to englist type
    respective_categories = {"Danh từ": "noun", "Tính từ": "adj", "Động từ": "verb"}

    check_point = 0

    # seperate type word
    for index_categorie in range(len(raw_data_categories)):
        try:
            current_index = check_point + (
                int(len(regex_data_process_list) / len(raw_data_categories))
            )

            # formular desc, ex, synonym, antonym
            regex_data[respective_categories[raw_data_categories[index_categorie]]] = (
                formular(regex_data_process_list[check_point:current_index])
            )

            check_point = current_index
        except NameError as e:
            print(e)
            return {
                "error": e,
            }

    return regex_data


# Load the input JSON data
with open("./prompt_text.json") as f:
    data = json.load(f)

output_data = []

# Process each word entry in the input data
for word in tqdm(data):
    output_data.append(regex_raw_data(word))

# Save the processed data to a new JSON file with UTF-8 encoding
with open("./output.json", "w", encoding="utf-8") as outfile:
    json.dump(output_data, outfile, ensure_ascii=False, indent=4)
