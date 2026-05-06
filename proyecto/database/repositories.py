from ..models.entities import Periodo, Transaccion, MetaAhorro

class PeriodoRepository:
    def __init__(self, db_manager):
        self.db = db_manager

    def get_or_create(self, mes, año):
        self.db.cursor.execute(
            "SELECT id, mes, año FROM periodos WHERE mes = ? AND año = ?",
            (mes, año)
        )
        row = self.db.cursor.fetchone()
        if row:
            return Periodo(id=row['id'], mes=row['mes'], año=row['año'])
        
        self.db.cursor.execute(
            "INSERT INTO periodos (mes, año) VALUES (?, ?)",
            (mes, año)
        )
        self.db.connection.commit()
        return Periodo(id=self.db.cursor.lastrowid, mes=mes, año=año)

    def list_all(self):
        self.db.cursor.execute("SELECT id, mes, año FROM periodos ORDER BY año DESC, mes DESC")
        rows = self.db.cursor.fetchall()
        return [Periodo(id=r['id'], mes=r['mes'], año=r['año']) for r in rows]

class TransaccionRepository:
    def __init__(self, db_manager):
        self.db = db_manager

    def add(self, transaccion: Transaccion):
        self.db.cursor.execute(
            """INSERT INTO transacciones (periodo_id, tipo, monto, descripcion, fecha)
               VALUES (?, ?, ?, ?, ?)""",
            (transaccion.periodo_id, transaccion.tipo, transaccion.monto, transaccion.descripcion, transaccion.fecha)
        )
        self.db.connection.commit()
        transaccion.id = self.db.cursor.lastrowid
        return transaccion

    def delete(self, transaccion_id):
        self.db.cursor.execute("DELETE FROM transacciones WHERE id = ?", (transaccion_id,))
        self.db.connection.commit()

    def list_by_periodo(self, periodo_id):
        self.db.cursor.execute(
            "SELECT id, periodo_id, tipo, monto, descripcion, fecha FROM transacciones WHERE periodo_id = ?",
            (periodo_id,)
        )
        rows = self.db.cursor.fetchall()
        return [Transaccion(**dict(r)) for r in rows]

    def get_all(self):
        self.db.cursor.execute("SELECT id, periodo_id, tipo, monto, descripcion, fecha FROM transacciones")
        rows = self.db.cursor.fetchall()
        return [Transaccion(**dict(r)) for r in rows]

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
