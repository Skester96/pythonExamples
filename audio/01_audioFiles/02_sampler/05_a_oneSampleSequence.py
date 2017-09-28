import simpleaudio as sa
import time
import random

"""
An example project in which a sequence (one measure, one sample) is played.
  - Sixteenth note is the smallest used note duration.
  - One meassure, time signature: 3 / 4
  - 3 * 4 sixteenth notes per measure = 12 'spots'

------ HANDS-ON TIPS ------
#TODO - add hands-on tips
"""

#load 1 audioFile and store it into a list
#note: using a list taking the next step into account: using multiple samples
samples = [sa.WaveObject.from_wave_file("../audioFiles/Pop.wav")]

#set bpm
bpm = 120
#calculate beatDuration with bpm
beatDuration = 60 / bpm
#number of beats per sequence (time signature: 3 / 4 = 3 beats per sequence)
beatsPerSequence = 3
#calculate stepDuration, this is the smalles note duration, a 16th note
#(16th note equals 1/4 of a quarter note -> 0.25)
stepDuration = 0.25
#calculate number of steps per sequence
stepsPerSequence = int(1 / stepDuration * beatsPerSequence)

#create a list to hold a rhythm notated in sixteenth notes
#these are the steps at which we will play the sample
sequence = [0, 2, 4, 8, 11]
#retrieve first event of sequence
#NOTE: pop(0) returns and removes the element at index 0
event = sequence.pop(0)
#play the sequence
for step in range(stepsPerSequence):
  print(event)
  if(step == event):
    samples[0].play()
    #retrieve the next event
    event = sequence.pop(0)
  #wait!
  time.sleep(stepDuration)
