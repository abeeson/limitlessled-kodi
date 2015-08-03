import xbmc,xbmcgui
import subprocess,os,socket,time

class MyPlayer(xbmc.Player) :

        def __init__ (self):
            xbmc.Player.__init__(self)

        def onPlayBackStarted(self):
            if xbmc.Player().isPlayingVideo():
                self.dim(self)

        def onPlayBackEnded(self):
            if (VIDEO == 1):
                self.brighten(self)

        def onPlayBackStopped(self):
            if (VIDEO == 1):
                self.brighten(self)

        def onPlayBackPaused(self):
            if xbmc.Player().isPlayingVideo():
                self.brighten(self)

        def onPlayBackResumed(self):
            if xbmc.Player().isPlayingVideo():
                self.dim(self)

        def lightsOn(self, event):
            self.sendUdpCommand(self, '\x42\x00', 0.1)

        def lightsOff(self, event):
            self.sendUdpCommand(self, '\x41\x00', 0.1)

        def dim(self, event):
            timer = 0.2
            messages = ['\x4E\x1B\x55','\x4E\x1A\x55','\x4E\x19\x55','\x4E\x18\x55','\x4E\x17\x55','\x4E\x16\x55','\x4E\x15\x55','\x4E\x14\x55','\x4E\x13\x55','\x4E\x12\x55','\x4E\x11\x55','\x4E\x10\x55','\x4E\x0E\x55','\x4E\x0D\x55','\x4E\x0C\x55','\x4E\x0B\x55','\x4E\x0A\x55','\x4E\x09\x55','\x4E\x08\x55','\x4E\x07\x55','\x4E\x06\x55','\x4E\x05\x55','\x4E\x04\x55','\x4E\x04\x55','\x4E\x04\x55']
            for message in messages:
                self.sendUdpCommand(self, message, timer)

        def brighten(self, event):
            timer = 0.2
            messages = ['\x4E\x04\x55','\x4E\x05\x55','\x4E\x06\x55','\x4E\x07\x55','\x4E\x08\x55','\x4E\x09\x55','\x4E\x0A\x55','\x4E\x0B\x55','\x4E\x0C\x55','\x4E\x0D\x55','\x4E\x0E\x55','\x4E\x10\x55','\x4E\x11\x55','\x4E\x12\x55','\x4E\x13\x55','\x4E\x14\x55','\x4E\x15\x55','\x4E\x16\x55','\x4E\x17\x55','\x4E\x18\x55','\x4E\x19\x55','\x4E\x1A\x55','\x4E\x1B\x55','\x4E\x1B\x55','\x4E\x1B\x55']
            for message in messages:
                self.sendUdpCommand(self, message, timer)

        def sendUdpCommand(self, event, message, timer):
            UDP_IP = '192.168.1.2'
            UDP_PORT = 8899
            print("sendUdpCommand UDP target IP:", UDP_IP)
            print("sendUdpCommand UDP target port:", UDP_PORT)
            print("sendUdpCommand message:", message)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
            sock.sendto(message, (UDP_IP, UDP_PORT))
            time.sleep(timer)

player=MyPlayer()

VIDEO = 0

while(1):
    if xbmc.Player().isPlaying():
      if xbmc.Player().isPlayingVideo():
        VIDEO = 1

      else:
        VIDEO = 0

    xbmc.sleep(1000)