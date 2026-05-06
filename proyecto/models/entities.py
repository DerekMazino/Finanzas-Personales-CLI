from dataclasses import dataclass
from typing import Optional

@dataclass
class Periodo:
    id: Optional[int]
    mes: int
    año: int

    def __str__(self):
        return f"{self.mes:02d}/{self.año}"

@dataclass
class Transaccion:
    id: Optional[int]
    periodo_id: int
    tipo: str # 'ingreso' o 'gasto'
    monto: float
    descripcion: str
    fecha: str

@dataclass
class MetaAhorro:
    monto_objetivo: float
    nombre: str = "Meta Principal"
