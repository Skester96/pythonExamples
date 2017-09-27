import simpleaudio as sa
import time
import random

"""
An example project in which three wav files are played after eachother with a
break in between of a random note duration.
Used note durations are: sixteenth, eight, quarter notes

------ HANDS-ON TIPS ------
#TODO - add hands-on tips
"""

#load 3 audioFiles into a list
samples = [sa.WaveObject.from_wave_file("../audioFiles/Pop.wav"),
              sa.WaveObject.from_wave_file("../audioFiles/Laser1.wav"),
              sa.WaveObject.from_wave_file("../audioFiles/Dog2.wav")]

#create a list with possible noteValues: sixteenth, eight and a quarter note
noteDurations = [0.25, 0.5, 1]
#set bpm
bpm = 120
#create a list to hold timeIntervals
timeIntervals = []

#transform noteDurations into timeIntervals, depending on bpm
#calculate beatDuration in seconds (equals duration of a quarter note)
beatDuration = 60.0 / bpm
for noteDuration in noteDurations:
  #calculate timeDuration and add to the list
  timeIntervals.append(beatDuration * noteDuration)

#display timeIntervals
print(timeIntervals)


#a function that plays a list of samples with random timeIntervals in between
def playSamples(samples, intervals):
  #play samples and wait in between (random duration)
  for sample in samples:
    #display the sample object
    print(sample)
    #play sample
    sample.play()
    #retrieve a random timeInterval
    #use the random.choice function -> returns a random element from a sequence
    interval = random.choice(intervals)
    #display the selected time interval
    print("waiting: " + str(interval) + " seconds.")
    #wait!
    time.sleep(interval)

#call the playSamples function 4 times
for i in range(4):
  playSamples(samples, timeIntervals)
