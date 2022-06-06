#----------------HEALTHY PROGRAMMER------------------------

#make the programmer drink 3-4 litres of water in quantity 15-18 ml at once
#every 30 min, do an eye exercise
#every 45 min, do a physical activity
#make a program to remind the programmer to perform the activities listed above
# the programmer sits between 9-5pm for programming
#
# Water - water.mp3 play this to make this drink (3.5 litres)
# - The user has to type an input "Drank"- Press enter - generate a log containing the time stamp for this input
#
# Eyes - eyes.mp3 - this will play in every 30min
# - The user has to input "Eye exercise Done" to make the music stop - this should reset the timer - Generate log for this too
#
# Physical activity - physical.mp3 - Play it every 45min
# - Make the user type "Exercise Done" - Reset the timer - Generate a log for this
#
# Rule:
# Use Pygame module to play audio
#
# Challenges:
# Timings can clash, if it does then wait for the programs the first program log to finish and then the other program to start without missing a beat

from pygame import mixer

while True:
    mixer.init()
    # Load audio file
    mixer.music.load('eye.mp3')
    # Set preferred volume
    mixer.music.set_volume(1.0)

    print("Enter - Eye exercise done - to stop the audio")
    mixer.music.play()
    userInput = input(" ")
    if userInput == 'Done':
        mixer.music.stop()
        print("music is stopped....")
        break
    else:
        print("Please enter a valid input")





