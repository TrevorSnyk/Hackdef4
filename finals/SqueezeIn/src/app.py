# -*- coding: utf-8 -*-
#!/usr/bin/python3
from flask import Flask, render_template, make_response, request, redirect, abort, redirect
from datetime import datetime, timedelta
from threading import Thread
from functools import wraps
from report import *
import jwt

app = Flask(__name__, template_folder="templates", static_url_path='/static')

JWT_ALGORITHM = 'HS256'
JWT_SECRET = "s7Ln2VL@etMV8Mv!!"
PWD = 'abb2XEAt8LNSPLQ'
FLAG = "hackdef{csp_4nd_*.gO0gl3.c0m_d0n7_90_w3Ll}"

def generate_token(username):
    utcnow = datetime.utcnow() + timedelta(seconds=-5)
    duration = timedelta(minutes=20)
    payload = {'user': username,'permissions':'all','iat':utcnow, 'exp': utcnow + duration}
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token

def get_csp():
    return "; ".join(
        ["script-src 'self' *.google.com fonts.googleapis.com *.bootstrapcdn.com", "connect-src " + "*"]
    )

def csp(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        resp = make_response(f(*args, **kwargs))
        resp.headers["Content-Security-Policy"] = get_csp()
        return resp

    return decorated_func

def verify_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        return True
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        return False

modules = [
    {
        "id": "BJ003CDMX",
        "alcaldia": "Benito Juarez",
        "dir": "Viaducto #7666. Col. Portales Nte.",
        "tel": "(55) 55443344",
        "mail": "bj003cdmx@mail.com",
        "horario": "L-V: 9:00 HRS - 17:00 HRS"
    },
    {
        "id": "VC005CDMX",
        "alcaldia": "Venustiano Carranza",
        "dir": "Av. M. Aleman #10. Col. Camarones Sur.",
        "tel": "(55) 57863646",
        "mail": "vc005cdmx@mail.com",
        "horario": "L-V: 9:00 HRS - 17:00 HRS"
    },
    {
        "id": "GAM009CDMX",
        "alcaldia": "Gustavo A. Madero",
        "dir": "Av. Instituto Politecnico Nacional s/n. Residencial Zacatenco",
        "tel": "(55) 57098765",
        "mail": "gam009cdmx@mail.com",
        "horario": "L-V: 10:00 HRS - 18:00 HRS"
    },
    {
        "id": "COY010CDMX",
        "alcaldia": "Coyoacan",
        "dir": "Av. Santa Ana #100. Col. San Fco. Culhuacan",
        "tel": "(55) 55231234",
        "mail": "coy010cdmx@mail.com",
        "horario": "L-V: 09:00 HRS - 16:00 HRS"
    },
    {
        "id": "IZ002CDMX",
        "alcaldia": "Iztacalco",
        "dir": "Av. Té #250. Col. Granjas México",
        "tel": "(55) 55332211",
        "mail": "iz002cdmx@mail.com",
        "horario": "L-V: 09:00 HRS - 16:00 HRS"
    }
]

@app.route('/', methods=['GET'])
def index():
    return render_template('admin.html')

@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')

@app.route('/search')
@csp
def search():
    param = request.args['param']
    for i in modules:
        if i['alcaldia'].lower() == param.lower():
            return render_template('modules.html', modulos=i)
    return render_template('modules.html', error=param)


@app.route('/modules')
def srvmodules():
    response = render_template("modules.html")
    return response

@app.route('/bugbountyprogram')
def bounties():
    response = render_template("bounties.html")
    return response

@app.route('/report', methods=['POST'])
def report():
    msg = "¡Gracias por contribuir a la seguridad de nuestro sitio!"
    url = request.form['url']
    if same_site(url):
        if 'param' in url:
            thread = Thread(target=visitor, args=(url,))
            thread.start()
    response = render_template("bounties.html", msg=msg)
    return response

@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.form['username'] != 'admin' or request.form['password'] != PWD:
        error = 'Usuario o Contraseña Incorrectos'
        return render_template("admin.html", error=error)
    else:
        return redirect("http://elecciones.hack-defender.mx:8000/polls/candidato/", code=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3142)