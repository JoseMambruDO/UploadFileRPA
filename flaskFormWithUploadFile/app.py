from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename

import os

UPLOAD_FOLDER = r"c:\tmp\uploads"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload',methods = ['POST', 'GET'])
@app.route('/',methods = ['POST', 'GET'])
def upload():
   if request.method == 'POST':
      user = request.form['name']
      last_name  = request.form['last_name']

      file = request.files['file']

      if file.filename == '':
          flash('No selected file')
          return redirect(request.url)
      if file and allowed_file(file.filename):
          filename = secure_filename(file.filename)
          file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
          flash('File uploaded successfully')
      else:
          flash('Could not save the file.')    
      return render_template('uploadform.html')
   else:
      user = request.args.get('name')
      return render_template('uploadform.html')

if __name__ == "__main__":
    app.run()