# from flask import Flask, render_template, request
# from pip install -U Werkzeug import secure_filename
from contextlib import nullcontext
import os 
# app = Flask(__name__)

# @app.route('/upload')
# def upload_file():
#    return render_template('upload.html')
	
# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'
		
# if __name__ == '__main__':
#    app.run(debug = True)

from tts.new import texttosppech
from flask import *  
app = Flask(__name__)  
# app.config[f'{os.path.realpath(os.path.dirname(__file__))}'+'/upload']

@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':
        statuss = "none"
        dir = os.path.realpath(os.path.dirname(__file__))
        print(dir)
        f = request.files['file']  
        # f.save(f.filename)  
        f.save(u'./upload/{}'.format(f.filename))
        whole= dir+'/upload/'+f.filename
        # retrun whole
        statuss  = texttosppech(whole)
        return render_template("success.html", name = statuss)
  
if __name__ == '__main__':  
    app.run(debug = True)  