from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector") 
def emotion_detection():
    text_to_analyse = request.args.get('textToAnalyze')
    
    # Get the emotion analysis response
    response = emotion_detector(text_to_analyse)

    # Prepare the string with the emotion scores
    emotions_str = ", ".join([f"'{emotion}': {score}" for emotion, score in response.items() if emotion != 'dominant_emotion'])

    # Get the dominant emotion
    dominant_emotion = response.get('dominant_emotion')

    return f"For the given statement, the system response is {emotions_str}. The dominant emotion is {dominant_emotion}."
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)