from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color palette
    c_navy = RGBColor(15, 23, 42)      # #0F172A
    c_blue_dark = RGBColor(30, 58, 138) # #1E3A8A
    c_blue_card = RGBColor(30, 41, 59)  # #1E293B
    c_gold = RGBColor(212, 175, 55)    # #D4AF37
    c_emerald = RGBColor(16, 185, 129) # #10B981
    c_red = RGBColor(239, 68, 68)      # #EF4444
    c_text_white = RGBColor(248, 250, 252)
    c_text_muted = RGBColor(148, 163, 184)
    c_white = RGBColor(255, 255, 255)

    blank_layout = prs.slide_layouts[6]

    def add_header(slide, title_text, category_text, speaker_text):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = c_navy
        bg.line.fill.background()

        # Top Category & Speaker bar
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = f"{category_text.upper()}  |  {speaker_text}"
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = c_gold
        p_cat.font.name = 'Segoe UI'

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.8))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = c_text_white
        p_t.font.name = 'Segoe UI'

        # Bottom footer
        ft_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.7), Inches(0.4))
        tf_ft = ft_box.text_frame
        p_ft = tf_ft.paragraphs[0]
        p_ft.text = "UNSA · EPIS · Gestión de Proyectos de Software · Control Económico PANVIZ · Equipo: Chambilla, Gutiérrez, Mollo, Suclle"
        p_ft.font.size = Pt(9)
        p_ft.font.color.rgb = c_text_muted
        p_ft.font.name = 'Segoe UI'

    # =========================================================================
    # SLIDE 1: Caso y Criterios Contables (Suclle Suca)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_header(s1, "Caso PANVIZ y Criterios Contables Fundamentales", "Diapositiva 01 · Fundamento y Caso de Estudio", "Orador: Suclle Suca, Michael Benjamin (Min 1)")
    
    b1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(5.6), Inches(4.9))
    b1.fill.solid()
    b1.fill.fore_color.rgb = c_blue_card
    b1.line.color.rgb = c_blue_dark
    tf1 = b1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "Escenario Didáctico: Andes Software & PANVIZ"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = c_gold
    
    pts_s1_left = [
        ("Objeto del Contrato:", "Desarrollo y puesta en marcha de PANVIZ para vigilancia sanitaria en salud pública."),
        ("Hito 1 (Mes 1):", "Carga y visualización de indicadores sanitarios. Entregado y aceptado."),
        ("Hito 2 (Mes 2):", "Módulo de alertas tempranas y reportes automatizados (en ejecución)."),
        ("Delimitación:", "Moneda en Soles (PEN), sin saldos iniciales, omisión didáctica de IGV, IR y depreciación."),
        ("Objetivo Económico:", "Vincular registros contables verificables con decisiones de continuidad operativa del servicio.")
    ]
    for title, desc in pts_s1_left:
        p = tf1.add_paragraph()
        p.text = f"• {title} {desc}"
        p.font.size = Pt(11)
        p.font.color.rgb = c_text_white
        p.space_before = Pt(8)

    b2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.7), Inches(5.7), Inches(4.9))
    b2.fill.solid()
    b2.fill.fore_color.rgb = c_blue_card
    b2.line.color.rgb = c_blue_dark
    tf2 = b2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    p2.text = "Criterios Contables Normativos Clave (NIIF / PCGE)"
    p2.font.size = Pt(15)
    p2.font.bold = True
    p2.font.color.rgb = c_gold
    
    pts_s1_right = [
        ("NIIF 15 (Anticipo S/ 9,000):", "No es ingreso ganado; es un pasivo por obligación de desempeño no satisfecha al cierre del mes."),
        ("NIC 16 (Hardware S/ 12,000):", "Se reconoce como Activo Fijo (PPE) a costo histórico, no como gasto, por su vida útil multianual."),
        ("NIC 38 / Costo del Servicio:", "Remuneraciones (S/ 15,000) y nube (S/ 2,000) se imputan a costo directo del servicio, no a intangible."),
        ("Principio del Devengo (OP10):", "Sueldos administrativos (S/ 1,500) se reconocen como gasto del mes aunque queden por pagar."),
        ("Control de Lectura 43:", "Los EEFF iluminan la gestión; el registro sin análisis de flujos y liquidez conduce a la insolvencia.")
    ]
    for title, desc in pts_s1_right:
        p = tf2.add_paragraph()
        p.text = f"• {title} {desc}"
        p.font.size = Pt(11)
        p.font.color.rgb = c_text_white
        p.space_before = Pt(8)

    # =========================================================================
    # SLIDE 2: Libro Diario, Mayor y Comprobación (Chambilla Perca)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Catálogo, Partida Doble y Balance de Comprobación", "Diapositiva 02 · Registro de Operaciones OP01 - OP11", "Orador: Chambilla Perca, Ricardo Mauricio (Min 2)")
    
    b_s2_left = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(6.0), Inches(4.9))
    b_s2_left.fill.solid()
    b_s2_left.fill.fore_color.rgb = c_blue_card
    b_s2_left.line.color.rgb = c_blue_dark
    tf_s2_l = b_s2_left.text_frame
    tf_s2_l.word_wrap = True
    p = tf_s2_l.paragraphs[0]
    p.text = "Resumen de las 11 Operaciones del Mes"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = c_gold
    
    op_list = [
        "OP01: Aporte socios en bancos S/ 40,000",
        "OP02: Compra equipos S/ 12,000 (8k bancos, 4k proveedor)",
        "OP03: Préstamo bancario recibido S/ 10,000 a 6 meses",
        "OP04: Anticipo salud pública S/ 9,000 (pasivo diferido)",
        "OP05: Remuneraciones desarrollo pagadas S/ 15,000",
        "OP06: Servicios de nube pagados S/ 2,000",
        "OP07: Gastos administrativos pagados S/ 3,000",
        "OP08: Hito 1 aceptado S/ 24,000 (16k cobrado, 8k a 45d)",
        "OP09: Amortización a proveedor de equipos S/ 2,000",
        "OP10: Sueldos admin. devengados pendientes S/ 1,500",
        "OP11: Intereses préstamo bancario pagados S/ 500"
    ]
    for op in op_list:
        p = tf_s2_l.add_paragraph()
        p.text = f"• {op}"
        p.font.size = Pt(10)
        p.font.color.rgb = c_text_white
        p.space_before = Pt(3)

    b_s2_right = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(1.7), Inches(5.4), Inches(4.9))
    b_s2_right.fill.solid()
    b_s2_right.fill.fore_color.rgb = c_blue_card
    b_s2_right.line.color.rgb = c_blue_dark
    tf_s2_r = b_s2_right.text_frame
    tf_s2_r.word_wrap = True
    p = tf_s2_r.paragraphs[0]
    p.text = "Verificación de Partida Doble y Saldos"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = c_gold

    metrics_s2 = [
        ("Total Debe (Libro Diario):", "S/ 119,000.00"),
        ("Total Haber (Libro Diario):", "S/ 119,000.00"),
        ("Control Partida Doble:", "CUADRADO EXACTO (S/ 0.00)"),
        ("Total Saldos Deudores:", "S/ 86,500.00"),
        ("Total Saldos Acreedores:", "S/ 86,500.00"),
        ("Control Balance Comprobación:", "CONFORME (S/ 0.00)")
    ]
    for lbl, val in metrics_s2:
        p = tf_s2_r.add_paragraph()
        p.text = f"{lbl}  {val}"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = c_emerald if "EXACTO" in val or "CONFORME" in val else c_text_white
        p.space_before = Pt(8)

    p_note = tf_s2_r.add_paragraph()
    p_note.text = "\nCuentas del Catálogo: 14 cuentas maestras codificadas bajo PCGE y sincronizadas con GnuCash."
    p_note.font.size = Pt(10)
    p_note.font.italic = True
    p_note.font.color.rgb = c_text_muted

    # =========================================================================
    # SLIDE 3: Estado de Situación Financiera y Conciliación (Gutiérrez Ccama)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Estado de Situación Financiera y Conciliación GnuCash", "Diapositiva 03 · Balance General al 30/11/2026", "Orador: Gutiérrez Ccama, Juan Diego (Min 3)")
    
    b_s3_act = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(3.8), Inches(4.9))
    b_s3_act.fill.solid()
    b_s3_act.fill.fore_color.rgb = c_blue_card
    b_s3_act.line.color.rgb = c_blue_dark
    tf_act = b_s3_act.text_frame
    tf_act.word_wrap = True
    p = tf_act.paragraphs[0]
    p.text = "ACTIVO TOTAL: S/ 64,500"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = c_gold
    
    pts_act = [
        ("Bancos (1041):", "S/ 44,500.00"),
        ("Clientes CxC (1212):", "S/ 8,000.00"),
        ("  Total Corriente:", "S/ 52,500.00"),
        ("Equipos Cómputo (3361):", "S/ 12,000.00"),
        ("  Total No Corriente:", "S/ 12,000.00"),
        ("Estructura Activo:", "81.4% Corriente | 18.6% No Cte.")
    ]
    for lbl, val in pts_act:
        p = tf_act.add_paragraph()
        p.text = f"• {lbl} {val}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = c_text_white
        p.space_before = Pt(6)

    b_s3_pas = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.8), Inches(1.7), Inches(3.8), Inches(4.9))
    b_s3_pas.fill.solid()
    b_s3_pas.fill.fore_color.rgb = c_blue_card
    b_s3_pas.line.color.rgb = c_blue_dark
    tf_pas = b_s3_pas.text_frame
    tf_pas.word_wrap = True
    p = tf_pas.paragraphs[0]
    p.text = "PASIVO Y PATRIMONIO: S/ 64,500"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = c_gold
    
    pts_pas = [
        ("Proveedores (4212):", "S/ 2,000.00"),
        ("Préstamo Bancario (4511):", "S/ 10,000.00"),
        ("Anticipo Clientes (4699):", "S/ 9,000.00"),
        ("Remun. por Pagar (4111):", "S/ 1,500.00"),
        ("  Total Pasivo Cte.:", "S/ 22,500.00"),
        ("Capital Social (5011):", "S/ 40,000.00"),
        ("Utilidad Neta (5911):", "S/ 2,000.00"),
        ("  Total Patrimonio:", "S/ 42,000.00")
    ]
    for lbl, val in pts_pas:
        p = tf_pas.add_paragraph()
        p.text = f"• {lbl} {val}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = c_text_white
        p.space_before = Pt(5)

    b_s3_conc = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.8), Inches(1.7), Inches(3.7), Inches(4.9))
    b_s3_conc.fill.solid()
    b_s3_conc.fill.fore_color.rgb = c_blue_card
    b_s3_conc.line.color.rgb = c_blue_dark
    tf_conc = b_s3_conc.text_frame
    tf_conc.word_wrap = True
    p = tf_conc.paragraphs[0]
    p.text = "Conciliación Calc vs GnuCash"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = c_gold

    pts_conc = [
        ("Bancos:", "Calc S/ 44.5k = Gnu S/ 44.5k"),
        ("Clientes CxC:", "Calc S/ 8k = Gnu S/ 8k"),
        ("Equipos:", "Calc S/ 12k = Gnu S/ 12k"),
        ("Pasivos:", "Calc S/ 22.5k = Gnu S/ 22.5k"),
        ("Patrimonio:", "Calc S/ 42k = Gnu S/ 42k"),
        ("Resultado:", "Calc S/ 2k = Gnu S/ 2k"),
        ("DIFERENCIA NETA:", "S/ 0.00 (CUADRADO)"),
        ("Evidencia:", "Reportes PDF & Capturas GnuCash")
    ]
    for lbl, val in pts_conc:
        p = tf_conc.add_paragraph()
        p.text = f"• {lbl} {val}"
        p.font.size = Pt(10)
        p.font.color.rgb = c_emerald if "S/ 0.00" in val else c_text_white
        p.space_before = Pt(4)

    # =========================================================================
    # SLIDE 4: Resultados, Flujo y Riesgo de Caja (Mollo Chuquicaña)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Resultados, Efectivo y la Paradoja de Liquidez", "Diapositiva 04 · Desempeño y Flujos de Efectivo", "Orador: Mollo Chuquicaña, Dolly Yadhira (Min 4)")
    
    b_s4_res = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(5.6), Inches(4.9))
    b_s4_res.fill.solid()
    b_s4_res.fill.fore_color.rgb = c_blue_card
    b_s4_res.line.color.rgb = c_blue_dark
    tf_res = b_s4_res.text_frame
    tf_res.word_wrap = True
    p = tf_res.paragraphs[0]
    p.text = "Estado de Resultados vs Flujo Directo"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = c_gold

    pts_res = [
        ("Ingresos Software (7041):", "S/ 24,000.00 (100.0%)"),
        ("(-) Costo Servicio (69):", "S/ 17,000.00 (70.8%)"),
        ("  Utilidad Bruta:", "S/ 7,000.00 (29.2%)"),
        ("(-) Gastos Admin. (94):", "S/ 4,500.00 (18.8%)"),
        ("  Utilidad Operativa:", "S/ 2,500.00 (10.4%)"),
        ("(-) Gastos Financ. (97):", "S/ 500.00 (2.1%)"),
        ("UTILIDAD NETA FINAL:", "S/ 2,000.00 (Margen: 8.33%)"),
        ("Flujo Operativo (NIC 7):", "+S/ 4,500.00"),
        ("Flujo Inversión (Equipos):", "-S/ 10,000.00"),
        ("Flujo Financiación:", "+S/ 50,000.00 (Socios + Crédito)")
    ]
    for lbl, val in pts_res:
        p = tf_res.add_paragraph()
        p.text = f"• {lbl} {val}"
        p.font.size = Pt(10)
        p.font.color.rgb = c_emerald if "UTILIDAD NETA" in lbl else c_text_white
        p.space_before = Pt(3)

    b_s4_caja = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.7), Inches(5.7), Inches(4.9))
    b_s4_caja.fill.solid()
    b_s4_caja.fill.fore_color.rgb = c_blue_card
    b_s4_caja.line.color.rgb = c_blue_dark
    tf_caja = b_s4_caja.text_frame
    tf_caja.word_wrap = True
    p = tf_caja.paragraphs[0]
    p.text = "Presupuesto 15 Días y la Trampa de 45 Días"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = c_gold

    pts_caja = [
        ("Saldo Inicial en Bancos:", "S/ 44,500.00"),
        ("(-) Egresos Ineludibles 15 días:", "S/ 23,500.00"),
        ("  • Nómina de desarrollo:", "S/ 18,000.00"),
        ("  • Infraestructura en nube:", "S/ 2,000.00"),
        ("  • Deuda restante equipos:", "S/ 2,000.00"),
        ("  • Sueldos admin. pendientes:", "S/ 1,500.00"),
        ("Excedente al Día 15:", "S/ 21,000.00 (Cobertura: 1.89)"),
        ("LA TRAMPA DE LIQUIDEZ (DÍA 45):", "Días 16 a 44 demandan > S/ 23,500 sin nuevos cobros."),
        ("Riesgo Inminente:", "Déficit de S/ 2,500 en día 35-44 antes de cobrar los S/ 8,000.")
    ]
    for lbl, val in pts_caja:
        p = tf_caja.add_paragraph()
        p.text = f"• {lbl} {val}"
        p.font.size = Pt(10)
        p.font.color.rgb = c_red if "TRAMPA" in lbl or "Riesgo" in lbl else c_text_white
        p.space_before = Pt(3)

    # =========================================================================
    # SLIDE 5: Tres Decisiones Estratégicas y Continuidad Sanitaria (Suclle & Mollo)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Tres Decisiones Gerenciales y Continuidad de PANVIZ", "Diapositiva 05 · Gobierno y Salud Pública", "Oradores: Suclle Suca & Mollo Chuquicaña (Min 5)")
    
    decisiones = [
        ("1. Factoring / Cobro Hito 1", "Evidencia: Cta 1212 retiene S/ 8,000 a 45 días.\nMedida: Negociar adenda de pronto pago o factoring bancario al día 15 con descuento del 2.5% (costo S/ 200).\nImpacto: Inyección inmediata de S/ 7,800 líquidos que anula el déficit de caja del día 35 y blinda salarios.\nResponsable: Mollo Chuquicaña · Plazo: 7 días."),
        ("2. Aceleración del Hito 2", "Evidencia: Pasivo 4699 tiene S/ 9,000 de anticipo no devengado.\nMedida: Sprint intensivo para entregar el módulo de alertas y reportes al día 25, devengando ingresos (NIIF 15) y habilitando la facturación siguiente.\nImpacto: Pone en marcha alertas sanitarias y genera nuevo flujo.\nResponsable: Chambilla Perca · Plazo: 25 días."),
        ("3. Reprogramación y Nube", "Evidencia: Deuda equipos S/ 2k y nube S/ 2k/mes.\nMedida: Negociar diferir saldo de hardware a 30 días y configurar autoscaling / instancias reservadas en cloud (-20%).\nImpacto: Preserva S/ 2,400 de colchón y garantiza SLA 99.9% para epidemiología.\nResponsable: Gutiérrez Ccama · Plazo: 10 días.")
    ]
    
    for idx, (title, desc) in enumerate(decisiones):
        left_pos = Inches(0.8 + idx * 3.95)
        b = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, Inches(1.7), Inches(3.8), Inches(4.9))
        b.fill.solid()
        b.fill.fore_color.rgb = c_blue_card
        b.line.color.rgb = c_blue_dark
        tf = b.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = c_gold
        
        for line in desc.split('\n'):
            p = tf.add_paragraph()
            p.text = line
            p.font.size = Pt(9.5)
            p.font.color.rgb = c_text_white
            p.space_before = Pt(4)

    prs.save(output_path)
    print(f"Presentación PPTX generada exitosamente en: {output_path}")

if __name__ == "__main__":
    import os
    target = os.path.join(r"C:\Users\micha\Downloads\Borrar entregable 6\GPS-Entregable-6", "PANVIZ_Presentacion.pptx")
    create_presentation(target)
