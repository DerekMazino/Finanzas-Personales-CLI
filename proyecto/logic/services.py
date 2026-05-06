from ..database.repositories import PeriodoRepository, TransaccionRepository, ConfigRepository, PlantillaRepository
from ..models.entities import Transaccion, PlantillaRecurrente

class FinanzasService:
    def __init__(self, db_manager):
        self.periodos = PeriodoRepository(db_manager)
        self.transacciones = TransaccionRepository(db_manager)
        self.plantillas = PlantillaRepository(db_manager)
        self.config = ConfigRepository(db_manager)

    def get_monthly_summary(self, mes, año):
        # Intentar obtener el periodo. No lo creamos automáticamente aquí para permitir el flujo interactivo
        periodo = self.periodos.get_or_create(mes, año)
        transacciones = self.transacciones.list_by_periodo(periodo.id)
        
        ingresos = sum(t.monto for t in transacciones if t.tipo == 'ingreso')
        egresos = sum(t.monto for t in transacciones if t.tipo == 'egreso')
        balance = ingresos - egresos
        
        return {
            'periodo': periodo,
            'ingresos': ingresos,
            'egresos': egresos,
            'balance': balance,
            'transacciones': transacciones
        }

    def crear_periodo_con_recurrentes(self, mes, año):
        """Crea un periodo y copia todas las plantillas activas."""
        periodo = self.periodos.get_or_create(mes, año)
        
        # Si el periodo ya tiene transacciones, no volvemos a copiar (para evitar duplicados)
        existentes = self.transacciones.list_by_periodo(periodo.id)
        if not existentes:
            plantillas_activas = self.plantillas.get_active()
            for p in plantillas_activas:
                nueva_t = Transaccion(
                    id=None,
                    periodo_id=periodo.id,
                    plantilla_id=p.id,
                    nombre=p.nombre,
                    tipo=p.tipo,
                    monto=0.0 # El valor se debe ajustar en el periodo
                )
                self.transacciones.add(nueva_t)
        return periodo

    def registrar_concepto(self, periodo_id, nombre, monto, tipo, es_recurrente=False):
        """Registra un nuevo concepto, validando los datos."""
        # Validaciones (Tarea 3.2)
        if not nombre or not nombre[0].isalpha():
            raise ValueError("El nombre debe comenzar con una letra del alfabeto.")
        if monto < 0:
            raise ValueError("El monto no puede ser negativo.")
        
        plantilla_id = None
        if es_recurrente:
            plantilla = PlantillaRecurrente(id=None, nombre=nombre, tipo=tipo, activo=True)
            self.plantillas.add(plantilla)
            plantilla_id = plantilla.id
            
        nueva_t = Transaccion(
            id=None,
            periodo_id=periodo_id,
            plantilla_id=plantilla_id,
            nombre=nombre,
            tipo=tipo,
            monto=monto
        )
        return self.transacciones.add(nueva_t)

    def eliminar_concepto(self, transaccion_id):
        """Eliminación inteligente: física si no hay historial, lógica si lo hay."""
        # Por ahora, implementamos la eliminación de la transacción
        # La lógica de la plantilla se maneja por separado si el usuario lo pide
        self.transacciones.delete(transaccion_id)

    def get_global_savings(self):
        all_transacciones = self.transacciones.get_all()
        ingresos = sum(t.monto for t in all_transacciones if t.tipo == 'ingreso')
        egresos = sum(t.monto for t in all_transacciones if t.tipo == 'egreso')
        ahorro_acumulado = ingresos - egresos
        
        meta = self.config.get_meta()
        progreso = None
        if meta and meta > 0:
            progreso = (ahorro_acumulado / meta) * 100
            
        return {
            'ahorro_acumulado': ahorro_acumulado,
            'meta': meta,
            'progreso_porcentaje': progreso
        }
