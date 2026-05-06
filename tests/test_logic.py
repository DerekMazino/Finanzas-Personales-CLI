import pytest
from proyecto.database.manager import DatabaseManager
from proyecto.logic.services import FinanzasService
from proyecto.models.entities import PlantillaRecurrente

@pytest.fixture
def service():
    # Usar una base de datos en memoria para los tests
    db = DatabaseManager(db_path=":memory:")
    db.connect()
    return FinanzasService(db)

def test_recurrence_propagation(service):
    # 1. Crear una plantilla recurrente
    service.plantillas.add(PlantillaRecurrente(id=None, nombre="Internet", tipo="egreso"))
    
    # 2. Crear un periodo nuevo
    periodo = service.crear_periodo_con_recurrentes(5, 2026)
    
    # 3. Verificar que se creó la transacción vinculada
    summary = service.get_monthly_summary(5, 2026)
    assert len(summary['transacciones']) == 1
    assert summary['transacciones'][0].nombre == "Internet"
    assert summary['transacciones'][0].monto == 0.0

def test_name_validation(service):
    periodo = service.periodos.get_or_create(5, 2026)
    
    # El nombre debe empezar con letra
    with pytest.raises(ValueError, match="El nombre debe comenzar con una letra"):
        service.registrar_concepto(periodo.id, "123 Invalido", 100, "egreso")
    
    # Monto positivo
    with pytest.raises(ValueError, match="El monto no puede ser negativo"):
        service.registrar_concepto(periodo.id, "Valido", -10, "egreso")

def test_logical_deletion_check(service):
    # Setup
    periodo = service.periodos.get_or_create(5, 2026)
    transaccion = service.registrar_concepto(periodo.id, "Gym", 50, "egreso", es_recurrente=True)
    
    # Verificar que tiene usos la plantilla que se creó automáticamente
    assert transaccion.plantilla_id is not None
    count = service.plantillas.count_usages(transaccion.plantilla_id)
    assert count == 1
