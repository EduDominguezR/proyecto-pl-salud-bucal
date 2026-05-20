# ============================================================
#  BASE DE CONOCIMIENTO - ODONTOLOGÍA BÁSICA
# ============================================================

ENFERMEDADES = {
    "caries": {
        "descripcion": "Destrucción del esmalte dental por bacterias y azúcares.",
        "tratamiento": "Visita al dentista para limpieza y empaste. Reduce azúcares.",
        "urgencia": "Media", "color": "#f39c12"
    },
    "gingivitis": {
        "descripcion": "Inflamación de las encías por placa bacteriana. Es reversible.",
        "tratamiento": "Limpieza profesional y cepillado correcto 2 veces al día.",
        "urgencia": "Media", "color": "#f39c12"
    },
    "periodontitis": {
        "descripcion": "Infección avanzada de encías que daña el hueso dental.",
        "tratamiento": "Tratamiento periodontal urgente con especialista.",
        "urgencia": "Alta", "color": "#e74c3c"
    },
    "bruxismo": {
        "descripcion": "Hábito de rechinar los dientes, generalmente de noche.",
        "tratamiento": "Placa dental nocturna. Reducir el estrés.",
        "urgencia": "Media", "color": "#f39c12"
    },
    "absceso_dental": {
        "descripcion": "Infección bacteriana grave con pus en la raíz del diente.",
        "tratamiento": "Atención URGENTE. Antibióticos y posible extracción.",
        "urgencia": "Urgente", "color": "#c0392b"
    },
    "sensibilidad_dental": {
        "descripcion": "Esmalte desgastado que expone la dentina.",
        "tratamiento": "Pasta para dientes sensibles y visita al dentista.",
        "urgencia": "Baja", "color": "#27ae60"
    },
    "aftas_bucales": {
        "descripcion": "Úlceras dolorosas en la mucosa bucal. Inofensivas.",
        "tratamiento": "Se curan solas en 1-2 semanas. Si persisten, ve al médico.",
        "urgencia": "Baja", "color": "#27ae60"
    },
}

SINTOMAS = {
    "sangrado_encias":    "Encías que sangran al cepillarse",
    "dolor_muela":        "Dolor agudo o pulsante en una muela",
    "sensibilidad":       "Molestia con cosas frías o calientes",
    "mal_aliento":        "Mal aliento persistente",
    "mancha_diente":      "Manchas oscuras o blancas en los dientes",
    "inflamacion_encia":  "Encías hinchadas o de color rojo",
    "movilidad_diente":   "Diente flojo o que se mueve",
    "dolor_mandibula":    "Dolor o chasquido en la mandíbula",
    "afta":               "Úlceras pequeñas y dolorosas en la boca",
    "sarro_visible":      "Sarro amarillo o café visible en dientes",
}

CONSEJOS = [
    ("🪥 Cepillado",         "Cepíllate mínimo 2 veces al día durante 2 minutos."),
    ("🧵 Hilo dental",       "Úsalo una vez al día para limpiar entre los dientes."),
    ("💧 Enjuague bucal",    "Ayuda a prevenir caries, pero no reemplaza el cepillado."),
    ("🥗 Alimentación",      "Reduce azúcares y refrescos. Prefiere agua y frutas enteras."),
    ("🏥 Visita dentista",   "Ve al dentista cada 6 meses aunque no tengas molestias."),
    ("🪥 Cambio cepillo",    "Cambia tu cepillo cada 3 meses."),
    ("🦷 Flúor",             "Usa pasta dental con flúor para fortalecer el esmalte."),
]

ALIMENTOS = [
    ("🍬 Dulces/gomitas",    "Alto",    "#e74c3c", "Generan ácidos dañinos para el esmalte."),
    ("🥤 Refrescos",         "Alto",    "#e74c3c", "Erosionan el esmalte dental."),
    ("🧃 Jugos naturales",   "Medio",   "#f39c12", "Tienen azúcares; prefiere la fruta entera."),
    ("🍞 Pan blanco",        "Medio",   "#f39c12", "Se convierte en azúcar en la boca."),
    ("☕ Café",              "Bajo",    "#2ecc71", "Puede manchar dientes pero riesgo cariogénico bajo."),
    ("🥛 Leche",             "Bajo",    "#2ecc71", "El calcio fortalece los dientes."),
    ("🥦 Verduras crudas",   "Ninguno", "#27ae60", "Limpian mecánicamente los dientes."),
    ("💧 Agua con flúor",    "Ninguno", "#27ae60", "La mejor bebida para la salud dental."),
]

