from flask import Flask, jsonify, request, render_template, redirect, url_for, flash, session
from flaskext.mysql import MySQL
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
from flask_mail import Mail, Message
import smtplib


app = Flask(__name__)
CORS(app)

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'landowolf10'
app.config['MYSQL_DATABASE_DB'] = 'minitourist'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['UPLOAD_FOLDER'] = './static/img'
mysql.init_app(app)

app.secret_key = 'mysecretkey'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'minitouristcards@gmail.com'
app.config['MAIL_PASSWORD'] = 'MiniTouristCards2020'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
clientImage = ''

@app.route('/')
def index():
    zihuatanejo_parques = [file for file in os.listdir('./static/img/Zihuatanejo/Frente/parques/') if file.endswith('.jpg')]
    zihuatanejo_restaurantes = [file for file in os.listdir('./static/img/Zihuatanejo/Frente/restaurantes/') if file.endswith('.jpg')]
    zihuatanejo_lugares = [file for file in os.listdir('./static/img/Zihuatanejo/Frente/lugares/') if file.endswith('.jpg')]
    zihuatanejo_tiendas = [file for file in os.listdir('./static/img/Zihuatanejo/Frente/tiendas/') if file.endswith('.jpg')]
    zihuatanejo_servicios = [file for file in os.listdir('./static/img/Zihuatanejo/Frente/servicios/') if file.endswith('.jpg')]

    zihuatanejo_parques_atras = [file for file in os.listdir('./static/img/Zihuatanejo/Atras/parques/') if file.endswith('.jpg')]
    zihuatanejo_restaurantes_atras = [file for file in os.listdir('./static/img/Zihuatanejo/Atras/restaurantes/') if file.endswith('.jpg')]
    zihuatanejo_lugares_atras = [file for file in os.listdir('./static/img/Zihuatanejo/Atras/lugares/') if file.endswith('.jpg')]
    zihuatanejo_tiendas_atras = [file for file in os.listdir('./static/img/Zihuatanejo/Atras/tiendas/') if file.endswith('.jpg')]
    zihuatanejo_servicios_atras = [file for file in os.listdir('./static/img/Zihuatanejo/Atras/servicios/') if file.endswith('.jpg')]

    print('zihuatanejo_lugares_atras: ' + str(zihuatanejo_lugares_atras))

    acapulco_parques = [file for file in os.listdir('./static/img/Acapulco/Frente/parques/') if file.endswith('.jpg')]
    acapulco_restaurantes = [file for file in os.listdir('./static/img/Acapulco/Frente/restaurantes/') if file.endswith('.jpg')]
    acapulco_lugares = [file for file in os.listdir('./static/img/Acapulco/Frente/lugares/') if file.endswith('.jpg')]
    acapulco_tiendas = [file for file in os.listdir('./static/img/Acapulco/Frente/tiendas/') if file.endswith('.jpg')]
    acapulco_servicios = [file for file in os.listdir('./static/img/Acapulco/Frente/servicios/') if file.endswith('.jpg')]

    sessionInitialized = False
    tipoUsuario = ''

    if 'user' in session:
        sessionInitialized = True
    else:
        sessionInitialized = False

    print('Session: ' + str(sessionInitialized))

    return render_template('index.html', zihuatanejo_parques = zihuatanejo_parques, zihuatanejo_restaurantes = zihuatanejo_restaurantes,
        zihuatanejo_lugares = zihuatanejo_lugares, zihuatanejo_tiendas = zihuatanejo_tiendas, zihuatanejo_servicios = zihuatanejo_servicios,
        acapulco_parques = acapulco_parques, acapulco_restaurantes = acapulco_restaurantes, acapulco_lugares = acapulco_lugares,
        acapulco_tiendas = acapulco_tiendas, acapulco_servicios = acapulco_servicios, logged_in = sessionInitialized)

@app.route('/quienes')
def quienesSomos():
    sessionInitialized = False

    if 'user' in session:
        sessionInitialized = True
    else:
        sessionInitialized = False

    print('Session: ' + str(sessionInitialized))

    return render_template('quienes_somos.html', logged_in = sessionInitialized)

@app.route('/mt')
def queSonLasMTC():
    sessionInitialized = False

    if 'user' in session:
        sessionInitialized = True
    else:
        sessionInitialized = False

    print('Session: ' + str(sessionInitialized))

    return render_template('que_son_las_mtc.html', logged_in = sessionInitialized)

