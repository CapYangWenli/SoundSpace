import math        #import needed modules
import pyaudio     #sudo apt-get install python-pyaudio


def genSound(tim, freq, bitr):
    PyAudio = pyaudio.PyAudio 
    if freq > bitr:
        bitr = freq + 100
    NUMBEROFFRAMES = int(bitr * tim)
    RESTFRAMES = NUMBEROFFRAMES % bitr
    WAVEDATA = ''
    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA+chr(int(math.sin(x/((bitr/freq)/math.pi))*127+128))    

    for x in range(RESTFRAMES): 
        WAVEDATA = WAVEDATA+chr(128)
    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(1), channels = 1, rate = bitr,  output = True)

    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()

#See https://en.wikipedia.org/wiki/Bit_rate#Audio

if __name__ == "__main__":
    genSound(1, 2000, 16000)

    

#generating wawes



