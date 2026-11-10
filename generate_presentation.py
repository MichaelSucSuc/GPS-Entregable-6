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
        # Background
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
        p_ft.text = "UNSA · EPIS · Gestión de Proyectos de Software · Control Económico PANVIZ (Equipo 06)"
        p_ft.font.size = Pt(9)
        p_ft.font.color.rgb = c_text_muted
        p_ft.font.name = 'Segoe UI'

    # =========================================================================
    # SLIDE 1: Caso y Criterios Contables
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_header(s1, "Caso PANVIZ y Criterios Contables Fundamentales", "Diapositiva 01 · Fundamento y Caso de Estudio", "Orador: Michael Benjamin Suclle Suca (1 min)")
    
    # Left Box: Caso
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

    # Right Box: Criterios Contables
    b2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.7), Inches(5.7), Inches(4.9))
    b2.fill.solid()
    b2.fill.fore_color.rgb = c_blue_card
    b2.line.color.rgb = c_blue_dark
    tf2 = b2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "Criterios Contables NIIF / PCGE Aplicados"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = c_emerald

    pts_s1_right = [
        ("Principio de Devengado (NIIF 15):", "El Hito 1 se reconoce como ingreso (S/ 24,000) por cumplimiento de la obligación de desempeño, aunque S/ 8,000 queden pendientes de cobro."),
        ("Anticipo de Clientes como Pasivo (S/ 9,000):", "No es ganancia ni utilidad. Representa la obligación exigible de prestar el servicio en el mes siguiente."),
        ("Equipos como Activo No Corriente (NIC 16):", "S/ 12,000 en hardware no se cargan como gasto íntegro del mes; son recursos que generarán beneficios futuros plurianuales."),
        ("Clasificación de Intereses (NIC 7, S/ 500):", "Declarados en Actividades de Operación por sustentar el capital de trabajo de la marcha diaria."),
        ("Ecuación Patrimonial:", "Activo = Pasivo + Patrimonio rigurosamente balanceado.")
    ]
    for title, desc in pts_s1_right:
        p = tf2.add_paragraph()
        p.text = f"• {title} {desc}"
        p.font.size = Pt(11)
        p.font.color.rgb = c_text_white
        p.space_before = Pt(8)

    # =========================================================================
    # SLIDE 2: Situación Financiera y Solvencia
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Estado de Situación Financiera al Cierre del Mes 1", "Diapositiva 02 · Estructura Patrimonial y Solvencia", "Orador: Rodrigo Alexander Fernandez Huarca (1 min)")

    # Card 1: Activos
    c1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(3.7), Inches(4.9))
    c1.fill.solid()
    c1.fill.fore_color.rgb = c_blue_card
    c1.line.color.rgb = c_blue_dark
    tfc1 = c1.text_frame
    tfc1.word_wrap = True
    p = tfc1.paragraphs[0]
    p.text = "ACTIVOS: S/ 64,500"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = c_emerald
    
    act_items = [
        ("Activo Corriente:", "S/ 52,500 (81.4%)"),
        ("  • Bancos (Cta. Cte.):", "S/ 44,500.00"),
        ("  • Cuentas por Cobrar:", "S/ 8,000.00"),
        ("    (Cobro a 45 días)", ""),
        ("Activo No Corriente:", "S/ 12,000 (18.6%)"),
        ("  • Equipos Informáticos:", "S/ 12,000.00"),
        ("Diagnóstico Activos:", "Alta concentración en bancos originada por aportes y préstamos, no por rotación comercial.")
    ]
    for t, v in act_items:
        p = tfc1.add_paragraph()
        p.text = f"{t} {v}"
        p.font.size = Pt(11)
        p.font.color.rgb = c_text_white
        p.space_before = Pt(6)

    # Card 2: Pasivos
    c2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.8), Inches(1.7), Inches(3.7), Inches(4.9))
    c2.fill.solid()
    c2.fill.fore_color.rgb = c_blue_card
    c2.line.color.rgb = c_blue_dark
    tfc2 = c2.text_frame
    tfc2.word_wrap = True
    p = tfc2.paragraphs[0]
    p.text = "PASIVOS: S/ 22,500"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = c_gold

    pas_items = [
        ("Pasivo Corriente:", "S/ 22,500 (100%)"),
        ("  • Proveedores Equipos:", "S/ 2,000.00"),
        ("  • Préstamo Bancario (6m):", "S/ 10,000.00"),
        ("  • Anticipos Clientes:", "S/ 9,000.00"),
        ("  • Sueldos por Pagar:", "S/ 1,500.00"),
        ("Pasivo No Corriente:", "S/ 0.00"),
        ("Diagnóstico Pasivos:", "Obligaciones exigibles a corto plazo que comprometen la entrega del software.")
    ]
    for t, v in pas_items:
        p = tfc2.add_paragraph()
        p.text = f"{t} {v}"
        p.font.size = Pt(11)
        p.font.color.rgb = c_text_white
        p.space_before = Pt(6)

    # Card 3: Patrimonio & Cuadre
    c3 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.8), Inches(1.7), Inches(3.7), Inches(4.9))
    c3.fill.solid()
    c3.fill.fore_color.rgb = c_blue_card
    c3.line.color.rgb = c_blue_dark
    tfc3 = c3.text_frame
    tfc3.word_wrap = True
    p = tfc3.paragraphs[0]
    p.text = "PATRIMONIO: S/ 42,000"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = c_text_white

    pat_items = [
        ("Capital Social:", "S/ 40,000.00"),
        ("Resultado del Mes:", "S/ 2,000.00"),
        ("Total Pasivo + Patr.:", "S/ 64,500.00"),
        ("Control Ecuación:", "ACTIVO = PASIVO + PATR."),
        ("Diferencia:", "S/ 0.00 (EXACTO)"),
        ("Razón Corriente:", "52,500 / 22,500 = 2.33"),
        ("Conciliación GnuCash:", "100% verificado contra balance exportado.")
    ]
    for t, v in pat_items:
        p = tfc3.add_paragraph()
        p.text = f"{t} {v}"
        p.font.size = Pt(11)
        p.font.color.rgb = c_text_white
        p.space_before = Pt(6)

    # =========================================================================
    # SLIDE 3: Resultado Económico vs Flujo de Efectivo
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Resultado del Ejercicio frente al Flujo de Efectivo", "Diapositiva 03 · Estado de Resultados y Liquidez", "Orador: Cielo Cristal Meza Vizcarra (1 min)")

    # Left: Estado de Resultados
    b_er = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(5.6), Inches(4.9))
    b_er.fill.solid()
    b_er.fill.fore_color.rgb = c_blue_card
    b_er.line.color.rgb = c_blue_dark
    tfe = b_er.text_frame
    tfe.word_wrap = True
    p = tfe.paragraphs[0]
    p.text = "Estado de Resultados (Devengado)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = c_gold

    er_lines = [
        ("Ingresos por Software (Hito 1):", "S/ 24,000.00", "100.0%"),
        ("(-) Costo de Remuneraciones Desarrollo:", "S/ 15,000.00", "62.5%"),
        ("(-) Costo de Servicios de Nube:", "S/ 2,000.00", "8.3%"),
        ("UTILIDAD BRUTA DEL PROYECTO:", "S/ 7,000.00", "29.2%"),
        ("(-) Gastos Administrativos Generales:", "S/ 3,000.00", "12.5%"),
        ("(-) Gastos Adm. Sueldos Devengados:", "S/ 1,500.00", "6.3%"),
        ("UTILIDAD OPERATIVA:", "S/ 2,500.00", "10.4%"),
        ("(-) Gastos Financieros (Intereses):", "S/ 500.00", "2.1%"),
        ("UTILIDAD NETA (MARGEN NETO 8.33%):", "S/ 2,000.00", "8.3%")
    ]
    for nom, val, pct in er_lines:
        p = tfe.add_paragraph()
        p.text = f"{nom:<32} {val:>12} ({pct})"
        p.font.size = Pt(10)
        p.font.color.rgb = c_emerald if "UTILIDAD" in nom else c_text_white
        p.font.bold = "UTILIDAD" in nom
        p.space_before = Pt(4)

    # Right: Flujo de Efectivo
    b_fe = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.7), Inches(5.7), Inches(4.9))
    b_fe.fill.solid()
    b_fe.fill.fore_color.rgb = c_blue_card
    b_fe.line.color.rgb = c_blue_dark
    tff = b_fe.text_frame
    tff.word_wrap = True
    p = tff.paragraphs[0]
    p.text = "Flujo de Efectivo - Método Directo"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = c_emerald

    fe_lines = [
        ("1. Actividades de Operación:", "+S/ 4,500.00"),
        ("  • Cobranza Hito 1:", "S/ 16,000.00"),
        ("  • Anticipo Cliente recibido:", "S/ 9,000.00"),
        ("  • Pagos Operativos (Nómina+Nube+Adm+Int):", "-S/ 20,500.00"),
        ("2. Actividades de Inversión (Equipos):", "-S/ 10,000.00"),
        ("  • Pago inicial S/ 8,000 + Amortización S/ 2,000", ""),
        ("3. Actividades de Financiación:", "+S/ 50,000.00"),
        ("  • Aporte de socios (S/ 40k) + Préstamo (S/ 10k)", ""),
        ("SALDO FINAL EN BANCOS:", "S/ 44,500.00"),
        ("Conciliación con Mayor y GnuCash:", "DIFERENCIA S/ 0.00")
    ]
    for t, v in fe_lines:
        p = tff.add_paragraph()
        p.text = f"{t} {v}"
        p.font.size = Pt(10)
        p.font.color.rgb = c_gold if "SALDO FINAL" in t or "1." in t or "2." in t or "3." in t else c_text_white
        p.font.bold = "SALDO" in t or "1." in t or "2." in t or "3." in t
        p.space_before = Pt(4)

    # =========================================================================
    # SLIDE 4: Riesgo de Caja y Presupuesto
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Presupuesto de Caja a 15 Días y la Trampa de la Liquidez", "Diapositiva 04 · Presupuesto de Tesorería y Riesgo Financiero", "Orador: Gabriela Nayely Borda Espinoza (1 min)")

    # Left: Presupuesto 15 Días
    bp1 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(5.6), Inches(4.9))
    bp1.fill.solid()
    bp1.fill.fore_color.rgb = c_blue_card
    bp1.line.color.rgb = c_blue_dark
    tfp1 = bp1.text_frame
    tfp1.word_wrap = True
    p = tfp1.paragraphs[0]
    p.text = "Presupuesto de Caja (Primeros 15 Días)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = c_gold

    caja_pts = [
        ("Saldo Inicial en Bancos:", "S/ 44,500.00"),
        ("(+) Cobros proyectados quincena:", "S/ 0.00 (Aplazado 45 días)"),
        ("(-) Remuneraciones técnicas previstas:", "S/ 18,000.00"),
        ("(-) Servicios de infraestructura en nube:", "S/ 2,000.00"),
        ("(-) Deuda restante proveedor equipos:", "S/ 2,000.00"),
        ("(-) Remuneraciones administrativas pendientes:", "S/ 1,500.00"),
        ("TOTAL EGRESOS EN 15 DÍAS:", "S/ 23,500.00"),
        ("SALDO FINAL AL DÍA 15 (EXCEDENTE):", "S/ 21,000.00"),
        ("COBERTURA INMEDIATA (44.5k / 23.5k):", "1.89 (Cobertura quincenal)")
    ]
    for t, v in caja_pts:
        p = tfp1.add_paragraph()
        p.text = f"• {t:<40} {v}"
        p.font.size = Pt(10)
        p.font.color.rgb = c_emerald if "SALDO" in t or "COBERTURA" in t else c_text_white
        p.font.bold = "TOTAL" in t or "SALDO" in t or "COBERTURA" in t
        p.space_before = Pt(5)

    # Right: La Ilusión de la Razón Corriente
    bp2 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.7), Inches(5.7), Inches(4.9))
    bp2.fill.solid()
    bp2.fill.fore_color.rgb = c_blue_card
    bp2.line.color.rgb = c_red
    tfp2 = bp2.text_frame
    tfp2.word_wrap = True
    p = tfp2.paragraphs[0]
    p.text = "¡Alerta! La Trampa de la Razón Corriente y la Utilidad"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = c_red

    crit_pts = [
        ("1. La Ilusión de la Utilidad (S/ 2,000):", "Es contable-devengada. Incluye S/ 8,000 por cobrar que no pagan sueldos hoy."),
        ("2. La Razón Corriente (2.33) engaña:", "El activo corriente contiene S/ 8,000 ilíquidos a 45 días y el pasivo tiene S/ 9,000 de anticipo que exige quemar caja en desarrollo sin generar nuevo efectivo."),
        ("3. Origen del Efectivo:", "De los S/ 44,500 iniciales, S/ 50,000 provienen de capital social y préstamo. La operación real sólo generó S/ 4,500 netos."),
        ("4. Escenario de Estrés (Día 16 al 45):", "En los siguientes 30 días se requieren > S/ 23,500 para nómina y nube de PANVIZ. Con S/ 21,000 de saldo, ¡se genera un DÉFICIT proyectado de -S/ 2,500 si no se acelera la cobranza!")
    ]
    for t, v in crit_pts:
        p = tfp2.add_paragraph()
        p.text = f"{t} {v}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = c_text_white
        p.space_before = Pt(6)

    # =========================================================================
    # SLIDE 5: Decisiones Estratégicas y Salud Pública
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Tres Decisiones Estratégicas y Continuidad de Salud Pública", "Diapositiva 05 · Decisiones Gerenciales y Sostenibilidad", "Orador: Italo Frankdux Ccoscco Alvis (1 min)")

    dec_items = [
        ("DECISIÓN 1: Cobranza Anticipada / Factoring de Cuenta de S/ 8,000",
         "Evidencia Contable: Cuentas por cobrar a 45 días provocan déficit en día 35.",
         "Acción & Responsable: Gerencia General negociará adenda por pronto pago (descuento 2-3%) o factoring con banco del proyecto. Plazo: 7 días.",
         "Impacto en PANVIZ: Ingreso inmediato de ~S/ 7,760 que cierra la brecha de liquidez antes del día 45.",
         c_emerald),
        ("DECISIÓN 2: Proteger Fondo Intangible de Nube y Personal Técnico",
         "Evidencia Contable: Presupuesto quincenal de S/ 20,000 indispensables para desarrollo y cloud.",
         "Acción & Responsable: Dirección de TI y Finanzas establecerán cuenta de reserva intangible para infraestructura cloud y salarios del equipo core. Plazo: Inmediato (3 días).",
         "Impacto en Salud Pública: Cero interrupciones en la ingesta de datos sanitarios y disponibilidad 24/7 de indicadores.",
         c_gold),
        ("DECISIÓN 3: Entrega Quincenal por Sub-hitos del Módulo Anticipado",
         "Evidencia Contable: Pasivo de S/ 9,000 por anticipo no genera nuevo flujo y consume horas de desarrollo.",
         "Acción & Responsable: Líder de Proyecto pactará entregas intermedias del módulo de alertas cada 15 días con la entidad de salud. Plazo: 10 días.",
         "Impacto en Salud Pública: Despliegue anticipado de alertas epidemiológicas para respuesta sanitaria temprana.",
         c_blue_dark)
    ]

    for idx, (tit, ev, acc, imp, col_b) in enumerate(dec_items):
        y_pos = Inches(1.7 + idx * 1.7)
        box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y_pos, Inches(11.7), Inches(1.55))
        box.fill.solid()
        box.fill.fore_color.rgb = c_blue_card
        box.line.color.rgb = col_b
        box.line.width = Pt(1.5)
        tf = box.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = tit
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = col_b

        p2 = tf.add_paragraph()
        p2.text = f"• {ev} | {acc}"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = c_text_white
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = f"• Impacto en Salud Pública: {imp}"
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = c_emerald
        p3.space_before = Pt(2)

    prs.save(output_path)
    print(f"Presentación PPTX generada exitosamente en: {output_path}")

if __name__ == '__main__':
    out_pptx = r"C:\Users\micha\Downloads\Borrar entregable 6\GPS-Entregable-6\PANVIZ_Presentacion_5Diapositivas.pptx"
    create_presentation(out_pptx)
