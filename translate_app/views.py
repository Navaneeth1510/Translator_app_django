# translate_app/views.py
from django.shortcuts import render
from google.cloud import translate_v2 as translate

def translate_text(request):
    translated_text = None
    if request.method == 'POST':
        text = request.POST.get('text')
        target_language = request.POST.get('target_language')
        if text and target_language:
            translate_client = translate.Client()
            result = translate_client.translate(text, target_language=target_language)
            translated_text = result['translatedText']
    return render(request, 'templates/translate_app/translate_form.html', {'translated_text': translated_text})
