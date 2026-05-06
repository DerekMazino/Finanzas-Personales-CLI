import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path=None):
        if db_path is None:
            home = os.path.expanduser("~")
            self.db_dir = os.path.join(home, ".Finanzas_3", "finanzas")
            self.db_path = os.path.join(self.db_dir, "finanzas.db")
        else:
            self.db_path = db_path
            self.db_dir = os.path.dirname(db_path)

        self._ensure_dir_exists()
        self.connection = None
        self.cursor = None

    def _ensure_dir_exists(self):
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir, exist_ok=True)

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        # Tabla de Periodos
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS periodos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mes INTEGER NOT NULL,
                año INTEGER NOT NULL,
                UNIQUE(mes, año)
            )
        """)

        # Tabla de Transacciones
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transacciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                periodo_id INTEGER NOT NULL,
                tipo TEXT NOT NULL, -- 'ingreso' o 'gasto'
                monto REAL NOT NULL,
                descripcion TEXT NOT NULL,
                fecha TEXT NOT NULL,
                FOREIGN KEY (periodo_id) REFERENCES periodos (id)
            )
        """)

        # Tabla de Configuración (para metas de ahorro, etc.)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS configuracion (
                clave TEXT PRIMARY KEY,
                valor TEXT NOT NULL
            )
        """)
        
        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()
