from flask import Flask, session, redirect, render_template, request, url_for
from flask_session import Session
from collections import deque
import os, shelve

app = Flask(__name__)

@app.route('/')
def index_session():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        session['urls'] = 'index.html'
        return render_template('logged.html')

@app.route('/comprobarLogin', methods=['GET', 'POST'])
def aux_login():
    s = shelve.open('BD.db', writeback=True)
    user = request.form['username']
    passw = request.form['password']
    if ((len(request.form['username']) == 0) or (len(request.form['password']) == 0)):
        s.close()
        return render_template('index.html', camposVacios=True)
    elif user in s:
        if passw == s[user]:
            session['logged_in'] = True
            session['username'] = request.form['username']
    else:
        return render_template('index.html', error=True)
    s.close()

    return redirect('/')

@app.route('/loginSession', methods=['GET', 'POST'])
def login():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return redirect('logged.html')

@app.route('/comprobarRegistro', methods=['GET', 'POST'])
def aux_registro():
    s = shelve.open('BD.db', writeback=True)
    if not session.get('logged_in'):
        if (request.form['username'] in s):
            s.close()
            return render_template('registro.html')
        elif ((len(request.form['username']) == 0) or (len(request.form['password']) == 0)):
            s.close()
            return render_template('registro.html', camposVacios=True)
        else:
            user = request.form['username']
            passw = request.form['password']
            s[user] = passw
            s.close()
            return render_template('index.html')
    else:
        s.close()
        return redirect('/')

@app.route('/registroSession', methods=["GET","POST"])
def registro():
    if not session.get('logged_in'):
        return render_template('registro.html')
    else:
        return redirect('/')

@app.route('/actualizarRegistro', methods=['POST'])
def actRegistro():
    s = shelve.open('BD.db', writeback=True)
    user = session['username']
    passw = request.form['password']
    if(len(passw) > 0):
        s[user] = passw
        return render_template('perfil.html', actDatos=True)
    else:
        return render_template('perfil.html', camposVacios=True)
    s.close()

#función para activar la ejecución de una función al final de una solicitud
@app.after_request
def history(response):
    if "username" in session and request.method == "GET" and response.mimetype == "text/html":
        try:                                                #Hay que añadir el tipo text/html porque si no me guarda todo tipo de peticiones.
            hist = deque(session["history"],3)
            hist.appendleft(request.path)
            session["history"] = list(hist)
        except:
            session["history"] = [request.path]
    return response

@app.route('/logout', methods=["GET","POST"])
def logout():
    session['logged_in'] = False
    session.clear()
    return render_template('index.html', sesionCerrada=True)

@app.route('/registro')
def registre():
    return render_template('registro.html')

@app.route('/profile')
def profile():
    session['urls'] = 'perfil.html'
    return render_template('perfil.html')

@app.route('/contacto')
def contact():
    session['urls'] = 'contacto.html'
    return render_template('contacto.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('http_404.html')

if __name__ == "__main__":
    app.secret_key = '123r1ihbqswpci·$%&·qwd'
    app.run(host="0.0.0.0", debug=True)
