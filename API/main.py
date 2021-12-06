# Johanel Perez Sanchez
# Matricula: 2019-9035

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import dbLite as connection
from database import *
from schemas import *

AllFacturas = []

app = FastAPI(title= 'Tarea 8',
    description='Esta es la tarea 8', 
    version='1.0')

# Solucion CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Funcion de bienvenida a la API
@app.get('api/v1/home', tags=['Bienvenid@'])
def home():
    return 'hola programadores, tarea 8: facturas y cliente'

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    
    connection.create_tables([Factura])
    connection.create_tables([Cliente])
    connection.create_tables([Articulo])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

#*********
@app.post('/api/v1/factura/agregar', tags=['Factura'])
async def agregar_factura(fac_request: FacturaRequestModel):
    fac = Factura.create(
        cliente_id = fac_request.cliente_id, 
        descripcion = fac_request.descripcion, 
        subtotal = fac_request.subtotal,
        itbis = fac_request.itbis, 
        total= fac_request.total
    )
    return fac_request

#Funcion para mostrar
@app.get('/api/v1/factura/{fac_id}', tags=['Factura'])
async def mostrar_factura(fac_id):
    fac = Factura.select().where(Factura.id == fac_id).first()

    if fac:
        return FacturaResponseModel(
            id=fac.id,
            cliente_id=fac.cliente_id, 
            descripcion=fac.descripcion, 
            subtotal=fac.subtotal,
            itbis=fac.itbis, 
            total= fac.total)
    else:
        return HTTPException(404, 'Factura no encontrada')


@app.delete('/api/v1/factura/delete/{fac_id}', tags=['Factura'])
async def eliminar_factura(fac_id):
    fac = Factura.select().where(Factura.id == fac_id).first()

    if fac:
        fac.delete_instance()
        return True, "La factura fue eliminada exitosamente"
    else:
        return HTTPException(404, "La factura no se encontro.")

@app.get("/api/v1/facturas/lista", tags=['Factura'])
async def lista_facturas():
    tmp = cargarFacturas()
    return tmp
# **************


# **************
@app.post('/api/v1/cliente/agregar', tags=['Clientes'])
async def agregar_cliente(cli_request: ClienteRequestModel):
    cli = Cliente.create(
        nombre = cli_request.nombre,
        apellido = cli_request.apellido,
        correo = cli_request.correo,
        rnc = cli_request.rnc,
        telefono = cli_request.telefono
    )
    return cli_request

#Funcion para mostrar
@app.get('/api/v1/cliente/{cli_id}', tags=['Clientes'])
async def mostrar_cliente(cli_id):
    cli = Cliente.select().where(Cliente.cliente_id == cli_id).first()

    if cli:
        return ClienteResponseModel(
            id=cli.id,
            nombre = cli.nombre,
            apellido = cli.apellido,
            correo = cli.correo,
            rnc = cli.rnc,
            telefono = cli.telefono
        )
    else:
        return HTTPException(404, 'Cliente no encontrado')


@app.delete('/api/v1/cliente/delete/{cli_id}', tags=['Clientes'])
async def eliminar_cliente(cli_id):
    cli = Cliente.select().where(Cliente.id == cli_id).first()

    if cli:
        cli.delete_instance()
        return True, "El cliente fue eliminado exitosamente"
    else:
        return HTTPException(404, "La factura no se encontro.")

@app.get("/api/v1/clientes/lista", tags=['Clientes'])
def lista_clientes():
    tmp = cargarClientes()
    return tmp




# *****************
@app.post('/api/v1/factura/articulo/agregar', tags=['Articulo'])
async def agregar_articulo(art_request: ArticuloRequestModel):
    art = Articulo.create(
        codigo = art_request.codigo, 
        tipo = art_request.tipo, 
        nombre = art_request.nombre,
        precio = art_request.precio, 
        cantidad = art_request.cantidad,
        comentario = art_request.comentario
    )
    return art_request