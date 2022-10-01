import PyPDF2
import random
import pyttsx3
engine = pyttsx3.init() # object creation
# from util_cleaner.cleaner import cleanaer
import sys
random.seed(5)
# def texttosppech(fileloc):
# creating a pdf file object 
pdfFileObj = open(sys.argv[1], 'rb') 
rap = sys.argv[1]   
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
dirt = ["https://mp4directs.com"]
# printing number of pages in pdf file 
k =0
txt=""
pgno = pdfReader.numPages
while(k< pgno):
	# creating a page object 
	pageObj = pdfReader.getPage(k) 
	# extracting text from page 
	txt+=pageObj.extractText()
	engine.save_to_file(pageObj.extractText(), 'test.mp3')
	
	k+=1

	# closing the pdf file object 
# print(txt)
pdfFileObj.close()
	# try:
		
engine.runAndWait()
# engine.stop()
print("comlete")
  	# return "te"
	# except Exception as e:
        #  print(e)
        #  return e