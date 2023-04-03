import requests
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    #return render_template('index.html')
    return send_file("index.html")

@app.route('/detect', methods=['POST'])
def detect():
    #auth_key = os.environ.get('AZURE_KEY')
    auth_key = "c3f3596e-e15d-45a3-b995-af4eb8a8933d"

    text = request.form['text-input']
    
    url = "https://cloud-languagedetection.cognitiveservices.azure.com/"

    headers = {
        "Authorization": f"Azure-Auth-Key {auth_key}"
    }

    data = {
        "query": text
    }

    response = requests.post(url, headers=headers, data=data)
    response_dict = response.json()
    print(response_dict)

    
    #translated_text = response.json()['translations'][0]['text']
    detected_language = response_dict['prediction']['intents']['Delivery']['childApp']['topIntent']
    #detected_language = response.json()['prediction'[0]]['topIntent']
    

    #return render_template('index.html', output=detected_language)
    return send_file("index.html", output = detected_language)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
