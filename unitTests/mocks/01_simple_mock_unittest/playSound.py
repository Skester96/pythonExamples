#simpleaudio is imported as sa -> shorter name
import simpleaudio as sa

def play_the_sample(a_path):
    # load audioFile, e.g. "../../../audio/01_audioFiles/audioFiles/Pop.wav"
    sample = sa.WaveObject.from_wave_file(a_path)
    sample_play = sample.play()
    # wait till sample is done playing
    sample_play.wait_done()

# run it
# play_the_sample("../../../audio/01_audioFiles/audioFiles/Pop.wav")
