# Sistema Experto de Salud Bucal Básica

Sistema experto desarrollado en Python para orientar sobre problemas básicos de salud bucal a partir de síntomas seleccionados por el usuario.

## Descripción

Este proyecto es una aplicación de escritorio hecha en Python con interfaz gráfica. Su propósito es ayudar al usuario a identificar de forma preliminar posibles problemas bucales como caries, gingivitis, periodontitis, bruxismo, absceso dental, sensibilidad dental y aftas bucales.

El sistema no reemplaza a un dentista. Solo ofrece una orientación inicial basada en reglas y hechos definidos en la base de conocimiento.

## Objetivo

El objetivo del proyecto es demostrar el funcionamiento de un sistema experto basado en reglas aplicado a la salud bucal básica. También busca ofrecer una herramienta sencilla, visual y fácil de usar para personas interesadas en su higiene oral.

## Funciones principales

* Diagnóstico preliminar por síntomas.
* Consejos de higiene bucal.
* Información sobre enfermedades comunes.
* Análisis de alimentos y su riesgo para los dientes.
* Visualización de resultados con gráfica.
* Explicación de las reglas activadas durante el análisis.

## Tecnologías utilizadas

* Python
* Tkinter
* Matplotlib
* PyInstaller

## Estructura del proyecto

```text
proyecto-odontologia/
├── base_conocimiento.py
├── motor_inferencia.py
├── grafica_sintomas.py
├── interfaz.py
├── interfaz.spec
├── build/
├── dist/
└── README.md
```

### Archivos principales

* `base_conocimiento.py`: contiene síntomas, enfermedades, reglas, consejos y alimentos.
* `motor_inferencia.py`: procesa los hechos y aplica las reglas.
* `grafica_sintomas.py`: genera la gráfica de resultados.
* `interfaz.py`: contiene la interfaz gráfica principal.
* `interfaz.spec`: archivo de configuración generado por PyInstaller.
* `dist/`: carpeta donde se genera el `.exe`.
* `build/`: carpeta temporal creada por PyInstaller.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

* Python 3.x
* Tkinter
* Matplotlib
* PyInstaller

### Instalación de dependencias

Si no tienes `matplotlib`, puedes instalarlo con:

```bash
python -m pip install matplotlib
```

Si no tienes `pyinstaller`, puedes instalarlo con:

```bash
python -m pip install pyinstaller
```

En muchos sistemas, `tkinter` ya viene incluido con Python.

## Cómo ejecutar el proyecto

### Desde Python
1. Descarga o clona el repositorio.
2. Abre la carpeta del proyecto.
3. Ejecuta el archivo principal:

```bash
python interfaz.py
```

### Desde el ejecutable
Si ya generaste el `.exe`, entra a la carpeta `dist` y ejecuta:

```text
dist/interfaz.exe
```

## Uso

1. Abre la aplicación.
2. Ve a la sección de diagnóstico.
3. Selecciona uno o más síntomas.
4. Presiona el botón de analizar.
5. Revisa el resultado, la explicación y la urgencia.
6. Si quieres, consulta la gráfica o revisa las demás secciones.

## Alcance

Este sistema está pensado para:
* Personas interesadas en su higiene bucal.
* Estudiantes.
* Proyectos académicos.
* Usuarios que buscan una orientación inicial.

No debe usarse como diagnóstico clínico definitivo.

## Cómo funciona

El sistema trabaja con una base de conocimientos y un motor de inferencia.

1. El usuario selecciona síntomas desde la interfaz.
2. Esos síntomas se convierten en hechos.
3. El motor compara los hechos con las reglas definidas.
4. Si una regla coincide, el sistema genera un diagnóstico preliminar.
5. La interfaz muestra el resultado y una breve explicación.

## Reglas del sistema

El sistema usa reglas tipo:

```python
if all(c in hechos for c in regla["condiciones"]):
    resultados.append(regla)
```

Esto permite comparar los síntomas seleccionados con las condiciones de cada regla y devolver un diagnóstico preliminar.

## Resultado esperado

El programa muestra:
* Síntomas seleccionados.
* Número de reglas disparadas.
* Diagnósticos encontrados.
* Explicación del resultado.
* Recomendación general.



## Bibliografía

Salud oral. (2026, March 5). OPS/OMS | Organización Panamericana de la Salud. [https://www.paho.org/es/temas/salud-oral](https://www.paho.org/es/temas/salud-oral)

Salud bucodental. (2025, March 16). Organización Mundial de la Salud. [https://www.who.int/es/news-room/fact-sheets/detail/oral-health](https://www.who.int/es/news-room/fact-sheets/detail/oral-health)

Tkinter — Python interface to Tcl/Tk. (2026). Python Software Foundation. [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)

Sistemas Expertos Basados en Reglas. (s. f.). Universidad de Cantabria. [https://personales.unican.es/gutierjm/cursos/expertos/reglas.pdf](https://personales.unican.es/gutierjm/cursos/expertos/reglas.pdf)
