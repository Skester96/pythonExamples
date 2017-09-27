import simpleaudio as sa
import time

"""
An example project in which three wav files are played after eachother with a
minor break in between.

------ HANDS-ON TIPS ------
- Can you repeat the forloop multiple times? (add a loop)
- Can you change the time into a random value? E.g. wait 0.25, 0.5, or 1 second.
  hint1: you will need a random function:
  hint2: there is a standard random package available with a random funtion
         https://docs.python.org/2/library/random.html
         (A standard package does not need to be installed with pip, but it does
         need to be imported)
"""
#load 3 audioFiles into a list
samples = [sa.WaveObject.from_wave_file("../audioFiles/Pop.wav"),
              sa.WaveObject.from_wave_file("../audioFiles/Laser1.wav"),
              sa.WaveObject.from_wave_file("../audioFiles/Dog2.wav")]


#play samples, wait 1 second in between
for sample in samples:
  #display the sample object
  print(sample)
  #play sample
  sample.play()
  #wait 1 second
  time.sleep(1)
