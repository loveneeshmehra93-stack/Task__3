from flask import Flask, render_template, request
from textblob import TextBlob


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ''
    sentiment = None
    polarity = None
    subjectivity = None
    feedback = None
    result_class = ''

    if request.method == 'POST':
        text = request.form.get('text', '').strip()

        if not text:
            feedback = 'Please enter a sentence or phrase before analyzing.'
        else:
            
            blob = TextBlob(text)
            polarity = round(blob.sentiment.polarity, 4)
            subjectivity = round(blob.sentiment.subjectivity, 4)

            if polarity > 0:
                sentiment = 'Positive'
                result_class = 'positive'
            elif polarity < 0:
                sentiment = 'Negative'
                result_class = 'negative'
            else:
                sentiment = 'Neutral'
                result_class = 'neutral'

    return render_template(
        'index.html',
        text=text,
        sentiment=sentiment,
        polarity=polarity,
        subjectivity=subjectivity,
        feedback=feedback,
        result_class=result_class,
    )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
