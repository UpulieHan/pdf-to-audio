import pyttsx3
import PyPDF2
from lyrics import boyfriend_lyrics

book = open('Michio-Kaku-Hyperspace(1994).pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book, strict=False)

#to know the amount of pages
pages = pdfReader.numPages
# print(pages)

speaker = pyttsx3.init()

voices = speaker.getProperty('voices')
#changing index, changes voices. 0,1,2 available
speaker.setProperty('voice', voices[0].id)

speaker.say(boyfriend_lyrics)

for num in range(5,pages):
    #which number to read from(4th page alas 3)
    page = pdfReader.getPage(3)
    text = page.extractText()
    # print(text)

    # speaker.say(text)
    speaker.runAndWait()