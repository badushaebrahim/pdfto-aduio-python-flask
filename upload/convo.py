# importing required modules 
import PyPDF2
from gtts import gTTS
import random

import sys

random.seed(5)

# creating a pdf file object 
pdfFileObj = open(sys.argv[1], 'rb') 
rap = sys.argv[1]   
	# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

	# printing number of pages in pdf file 
k =0
txt=""
pgno = pdfReader.numPages
while(k< pgno):
        pageObj = pdfReader.getPage(k)
        txt+=pageObj.extractText()
        k+=1
pdfFileObj.close()	
	# closing the pdf file object 
fs = open("demofile2.txt", "w")
fs.write(txt)
fs.close()

