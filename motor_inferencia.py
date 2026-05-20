# ============================================================
#  MOTOR DE INFERENCIA - ENCADENAMIENTO HACIA ADELANTE
# ============================================================

from base_conocimiento import REGLAS

def ejecutar_inferencia(hechos: set) -> list:
    """
    Recibe un conjunto de hechos (síntomas activos) y aplica
    las reglas de la base de conocimiento.
    Retorna lista de reglas disparadas (sin duplicar conclusiones).
    """
    resultados = []
    conclusiones_vistas = set()

    for regla in REGLAS:
        if all(cond in hechos for cond in regla["condiciones"]):
            if regla["conclusion"] not in conclusiones_vistas:
                resultados.append(regla)
                conclusiones_vistas.add(regla["conclusion"])

    return resultados


def obtener_resumen(hechos: set) -> dict:
    """
    Retorna un resumen con el total de síntomas y diagnósticos.
    Útil para la gráfica.
    """
    resultados = ejecutar_inferencia(hechos)
    return {
        "total_sintomas":     len(hechos),
        "total_diagnosticos": len(resultados),
        "diagnosticos":       [r["conclusion"] for r in resultados],
        "reglas_disparadas":  [r["id"] for r in resultados],
    }