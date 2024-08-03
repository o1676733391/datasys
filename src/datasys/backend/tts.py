import requests
import config as c
import json
import os
import time

def create_audio_link(text, speed=c.DEFAULT_SPEED, voice=c.DEFAULT_VOICE):
    url = c.API_URL
    api_key = c.API_KEY
    
    headers = {
        'api-key': api_key,
        'speed': speed,
        'voice': voice
    }
    
    try:
        response = requests.post(url, data=text.encode('utf-8'), headers=headers)
        response.raise_for_status()  # Check for HTTP request errors
        
        result = response.json()

        # Safely access the 'async' key or provide a default value
        audio_url = result.get('async', result.get('error', None))
        
        if audio_url is None:
            print("Error: Neither 'async' nor 'error' key found in the result.")
            print(f"Full response: {result}")
            return None
        
        return audio_url
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decode failed: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Ensure the output directory exists
output_dir = os.path.join('datasys', 'data', 'sound')
os.makedirs(output_dir, exist_ok=True)

# Read the JSON data from the file
with open('dictionary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Generate audio links for each word and store in a list
audio_links = []
for index, entry in enumerate(data):
    print(f"Generating audio link for '{entry['word']}' (entry {index+1}/{len(data)})...")
    word = entry['word']
    file_id = entry['_id']
    
    audio_url = create_audio_link(word)
    if audio_url:
        audio_links.append({'_id': file_id, 'word': word, 'audio_url': audio_url})
    
    # Add a delay to avoid hitting rate limits
    time.sleep(2)  # Adjust the sleep duration as needed

# Save audio links to a JSON file
with open('audio_links.json', 'w', encoding='utf-8') as f:
    json.dump(audio_links, f, ensure_ascii=False, indent=4)

print("Audio links have been generated and saved to 'audio_links.json'.")
