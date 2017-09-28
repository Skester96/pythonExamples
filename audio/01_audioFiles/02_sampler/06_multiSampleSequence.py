import simpleaudio as sa
import time
import random

"""
An example project in which a sequence (one measure, multiple samples) is played.
  - Sixteenth note is the smallest used note duration.
  - One meassure, time signature: 3 / 4

Instead of using steps to iterate to true a sequence, we are checking the time.
We will trigger events at based on their eventtime.

------ HANDS-ON TIPS ------
#TODO - add hands-on tips
- Line 62 is outcommented. However, this line is essential to enable correct
  playback of the sequence.
  Run the script with the outcommented line, what goes wrong?
  Remove the [#] at the of the line, what will happen now?
- Are you able you detect the duplicate code?
  Think of a solution to prevent this duplicate code.
  Implement your solution.
- Currently the sequence is only played once.
  Alter the code to play it multiple times.
  hint: The events list is emptied using the pop() function. Copy it first?
"""

#______________________________________________________________________________
#NOTE: THIS SCRIPT CONTAINS DUPLICATE CODE = USEFULL EXAMPLE, SEE HANDS-ON TIPS
#______________________________________________________________________________

#load 3 audioFiles and store it into a list
samples = [ sa.WaveObject.from_wave_file("../audioFiles/Pop.wav"),
            sa.WaveObject.from_wave_file("../audioFiles/Laser1.wav"),
            sa.WaveObject.from_wave_file("../audioFiles/Dog2.wav"), ]

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
events = []
#create lists with the moments (in 16th) at which we should play the samples
sequence1 = [0, 2, 4, 8, 11]
sequence2 = [3, 6, 10]
sequence3 = [9, 13]

#transform the sixteenthNoteSequece to an eventlist with time values
for sixteenNoteIndex in sequence1:
  events.append([sixteenNoteIndex * sixteenthNoteDuration, 0])

#transform the sixteenthNoteSequece to an eventlist with time values
for sixteenNoteIndex in sequence2:
  events.append([sixteenNoteIndex * sixteenthNoteDuration, 1])

#transform the sixteenthNoteSequece to an eventlist with time values
for sixteenNoteIndex in sequence3:
  events.append([sixteenNoteIndex * sixteenthNoteDuration, 2])

#NOTE: The line below is essential to enable a correct playback of the events
#events.sort()

#display the event list
print(events)

#retrieve first event
#NOTE: pop(0) returns and removes the element at index 0
event = events.pop(0)
#retrieve the startime: current time
startTime = time.time()
keepPlaying = True
#play the sequence
while keepPlaying:
  #retrieve current time
  currentTime = time.time()
  #check if the event's time (which is at index 0 of event) is passed
  if(currentTime - startTime >= event[0]):
    #play sample -> sample index is at index 1
    samples[event[1]].play()
    #if there are events left in the events list
    if events:
      #retrieve the next event
      event = events.pop(0)
    else:
      #list is empty, stop loop
      keepPlaying = False
  else:
    #wait for a very short moment
    time.sleep(0.001)
