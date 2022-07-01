var redis = require('redis')
var express = require('express')

var redis_cliente = redis.createClient(6379, 'db-redis')
var app = express()


redis_cliente.on('connect', function(){
    console.log("conectado a redis")
})

app.listen(3000, function(){
    console.log('Aplicación ejemplo, escuchando el puerto 3000!')
})

redis_cliente.set("nahuel", "sistema3")
redis_cliente.set("mily", "sistema2")
redis_cliente.set("santi", "sistema1")

redis_cliente.exists("mily", function(err, value){
    console.log(value)
})

redis_cliente.exists("nahuel", function(err, value){
    console.log(value)
})

redis_cliente.exists("santi", function(err, value){
    console.log(value)
})

redis_cliente.exists("nahue", function(err, value){
    console.log(value)
})

redis_cliente.lpush("personajes", ["facu", "alexis", "martin", "tito", "walter"])

//Listar lista personajes
app.get('/', function( req, res){
    redis_cliente.lrange('personajes', 0, -1, function(err, values){
        res.send(JSON.stringify(values))
    })
})

//Ejercicios 
//1)Genere un ruta agregar personajes, la cual reciba como parámetro el número episodio
//y el nombre del personaje.
app.get('/cargarPersonaje', function( req, res){
    redis_cliente.lpush(req.param("episodio"), [req.param("personaje")])
    res.send("Carga con exito")
})

//2) Genere una ruta para quitar personajes, ídem anterior.
app.delete('/quitarPersonaje', function( req, res){
    redis_cliente.lrem(req.params("episodio"), -1, [req.params("personaje")])
    res.send("Personaje eliminado")
})

//3) Genere una ruta para listar los personajes de un episodio, la cual reciba como
//parámetro el número episodio.
app.get('/listarPersonaje', function( req, res){
    redis_cliente.lrange(req.param("episodio"), 0, -1, function(err, values){
        res.send(JSON.stringify(values))
    })
})

