from TV import TV
def main():
  tv1 =  TV()
  tv1.turnOn()
  tv1.setChannel(30)
  tv1.setVolumeLevel(3)
  
  tv2 = TV()
  tv2.turnOn()
  tv2.channelUp()
  tv2.channelUp()
  tv2.volumeUp()
  print("tv1's channel is",tv1.getChannel(), "tv1's volume is",tv1.getVolumeLevel())
  print("tv2's channel is",tv2.getChannel(), "tv1's volume is",tv2.getVolumeLevel())
main()

