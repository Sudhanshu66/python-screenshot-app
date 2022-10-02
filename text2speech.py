#library used google text to speech for tha we have to install a package

import gtts 
import playsound

text =input("enter your word: ")  #text we used can pe pre defined or user defined. input keyword is used to take input-text from the user

sound = gtts.gTTS(text, lang="en") # when text in input by the user then it shoud be convert to text. for this we make a sound variable. we can use differnt lang also.

#now to play the text speech we use another lib - play sound. 
sound.save("speech2.mp3")   # we have to save the file in mp3 form because it is audio form

playsound.playsound("speech2.mp3") #plays the sound of your speech