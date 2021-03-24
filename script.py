#from __init__ import app, db, migrate
from flask import Flask, redirect,session, render_template, request, flash, send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError, OperationalError
from werkzeug.utils import secure_filename
#from sqlalchemy_imageattach.entity import Image, image_attachment
#import models
from settinhs import MASTER_KEY
import secrets
import os
import base64
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///password_manager.sqlite3 '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)
migrate = Migrate(app, db)
migrate.init_app(app, db)

class Password(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  res_name = db.Column(db.String(15), unique=True, nullable=False)
  res_password = db.Column(db.String(15), unique=False, nullable=False)
  #master_key = db.Column(db.String(10), unique=False)
  img = db.Column(db.String(20), unique=False, nullable=False, default='lgbt_steam.jpg')

  def __init__(self, res_name, res_password):
    self.res_name = res_name
    self.res_password = res_password
    
# class Image(db.Model):

#   def __init__(self, img):
#     self.img = img

# @app.route('/master')
# def master():
#   master_key = True
#   return render_template('masterkey.html')

@app.route('/')
def main():
  #return render_template('home.html', data=data)
  #for i in Password.query.all():
  #  db.session.delete(i)
  #  print(Password.query.all())
  #  db.session.commit()
  
  return render_template('home.html', title = 'Sweat Home Page')

UPLOAD_FOLDER = r'C:\Users\user1\Documents\MyScripts\PythonScripts\pass_manager\static\images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#print(UPLOAD_FOLDER,app.config['UPLOAD_FOLDER'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/view_all', methods=['POST', 'GET'])
def view_all():
  data = Password.query.all()
      # if user does not select file, browser also
      # submit an empty part without filename
  #flash('qrqr')
  title = 'View passwords'
  if request.method=='POST':
    file = request.files['resourse__img']
    crutch = request.form['crutch']
    if file and allowed_file(file.filename):

      #image_name = secure_filename(file.filename) ????
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
      print(crutch, file,file.filename)#image_name, 
      passw = Password.query.filter_by(id=int(crutch)).one()
      passw.img = file.filename
      db.session.commit()
      return render_template('all_passwords.html', data=data, title=title)#
      #with open(file, 'rb') as img:
      #  image = base64.b64encode(img).decode('ascii')
      #  passw.img = image.read()
      #  #Password.query.filter_by(id=int(crutch))#.update(img=file.read())
      #  db.session.commit()
      

      #filename = secure_filename(file.filename)
      #print(crutch)
      #img = Image(img=file.read())  
      #return render_template('all_passwords.html', data=data, title=title)

      #return redirect(url_for('redirectqe'))
      #return redirect(url_for('uploaded_file', filename=filename))
    #print(image)

  return render_template('all_passwords.html', data=data, title=title)

@app.route('/view_all/info_passwordid=<id>')
def password_info(id):
  # master_key_validation = False

  # if not master_key_validation:
  #   master_key_validation = True
  #   return render_template('masterkey.html', url=f'/view_all/info_passwordid={id}')

  info = Password.query.filter_by(id=int(id)).one()
  return render_template('pass.html', info=info)
@app.route("/clear")
def clear():
  data = Password.query.all()
  #print(len(data))
  for i in data:
    db.session.delete(i)
    db.session.commit()  
    #print(len(data))
    #print(data)
  
  db.session.commit()  
  
  return redirect(url_for('main'))

@app.route("/generator", methods=['POST', 'GET'])
def generator():
  tittle = 'PG'
  if request.method=='POST':
    try:
      iteration = request.form['generator__item-input']
      if int(iteration) + len(Password.query.all()) <= 12:
        for n in range(int(iteration)):
          password = secrets.token_urlsafe(10)
          resourse = secrets.token_urlsafe(10)
          new = Password(res_name=resourse, res_password=password)
          db.session.add(new)  
          db.session.commit() 
          #print(password)
            #print(data)
        #print(len(Password.query.all()))


        #print(len(Password.query.all()))
        
    except ValueError:
      return redirect(url_for('generator'))

    else:      
      return redirect(url_for('generator'))
    return redirect(url_for('generator'))
    
  return render_template('generator.html', title=tittle)

@app.route('/remove_password_id=<id>', methods=['POST', 'GET'])
def removing_password(id):

  #if request.method=='POST':
    #print(Password.query.all())
  password = Password.query.filter_by(id=id).one()
  db.session.delete(password)
  db.session.commit()

  return redirect(url_for('view_all'))
  #  return redirect(url_for('view_all'))
  #else:
  #  return render_template('remove_mod.html')

@app.route('/add_pass', methods=['POST', 'GET'])
def add_password():
  title = 'Add new password'
  if request.method == 'POST':
    resource = request.form['input__res']
    password = request.form['input__pass']
    if 0 < len(resource) < 11 and 0 < len(password) < 11:
      try:
        passw = Password(res_name=resource, res_password=password)
        if len(Password.query.all()) < 10:
            db.session.add(passw)
            db.session.commit()
            return redirect(url_for('main'))
        
        else: 
          return render_template('password_adding.html', title=title)  
          #db.commit()
          
          #password=request.args.get('input__password')
          #print(Password.query.all())
          #data = Password.query.all()
      except (IntegrityError):
      #  flash('input unique res and pass')
        #pass
        #flash('ты конченный? норм название запиши уникальное')
        #print('errororor')
        return render_template('password_adding.html', title=title)  

    else:
      return render_template('password_adding.html', title=title)  
      
  else: 
    #resource=request.args.get('input__res') 
    #thread.start_new_thread(add_password, (request))

    return render_template('password_adding.html', title=title)

if __name__=="__main__":

  # app.config['SESSION_TYPE'] = 'filesystem'

  # session.init_app(app)
  
  db.create_all()
  db.session.commit()
  app.run(debug=True)
