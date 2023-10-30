from googletrans import Translator

def functranslate(text,language):
    translator = Translator()
    translatedText = translator.translate(text, dest=language)
    return translatedText.text







