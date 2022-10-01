
# importing required modules 
import PyPDF2
from gtts import gTTS
import random

from util_cleaner.cleaner import cleanaer

random.seed(5)
def texttosppech(fileloc):
# creating a pdf file object 
	pdfFileObj = open(fileloc, 'rb') 
	rap = fileloc   
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
		k+=1
	
	# closing the pdf file object 

	pdfFileObj.close()
	try:
		# tts = gTTS(txt)
		# ran = random.random()*0
		##nam =rap+str(ran)+'0.mp3'
		# nam =rap+'0.mp3'
		# tts.save(nam)
		restxt = cleanaer(txt)
		print(restxt)
		return restxt
	except Exception as e:
         print(e)
         return e