"""
Este programa utiliza la librería simpleaudio para crear un metrónomo virtual que reproduce un sonido repetitivo en un intervalo específico,
emulando el ritmo de un metrónomo musical. El usuario proporciona un intervalo de repetición en BPM (beats por minuto) para definir la velocidad
del metrónomo.

Autor:
    Pablo Codelia pablo.codelia@elevaproductora.cl
"""
import simpleaudio
import time

def reproducir_metronomo(archivo, intervalo):
    """
    Reproduce el archivo de sonido del metrónomo en un intervalo de tiempo específico.

    Args:
        archivo (str): Ruta del archivo WAV que se reproducirá como sonido del metrónomo.
        intervalo (float): Intervalo de tiempo en segundos entre cada reproducción del sonido.

    Returns:
        None
    """
    audio = simpleaudio.WaveObject.from_wave_file(archivo)
    while True:
        play_obj = audio.play()
        time.sleep(intervalo)

if __name__ == "__main__":
    archivo = "checked.wav"  # Ruta del archivo WAV
    tempo_bpm = float(input("Introduce el intervalo de repetición en BPM: "))
    intervalo = 60 / tempo_bpm 
    
    reproducir_metronomo(archivo, intervalo)
