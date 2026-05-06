from ..models.entities import Periodo, Transaccion, MetaAhorro, PlantillaRecurrente
from .utils import QueryBuilder

class PlantillaRepository:
    def __init__(self, db_manager):
        self.db = db_manager
        self.table = "plantillas_recurrentes"

    def add(self, plantilla: PlantillaRecurrente):
        data = {
            "nombre": plantilla.nombre,
            "tipo": plantilla.tipo,
            "activo": 1 if plantilla.activo else 0
        }
        sql, values = QueryBuilder.insert(self.table, data)
        self.db.cursor.execute(sql, values)
        self.db.connection.commit()
        plantilla.id = self.db.cursor.lastrowid
        return plantilla

    def update(self, plantilla: PlantillaRecurrente):
        data = {
            "nombre": plantilla.nombre,
            "tipo": plantilla.tipo,
            "activo": 1 if plantilla.activo else 0
        }
        sql, values = QueryBuilder.update(self.table, data, {"id": plantilla.id})
        self.db.cursor.execute(sql, values)
        self.db.connection.commit()

    def get_active(self):
        sql, values = QueryBuilder.select(self.table, where={"activo": 1})
        self.db.cursor.execute(sql, values)
        rows = self.db.cursor.fetchall()
        return [PlantillaRecurrente(id=r['id'], nombre=r['nombre'], tipo=r['tipo'], activo=bool(r['activo'])) for r in rows]

    def find_by_id(self, id):
        sql, values = QueryBuilder.select(self.table, where={"id": id})
        self.db.cursor.execute(sql, values)
        row = self.db.cursor.fetchone()
        if row:
            return PlantillaRecurrente(id=row['id'], nombre=row['nombre'], tipo=row['tipo'], activo=bool(row['activo']))
        return None

    def delete_physical(self, id):
        sql, values = QueryBuilder.delete(self.table, where={"id": id})
        self.db.cursor.execute(sql, values)
        self.db.connection.commit()

    def count_usages(self, plantilla_id):
        sql = "SELECT COUNT(*) as count FROM transacciones WHERE plantilla_id = ?"
        self.db.cursor.execute(sql, (plantilla_id,))
        row = self.db.cursor.fetchone()
        return row['count'] if row else 0
class PeriodoRepository:
    def __init__(self, db_manager):
        self.db = db_manager
        self.table = "periodos"

    def find(self, mes, año):
        sql, values = QueryBuilder.select(self.table, where={"mes": mes, "año": año})
        self.db.cursor.execute(sql, values)
        row = self.db.cursor.fetchone()
        if row:
            return Periodo(id=row['id'], mes=row['mes'], año=row['año'])
        return None

    def get_or_create(self, mes, año):
        sql, values = QueryBuilder.select(self.table, where={"mes": mes, "año": año})
        self.db.cursor.execute(sql, values)
        row = self.db.cursor.fetchone()
        if row:
            return Periodo(id=row['id'], mes=row['mes'], año=row['año'])
        
        data = {"mes": mes, "año": año}
        sql, values = QueryBuilder.insert(self.table, data)
        self.db.cursor.execute(sql, values)
        self.db.connection.commit()
        return Periodo(id=self.db.cursor.lastrowid, mes=mes, año=año)

    def list_all(self):
        sql, values = QueryBuilder.select(self.table, order_by="año DESC, mes DESC")
        self.db.cursor.execute(sql, values)
        rows = self.db.cursor.fetchall()
        return [Periodo(id=r['id'], mes=r['mes'], año=r['año']) for r in rows]

class TransaccionRepository:
    def __init__(self, db_manager):
        self.db = db_manager
        self.table = "transacciones"

    def add(self, transaccion: Transaccion):
        data = {
            "periodo_id": transaccion.periodo_id,
            "plantilla_id": transaccion.plantilla_id,
            "nombre": transaccion.nombre,
            "tipo": transaccion.tipo,
            "monto": transaccion.monto
        }
        sql, values = QueryBuilder.insert(self.table, data)
        self.db.cursor.execute(sql, values)
        self.db.connection.commit()
        transaccion.id = self.db.cursor.lastrowid
        return transaccion

    def delete(self, transaccion_id):
        sql, values = QueryBuilder.delete(self.table, where={"id": transaccion_id})
        self.db.cursor.execute(sql, values)
        self.db.connection.commit()

    def list_by_periodo(self, periodo_id):
        sql, values = QueryBuilder.select(self.table, where={"periodo_id": periodo_id})
        self.db.cursor.execute(sql, values)
        rows = self.db.cursor.fetchall()
        return [Transaccion(
            id=r['id'],
            periodo_id=r['periodo_id'],
            plantilla_id=r['plantilla_id'],
            nombre=r['nombre'],
            tipo=r['tipo'],
            monto=r['monto'],
            fecha_creacion=r['fecha_creacion']
        ) for r in rows]

    def get_all(self):
        sql, values = QueryBuilder.select(self.table)
        self.db.cursor.execute(sql, values)
        rows = self.db.cursor.fetchall()
        return [Transaccion(
            id=r['id'],
            periodo_id=r['periodo_id'],
            plantilla_id=r['plantilla_id'],
            nombre=r['nombre'],
            tipo=r['tipo'],
            monto=r['monto'],
            fecha_creacion=r['fecha_creacion']
        ) for r in rows]

class ConfigRepository:
    def __init__(self, db_manager):
        self.db = db_manager

    def set_meta(self, monto):
        self.db.cursor.execute(
            "INSERT OR REPLACE INTO configuracion (clave, valor) VALUES (?, ?)",
            ('meta_ahorro', str(monto))
        )
        self.db.connection.commit()

    def get_meta(self):
        self.db.cursor.execute("SELECT valor FROM configuracion WHERE clave = ?", ('meta_ahorro',))
        row = self.db.cursor.fetchone()
        if row:
            return float(row['valor'])
        return None
