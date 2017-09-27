#simpleaudio is imported as sa -> shorter name
import simpleaudio as sa

"""
An example project in which three wav files are played after eachother.

------ HANDS-ON TIPS ------
- A question before running the code: do you expect to hear the samples played simultaniously or
  after eachother?
- Can you identify the duplicate code? With duplicate code we refer to code
  that occurs more than once.
- Can you alter the code to play the sounds simultaniously?
"""

#load 3 audioFiles
sampleHigh = sa.WaveObject.from_wave_file("../audioFiles/Pop.wav")
sampleMid = sa.WaveObject.from_wave_file("../audioFiles/Laser1.wav")
sampleLow = sa.WaveObject.from_wave_file("../audioFiles/Dog2.wav")

#play high sample
sampleHighPlay = sampleHigh.play()
#wait till sample is done playing
sampleLowPlay.wait_done()

#play mid sample
sampleMidPlay = sampleMid.play()
#wait till sample is done playing
sampleHighPlay.wait_done()

#play low sample
sampleLowPlay = sampleLow.play()
#wait till sample is done playing
sampleMidPlay.wait_done()