REGLAS = [
    # ── 1 síntoma ──────────────────────────────────────────────
    {"id": "R1",  "condiciones": ["sangrado_encias"],
     "conclusion": "gingivitis",
     "explicacion": "Sangrado de encías solo → posible inicio de gingivitis."},

    {"id": "R2",  "condiciones": ["dolor_muela"],
     "conclusion": "caries",
     "explicacion": "Dolor en muela solo → posible caries activa."},

    {"id": "R3",  "condiciones": ["sensibilidad"],
     "conclusion": "sensibilidad_dental",
     "explicacion": "Sensibilidad sola → desgaste de esmalte o dentina expuesta."},

    {"id": "R4",  "condiciones": ["mal_aliento"],
     "conclusion": "gingivitis",
     "explicacion": "Mal aliento persistente → acumulación de placa bacteriana."},

    {"id": "R5",  "condiciones": ["mancha_diente"],
     "conclusion": "caries",
     "explicacion": "Manchas en dientes → inicio de caries o desmineralización."},

    {"id": "R6",  "condiciones": ["inflamacion_encia"],
     "conclusion": "gingivitis",
     "explicacion": "Encías inflamadas → gingivitis por placa bacteriana."},

    {"id": "R7",  "condiciones": ["movilidad_diente"],
     "conclusion": "periodontitis",
     "explicacion": "Diente flojo → daño en el hueso de soporte dental."},

    {"id": "R8",  "condiciones": ["dolor_mandibula"],
     "conclusion": "bruxismo",
     "explicacion": "Dolor en mandíbula solo → posible bruxismo o tensión muscular."},

    {"id": "R9",  "condiciones": ["afta"],
     "conclusion": "aftas_bucales",
     "explicacion": "Úlceras en la mucosa → aftas bucales."},

    {"id": "R10", "condiciones": ["sarro_visible"],
     "conclusion": "gingivitis",
     "explicacion": "Sarro visible → acumulación que genera gingivitis."},

    # ── 2 síntomas ─────────────────────────────────────────────
    {"id": "R11", "condiciones": ["sangrado_encias", "inflamacion_encia"],
     "conclusion": "gingivitis",
     "explicacion": "Sangrado + inflamación → gingivitis confirmada."},

    {"id": "R12", "condiciones": ["mancha_diente", "dolor_muela"],
     "conclusion": "caries",
     "explicacion": "Manchas + dolor → caries activa con destrucción del esmalte."},

    {"id": "R13", "condiciones": ["sangrado_encias", "movilidad_diente"],
     "conclusion": "periodontitis",
     "explicacion": "Sangrado + movilidad → daño óseo avanzado (periodontitis)."},

    {"id": "R14", "condiciones": ["dolor_mandibula", "sensibilidad"],
     "conclusion": "bruxismo",
     "explicacion": "Dolor mandibular + sensibilidad → bruxismo confirmado."},

    {"id": "R15", "condiciones": ["dolor_muela", "inflamacion_encia"],
     "conclusion": "absceso_dental",
     "explicacion": "Dolor intenso + inflamación → posible absceso dental (urgente)."},

    # ── 3 síntomas ─────────────────────────────────────────────
    {"id": "R16", "condiciones": ["inflamacion_encia", "movilidad_diente", "mal_aliento"],
     "conclusion": "periodontitis",
     "explicacion": "Inflamación + movilidad + mal aliento → periodontitis severa."},

    {"id": "R17", "condiciones": ["sarro_visible", "sangrado_encias", "movilidad_diente"],
     "conclusion": "periodontitis",
     "explicacion": "Sarro + sangrado + movilidad → periodontitis con daño óseo."},
]