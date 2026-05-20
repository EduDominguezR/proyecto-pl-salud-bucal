# ============================================================
#  INTERFAZ PRINCIPAL - SISTEMA EXPERTO ODONTOLOGÍA
#  eduardo - Ingeniería en Sistemas
# ============================================================

import tkinter as tk
from tkinter import ttk
from base_conocimiento import (
    ENFERMEDADES, SINTOMAS, CONSEJOS, ALIMENTOS, REGLAS
)
from motor_inferencia import ejecutar_inferencia
from grafica_sintomas import mostrar_grafica

COLOR_BG      = "#0d1b2a"
COLOR_PANEL   = "#1b2a3b"
COLOR_ACENTO  = "#00b4d8"
COLOR_ACENTO2 = "#0077b6"
COLOR_TEXTO   = "#e0f0ff"
COLOR_SUB     = "#a0b8cc"
COLOR_BTN     = "#0077b6"
COLOR_BTN_HV  = "#00b4d8"
F_TITULO  = ("Segoe UI", 20, "bold")
F_SUBTIT  = ("Segoe UI", 13, "bold")
F_NORMAL  = ("Segoe UI", 11)
F_SMALL   = ("Segoe UI", 10)


class AppOdontologia:
    def __init__(self, root):
        self.root = root
        self.root.title("🦷 Sistema Experto · Salud Bucal")
        self.root.geometry("920x660")
        self.root.configure(bg=COLOR_BG)
        self.root.resizable(True, True)
        self._hechos_activos   = set()
        self._ultimo_resultado = []
        self._construir_layout()

    # ── Layout base ──────────────────────────────────────────
    def _construir_layout(self):
        header = tk.Frame(self.root, bg=COLOR_ACENTO2, pady=12)
        header.pack(fill="x")
        tk.Label(header, text="🦷 Sistema Experto · Salud Bucal Básica",
                 font=F_TITULO, bg=COLOR_ACENTO2, fg="white").pack()
        tk.Label(header, text="Ingeniería en Sistemas  ·  Base de Conocimiento Odontológica",
                 font=F_SMALL, bg=COLOR_ACENTO2, fg="#cce8ff").pack()

        main = tk.Frame(self.root, bg=COLOR_BG)
        main.pack(fill="both", expand=True, padx=10, pady=10)

        # Sidebar
        sidebar = tk.Frame(main, bg=COLOR_PANEL, width=195)
        sidebar.pack(side="left", fill="y", padx=(0, 8))
        sidebar.pack_propagate(False)
        tk.Label(sidebar, text="MENÚ", font=("Segoe UI", 10, "bold"),
                 bg=COLOR_PANEL, fg=COLOR_ACENTO).pack(pady=(15, 5))

        for texto, cmd in [
            ("🔍 Diagnóstico",  self.vista_diagnostico),
            ("💡 Consejos",     self.vista_consejos),
            ("🦷 Enfermedades", self.vista_enfermedades),
            ("🍽️ Alimentos",   self.vista_alimentos),
            ("📋 Reglas",       self.vista_reglas),
        ]:
            tk.Button(sidebar, text=texto, font=F_NORMAL,
                      bg=COLOR_BTN, fg="white", relief="flat",
                      activebackground=COLOR_BTN_HV, activeforeground="white",
                      cursor="hand2", pady=9, command=cmd
                      ).pack(fill="x", padx=10, pady=3)

        self.area = tk.Frame(main, bg=COLOR_BG)
        self.area.pack(side="left", fill="both", expand=True)
        self.vista_inicio()

    # ── Helpers ──────────────────────────────────────────────
    def _limpiar(self):
        for w in self.area.winfo_children():
            w.destroy()

    def _scroll_frame(self):
        cont = tk.Frame(self.area, bg=COLOR_BG)
        cont.pack(fill="both", expand=True)
        canvas = tk.Canvas(cont, bg=COLOR_BG, highlightthickness=0)
        sb = ttk.Scrollbar(cont, orient="vertical", command=canvas.yview)
        fi = tk.Frame(canvas, bg=COLOR_BG)
        fi.bind("<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=fi, anchor="nw")
        canvas.configure(yscrollcommand=sb.set)
        canvas.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        canvas.bind_all("<MouseWheel>",
                        lambda e: canvas.yview_scroll(-1*(e.delta//120), "units"))
        return fi

    def _titulo_sec(self, parent, texto):
        tk.Label(parent, text=texto, font=F_SUBTIT,
                 bg=COLOR_BG, fg=COLOR_ACENTO).pack(anchor="w", padx=5, pady=(10, 3))
        tk.Frame(parent, bg=COLOR_ACENTO, height=2).pack(fill="x", padx=5, pady=(0, 10))

    # ── Vistas ───────────────────────────────────────────────
    def vista_inicio(self):
        self._limpiar()
        f = tk.Frame(self.area, bg=COLOR_BG)
        f.pack(expand=True)
        tk.Label(f, text="🦷", font=("Segoe UI", 60),
                 bg=COLOR_BG, fg=COLOR_ACENTO).pack(pady=(30, 5))
        tk.Label(f, text="Bienvenido al Sistema Experto",
                 font=("Segoe UI", 17, "bold"), bg=COLOR_BG, fg=COLOR_TEXTO).pack()
        tk.Label(f, text="de Salud Bucal Básica",
                 font=("Segoe UI", 13), bg=COLOR_BG, fg=COLOR_SUB).pack(pady=(2, 20))
        for txt in [
            "✅ Diagnóstico basado en síntomas con motor de inferencia",
            "📊 Resumen de reglas disparadas por cada análisis",
            "📈 Gráfica de pastel con resultados del diagnóstico",
            "💡 Consejos de higiene bucal",
            "📚 Enfermedades bucales con nivel de urgencia",
            "🍽️ Análisis de riesgo de alimentos",
            "📋 Base de conocimiento con 17 reglas SI-ENTONCES",
        ]:
            tk.Label(f, text=txt, font=F_NORMAL,
                     bg=COLOR_BG, fg=COLOR_SUB).pack()
        tk.Label(f, text="\n⚠️ Este sistema NO reemplaza a un dentista profesional.",
                 font=F_SMALL, bg=COLOR_BG, fg="#f39c12").pack(pady=(15, 0))

    # ── Diagnóstico ──────────────────────────────────────────
    def vista_diagnostico(self):
        self._limpiar()
        self.checks = {}
        f = self._scroll_frame()
        self._titulo_sec(f, "🔍 Diagnóstico por Síntomas")
        tk.Label(f, text="Selecciona los síntomas que presentas:",
                 font=F_NORMAL, bg=COLOR_BG, fg=COLOR_SUB).pack(anchor="w", padx=10)

        grid = tk.Frame(f, bg=COLOR_BG)
        grid.pack(fill="x", padx=10, pady=5)
        for i, (clave, desc) in enumerate(SINTOMAS.items()):
            var = tk.BooleanVar()
            self.checks[clave] = var
            tk.Checkbutton(grid, text=f"  {desc}", variable=var,
                           font=F_NORMAL, bg=COLOR_PANEL, fg=COLOR_TEXTO,
                           selectcolor=COLOR_ACENTO2, activebackground=COLOR_PANEL,
                           activeforeground=COLOR_TEXTO, anchor="w",
                           padx=10, pady=5, relief="flat"
                           ).grid(row=i//2, column=i%2, sticky="ew", padx=4, pady=2)
        grid.columnconfigure(0, weight=1)
        grid.columnconfigure(1, weight=1)

        btn_frame = tk.Frame(f, bg=COLOR_BG)
        btn_frame.pack(pady=12)
        tk.Button(btn_frame, text="  🔍  Analizar síntomas  ",
                  font=("Segoe UI", 12, "bold"), bg=COLOR_ACENTO, fg="white",
                  relief="flat", cursor="hand2", pady=7,
                  command=self._ejecutar_diagnostico
                  ).pack(side="left", padx=5)
        tk.Button(btn_frame, text="  📊  Ver gráfica  ",
                  font=("Segoe UI", 12, "bold"), bg="#8e44ad", fg="white",
                  relief="flat", cursor="hand2", pady=7,
                  command=self._abrir_grafica
                  ).pack(side="left", padx=5)

        self._res_frame = tk.Frame(f, bg=COLOR_BG)
        self._res_frame.pack(fill="x", padx=10)

    def _ejecutar_diagnostico(self):
        for w in self._res_frame.winfo_children():
            w.destroy()

        hechos = {k for k, v in self.checks.items() if v.get()}
        self._hechos_activos   = hechos
        self._ultimo_resultado = ejecutar_inferencia(hechos)

        # ── Barra de resumen ─────────────────────────────────
        resumen = tk.Frame(self._res_frame, bg="#1b2a3b", padx=15, pady=8)
        resumen.pack(fill="x", pady=(5, 8))
        tk.Label(resumen, text="📊 Resumen del análisis",
                 font=("Segoe UI", 10, "bold"), bg="#1b2a3b", fg=COLOR_ACENTO).pack(anchor="w")

        fila = tk.Frame(resumen, bg="#1b2a3b")
        fila.pack(anchor="w", pady=(4, 0))

        for etiqueta, valor, color in [
            ("🔲 Síntomas seleccionados",  len(hechos),                 "#e0f0ff"),
            ("⚡ Reglas disparadas",        len(self._ultimo_resultado), "#f39c12"),
            ("🦷 Diagnósticos encontrados", len(self._ultimo_resultado), "#00b4d8"),
        ]:
            bloque = tk.Frame(fila, bg="#0d1b2a", padx=12, pady=6)
            bloque.pack(side="left", padx=5)
            tk.Label(bloque, text=str(valor),
                     font=("Segoe UI", 22, "bold"), bg="#0d1b2a", fg=color).pack()
            tk.Label(bloque, text=etiqueta,
                     font=("Segoe UI", 8), bg="#0d1b2a", fg="#a0b8cc").pack()

        if self._ultimo_resultado:
            ids = "  ·  ".join([r["id"] for r in self._ultimo_resultado])
            tk.Label(resumen, text=f"Reglas activadas: {ids}",
                     font=("Segoe UI", 9), bg="#1b2a3b", fg="#7090a0"
                     ).pack(anchor="w", pady=(4, 0))

        # ── Tarjetas de resultado ────────────────────────────
        if not self._ultimo_resultado:
            card = tk.Frame(self._res_frame, bg="#1e3a2f", padx=15, pady=12)
            card.pack(fill="x", pady=5)
            tk.Label(card, text="✅ Sin condición detectada",
                     font=("Segoe UI", 13, "bold"), bg="#1e3a2f", fg="#2ecc71").pack(anchor="w")
            tk.Label(card,
                     text="No se encontró ninguna condición con los síntomas seleccionados.\n"
                          "Mantén tu higiene bucal y visita al dentista preventivamente.",
                     font=F_NORMAL, bg="#1e3a2f", fg=COLOR_TEXTO, justify="left").pack(anchor="w", pady=4)
        else:
            tk.Label(self._res_frame, text="Resultados del diagnóstico:",
                     font=("Segoe UI", 12, "bold"), bg=COLOR_BG, fg=COLOR_TEXTO
                     ).pack(anchor="w", pady=(5, 3))
            for r in self._ultimo_resultado:
                enf  = ENFERMEDADES[r["conclusion"]]
                bg_c = "#2a1a1a" if enf["urgencia"] in ("Urgente", "Alta") else "#1a2a2a"
                card = tk.Frame(self._res_frame, bg=bg_c,
                                highlightbackground=enf["color"], highlightthickness=2,
                                padx=15, pady=10)
                card.pack(fill="x", pady=4)
                tk.Label(card,
                         text=f"🦷 {r['conclusion'].upper().replace('_',' ')}  ·  Urgencia: {enf['urgencia']}",
                         font=("Segoe UI", 12, "bold"), bg=bg_c, fg=enf["color"]).pack(anchor="w")
                tk.Label(card, text=f"Regla: {r['id']}  ·  {r['explicacion']}",
                         font=F_SMALL, bg=bg_c, fg=COLOR_SUB,
                         wraplength=560, justify="left").pack(anchor="w")
                tk.Label(card, text=f"📋 {enf['descripcion']}",
                         font=F_NORMAL, bg=bg_c, fg=COLOR_TEXTO,
                         wraplength=560, justify="left").pack(anchor="w", pady=(3, 0))
                tk.Label(card, text=f"💊 {enf['tratamiento']}",
                         font=F_NORMAL, bg=bg_c, fg="#a8d8a8",
                         wraplength=560, justify="left").pack(anchor="w")

        tk.Label(self._res_frame,
                 text="⚠️ Consulta siempre a un dentista para diagnóstico definitivo.",
                 font=F_SMALL, bg=COLOR_BG, fg="#f39c12").pack(pady=6)

    def _abrir_grafica(self):
        hechos    = {k for k, v in self.checks.items() if v.get()}
        resultados = ejecutar_inferencia(hechos)
        mostrar_grafica(self.root, hechos, resultados)

    # ── Consejos ─────────────────────────────────────────────
    def vista_consejos(self):
        self._limpiar()
        f = self._scroll_frame()
        self._titulo_sec(f, "💡 Consejos de Higiene Bucal")
        for tema, texto in CONSEJOS:
            card = tk.Frame(f, bg=COLOR_PANEL, padx=15, pady=10)
            card.pack(fill="x", padx=10, pady=4)
            tk.Label(card, text=tema, font=("Segoe UI", 11, "bold"),
                     bg=COLOR_PANEL, fg=COLOR_ACENTO).pack(anchor="w")
            tk.Label(card, text=texto, font=F_NORMAL, bg=COLOR_PANEL,
                     fg=COLOR_TEXTO, wraplength=600, justify="left").pack(anchor="w")

    # ── Enfermedades ─────────────────────────────────────────
    def vista_enfermedades(self):
        self._limpiar()
        f = self._scroll_frame()
        self._titulo_sec(f, "🦷 Enfermedades Bucales Comunes")
        for nombre, datos in ENFERMEDADES.items():
            card = tk.Frame(f, bg=COLOR_PANEL,
                            highlightbackground=datos["color"], highlightthickness=1,
                            padx=15, pady=12)
            card.pack(fill="x", padx=10, pady=5)
            top = tk.Frame(card, bg=COLOR_PANEL)
            top.pack(fill="x")
            tk.Label(top, text=nombre.upper().replace("_", " "),
                     font=("Segoe UI", 12, "bold"), bg=COLOR_PANEL, fg=datos["color"]).pack(side="left")
            tk.Label(top, text=f"   Urgencia: {datos['urgencia']}",
                     font=F_SMALL, bg=COLOR_PANEL, fg=datos["color"]).pack(side="left")
            tk.Label(card, text=datos["descripcion"], font=F_NORMAL,
                     bg=COLOR_PANEL, fg=COLOR_TEXTO, wraplength=600, justify="left").pack(anchor="w", pady=(4, 0))
            tk.Label(card, text=f"💊 {datos['tratamiento']}", font=F_NORMAL,
                     bg=COLOR_PANEL, fg="#a8d8a8", wraplength=600, justify="left").pack(anchor="w")

    # ── Alimentos ────────────────────────────────────────────
    def vista_alimentos(self):
        self._limpiar()
        f = self._scroll_frame()
        self._titulo_sec(f, "🍽️ Riesgo de Alimentos para tus Dientes")
        for alimento, riesgo, color, nota in ALIMENTOS:
            card = tk.Frame(f, bg=COLOR_PANEL, padx=15, pady=8)
            card.pack(fill="x", padx=10, pady=3)
            fila = tk.Frame(card, bg=COLOR_PANEL)
            fila.pack(fill="x")
            tk.Label(fila, text=alimento, font=("Segoe UI", 11, "bold"),
                     bg=COLOR_PANEL, fg=COLOR_TEXTO, width=24, anchor="w").pack(side="left")
            tk.Label(fila, text=f"Riesgo: {riesgo}",
                     font=("Segoe UI", 11, "bold"), bg=COLOR_PANEL, fg=color).pack(side="left")
            tk.Label(card, text=nota, font=F_SMALL, bg=COLOR_PANEL,
                     fg=COLOR_SUB, wraplength=580, justify="left").pack(anchor="w")

    # ── Reglas ───────────────────────────────────────────────
    def vista_reglas(self):
        self._limpiar()
        f = self._scroll_frame()
        self._titulo_sec(f, "📋 Base de Conocimiento · Reglas SI-ENTONCES")
        for r in REGLAS:
            conds = "  AND  ".join(r["condiciones"])
            card  = tk.Frame(f, bg=COLOR_PANEL, padx=15, pady=10)
            card.pack(fill="x", padx=10, pady=3)
            enf_color = ENFERMEDADES[r["conclusion"]]["color"]
            tk.Label(card, text=f"{r['id']}  →  SI:",
                     font=("Segoe UI", 10, "bold"), bg=COLOR_PANEL, fg=COLOR_ACENTO).pack(anchor="w")
            tk.Label(card, text=f"   {conds}", font=F_SMALL,
                     bg=COLOR_PANEL, fg=COLOR_SUB, wraplength=580, justify="left").pack(anchor="w")
            tk.Label(card,
                     text=f"   ENTONCES → {r['conclusion'].upper().replace('_', ' ')}",
                     font=("Segoe UI", 11, "bold"), bg=COLOR_PANEL, fg=enf_color).pack(anchor="w")


# ── Punto de entrada ─────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    AppOdontologia(root)
    root.mainloop()