import pywhatkit as pw
import random

txt= input("Enter Text : ")
print("Please Wait..")

pw.text_to_handwriting(txt,str(random.randint(0,1000000000000)) + ".png",[0,0,138])  #text_to_handwritting is a fun used to convert text to handwritting. [0,0,138]- color code

print("End..")
