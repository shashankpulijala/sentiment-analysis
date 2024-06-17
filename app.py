from flask import Flask, render_template, request
from transformers import pipeline

rom flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the pre-trained sentiment analysis model
sentiment_analysis = pipeline('sentiment-analysis')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        result = sentiment_analysis(text)
        sentiment = result[0]['label']
        return render_template('result.html', sentiment=sentiment, text=text)
if __name__ == '__main__':
    app.run(debug=True)