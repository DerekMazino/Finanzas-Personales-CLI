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
class PlantillaRecurrente:
    id: Optional[int]
    nombre: str
    tipo: str # 'ingreso' o 'egreso'
    activo: bool = True

@dataclass
class Transaccion:
    id: Optional[int]
    periodo_id: int
    nombre: str
    tipo: str # 'ingreso' o 'egreso'
    monto: float
    plantilla_id: Optional[int] = None
    fecha_creacion: Optional[str] = None

@dataclass
class MetaAhorro:
    monto_objetivo: float
    nombre: str = "Meta Principal"
