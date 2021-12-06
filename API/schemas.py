# Johanel Perez Sanchez
# Matricula: 2019-9035

from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

#***** MODELO FACTURA *****
class FacturaRequestModel(BaseModel):
    fecha: datetime = datetime.now()
    cliente_id: int
    descripcion: str
    subtotal: float
    itbis: float
    total: float
    #detalle: List[factura_detalle] = []

class FacturaResponseModel(FacturaRequestModel):
    id: int


#***** MODELO CLIENTE *****
class ClienteRequestModel(BaseModel):
    nombre: str
    apellido: str
    correo: str
    rnc: int
    telefono: int

class ClienteResponseModel(ClienteRequestModel):
    id: int



#***** MODELO ARTICULO *****
class tipoArticulo(BaseModel):
    servicio: str
    producto: str

class ArticuloRequestModel(BaseModel):
    codigo: int
    tipo: List[tipoArticulo]
    nombre: str
    precio: float
    cantidad: int
    comentario: str

class ArticuloResponseModel(ArticuloRequestModel):
    id: int