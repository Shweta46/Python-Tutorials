import random #module used here which has many functions
import sklearn
#master python and see the functions of the module by searching it in google
random_number = random.randint(0,5) #accesing the module and then the function inside it
#will generate a random number between 0 and 5
print(random_number)

rand = random.random() #generates a random number, not integer, between 0 to 1
print(rand)
#if we want to generate a random number between 0 and 100 then
rand2 = random.random()*100 #multiply the function with 100
print(rand2)

list1 = ["Star Plus", "DD1", "NDTV", "Cartoon Network"]
choice = random.choice(list1)
print(choice) #prints a random choice from the list we have chosen above
#sort of life playing ludo, anything can come from 1 to 6 in the dice
list2 = ["1", "2", "3", "4","5", "6"] #ludo dice
choice1 = random.choice(list2)
print(choice1)

#task: pick two modules and use two functions of those modules to print something

#Plays the video in a mediaplayer for a set amount of time
# import time
# import vlc
# import pafy
#
# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" #stored youtube link in url variable
# video = pafy.new(url) #creates pafy object of the video
# best = video.getbest() #gets the best stream
# playurl = best.url
# instance = vlc.Instance()
# player = instance.media_player_new()
# media = instance.media_new(playurl)
# media.get_mrl()
# player.set_media(media)
# player.play()
# time.sleep(10)

#OR
# this directly plays the youtube video in youtube
import pywhatkit as kit
kit.playonyt("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
