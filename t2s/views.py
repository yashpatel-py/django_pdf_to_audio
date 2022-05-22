from django.shortcuts import render
from gtts import gTTS
import textract as tx
import os

# Create your views here.
def text_to_speech(request):
    language = 'en'
    music = ''

    if request.method == 'POST':
        text = request.POST.get('text')
        lang = request.POST.get('lang')
        my_speech = gTTS(text=text, lang=lang, slow=False)
        my_speech.save("static/speech.mp3")
        music = "done"
        context = {
            'music': music
        }
        return render(request, 'text_to_audio.html', context)
    else:
        pass
    context = {
        'music': music
    }
    return render(request, 'text_to_audio.html', context)