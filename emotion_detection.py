
import requests

import json

def emotion_detector(text_to_analyze):    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'    
    myobj = { "raw_document": { "text": text_to_analyze } }    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}    
    response = requests.post(url, json=myobj, headers=header)    
    formatted_response = json.loads(response.text)    
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']    
    anger_score = emotion_predictions['anger']    
    disgust_score = emotion_predictions['disgust']    
    fear_score = emotion_predictions['fear']    
    joy_score = emotion_predictions['joy']    
    sadness_score = emotion_predictions['sadness']        
    dominant_emotion = max(emotion_predictions.items(), key=lambda x: x[1])    
    return {        
        'anger': anger_score,        
        'disgust': disgust_score,        
        'fear': fear_score,        
        'joy': joy_score,        
        'sadness': sadness_score,        
        'dominant_emotion': dominant_emotion[0]      
        }  
