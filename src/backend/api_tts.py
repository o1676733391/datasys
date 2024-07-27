import requests
import time
import api_config

def call_tts_api(voice='banmai', speed=''):
    url = api_config.URL
    headers = {
        'api-key': api_config.API_KEY,
        'speed': speed,
        'voice': voice
    }
    response = requests.post(url, data=text.encode('utf-8'), headers=headers)
    return response

def tts_function(api_key, text, voice, speed):
    if api_key and text:
        response = call_tts_api(text, api_key, voice, str(speed))
        if response.status_code == 200:
            result = response.json()
            async_url = result.get("async")
            if async_url:
                for _ in range(10):  # Thử lại 10 lần với độ trễ
                    audio_response = requests.get(async_url)
                    if audio_response.status_code == 200:
                        # Lưu nội dung âm thanh vào file tạm thời
                        with open("temp_audio.mp3", "wb") as audio_file:
                            audio_file.write(audio_response.content)
                        return 'Chuyển đổi thành công!', "temp_audio.mp3"
                    time.sleep(2)
                return 'Không thể lấy tệp âm thanh sau nhiều lần thử.', None
            else:
                return 'Không tìm thấy URL không đồng bộ trong phản hồi.', None
        else:
            return f'Lỗi: {response.status_code}\n{response.text}', None
    else:
        return 'Cần phải nhập API Key và văn bản.', None