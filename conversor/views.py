from django.shortcuts import render, redirect
from django.conf import settings
from .forms import VideoForm
from .models import Video, Audio
from pydub import AudioSegment
import os

def converter_video(request):
    nome_arquivo = None
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            caminho_video = video.arquivo.path
            nome_arquivo, _ = os.path.splitext(video.arquivo.name)
            caminho_audio = os.path.join(settings.MEDIA_ROOT, 'audios/videos', f'{nome_arquivo}.mp3')

            # Verifica se o diretório existe, caso contrário, cria
            diretorio_audio = os.path.dirname(caminho_audio)
            if not os.path.exists(diretorio_audio):
                os.makedirs(diretorio_audio)

            # Conversão do vídeo para áudio
            audio = AudioSegment.from_file(caminho_video)
            audio.export(caminho_audio, format='mp3')

            # Salvando o áudio no modelo
            Audio.objects.create(video=video, arquivo=caminho_audio)

            nome_arquivo = f'audios/videos/{nome_arquivo}.mp3'
            return render(request, 'conversor/sucesso.html', {'nome_arquivo': nome_arquivo})
    else:
        form = VideoForm()
    return render(request, 'conversor/converter.html', {'form': form})

def sucesso(request):
    return render(request, 'conversor/sucesso.html', {'MEDIA_URL': settings.MEDIA_URL})
