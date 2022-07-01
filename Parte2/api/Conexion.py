import redis

def connect_db():
    conexion = redis.StrictRedis(port=6379, db=0, host="db-redis")
    if(conexion.ping()):
        print("conectado a redis")
    else:
        print("error de conexion con redis")
    return conexion

def get_list():
    conexion = connect_db()
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
