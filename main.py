import pyttsx3
import PyPDF2

book = open('new.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print(pages)

friend = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.pages[num] 
    text = page.extract_text()  
    friend.say(text)
    friend.runAndWait()
