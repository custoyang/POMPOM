class Compartment:
  def __init__(self, channel, pillCount, pill, frequency):
    self.channel = channel
    self.pillCount = pillCount
    self.pill = pill
    self.frequency = frequency
 
  def setPills(self, added):
    self.pillCount = added

  def addPills(self, added):
    pillCount += added

  def getPills(self):
    return self.pillCount
  
  def getChannel(self):
    return self.channel
