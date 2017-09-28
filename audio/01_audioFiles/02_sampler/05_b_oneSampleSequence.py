import simpleaudio as sa
import time
import random

"""
An example project in which a sequence (one measure, one sample) is played.
  - Sixteenth note is the smallest used note duration.
  - One meassure, time signature: 3 / 4

Instead of using steps to iterate to true a sequence, we are checking the time.
We will trigger events at based on their eventtime.

------ HANDS-ON TIPS ------
#TODO - add hands-on tips
"""

#load 1 audioFile and store it into a list
#note: using a list taking the next step into account: using multiple samples
samples = [sa.WaveObject.from_wave_file("../audioFiles/Dog2.wav")]

#set bpm
bpm = 120
#calculate the duration of a quarter note
quarterNoteDuration = 60 / bpm
#calculate the duration of a sixteenth note
sixteenthNoteDuration = quarterNoteDuration / 4.0
#number of beats per sequence (time signature: 3 / 4 = 3 beats per sequence)
beatsPerMeasure = 3
#calculate the duration of a measure
measureDuration = beatsPerMeasure  * quarterNoteDuration

#create a list to hold the events
timeEvents = []
#create a list with the moments (in 16th) at which we should play the sample
sixteenthNoteSequece = [0, 2, 4, 8, 11]
#transform the sixteenthNoteSequece to an eventlist with time values
for sixteenNoteIndex in sixteenthNoteSequece:
  timeEvents.append(sixteenNoteIndex * sixteenthNoteDuration)

print(timeEvents)

#retrieve first event
#NOTE: pop(0) returns and removes the element at index 0
timeEvent = timeEvents.pop(0)
#retrieve the startime: current time
startTime = time.time()
keepPlaying = True
#play the sequence
while keepPlaying:
  #retrieve current time
  currentTime = time.time()
  #check if the timeEvent's time is passed
  if(currentTime - startTime >= timeEvent):
    #play sample
    samples[0].play()

    #if there are events left in the timeEvents list
    if timeEvents:
      #retrieve the next event
      timeEvent = timeEvents.pop(0)
    else:
      #list is empty, stop loop
      keepPlaying = False
  else:
    #wait for a very short moment
    time.sleep(0.001)
