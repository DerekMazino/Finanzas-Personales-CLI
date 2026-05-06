from ..database.repositories import PeriodoRepository, TransaccionRepository, ConfigRepository

class FinanzasService:
    def __init__(self, db_manager):
        self.periodos = PeriodoRepository(db_manager)
        self.transacciones = TransaccionRepository(db_manager)
        self.config = ConfigRepository(db_manager)

    def get_monthly_summary(self, mes, año):
        periodo = self.periodos.get_or_create(mes, año)
        transacciones = self.transacciones.list_by_periodo(periodo.id)
        
        ingresos = sum(t.monto for t in transacciones if t.tipo == 'ingreso')
        gastos = sum(t.monto for t in transacciones if t.tipo == 'gasto')
        balance = ingresos - gastos
        
        return {
            'periodo': periodo,
            'ingresos': ingresos,
            'gastos': gastos,
            'balance': balance,
            'transacciones': transacciones
        }

    def get_global_savings(self):
        all_transacciones = self.transacciones.get_all()
        ingresos = sum(t.monto for t in all_transacciones if t.tipo == 'ingreso')
        gastos = sum(t.monto for t in all_transacciones if t.tipo == 'gasto')
        ahorro_acumulado = ingresos - gastos
        
        meta = self.config.get_meta()
        progreso = None
        if meta and meta > 0:
            progreso = (ahorro_acumulado / meta) * 100
            
        return {
            'ahorro_acumulado': ahorro_acumulado,
            'meta': meta,
            'progreso_porcentaje': progreso
        }
