# Johanel Perez Sanchez
# Matricula: 2019-9035

import datetime
from peewee import *
from typing import * 

dbLite = SqliteDatabase('BDGeneral.db')

#******** CRUD FACTURAS *********
class Factura(Model):
    fecha =  DateTimeField(default=datetime.datetime.now)
    cliente_id = IntegerField()
    descripcion = TextField()
    subtotal = FloatField()
    itbis = FloatField()
    total = FloatField()

    class Meta:
        database = dbLite
        table_name = 'facturas'

def cargarFacturas():
    facturas = []
    for fac in Factura.select().dicts():
        facturas.append(fac)
        #print(pokemones) -- 
    return facturas



#******** CRUD CLIENTES *********
class Cliente(Model):
    nombre = TextField()
    apellido = TextField()
    correo = TextField()
    rnc = IntegerField()
    telefono = IntegerField()

    class Meta:
        database = dbLite
        table_name = 'clientes'

def cargarClientes():
    clientes = []
    for cli in Cliente.select().dicts():
        clientes.append(cli)
        #print(pokemones) -- 
    return clientes




#******** CRUD ARTICULO *********
class Articulo(Model):
    codigo = IntegerField()
    nombre = TextField()
    precio = FloatField()
    cantidad = IntegerField()
    comentario = TextField()

    class Meta:
        database = dbLite
        table_name = 'articulos'

def cargarArticulos():
    articulos = []
    for art in Articulo.select().dicts():
        articulos.append(art)
        #print(pokemones) -- 
    return articulos
dbLite.connect()