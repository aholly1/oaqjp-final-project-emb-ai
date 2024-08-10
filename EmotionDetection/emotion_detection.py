'''Import requests and JSON'''
import requests
import json

'''
Method to send a request to an Emotion Detector AI API and return a response.
The response entails a dictionary of emoitions and their respective scores baised
on the language and syntax of the text. The result is a final dictionary of the emotions 
and their respective scores and the domminant emotion of the text.
''''
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=headers)

     if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!", 400

    response_dict = json.loads(response.text)

    emotions = response_dict['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return result

    
