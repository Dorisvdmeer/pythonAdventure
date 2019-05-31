from google.cloud import translate

def translate_text(text, target='nl'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target)

    bodyInput =result['input']
    bodyLanguage = result['translatedText']
    bodyTranslation = result['detectedSourceLanguage']

    return("Blog input: {bodyInput}\nVertaling:  {bodyLanguage}\nTaal herkend: {bodyTranslation}".format(bodyInput=bodyInput, bodyLanguage=bodyLanguage, bodyTranslation=bodyTranslation))

