import time
from playsound import playsound

print("yo wassup")
time.sleep(0.5)
print("Welcome to the Groove Playlist, ENJOY!!!")
time.sleep(2.5)
print("Songs avalable: ")
time.sleep(1)
print("1. Bread")
time.sleep(1)
print("2. Rerun")
time.sleep(1)
print("3. Magic")
time.sleep(1)

choice = int(input("Choose the song you want to play: "))

if(choice == 1):
    print("Playing Bread")
    playsound("Bread.wav")
    choice = 2
    print("Now playing Rerun")

if(choice == 2):
    print("Playing Rerun by Neo Nomen")
    playsound("Rerun.mp3")
    choice = 3
    print("Now playing Magic")

if(choice == 3):
    print("Playing Magic by Rudy Mancuso")
    playsound("Magic.mp3")

if(choice >= 4):
    print("Error 404, not found")

