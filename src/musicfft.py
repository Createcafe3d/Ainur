import echonest.audio as audio

class MusicFFT():
    def __init__(songFile,resolution):
        self._audio_file = audio.LocalAudioFile(songFile)

