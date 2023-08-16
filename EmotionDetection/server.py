"""
Emotion Detection Server
This script sets up a Flask server for emotion detection.
"""

from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detection_endpoint():
    """
    Emotion Detection Endpoint
    This function handles emotion detection requests.
    """
    data = request.get_json()
    statement = data.get('statement', '')

    if statement:
        result = emotion_detector(statement)
        dominant_emotion = result['dominant_emotion']

        if dominant_emotion is not None:
            response = {
                "anger": result['anger'],
                "disgust": result['disgust'],
                "fear": result['fear'],
                "joy": result['joy'],
                "sadness": result['sadness'],
                "dominant_emotion": result['dominant_emotion']
            }

            output = (
                f"For the given statement, the system response is "
                f"'anger': {response['anger']}, "
                f"'disgust': {response['disgust']}, "
                f"'fear': {response['fear']}, "
                f"'joy': {response['joy']}, "
                f"'sadness': {response['sadness']}. "
                f"The dominant emotion is {response['dominant_emotion']}."
            )
        else:
            output = "Invalid text! Please try again."
    else:
        output = "Invalid text! Please try again."

    return jsonify(output)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
