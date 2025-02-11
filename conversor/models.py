from django.db import models

class Video(models.Model):
    arquivo = models.FileField(upload_to='videos/')
    data_envio = models.DateTimeField(auto_now_add=True)

class Audio(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='audios/')
    data_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Áudio para {self.video}'