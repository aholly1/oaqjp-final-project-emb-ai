'''
Importing the Flask framework, render_template, and request
'''
from flask import Flask, render_template, request
'''
Importing the emotion_detector method from the EmotionDetection Package
'''
from EmotionDetection.emotion_detection import emotion_detector

'''
Flask App
'''
app = Flask("Emotion Detection")

'''
Router to handle user inputed text to be analysed
'''
@app.route("/emotionDetector") 
def emotion_detection():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    emotions_str = ", ".join([f"'{emotion}': {score}" for emotion, score in response.items() if emotion != 'dominant_emotion'])
    dominant_emotion = response.get('dominant_emotion')
    return f"For the given statement, the system response is {emotions_str}. The dominant emotion is {dominant_emotion}."

'''
Router to handle reandering the page supplied to by IBM Coursera
'''
@app.route("/")
def render_index_page():
    return render_template("index.html")
    
'''
Establishing host & port
'''
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
