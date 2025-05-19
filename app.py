from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    source_lang_detected = None
    text_to_translate = ""
    src_lang = "auto"
    dest_lang = "fr"

    if request.method == "POST":
        text_to_translate = request.form["text"]
        src_lang = request.form["src_lang"]
        dest_lang = request.form["dest_lang"]

        if src_lang == "auto":
            detected = translator.detect(text_to_translate)
            source_lang_detected = LANGUAGES.get(detected.lang, detected.lang)
            src_lang = detected.lang

        translation = translator.translate(text_to_translate, src=src_lang, dest=dest_lang)
        translated_text = translation.text

    languages = LANGUAGES  # Dictionnaire code: nom
    return render_template("index.html",
                           translated_text=translated_text,
                           text_to_translate=text_to_translate,
                           languages=languages,
                           source_lang_detected=source_lang_detected)

if __name__ == "__main__":
    app.run(debug=True)
