# ============================================================
# GRÁFICA DE PASTEL - SÍNTOMAS 
# ============================================================

import tkinter as tk
from tkinter import messagebox

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from base_conocimiento import ENFERMEDADES

COLOR_BG = "#0d1b2a"
COLOR_PANEL = "#1b2a3b"
COLOR_TEXTO = "#e0f0ff"


def mostrar_grafica(parent_window, hechos: set, resultados: list):
    """
    Abre una ventana con:
    - Gráfica de pastel: distribución de diagnósticos detectados
    - Barra lateral con detalles
    """
    if not resultados:
        messagebox.showinfo(
            "Sin datos",
            "No hay diagnósticos para graficar.\nSelecciona al menos un síntoma."
        )
        return

    ventana = tk.Toplevel(parent_window)
    ventana.title("📊 Gráfica de Diagnósticos")
    ventana.geometry("750x500")
    ventana.configure(bg=COLOR_BG)

    labels = [r["conclusion"].replace("_", " ").title() for r in resultados]
    colores = [ENFERMEDADES[r["conclusion"]]["color"] for r in resultados]
    valores = [1] * len(resultados)

    frame_graf = tk.Frame(ventana, bg=COLOR_BG)
    frame_graf.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    fig = plt.figure(figsize=(4.5, 4), facecolor=COLOR_BG)
    ax = fig.add_subplot(111)

    wedges, texts, autotexts = ax.pie(
        valores,
        labels=labels,
        colors=colores,
        autopct="%1.0f%%",
        startangle=90,
        textprops={"color": COLOR_TEXTO, "fontsize": 9},
        wedgeprops={"edgecolor": COLOR_BG, "linewidth": 2}
    )

    for at in autotexts:
        at.set_color("white")
        at.set_fontsize(9)

    ax.set_title("Diagnósticos detectados", color=COLOR_TEXTO, fontsize=11, pad=10)
    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=frame_graf)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    frame_info = tk.Frame(ventana, bg=COLOR_PANEL, width=230)
    frame_info.pack(side="right", fill="y", padx=(0, 10), pady=10)
    frame_info.pack_propagate(False)

    tk.Label(
        frame_info,
        text="Resumen",
        font=("Segoe UI", 12, "bold"),
        bg=COLOR_PANEL,
        fg="#00b4d8"
    ).pack(pady=(15, 5))

    tk.Label(
        frame_info,
        text=f"Síntomas marcados: {len(hechos)}",
        font=("Segoe UI", 10),
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO
    ).pack(anchor="w", padx=10)

    tk.Label(
        frame_info,
        text=f"Diagnósticos: {len(resultados)}",
        font=("Segoe UI", 10),
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO
    ).pack(anchor="w", padx=10, pady=(0, 10))

    for r in resultados:
        enf = ENFERMEDADES[r["conclusion"]]
        card = tk.Frame(frame_info, bg="#1f3040", padx=8, pady=6)
        card.pack(fill="x", padx=8, pady=3)

        tk.Label(
            card,
            text=r["conclusion"].replace("_", " ").upper(),
            font=("Segoe UI", 9, "bold"),
            bg="#1f3040",
            fg=enf["color"]
        ).pack(anchor="w")

        tk.Label(
            card,
            text=f"Urgencia: {enf['urgencia']}",
            font=("Segoe UI", 9),
            bg="#1f3040",
            fg=COLOR_TEXTO
        ).pack(anchor="w")

        tk.Label(
            card,
            text=f"Regla: {r['id']}",
            font=("Segoe UI", 8),
            bg="#1f3040",
            fg="#7090a0"
        ).pack(anchor="w")

    tk.Button(
        frame_info,
        text="Cerrar",
        font=("Segoe UI", 10),
        bg="#e74c3c",
        fg="white",
        relief="flat",
        cursor="hand2",
        command=ventana.destroy
    ).pack(pady=15, padx=10, fill="x")