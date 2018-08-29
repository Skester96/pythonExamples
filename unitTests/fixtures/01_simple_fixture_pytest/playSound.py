#simpleaudio is imported as sa -> shorter name
import simpleaudio as sa

def play_the_sample():
    #load audioFile
    sample = sa.WaveObject.from_wave_file("../../../audio/01_audioFiles/audioFiles/Pop.wav")
    sample_play = sample.play()
    #wait till sample is done playing
    sample_play.wait_done()
