import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    payload = {'text': text_to_analyze}
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        response_data = response.json()
        return response_data.get('text', '')
    else:
        print(f"Error: Request failed with status code {response.status_code}")
        return None