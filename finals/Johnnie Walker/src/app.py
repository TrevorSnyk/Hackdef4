# -*- coding: utf-8 -*-
#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for, request, make_response,abort, send_from_directory
from datetime import datetime, timedelta
import uuid
import jwt
import pyotp

JWT_SECRET = 'qwerty'
JWT_ALGORITHM = 'HS256'
DOWNLOAD_DIRECTORY = "resources/"
flag = 'hackdef{Dyn4m1c_4n4LYSYS_4LW4S_F1RST}'

app = Flask(__name__, template_folder="templates", static_url_path='/static')

def generate_token():
	utcnow = datetime.utcnow() + timedelta(seconds=5)
	duration = timedelta(minutes=20)
	payload = {'user': 'rutilosoberano','download':'False','iat':utcnow, 'exp': utcnow + duration}
	token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
	return token

def verify_otp(otpcode):
	totp = pyotp.TOTP('CG6HLIXEOJBHPUDPL7TGLHKA636V6B2U')
	return totp.verify(otpcode)

def verify_token(token):
	try:
		payload = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
		return True
	except (jwt.DecodeError, jwt.ExpiredSignatureError):
		return False

@app.route('/',methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
    	if request.form['id'] == '983348933400987' and verify_otp(request.form['captcha']):
    		session_uuid = str(uuid.uuid1())
    		response = make_response(redirect("/qrcode/"+ session_uuid))
    		response.set_cookie("token", generate_token())
    		return response
    	else:
    		error = 'Datos Incorrectos. Intenta nuevamente'
    return render_template('login.html', error=error)

@app.route('/qrcode/<uuid>')
def qrcode(uuid):
    if "token" not in request.cookies:
    	response = make_response(redirect("/"))
    else:
    	jwt_token = request.cookies.get('token', None)
    	if verify_token(jwt_token):
    		response = render_template("index.html",flag=flag)
    	else:
    		response = make_response(redirect("/"))
    return response

@app.route('/resources/download/<filename>')
def get_resources(filename):
	if "Referer" in request.headers:
		if "token" not in request.cookies:
			error = "Acceso no authorizado (code:401)"
			return render_template('index.html', error=error, flag=flag)
		else:
			jwt_token = request.cookies.get('token', None)
			try:
				payload = jwt.decode(jwt_token, JWT_SECRET, JWT_ALGORITHM)
				if payload['download'].lower() == 'true':
					return send_from_directory(DOWNLOAD_DIRECTORY, filename, as_attachment=True)
				else:
					error = "No tienes permiso para descargar el archivo (code:403)"
					return render_template('index.html', error=error, flag=flag)
			except jwt.DecodeError:
				error = u"Error al decodificar el token - Posiblemente necesites el secret para generar un token válido (code:400)"
				return render_template('index.html', error=error, flag=flag)
			except jwt.ExpiredSignatureError:
				error = u"Error al decodificar el token - El token expiró (code:400)"
				return  make_response(redirect("/logout"))
			except:
				abort(404)
	else:
		if "token" in request.cookies:
			jwt_token = request.cookies.get('token', None)
			response = make_response(redirect("/"))
			response.set_cookie("token",jwt_token,max_age=0)
			return response
		else:
			response = make_response(redirect("/"))
			return response

@app.route('/logout')
def bye():
	if "token" in request.cookies:
		jwt_token = request.cookies.get('token', None)
		response = make_response(redirect("/"))
		response.set_cookie("token",jwt_token,max_age=0)
		return response
	else:
		response = make_response(redirect("/"))
		return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3120)    
