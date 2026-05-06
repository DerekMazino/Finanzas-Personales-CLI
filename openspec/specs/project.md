# Proyecto: Finanzas Personales

## Overview
Este proyecto es CLI de gestion de ingresos y gastos para finanzas personales. Permitira saber cuanto dinero se tiene y en que se gasta. Permitirá controlar un ahorro para un objetivo futuro. Este proyecto será la base para un proyecto mas grande que permita gestionar finanzas personales.

## Características principales
- Listar periodos.
- Agregar ingresos y egresos.
- Eliminar ingresos y egresos.
- Modificar ingresos y egresos.
- Listar ingresos y egresos por periodo.
- Crear periodo.
- Eliminar periodo.
- Modificar periodo.
- Controlar ahorro.
- Saldo del periodo.
- Saldo total.
- Egresos totales.
- Ingresos totales.
- Meta de ahorro.
- Progreso hacia la meta.

## Comportamiento del usuario
- El usuario puede seleccionar un periodo.
- El dashboard actualiza los datos mostrados en consecuencia.
- El usuario puede agregar ingresos y egresos.
- El usuario puede eliminar ingresos y egresos.
- El usuario puede modificar ingresos y egresos.
- El usuario puede listar ingresos y egresos por periodo.
- El usuario puede crear periodo.
- El usuario puede eliminar periodo.
- El usuario puede modificar periodo.
- El usuario puede controlar ahorro.
- El usuario puede ver saldo del periodo.
- El usuario puede ver saldo total.
- El usuario puede ver egresos totales.
- El usuario puede ver ingresos totales.
- El usuario puede ver meta de ahorro.
- El usuario puede ver progreso hacia la meta.

## Tech Stack
- Python

## Objetivos de diseño
- CLI limpio y moderno.
- Layout de dashboard.
- Componentes simples y legibles.

## Limitaciones de alcance
- No autenticación.

## Lógica de negocio
- **Periodos**: Los periodos son estrictamente mensuales (Mes/Año). El sistema debe permitir la creación de periodos basados en el calendario.
- **Ahorro Acumulado**: El sistema siempre debe calcular el ahorro del mes (Ingresos - Egresos) y el ahorro acumulado de todos los periodos. La Meta de Ahorro es opcional; si se define, se muestra el progreso hacia ella, de lo contrario, solo se muestran los totales ahorrados.
- **Recurrencia**: Los conceptos (Ingresos/Egresos) marcados como recurrentes deben ser creados automáticamente al generar un nuevo periodo, manteniendo su nombre y tipo, pero permitiendo que el valor sea ajustado individualmente en cada periodo.
- **Flujo CLI**: El acceso principal será a través de comandos directos, donde el mes actual es el contexto por defecto para las operaciones de lectura y escritura.

## Objetivo de este proyecto
Este proyecto es para explorar como definir un sistema usando OpenSpec y generar un CLI usando IA.