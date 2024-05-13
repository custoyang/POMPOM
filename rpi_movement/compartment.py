class Compartment:
  def __init__(self, channel, pillCount, pill, frequency):
    self.channel = channel
    self.pillCount = pillCount
    self.pill = pill
    self.frequency = frequency # in hours

  # Sets pill count
  def setPills(self, added):
    self.pillCount = added

  # Adds pills to pill count
  def addPills(self, added):
    pillCount += added

  # Returns the number of pills in the compartment
  def getPills(self):
    return self.pillCount
  
  # Returns the channel of the motor in the compartment
  def getChannel(self):
    return self.channel
