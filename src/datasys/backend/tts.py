import requests
import config
def text_to_speech(text, path=OUTPUT_PATH, speed=DEFAULT_SPEED, voice=DEFAULT_VOICE):
    url = API_URL
    api_key = API_KEY
    
    headers = {
        'api-key': api_key,
        'speed': speed,
        'voice': voice
    }
    
    response = requests.request('POST', url, data=text.encode('utf-8'), headers=headers)
    # turn the response content into a json object
    result = response.json()

    audio_url = result['async'] if 'async' in result else result['error']
    audio = requests.get(audio_url)
    with open(path, 'wb') as f:
        f.write(audio.content)



# Example usage
result = text_to_speech('xin chào')
