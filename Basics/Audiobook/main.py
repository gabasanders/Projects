import pyttsx3
import PyPDF2
from tkinter.filedialog import *
from translate import functranslate


# Selects the desired PDF
book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)


#Set the Voice's Properties
player = pyttsx3.init()

    #get the properties
voices = player.getProperty('voices')
rate = player.getProperty('rate')

    #set the properties
player.setProperty('voice',voices[2].id)
player.setProperty('rate', 150)

#Set the language to be translated
language = 'en'



for num in range(0, pages):

    page = pdfreader.pages[num]
    text = page.extract_text()

    translated = functranslate(text,language)
    
    player.say(translated)
    player.runAndWait()


