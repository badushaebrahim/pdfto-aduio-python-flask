# from flask import Flask, render_template, request
# from pip install -U Werkzeug import secure_filename
from contextlib import nullcontext
import os 

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
        try:
            return send_file(str(statuss), 'conv.mp3')
        except Exception as e:
         return str(e)
  
if __name__ == '__main__':  
    app.run(debug = True)  