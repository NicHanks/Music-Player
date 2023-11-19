
import pygame
import time
import random 

pygame.init()
pygame.mixer.init()

class musicPlayer :
    pygame.init()
    pygame.mixer.init()
    def __init__(self) :
        self.playlist = []
        self.index = 0
        self.status = ""
        self._PAUSED = "paused"
        self._PLAYING = "playing"
        self._UNLOADED = ""
        self.status = self._UNLOADED



    def _load(self, filepath) :
        pygame.mixer.music.load(self.playlist[self.index])
        self.status = self._PAUSED

        def _play(self) :
            pygame.mixer.music.play()
            self.status = self._PLAYING
        def _pause(self) :
            pygame.mixer.music.pause()
            self.status = self._PLAYING
        def _unpause(self) :
            pygame.mixer.music.unpause()
            self.status = self._PLAYING
        def _stop(self) :
            pygame.mixer.music.stop()
            self.status = SELF._unloaded

        def next(self) :
            self.index += 1
            self._load()
            self._play()
            
        def previous(self) :
            pass

        def toggle_play(self) :
            if self.status == self._PAUSED :
                self._UNPAUSE
            elif self.status == self._PLAYING :
                self._UNPAUSE
            else :
                self._load()
                self._play()

player = musicPlayer()
player.playlist = ["C:\Users\nicha\OneDrive\Documents\computerprogramming\Connecting to Music\I Got a Stick Feat James Gavins.mp3", r]
random.shuffle(player.playlist)

player._load()
player._play()
time.sleep(5)
player.next()
time.sleep(5)
player.next()
time.sleep(5)
player.previous()
time.sleep(300) 


pygame.mixer.music.load("C:\Users\nicha\OneDrive\Documents\computerprogramming\Connecting to Music\I Got a Stick Feat James Gavins.mp3")
pygame.mixer.music.play()
time.sleep(3)
pygame.mixer.music.pause()
time.sleep(3)
pygame.mixer.music.unpause()
time.sleep(3)
pygame.mixer.music.stop()
time.sleep(150)

player.toggle_play()
time.sleep(7)
player.toggle_play()
time.sleep(3)
player.next()
time.sleep(7)
player.toggle_play()
time.sleep(3)
player.previous()
time.sleep(500)