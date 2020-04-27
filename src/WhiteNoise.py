import pyaudio
import wave

CHUNK = 32768

class WhiteNoiseApplet():
    def __init__(self):
        self.waveFile = wave.open('whitenoise.wav', 'rb')
        self.data = self.waveFile.readframes(CHUNK)
        self.stream  = None
        self.audio = None
        self.on = False
        
    def openStream(self):
        self.audio = pyaudio.PyAudio()
        print('check1')
        self.stream = self.audio.open(format = self.audio.get_format_from_width(self.waveFile.getsampwidth()),
        channels = self.waveFile.getnchannels(),
        rate=self.waveFile.getframerate(),
        output=True
        )
        print('check2')
        
    
    def playStream(self):
        print('check3')
        while len(self.data)>0:
            self.stream.write(self.data)
            self.data=self.waveFile.readframes(CHUNK)
        print('check4')
    def stopStream(self):
        print('check5')
        self.stream.stop_stream()
        print('check6')
        self.stream.close()
        print('check7')
        self.audio.terminate()
        print('check8')       
    
    def playWhiteNoise(self):
        self.openStream()
        self.playStream()
        print("check9")
        self.playStream()
        self.stopStream()

def main():
    # Gmail unit tests
    whiteNoiseApp = WhiteNoiseApplet()
    whiteNoiseApp.playWhiteNoise()
    

if __name__ == '__main__':
    main()
    