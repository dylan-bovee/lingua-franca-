from flask import Flask, render_template, request, jsonify
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route("/")
def index():
    return render_template("index.html", languages=LANGUAGES)

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    src_lang = data.get("src_lang", "auto")
    dest_lang = data.get("dest_lang", "en")

    if not text.strip():
        return jsonify(translated_text="", detected_lang="")

    result = translator.translate(text, src=src_lang, dest=dest_lang)
    return jsonify(
        translated_text=result.text,
        detected_lang=LANGUAGES.get(result.src, result.src)
    )

if __name__ == "__main__":
    app.run(debug=True)
