from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    from azure.ai.textanalytics import TextAnalyticsClient
    from azure.core.credentials import AzureKeyCredential
    key = "648a547b8b7f46f19eec09aba8f1f9af"
    text = request.form['text-input']
    endpoint = "https://cloudii-languagedetectionservice.cognitiveservices.azure.com/"
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    language = text_analytics_client.detect_language(documents=[text])[0].primary_language.name
    return render_template("index.html", output = language)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    