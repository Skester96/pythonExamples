import sineGenerator

class AudioProcessor:
    def __init__(self, audioSettings):
      self.audioSettings = audioSettings
      self.sine = sineGenerator.Sine(audioSettings)
      self.sine2 = sineGenerator.Sine(audioSettings, 440)

    def process(self, inputFrame):
      #move sine a step forward
      self.sine.tick()
      self.sine2.tick()
      #retrieve the new value

      return self.sine.value + self.sine2.value
