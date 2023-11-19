from tkinter import *
import random
from musicPlayer import musicPlayer

player = musicPlayer()
player.playlist = [r""]
random.shuffle(player.playlist)

tkinter = Tk()
tkinter.title("mp3 player")

tkinter.mainloop()

next = Button(tkinter, text="next", padx=40, pady=20, command=player.next)
previous = Button(tkinter, text="previous", padx=40, pady=20, command=player.previous)
toggle_play = Button(tkinter, text="toggle play", padx=40, pady=20, command=player.toggle_play)

previous.grid(row=0, column=0)
toggle_play.grid(row=0, column=1)
next.grid(row=0, row=2)

tkinter.mainloop()
