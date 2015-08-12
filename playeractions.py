import xbmc,xbmcgui
import subprocess,os,socket,time,ConfigParser

class MyPlayer(xbmc.Player) :

        def __init__ (self):
            self.isMovie = 0
            config = ConfigParser.ConfigParser()
            config.readfp(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'llled.ini')))
            self.ip = config.get('connection', 'ip')
            self.port = config.getint('connection', 'port')
            self.dimForTv = config.get('options', 'dimForTv')
            self.dimForMovies = config.get('options', 'dimForMovies')
            self.commandInterval = config.getfloat('lights', 'commandInterval')
            type = config.get('lights', 'type')
            if type == 'rgbw':
                self.dimCommands = ['\x4E\x1B\x55','\x4E\x1A\x55','\x4E\x19\x55','\x4E\x18\x55','\x4E\x17\x55','\x4E\x16\x55','\x4E\x15\x55','\x4E\x14\x55','\x4E\x13\x55','\x4E\x12\x55','\x4E\x11\x55','\x4E\x10\x55','\x4E\x0E\x55','\x4E\x0D\x55','\x4E\x0C\x55','\x4E\x0B\x55','\x4E\x0A\x55','\x4E\x09\x55','\x4E\x08\x55','\x4E\x07\x55','\x4E\x06\x55','\x4E\x05\x55','\x4E\x04\x55','\x4E\x04\x55','\x4E\x04\x55']
                self.brightenCommands = ['\x4E\x04\x55','\x4E\x05\x55','\x4E\x06\x55','\x4E\x07\x55','\x4E\x08\x55','\x4E\x09\x55','\x4E\x0A\x55','\x4E\x0B\x55','\x4E\x0C\x55','\x4E\x0D\x55','\x4E\x0E\x55','\x4E\x10\x55','\x4E\x11\x55','\x4E\x12\x55','\x4E\x13\x55','\x4E\x14\x55','\x4E\x15\x55','\x4E\x16\x55','\x4E\x17\x55','\x4E\x18\x55','\x4E\x19\x55','\x4E\x1A\x55','\x4E\x1B\x55','\x4E\x1B\x55','\x4E\x1B\x55']
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

        def shouldDim(self, event):
            doDim = 0
            if self.isMovie and self.dimForMovies == 'true':
                doDim = 1
            if self.isEpisode and self.dimForTv == 'true':
                doDim = 1
            return doDim

        def dim(self, event):
            self.isMovie = xbmc.getCondVisibility('VideoPlayer.Content(movies)')
            self.isEpisode = xbmc.getCondVisibility('VideoPlayer.Content(episodes)')
            if self.shouldDim(self):
                for message in self.dimCommands:
                    self.sendUdpCommand(self, message)

        def brighten(self, event):
            if self.shouldDim(self):
                self.isMovie = 0
                self.isEpisode = 0
                for message in self.brightenCommands:
                    self.sendUdpCommand(self, message)

        def sendUdpCommand(self, event, message):
            UDP_IP = self.ip
            UDP_PORT = self.port
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
            sock.sendto(message, (UDP_IP, UDP_PORT))
            time.sleep(self.commandInterval)

player=MyPlayer()

VIDEO = 0

while(1):
    if xbmc.Player().isPlaying():
      if xbmc.Player().isPlayingVideo():
        VIDEO = 1

      else:
        VIDEO = 0

    xbmc.sleep(1000)