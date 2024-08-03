import json
import os
import time
import requests

def download_audio_file(audio_url, path, retries=3, delay=5):
    for attempt in range(retries):
        try:
            audio = requests.get(audio_url)
            if audio.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(audio.content)
                return True
            else:
                print(f"Attempt {attempt + 1} failed: {audio.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
        
        time.sleep(delay)  # Wait before retrying

    print(f"Failed to download audio after {retries} attempts.")
    return False

# Ensure the output directory exists
output_dir = os.path.join('datasys', 'data', 'sound')
os.makedirs(output_dir, exist_ok=True)

# Wait for 5 minutes before starting the download
# print("Waiting for 5 minutes before starting the download...")
# time.sleep(300)

# Read the audio links from the JSON file
with open('audio_links.json', 'r', encoding='utf-8') as f:
    audio_links = json.load(f)

# Download audio files for each link
for index, entry in enumerate(audio_links):
    print(f"Downloading audio for '{entry['word']}' (entry {index+1}/{len(audio_links)})...")
    file_id = entry['_id']
    audio_url = entry['audio_url']
    output_path = os.path.join(output_dir, f"{file_id}.mp3")
    
    success = download_audio_file(audio_url, output_path)
    if not success:
        print(f"Failed to download audio for '{entry['word']}' (entry {index+1}/{len(audio_links)})")

print("MP3 files have been downloaded.")
