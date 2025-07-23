from flask import Flask, request, jsonify, render_template
from deep_translator import GoogleTranslator  # or any translator of your choice

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text')
    target_lang = data.get('target_lang')

    try:
        translated_text = GoogleTranslator(target=target_lang).translate(text)
        return jsonify({'translatedText': translated_text})
    except Exception as e:
        return jsonify({'translatedText': f"Error: {str(e)}"}), 500

if __name__ == '__main__':
import os

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port, debug=True)

