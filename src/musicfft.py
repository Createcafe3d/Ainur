import librosa

class MusicFFT():
    def __init__(self,songFile,resolution):
        self._audio_file = librosa.util.example_audio_file()
        self._audio = librosa.load(self._audio_file)
        #self._audio_file = librosa.load(songFile)
        print self._audio_file


if __name__ == "__main__":
    resolution = 1.0
    song = '/home/green/Downloads/Lionel Richie - Hello.mp3'
    song = '/home/green/Downloads/Lionel Richie - Hello.mp3'
    MyClass = MusicFFT(song,resolution)