@app.route('/contacto')
def contacto():
    sessionInitialized = False

    if 'user' in session:
        sessionInitialized = True
    else:
        sessionInitialized = False

    print('Session: ' + str(sessionInitialized))

    return render_template('contacto.html', logged_in = sessionInitialized)

@app.route('/login')
def login():
    sessionInitialized = False

    if 'user' in session:
        sessionInitialized = True
    else:
        sessionInitialized = False

    print('Session: ' + str(sessionInitialized))

    return render_template('login.html', logged_in = sessionInitialized)

@app.route('/clients')
def clientForm():
    getAllClients()

    sessionInitialized = False

    if 'user' in session:
        sessionInitialized = True
    else:
        sessionInitialized = False

    print('Session: ' + str(sessionInitialized))

    return render_template('add_client.html', client_data = getAllClients(), logged_in = sessionInitialized)

@app.route('/add_clients', methods=['POST'])
def insertClient():
    try:
        nombre = request.form['name']
        direccion = request.form['direction']
        telefono = request.form['phone']
        email = request.form['email']
        psw = request.form['pass']
        location = request.form['location']
        card_type = request.form['card-type']
        front_image = request.files['front_image']
        back_image = request.files['back_image']

        fileNameFront = secure_filename(front_image.filename)
        fileNameBack = secure_filename(back_image.filename)

        if location == 'Zihuatanejo':             
            if card_type == 'lugares':
                front_image.save(os.path.join('./static/img/Zihuatanejo/Frente/lugares', fileNameFront))
                back_image.save(os.path.join('./static/img/Zihuatanejo/Atras/lugares', fileNameBack))
                os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/lugares/' + str(fileNameBack),
                '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/lugares/' + str(fileNameFront))
            elif card_type == 'parques':
                front_image.save(os.path.join('./static/img/Zihuatanejo/Frente/parques', fileNameFront))
                back_image.save(os.path.join('./static/img/Zihuatanejo/Atras/parques', fileNameBack))
                os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/parques/' + str(fileNameBack),
                '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/parques/' + str(fileNameFront))
            elif card_type == 'restaurantes':
                front_image.save(os.path.join('./static/img/Zihuatanejo/Frente/restaurantes', fileNameFront))
                back_image.save(os.path.join('./static/img/Zihuatanejo/Atras/restaurantes', fileNameBack))
                os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/restaurantes/' + str(fileNameBack),
                '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/restaurantes/' + str(fileNameFront))
            elif card_type == 'servicios':
                front_image.save(os.path.join('./static/img/Zihuatanejo/Frente/servicios', fileNameFront))
                back_image.save(os.path.join('./static/img/Zihuatanejo/Atras/servicios', fileNameBack))
                os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/servicios/' + str(fileNameBack),
                '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/servicios/' + str(fileNameFront))
            elif card_type == 'tiendas':
                front_image.save(os.path.join('./static/img/Zihuatanejo/Frente/tiendas', fileNameFront))
                back_image.save(os.path.join('./static/img/Zihuatanejo/Atras/tiendas', fileNameBack))
                os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/tiendas/' + str(fileNameBack),
                '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/tiendas/' + str(fileNameFront))
        elif location == 'Acapulco':
            if card_type == 'lugares':
                front_image.save(os.path.join('./static/img/Acapulco/Frente/lugares', fileNameFront))
                back_image.save(os.path.join('./static/img/Acapulco/Atras/lugares', fileNameBack))
                os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/lugares/' + str(fileNameBack),
                '../MinitouristCardsFinal/static/img/Acapulco/Atras/lugares/' + str(fileNameFront))
            elif card_type == 'parques':
                front_image.save(os.path.join('./static/img/Acapulco/Frente/parques', fileNameFront))
                back_image.save(os.path.join('./static/img/Acapulco/Atras/parques', fileNameBack))
                os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/parques/' + str(fileNameBack),
                '../MinitouristCardsFinal/static/img/Acapulco/Atras/parques/' + str(fileNameFront))
            elif card_type == 'restaurantes':
                front_image.save(os.path.join('./static/img/Acapulco/Frente/restaurantes', fileNameFront))
                back_image.save(os.path.join('./static/img/Acapulco/Atras/restaurantes', fileNameBack))
                os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/restaurantes/' + str(fileNameBack),
                '../MinitouristCardsFinal/static/img/Acapulco/Atras/restaurantes/' + str(fileNameFront))
            elif card_type == 'servicios':
                front_image.save(os.path.join('./static/img/Acapulco/Frente/servicios', fileNameFront))
                back_image.save(os.path.join('./static/img/Acapulco/Atras/servicios', fileNameBack))
                os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/servicios/' + str(fileNameBack),
                '../MinitouristCardsFinal/static/img/Acapulco/Atras/servicios/' + str(fileNameFront))
            elif card_type == 'tiendas':
                front_image.save(os.path.join('./static/img/Acapulco/Frente/tiendas', fileNameFront))
                back_image.save(os.path.join('./static/img/Acapulco/Atras/tiendas', fileNameBack))
                os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/tiendas/' + str(fileNameBack),
                '../MinitouristCardsFinal/static/img/Acapulco/Atras/tiendas/' + str(fileNameFront))

        print(nombre)
        print(direccion)
        print(telefono)
        print(email)
        print(location)
        print(card_type)
        print("IMAGE: " + fileNameFront)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spInsertUser', (nombre, direccion, location, telefono, email, psw, fileNameFront, 'Cliente', card_type))
        conn.commit()

        flash('Cliente agregado correctamente')

        return redirect(url_for('clientForm'))
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/edit/<id>')
def updateClientForm(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spGetClientData', [id])
        data = cursor.fetchall()

        clientData = data[0]
        print(clientData)

        return render_template('update_client.html', data = clientData)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/update/<id>', methods=['POST'])
def updateClient(id):
    try:
        if  request.method == 'POST':
            nombre = request.form['client']
            direccion = request.form['direction']
            location = request.form['location']
            telefono = request.form['phone']
            email = request.form['email']
            oldImage = request.form['old-img']
            cardType = request.form['card-type']
            newCard = request.form['new-card']
            newCardBack = request.form['new-card-back']
            f = request.files['front-image']
            fileNameBack = request.files['back-image']

            print("OLD IMAGE: " + oldImage)
            print("LOCATION: " + location)
            print("CARD TYPE: " + cardType)
            print("NEW CARD: " + newCard)

            if oldImage != newCard:
                deleteImage(oldImage, location, cardType)

                fileName = secure_filename(f.filename)
            
                print('fileName: ' + fileName)

                clientLocation = selectClientLocation(id)

                newClientImage = newCard.replace(' ', '_')

                conn2 = mysql.connect()
                cursor2 = conn2.cursor()
                cursor2.callproc('spUpdateOldImage', (newClientImage, oldImage, clientLocation[0]))
                conn2.commit()

                if location == 'Zihuatanejo':
                    if cardType == 'parques':
                        f.save(os.path.join('./static/img/Zihuatanejo/Frente/' + cardType, fileName))
                        os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/parques/' + str(oldImage),
                            '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/parques/' + str(newClientImage))
                    elif cardType == 'restaurantes':
                        f.save(os.path.join('./static/img/Zihuatanejo/Frente/' + cardType, fileName))
                        os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/restaurantes/' + str(oldImage),
                            '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/restaurantes/' + str(newClientImage))
                    elif cardType == 'lugares':
                        f.save(os.path.join('./static/img/Zihuatanejo/Frente/' + cardType, fileName))
                        os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/lugares/' + str(oldImage),
                            '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/lugares/' + str(newClientImage))
                    elif cardType == 'tiendas':
                        f.save(os.path.join('./static/img/Zihuatanejo/Frente/' + cardType, fileName))
                        os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/tiendas/' + str(oldImage),
                            '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/tiendas/' + str(newClientImage))
                    elif cardType == 'servicios':
                        f.save(os.path.join('./static/img/Zihuatanejo/Frente/' + cardType, fileName))
                        os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/servicios/' + str(oldImage),
                            '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/servicios/' + str(newClientImage))
                elif location == 'Acapulco':
                    if cardType == 'parques':
                        f.save(os.path.join('./static/img/Acapulco/Frente/' + cardType, fileName))
                        os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/parques/' + str(oldImage),
                            '../MinitouristCardsFinal/static/img/Acapulco/Atras/parques/' + str(newClientImage))
                    elif cardType == 'restaurantes':
                        f.save(os.path.join('./static/img/Acapulco/Frente/' + cardType, fileName))
                        os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/restaurantes/' + str(oldImage),
                            '../MinitouristCardsFinal/static/img/Acapulco/Atras/restaurantes/' + str(newClientImage))
                    elif cardType == 'lugares':
                        f.save(os.path.join('./static/img/Acapulco/Frente/' + cardType, fileName))
                        os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/lugares/' + str(oldImage),
                            '../MinitouristCardsFinal/static/img/Acapulco/Atras/lugares/' + str(newClientImage))
                    elif cardType == 'tiendas':
                        f.save(os.path.join('./static/img/Acapulco/Frente/' + cardType, fileName))
                        os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/tiendas/' + str(oldImage),
                            '../MinitouristCardsFinal/static/img/Acapulco/Atras/tiendas/' + str(newClientImage))
                    elif cardType == 'servicios':
                        f.save(os.path.join('./static/img/Acapulco/Frente/' + cardType, fileName))
                        os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/servicios/' + str(oldImage),
                            '../MinitouristCardsFinal/static/img/Acapulco/Atras/servicios/' + str(newClientImage))

            if oldImage != newCardBack:
                deleteImageBack(oldImage, location, cardType)

                fileNameBackOld = secure_filename(fileNameBack.filename)
            
                print('fileNameBackOld: ' + fileNameBackOld)

                newClientImageBack = oldImage.replace(' ', '_')

                if location == 'Zihuatanejo':
                    if cardType == 'parques':
                        fileNameBack.save(os.path.join('./static/img/Zihuatanejo/Atras/' + cardType, fileNameBackOld))
                        os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/parques/' + str(fileNameBackOld),
                            '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/parques/' + str(newClientImageBack))
                    elif cardType == 'restaurantes':
                        fileNameBack.save(os.path.join('./static/img/Zihuatanejo/Atras/' + cardType, fileNameBackOld))
                    elif cardType == 'lugares':
                        fileNameBack.save(os.path.join('./static/img/Zihuatanejo/Atras/' + cardType, fileNameBackOld))
                        os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/lugares/' + str(fileNameBackOld),
                            '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/lugares/' + str(newClientImageBack))
                    elif cardType == 'tiendas':
                        fileNameBack.save(os.path.join('./static/img/Zihuatanejo/Atras/' + cardType, fileNameBackOld))
                        os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/tiendas/' + str(fileNameBackOld),
                            '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/tiendas/' + str(newClientImageBack))
                    elif cardType == 'servicios':
                        fileNameBack.save(os.path.join('./static/img/Zihuatanejo/Atras/' + cardType, fileNameBackOld))
                        os.rename('../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/servicios/' + str(fileNameBackOld),
                            '../MinitouristCardsFinal/static/img/Zihuatanejo/Atras/servicios/' + str(newClientImageBack))
                elif location == 'Acapulco':
                    if cardType == 'parques':
                        fileNameBack.save(os.path.join('./static/img/Acapulco/Atras/' + cardType, fileNameBackOld))
                        os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/parques/' + str(fileNameBackOld),
                            '../MinitouristCardsFinal/static/img/Acapulco/Atras/parques/' + str(newClientImageBack))
                    elif cardType == 'restaurantes':
                        fileNameBack.save(os.path.join('./static/img/Acapulco/Atras/' + cardType, fileNameBackOld))
                        os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/restaurantes/' + str(fileNameBackOld),
                            '../MinitouristCardsFinal/static/img/Acapulco/Atras/restaurantes/' + str(newClientImageBack))
                    elif cardType == 'lugares':
                        fileNameBack.save(os.path.join('./static/img/Acapulco/Atras/' + cardType, fileNameBackOld))
                        os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/lugares/' + str(fileNameBackOld),
                            '../MinitouristCardsFinal/static/img/Acapulco/Atras/lugares/' + str(newClientImageBack))
                    elif cardType == 'tiendas':
                        fileNameBack.save(os.path.join('./static/img/Acapulco/Atras/' + cardType, fileNameBackOld))
                        os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/tiendas/' + str(fileNameBackOld),
                            '../MinitouristCardsFinal/static/img/Acapulco/Atras/tiendas/' + str(newClientImageBack))
                    elif cardType == 'servicios':
                        fileNameBack.save(os.path.join('./static/img/Acapulco/Atras/' + cardType, fileNameBackOld))
                        os.rename('../MinitouristCardsFinal/static/img/Acapulco/Atras/servicios/' + str(fileNameBackOld),
                            '../MinitouristCardsFinal/static/img/Acapulco/Atras/servicios/' + str(newClientImageBack))

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spUpdateClient', (id, nombre, direccion, telefono, email, newCard))
            conn.commit()

            flash('Cliente actualizado correctamente')

            return redirect(url_for('clientForm'))
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete/<id>')
def deleteClient(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        image = selectClientImage(id)
        clientLocation = selectClientLocation(id)

        clientImage = image.replace(' ', '_')

        cursor.callproc('spDeleteClient', (id, clientImage, clientLocation[0]))
        conn.commit()

        print('Image to delete: ' + clientImage)

        deleteImage(clientImage, clientLocation[0], clientLocation[1])
        deleteImageBack(clientImage, clientLocation[0], clientLocation[1])

        flash('Cliente eliminado correctamente')

        return redirect(url_for('clientForm'))
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/login_data', methods=['POST'])
def loginData():
    try:
        msg = ''
        correo = request.form['correo']
        password = request.form['pass']

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spLogin', (correo, password))
        data = cursor.fetchall()

        if data:
            mail = data[0][5]
            psw = data[0][6]
            loginData.clientImage = data[0][7]
            tipoUsuario = data[0][8]
            session["tipo_usuario"] = tipoUsuario

            print('Logged user: ' + tipoUsuario)

            if tipoUsuario == 'Administrador':
                msg = redirect(url_for('clientForm'))
            elif tipoUsuario == 'Cliente':
                msg = redirect(url_for('tarjetaStatus'))
            
            session["user"] = correo
        else:
            flash('Usuario y/o contraseña incorrectos')
            print('Usuario y/o contraseña incorrectos')
            msg = redirect(url_for('login'))

        return msg
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('tipo_usuario', None)

    return render_template('login.html')

@app.route('/visitas_descargas', methods=['POST'])
def insertarTarjetaVisitaDescarga():
    try:
        jsonData = request.json
        print('JSON DATA: ' + str(jsonData))

        nombre = jsonData['nombre']
        ciudad = jsonData['ciudad']
        tipo = jsonData['tipo']

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spTarjetaStatus', [nombre, ciudad, tipo])
        conn.commit()

        resp = jsonify('Tarjeta visitada')
        resp.status_code = 200

        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/tarjeta_status')
def tarjetaStatus():
    dashboardRedirect = ''

    if "user" in session:
        getAllClients()
        status = getCardStatus()

        sessionInitialized = False

        if 'user' in session:
            sessionInitialized = True
        else:
            sessionInitialized = False

        print('Session: ' + str(sessionInitialized))

        tipoUsuario = session['tipo_usuario']
        print('tipoUsuario: ' + tipoUsuario)

        if 'tipo_usuario' in session:
            if tipoUsuario == 'Administrador':
                print('Admin')
                getAllClients()
                dashboardRedirect = render_template('add_client.html', client_data = getAllClients(), logged_in = sessionInitialized)
            elif tipoUsuario == 'Cliente':
                print('Client')
                dashboardRedirect = render_template('client_view.html', visitas = status[0], descargas = status[1], logged_in = sessionInitialized)
        
        return dashboardRedirect
    else:
        return render_template('login.html')

def getAllClients():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spShowClients')
        data = cursor.fetchall()

        return data
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/show_all', methods=['POST'])
def getCardStatus():
    try:
        clientImage = loginData.clientImage.replace(' ', '_')

        print('clientImage: ' + clientImage)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spMostrarVisitas', [clientImage])
        data = cursor.fetchall()

        cursor2 = conn.cursor()
        cursor2.callproc('spMostrarDescargas', [clientImage])
        data2 = cursor2.fetchall()

        visitas = data[0][0]
        descargas = data2[0][0]

        print('VISITAS: ' + str(visitas))
        print('DESCARGAS: ' + str(descargas))

        return visitas, descargas
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/show_card_info_date', methods=['POST'])
def getCardStatusDate():
    try:
        clientImage = loginData.clientImage.replace(' ', '_')

        date = request.get_json()
        fecha = date['fecha'].replace('/', '-')
        print(fecha)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spMostrarDescargasFecha', [clientImage, fecha])
        data = cursor.fetchall()

        cursor2 = conn.cursor()
        cursor2.callproc('spMostrarVisitasFecha', [clientImage, fecha])
        data2 = cursor2.fetchall()

        descargas = data[0][0]
        visitas = data2[0][0]

        print('VISITAS: ' + str(visitas))
        print('DESCARGAS: ' + str(descargas))

        cardInfo = {
            'visitas': visitas,
            'descargas': descargas
        }

        print(cardInfo)

        return cardInfo
    except Exception as e:
        print(e)

@app.route('/show_card_info_range', methods=['POST'])
def getCardStatusRangeDate():
    try:
        clientImage = loginData.clientImage.replace(' ', '_')

        date = request.get_json()
        fecha_inicio = date['fecha_inicio'].replace('/', '-')
        fecha_fin = date['fecha_fin'].replace('/', '-')

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spMostrarDescargasRangoFecha', [clientImage, fecha_inicio, fecha_fin])
        data = cursor.fetchall()

        cursor2 = conn.cursor()
        cursor2.callproc('spMostrarVisitasRangoFecha', [clientImage, fecha_inicio, fecha_fin])
        data2 = cursor2.fetchall()

        descargas = data[0][0]
        visitas = data2[0][0]

        print('VISITAS: ' + str(visitas))
        print('DESCARGAS: ' + str(descargas))

        cardInfo = {
            'visitas': visitas,
            'descargas': descargas
        }

        print(cardInfo)

        return cardInfo
    except Exception as e:
        print(e)

def selectClientImage(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spSelectClientData', [id])
        data = cursor.fetchall()

        imageName = data[0][1]

        print('imageName: ' + str(imageName))

        return imageName
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def selectOldClientImage(imageName, clientLocation):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spSelectOldImage', [imageName, clientLocation])
        data = cursor.fetchall()

        imageName = data[0][1]

        print('imageName: ' + str(imageName))

        return imageName
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def selectClientLocation(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spSelectClientLocation', [id])
        data = cursor.fetchall()

        clientLocation = data[0][0]
        cardType = data[0][1]

        print(clientLocation)
        print(cardType)

        return clientLocation, cardType
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def deleteImage(image, location, cardType):
    imageToDelete = image.replace(' ', '_')

    print('IMAGE TO DELETE: ' + imageToDelete)
    print('LOCATION: ' + location)
    print('CARD TYPE: ' + cardType)

    if location == 'Zihuatanejo':
        if cardType == 'lugares':
            if os.path.exists('./static/img/Zihuatanejo/Frente/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Zihuatanejo/Frente/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'parques':
            if os.path.exists('./static/img/Zihuatanejo/Frente/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Zihuatanejo/Frente/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'restaurantes':
            if os.path.exists('./static/img/Zihuatanejo/Frente/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Zihuatanejo/Frente/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'servicios':
            if os.path.exists('./static/img/Zihuatanejo/Frente/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Zihuatanejo/Frente/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'tiendas':
            if os.path.exists('./static/img/Zihuatanejo/Frente/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Zihuatanejo/Frente/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
    elif location == 'Acapulco':
        if cardType == 'lugares':
            if os.path.exists('./static/img/Acapulco/Frente/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Acapulco/Frente/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'parques':
            if os.path.exists('./static/img/Acapulco/Frente/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Acapulco/Frente/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'restaurantes':
            if os.path.exists('./static/img/Acapulco/Frente/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Acapulco/Frente/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'servicios':
            if os.path.exists('./static/img/Acapulco/Frente/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Acapulco/Frente/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'tiendas':
            if os.path.exists('./static/img/Acapulco/Frente/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Acapulco/Frente/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'

    print(message)

def deleteImageBack(image, location, cardType):
    imageToDelete = image.replace(' ', '_')

    print('IMAGE TO DELETE BACK: ' + imageToDelete)
    print('LOCATION BACK: ' + location)
    print('CARD TYPE BACK: ' + cardType)

    if location == 'Zihuatanejo':
        if cardType == 'lugares':
            if os.path.exists('./static/img/Zihuatanejo/Atras/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Zihuatanejo/Atras/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'parques':
            if os.path.exists('./static/img/Zihuatanejo/Atras/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Zihuatanejo/Atras/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'restaurantes':
            if os.path.exists('./static/img/Zihuatanejo/Atras/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Zihuatanejo/Atras/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'servicios':
            if os.path.exists('./static/img/Zihuatanejo/Atras/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Zihuatanejo/Atras/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'tiendas':
            if os.path.exists('./static/img/Zihuatanejo/Atras/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Zihuatanejo/Atras/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
    elif location == 'Acapulco':
        if cardType == 'lugares':
            if os.path.exists('./static/img/Acapulco/Atras/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Acapulco/Atras/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'parques':
            if os.path.exists('./static/img/Acapulco/Atras/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Acapulco/Atras/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'restaurantes':
            if os.path.exists('./static/img/Acapulco/Atras/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Acapulco/Atras/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'servicios':
            if os.path.exists('./static/img/Acapulco/Atras/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Acapulco/Atras/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'
        elif cardType == 'tiendas':
            if os.path.exists('./static/img/Acapulco/Atras/' + cardType + '/' + imageToDelete):
                os.remove('./static/img/Acapulco/Atras/' + cardType + '/' + imageToDelete)
                message = "Cliente eliminado"
            else:
                message = 'El archivo no existe'

    print(message)

@app.route('/send_email', methods=['POST'])
def sendEmail():
    if  request.method == 'POST':
        nombre = request.form['name']
        email = request.form['email']
        telefono = request.form['phone']
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']

        msg = Message(asunto, sender='minitouristcards@gmail.com', recipients=['minitouristcards@gmail.com'])
        msg.body = 'Mensaje de ' + nombre + '\n' + 'Email: ' + email + '\n' + 'Teléfono: ' + telefono + '\n\n\n' + mensaje
        mail.send(msg)


        flash('Mensaje enviado correctamente')

        return redirect(url_for('contacto'))

@app.route('/tarjetas_lugares_zihua', methods=['GET'])
def zihuaCardsLugares():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spContarTarjetasLugaresZihua')
        data = cursor.fetchall()

        print('spContarTarjetasLugaresZihua: ' + str(data[0][0]))

        return str(data[0][0])
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/tarjetas_restaurantes_zihua', methods=['GET'])
def zihuaCardsRestaurantes():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spContarTarjetasRestZihua')
        data = cursor.fetchall()

        print(data[0][0])

        return str(data[0][0])
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/tarjetas_parques_zihua', methods=['GET'])
def zihuaCardsParques():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spContarTarjetasParquesZihua')
        data = cursor.fetchall()

        print(data[0][0])

        return str(data[0][0])
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/tarjetas_tiendas_zihua', methods=['GET'])
def zihuaCardsTiendas():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spContarTarjetasTiendasZihua')
        data = cursor.fetchall()

        print(data[0][0])

        return str(data[0][0])
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/tarjetas_servicios_zihua', methods=['GET'])
def zihuaCardsServicios():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spContarTarjetasServiciosZihua')
        data = cursor.fetchall()

        print(data[0][0])

        return str(data[0][0])
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/tarjetas_lugares_acapulco', methods=['GET'])
def acapulcoCardsLugares():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spContarTarjetasLugaresAcapulco')
        data = cursor.fetchall()

        print('spContarTarjetasLugaresAcapulco: ' + str(data[0][0]))

        return str(data[0][0])
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/tarjetas_restaurantes_acapulco', methods=['GET'])
def acapulcoCardsRestaurantes():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spContarTarjetasRestAcapulco')
        data = cursor.fetchall()

        print(data[0][0])

        return str(data[0][0])
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/tarjetas_parques_acapulco', methods=['GET'])
def acapulcoCardsParques():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spContarTarjetasParquesAcapulco')
        data = cursor.fetchall()

        print(data[0][0])

        return str(data[0][0])
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/tarjetas_tiendas_acapulco', methods=['GET'])
def acapulcoCardsTiendas():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spContarTarjetasTiendasAcapulco')
        data = cursor.fetchall()

        print(data[0][0])

        return str(data[0][0])
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/tarjetas_servicios_acapulco', methods=['GET'])
def acapulcoCardsServicios():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spContarTarjetasServiciosAcapulco')
        data = cursor.fetchall()

        print(data[0][0])

        return str(data[0][0])
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 5000)