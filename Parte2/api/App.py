from ctypes.wintypes import PINT
from urllib import response
from flask import Flask
from flask import render_template, jsonify, request, redirect, url_for
import json
from Conexion import connect_db, get_list
import itertools
import time
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Retorna la pagina index."""
    print("OK")
    if(request.method == 'GET'):
        con = connect_db()

        lista = get_list()
    return render_template('/index.html', datos=lista)

@app.route('/about')
def about():
    """Retorna la pagina about."""
    return "About Python Flask"

@app.route('/punto6y7')
def punto6y7():
    """6) Probemos ahora almacenar algunos datos."""
    """7) Ahora intentemos recuperarlos para ver si todo va bien."""
    conexion = connect_db()
    conexion.select(3)
    #conexion.flushdb(3)
    #conexion.set("valor1","Cargo bien")
    #conexion.set("valor1","Cargo bien2")
    respuesta = conexion.get("valor1")

    #Tambien se podria hacer mediante el key
    #respuesta = conexion.keys("*")
    #return respuesta[0]

    return respuesta

def punto8(valor):
    """8) Ahora carguemos una lista y mostremos su contenido"""    
    conexion = connect_db()
    conexion.lpush(valor, "hasta,  ahora, cargo, bien")
    mostrar = conexion.lrange(valor,0,-1)
    return mostrar

@app.route('/punto8y10', methods=['GET'])
def punto8y9():
    """Mostramos el contenido de una lista."""
    #conexion.flushdb()
    if(request.method == 'GET'):
        conexion = connect_db()

        mostrar = punto8("valor3")
    return render_template('/punto9.html', listacompleta=mostrar)

def punto1():
    conexion = connect_db()
    conexion.select(0)
    conexion.flushdb()
    lista1 = conexion.lpush("s1_ch1", "Chapter 1, The Mandalorian")
    lista1 = conexion.lrange("s1_ch1",0,-1)
    lista2 = conexion.lpush("s1_ch2", "Chapter 2, The Child")
    lista2 = conexion.lrange("s1_ch2",0,-1)
    lista3 = conexion.lpush("s1_ch3", "Chapter 3, The Sin")
    lista3 = conexion.lrange("s1_ch3",0,-1)
    lista4 = conexion.lpush("s1_ch4", "Chapter 4, Sanctuary")
    lista4 = conexion.lrange("s1_ch4",0,-1)
    lista5 = conexion.lpush("s1_ch5", "Chapter 5, The Gunslinger")
    lista5 = conexion.lrange("s1_ch5",0,-1)
    lista6 = conexion.lpush("s1_ch6", "Chapter 6, The Prisoner")
    lista6 = conexion.lrange("s1_ch6",0,-1)
    lista7 = conexion.lpush("s1_ch7", "Chapter 7, The Reckoning")
    lista7 = conexion.lrange("s1_ch7",0,-1)
    lista8 = conexion.lpush("s1_ch8", "Chapter 8, Redemption")
    lista8 = conexion.lrange("s1_ch8",0,-1)
    lista = lista1 + lista2 + lista3 + lista4 + lista5 + lista6 + lista7 + lista8
    return lista

def punto1_2():
    conexion = connect_db()
    conexion.select(1)
    #conexion.flushdb(1)
    #conexion.lpush("1", "Disponible")
    #conexion.lpush("2", "Disponible")
    #conexion.lpush("3", "Disponible")
    #conexion.lpush("4", "Disponible")
    #conexion.lpush("5", "Disponible")
    #conexion.lpush("6", "Disponible")
    #conexion.lpush("7", "Disponible")
    #conexion.lpush("8", "Disponible")
    lista1 = conexion.lrange("1",0,-1)
    lista2 = conexion.lrange("2",0,-1)
    lista3 = conexion.lrange("3",0,-1)
    lista4 = conexion.lrange("3",0,-1)
    lista5 = conexion.lrange("5",0,-1)
    lista6 = conexion.lrange("6",0,-1)
    lista7 = conexion.lrange("7",0,-1)
    lista8 = conexion.lrange("8",0,-1)
    listaf = lista1 + lista2 + lista3 + lista4 + lista5 + lista6 + lista7 + lista8 
    return listaf

def precio():
    conexion = connect_db()
    conexion.select(2)
    #conexion.flushdb(2)
    #conexion.lpush("p1", "1000")
    #conexion.lpush("p2", "2000")
    #conexion.lpush("p3", "3000")
    #conexion.lpush("p4", "4000")
    #conexion.lpush("p5", "5000")
    #conexion.lpush("p6", "6000")
    #conexion.lpush("p7", "7000")
    #conexion.lpush("p8", "8000")
    lista1 = conexion.lrange("p1",0,-1)
    lista2 = conexion.lrange("p2",0,-1)
    lista3 = conexion.lrange("p3",0,-1)
    lista4 = conexion.lrange("p3",0,-1)
    lista5 = conexion.lrange("p5",0,-1)
    lista6 = conexion.lrange("p6",0,-1)
    lista7 = conexion.lrange("p7",0,-1)
    lista8 = conexion.lrange("p8",0,-1)
    listap = lista1 + lista2 + lista3 + lista4 + lista5 + lista6 + lista7 + lista8 
    return listap


@app.route('/punto1', methods=['GET', 'POST'])
def mostrar1():
    if(request.method == 'GET'):
        con = connect_db()

        lista = punto1()
        listaf = punto1_2()
        listap = precio()
        
    return render_template('/punto1.html', listacap=lista, listad=listaf, listaprec=listap)

@app.route("/punto2")
def alquilar():
    """Cuando se alquile un capítulo deberá quedar reservado por 4 minutos, hasta que se
    confirme el pago, de no confirmarse el apgo deberá estar disponible nuevamente una
    vez pasado el tiempo."""
    conexion = connect_db()
    conexion.select(1)
    listadis = conexion.lrange("2",0,-1)
    dispo= [b'Disponible']
    if (listadis == dispo):
        print('OK')
        respuesta = 'Disponible'
        conexion.lpop("2")
        conexion.lpush("2", "Reservado")
        time.sleep(240)
        conexion.lpop("2")
        conexion.lpush("2", "Disponible")
    else:
        print('No disponible')
        respuesta = 'NO disponible'
    
    return respuesta

@app.route("/reserva")
def reservar_conf(cap, precio):
    """Genere una ruta para confirmar el pago la cual recibirá el número del capítulo y el
        precio, para que se pueda confirme el pago y registre el alquiler por 24 hs."""
    conexion = connect_db()
    conexion.select(2)
    prec = conexion.lrange(precio,0,-1)
    conexion.select(0)
    capi = conexion.lrange(cap,0,-1)
    listaconf =  capi +prec
    capitulos = [b"s1_ch1", b"s1_ch2", b"s1_ch3", b"s1_ch4", b"s1_ch5", b"s1_ch6" ,b"s1_ch7", b"s1_ch8"]
    print(capitulos[0])
    for i in capitulos:
        if i == cap:
            print('son iguales')
            conexion.select(1)
            conexion.lpop("1")
            conexion.lpush("1", "Alquilado")
        else:
            print('distintos')

    return listaconf

@app.route('/punto3', methods=['GET'])
def p3():
    """Retorna la pagina punto3."""
    print("OK")
    if(request.method == 'GET'):
        con = connect_db()

        listaconf = reservar_conf("s1_ch1","p1")
    return render_template('/punto3.html', listaconfirmacion=listaconf)

if __name__ == '__main__':
    app.run(host='web-app-flask', port='5000', debug=True)