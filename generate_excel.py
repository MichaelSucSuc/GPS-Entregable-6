import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build_panviz_excel(filepath):
    wb = openpyxl.Workbook()
    wb.remove(wb.active) # Remove default sheet

    # Typography & Styles
    font_title = Font(name='Segoe UI', size=14, bold=True, color='1E293B')
    font_subtitle = Font(name='Segoe UI', size=10, italic=True, color='64748B')
    font_header = Font(name='Segoe UI', size=11, bold=True, color='FFFFFF')
    font_sub_header = Font(name='Segoe UI', size=10, bold=True, color='1E293B')
    font_bold = Font(name='Segoe UI', size=10, bold=True, color='0F172A')
    font_regular = Font(name='Segoe UI', size=10, color='334155')
    font_success = Font(name='Segoe UI', size=10, bold=True, color='047857')

    fill_navy = PatternFill(start_color='1E3A8A', end_color='1E3A8A', fill_type='solid') # Navy Header
    fill_slate = PatternFill(start_color='334155', end_color='334155', fill_type='solid')
    fill_light_blue = PatternFill(start_color='F1F5F9', end_color='F1F5F9', fill_type='solid')
    fill_accent = PatternFill(start_color='E0E7FF', end_color='E0E7FF', fill_type='solid')
    fill_success = PatternFill(start_color='DCFCE7', end_color='DCFCE7', fill_type='solid')
    fill_gold = PatternFill(start_color='FEF3C7', end_color='FEF3C7', fill_type='solid')

    border_thin = Side(border_style='thin', color='CBD5E1')
    border_double = Side(border_style='double', color='1E293B')
    border_thick = Side(border_style='medium', color='1E293B')

    box_border = Border(left=border_thin, right=border_thin, top=border_thin, bottom=border_thin)
    total_border = Border(top=border_thin, bottom=border_double)
    header_border = Border(left=border_thin, right=border_thin, top=border_thick, bottom=border_thick)

    align_center = Alignment(horizontal='center', vertical='center')
    align_left = Alignment(horizontal='left', vertical='center')
    align_right = Alignment(horizontal='right', vertical='center')
    align_header = Alignment(horizontal='center', vertical='center', wrap_text=True)

    fmt_currency = 'S/ #,##0.00'
    fmt_percent = '0.00%'
    fmt_number = '#,##0.00'

    # =========================================================================
    # 1. HOJA: CUENTAS (Catálogo Contable)
    # =========================================================================
    ws = wb.create_sheet(title='Cuentas')
    ws.views.sheetView[0].showGridLines = True

    ws['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws['A1'].font = font_title
    ws['A2'] = "Catálogo Mínimo de Cuentas Contables y Criterios de Clasificación (NIIF / PCGE)"
    ws['A2'].font = font_subtitle

    headers_cuentas = ["Código", "Nombre de la Cuenta", "Elemento", "Naturaleza", "Estado Financiero", "Criterio Técnico / Sustento Normativo"]
    for col_idx, h in enumerate(headers_cuentas, 1):
        c = ws.cell(row=4, column=col_idx, value=h)
        c.font = font_header
        c.fill = fill_navy
        c.alignment = align_header
        c.border = box_border

    cuentas_data = [
        ("1041", "Cuentas Corrientes Bancarias", "Activo", "Deudora", "Situación Financiera", "Fondos de libre disponibilidad depositados en la institución financiera."),
        ("1212", "Cuentas por Cobrar Comerciales - Clientes", "Activo", "Deudora", "Situación Financiera", "Derecho exigible derivado de entregable aceptado (Hito 1) con cobro a 45 días."),
        ("3361", "Equipos para Procesamiento de Información", "Activo", "Deudora", "Situación Financiera", "Hardware informático operativo con vida útil mayor a un año (NIC 16)."),
        ("4111", "Remuneraciones por Pagar", "Pasivo", "Acreedora", "Situación Financiera", "Obligación devengada con personal administrativo del mes pendiente de pago."),
        ("4212", "Cuentas por Pagar Comerciales - Proveedores", "Pasivo", "Acreedora", "Situación Financiera", "Obligación con proveedor de hardware informático por saldo pendiente."),
        ("4511", "Préstamos Bancarios a Corto Plazo", "Pasivo", "Acreedora", "Situación Financiera", "Obligación financiera con vencimiento a 6 meses para fondeo operativo."),
        ("4699", "Anticipos de Clientes (Ingresos Diferidos)", "Pasivo", "Acreedora", "Situación Financiera", "Cobro adelantado por Hito 2; obligación de desempeño no satisfecha (NIIF 15)."),
        ("5011", "Capital Social Aportado", "Patrimonio", "Acreedora", "Situación Financiera", "Aporte dinerario inicial de los socios para la constitución de la empresa."),
        ("5911", "Utilidad Neta del Ejercicio", "Patrimonio", "Acreedora", "Situación Financiera", "Resultado acumulado neto obtenido de las operaciones del primer mes."),
        ("7041", "Ingresos por Desarrollo de Software", "Ingreso", "Acreedora", "Resultados", "Ingreso ganado por entrega y aceptación formal del primer hito independiente."),
        ("6941", "Costo del Servicio - Remuneraciones de Desarrollo", "Costo", "Deudora", "Resultados", "Mano de obra directa de programación devengada y pagada en el mes."),
        ("6942", "Costo del Servicio - Servicios de Nube", "Costo", "Deudora", "Resultados", "Infraestructura cloud computing directamente consumida para el servicio."),
        ("9411", "Gastos Administrativos - Operativos Generales", "Gasto", "Deudora", "Resultados", "Servicios y consumos generales de administración incurridos en el mes."),
        ("9412", "Gastos Administrativos - Sueldos Devengados", "Gasto", "Deudora", "Resultados", "Costo laboral del personal administrativo devengado en el periodo."),
        ("9711", "Gastos Financieros - Intereses Bancarios", "Gasto", "Deudora", "Resultados", "Costo financiero por intereses devengados del préstamo bancario recibido.")
    ]

    for row_idx, r in enumerate(cuentas_data, 5):
        for col_idx, val in enumerate(r, 1):
            c = ws.cell(row=row_idx, column=col_idx, value=val)
            c.font = font_regular
            c.border = box_border
            if col_idx in [1, 3, 4]:
                c.alignment = align_center

    # =========================================================================
    # 2. HOJA: DIARIO (Libro Diario OP01 - OP11)
    # =========================================================================
    ws_d = wb.create_sheet(title='Diario')
    ws_d.views.sheetView[0].showGridLines = True

    ws_d['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_d['A1'].font = font_title
    ws_d['A2'] = "Libro Diario General - Operaciones del Primer Mes (OP01 - OP11)"
    ws_d['A2'].font = font_subtitle

    headers_diario = ["ID", "Fecha", "Cód. Cuenta", "Denominación de la Cuenta", "Glosa / Explicación de la Operación", "Debe (S/)", "Haber (S/)"]
    for col_idx, h in enumerate(headers_diario, 1):
        c = ws_d.cell(row=4, column=col_idx, value=h)
        c.font = font_header
        c.fill = fill_navy
        c.alignment = align_header
        c.border = box_border

    asientos = [
        ("OP01", "02/11/2026", "1041", "Cuentas Corrientes Bancarias", "Aporte de capital inicial de los socios en cuenta corriente", 40000.00, 0.0),
        ("OP01", "02/11/2026", "5011", "Capital Social Aportado", "Aporte de capital inicial de los socios en cuenta corriente", 0.0, 40000.00),
        ("OP02", "04/11/2026", "3361", "Equipos para Procesamiento de Información", "Compra de equipos informáticos (S/ 12,000 total)", 12000.00, 0.0),
        ("OP02", "04/11/2026", "1041", "Cuentas Corrientes Bancarias", "Pago inicial en efectivo con fondos de bancos", 0.0, 8000.00),
        ("OP02", "04/11/2026", "4212", "Cuentas por Pagar Comerciales - Proveedores", "Saldo pendiente a pagar a proveedor de equipos", 0.0, 4000.00),
        ("OP03", "06/11/2026", "1041", "Cuentas Corrientes Bancarias", "Desembolso de préstamo bancario a 6 meses", 10000.00, 0.0),
        ("OP03", "06/11/2026", "4511", "Préstamos Bancarios a Corto Plazo", "Obligación por préstamo bancario recibido", 0.0, 10000.00),
        ("OP04", "09/11/2026", "1041", "Cuentas Corrientes Bancarias", "Recepción de anticipo por módulo hito 2 salud pública", 9000.00, 0.0),
        ("OP04", "09/11/2026", "4699", "Anticipos de Clientes (Ingresos Diferidos)", "Pasivo por obligación de desempeño pendiente (NIIF 15)", 0.0, 9000.00),
        ("OP05", "13/11/2026", "6941", "Costo del Servicio - Remuneraciones de Desarrollo", "Pago de remuneraciones del mes al equipo de software", 15000.00, 0.0),
        ("OP05", "13/11/2026", "1041", "Cuentas Corrientes Bancarias", "Salida de fondos de cuenta bancaria", 0.0, 15000.00),
        ("OP06", "16/11/2026", "6942", "Costo del Servicio - Servicios de Nube", "Servicios de nube consumidos y pagados en el mes", 2000.00, 0.0),
        ("OP06", "16/11/2026", "1041", "Cuentas Corrientes Bancarias", "Salida de bancos por pago de nube cloud", 0.0, 2000.00),
        ("OP07", "19/11/2026", "9411", "Gastos Administrativos - Operativos Generales", "Pago de gastos administrativos operativos del mes", 3000.00, 0.0),
        ("OP07", "19/11/2026", "1041", "Cuentas Corrientes Bancarias", "Salida de bancos por gastos operativos", 0.0, 3000.00),
        ("OP08", "23/11/2026", "1041", "Cuentas Corrientes Bancarias", "Cobro inmediato al contado por hito 1 aceptado", 16000.00, 0.0),
        ("OP08", "23/11/2026", "1212", "Cuentas por Cobrar Comerciales - Clientes", "Cuenta por cobrar comercial por hito 1 a 45 días", 8000.00, 0.0),
        ("OP08", "23/11/2026", "7041", "Ingresos por Desarrollo de Software", "Reconocimiento de ingreso por hito 1 entregado y aceptado", 0.0, 24000.00),
        ("OP09", "25/11/2026", "4212", "Cuentas por Pagar Comerciales - Proveedores", "Amortización de deuda con proveedor de equipos", 2000.00, 0.0),
        ("OP09", "25/11/2026", "1041", "Cuentas Corrientes Bancarias", "Salida de bancos para pago a proveedor", 0.0, 2000.00),
        ("OP10", "28/11/2026", "9412", "Gastos Administrativos - Sueldos Devengados", "Reconocimiento de sueldo administrativo devengado", 1500.00, 0.0),
        ("OP10", "28/11/2026", "4111", "Remuneraciones por Pagar", "Obligación de pago a personal administrativo al cierre", 0.0, 1500.00),
        ("OP11", "30/11/2026", "9711", "Gastos Financieros - Intereses Bancarios", "Pago de intereses financieros devengados del préstamo", 500.00, 0.0),
        ("OP11", "30/11/2026", "1041", "Cuentas Corrientes Bancarias", "Salida de bancos por pago de intereses", 0.0, 500.00)
    ]

    for row_idx, r in enumerate(asientos, 5):
        for col_idx, val in enumerate(r, 1):
            c = ws_d.cell(row=row_idx, column=col_idx, value=val)
            c.font = font_regular
            c.border = box_border
            if col_idx in [1, 2, 3]:
                c.alignment = align_center
            elif col_idx in [6, 7]:
                c.alignment = align_right
                c.number_format = fmt_currency

    tot_row = len(asientos) + 5
    ws_d.cell(row=tot_row, column=5, value="TOTALES DEL LIBRO DIARIO:").font = font_bold
    ws_d.cell(row=tot_row, column=5).alignment = align_right

    c_debe = ws_d.cell(row=tot_row, column=6, value=f"=SUM(F5:F{tot_row-1})")
    c_debe.font = font_bold
    c_debe.alignment = align_right
    c_debe.number_format = fmt_currency
    c_debe.border = total_border

    c_haber = ws_d.cell(row=tot_row, column=7, value=f"=SUM(G5:G{tot_row-1})")
    c_haber.font = font_bold
    c_haber.alignment = align_right
    c_haber.number_format = fmt_currency
    c_haber.border = total_border

    ctrl_row = tot_row + 2
    ws_d.cell(row=ctrl_row, column=5, value="CONTROL DE PARTIDA DOBLE (DEBE - HABER = 0):").font = font_bold
    ws_d.cell(row=ctrl_row, column=5).alignment = align_right
    c_dif = ws_d.cell(row=ctrl_row, column=6, value=f"=F{tot_row}-G{tot_row}")
    c_dif.font = font_bold
    c_dif.alignment = align_right
    c_dif.number_format = fmt_currency

    c_st = ws_d.cell(row=ctrl_row, column=7, value=f'=IF(F{tot_row}=G{tot_row}, "CUADRADO EXACTO", "DESCUADRADO")')
    c_st.font = font_success
    c_st.fill = fill_success
    c_st.alignment = align_center

    # =========================================================================
    # 3. HOJA: MAYOR (Libro Mayor con fórmulas SUMAR.SI)
    # =========================================================================
    ws_m = wb.create_sheet(title='Mayor')
    ws_m.views.sheetView[0].showGridLines = True

    ws_m['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_m['A1'].font = font_title
    ws_m['A2'] = "Libro Mayor General - Agrupación por Cuentas T y Determinación de Saldos"
    ws_m['A2'].font = font_subtitle

    headers_mayor = ["Cód.", "Denominación de la Cuenta", "Elemento", "Total Cargos / Debe (S/)", "Total Abonos / Haber (S/)", "Saldo Deudor (S/)", "Saldo Acreedor (S/)"]
    for col_idx, h in enumerate(headers_mayor, 1):
        c = ws_m.cell(row=4, column=col_idx, value=h)
        c.font = font_header
        c.fill = fill_navy
        c.alignment = align_header
        c.border = box_border

    cuentas_mayor = [
        ("1041", "Cuentas Corrientes Bancarias", "Activo", "Deudora"),
        ("1212", "Cuentas por Cobrar Comerciales - Clientes", "Activo", "Deudora"),
        ("3361", "Equipos para Procesamiento de Información", "Activo", "Deudora"),
        ("4111", "Remuneraciones por Pagar", "Pasivo", "Acreedora"),
        ("4212", "Cuentas por Pagar Comerciales - Proveedores", "Pasivo", "Acreedora"),
        ("4511", "Préstamos Bancarios a Corto Plazo", "Pasivo", "Acreedora"),
        ("4699", "Anticipos de Clientes (Ingresos Diferidos)", "Pasivo", "Acreedora"),
        ("5011", "Capital Social Aportado", "Patrimonio", "Acreedora"),
        ("7041", "Ingresos por Desarrollo de Software", "Ingreso", "Acreedora"),
        ("6941", "Costo del Servicio - Remuneraciones de Desarrollo", "Costo", "Deudora"),
        ("6942", "Costo del Servicio - Servicios de Nube", "Costo", "Deudora"),
        ("9411", "Gastos Administrativos - Operativos Generales", "Gasto", "Deudora"),
        ("9412", "Gastos Administrativos - Sueldos Devengados", "Gasto", "Deudora"),
        ("9711", "Gastos Financieros - Intereses Bancarios", "Gasto", "Deudora")
    ]

    for row_idx, (code, name, elem, nat) in enumerate(cuentas_mayor, 5):
        ws_m.cell(row=row_idx, column=1, value=code).alignment = align_center
        ws_m.cell(row=row_idx, column=2, value=name).alignment = align_left
        ws_m.cell(row=row_idx, column=3, value=elem).alignment = align_center

        # SUMAR.SI dinámico desde Diario
        c_debe = ws_m.cell(row=row_idx, column=4, value=f"=SUMIF(Diario!$C$5:$C$28, A{row_idx}, Diario!$F$5:$F$28)")
        c_debe.alignment = align_right
        c_debe.number_format = fmt_currency

        c_haber = ws_m.cell(row=row_idx, column=5, value=f"=SUMIF(Diario!$C$5:$C$28, A{row_idx}, Diario!$G$5:$G$28)")
        c_haber.alignment = align_right
        c_haber.number_format = fmt_currency

        c_sdeudor = ws_m.cell(row=row_idx, column=6, value=f"=MAX(0, D{row_idx}-E{row_idx})")
        c_sdeudor.alignment = align_right
        c_sdeudor.number_format = fmt_currency

        c_sacreedor = ws_m.cell(row=row_idx, column=7, value=f"=MAX(0, E{row_idx}-D{row_idx})")
        c_sacreedor.alignment = align_right
        c_sacreedor.number_format = fmt_currency

        for col_idx in range(1, 8):
            ws_m.cell(row=row_idx, column=col_idx).font = font_regular
            ws_m.cell(row=row_idx, column=col_idx).border = box_border

    tot_m = len(cuentas_mayor) + 5
    ws_m.cell(row=tot_m, column=3, value="TOTALES:").font = font_bold
    ws_m.cell(row=tot_m, column=3).alignment = align_right

    for c_idx, col_let in [(4, 'D'), (5, 'E'), (6, 'F'), (7, 'G')]:
        cell = ws_m.cell(row=tot_m, column=c_idx, value=f"=SUM({col_let}5:{col_let}{tot_m-1})")
        cell.font = font_bold
        cell.alignment = align_right
        cell.number_format = fmt_currency
        cell.border = total_border

    # =========================================================================
    # 4. HOJA: COMPROBACIÓN (Balance de Comprobación)
    # =========================================================================
    ws_c = wb.create_sheet(title='Comprobación')
    ws_c.views.sheetView[0].showGridLines = True

    ws_c['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_c['A1'].font = font_title
    ws_c['A2'] = "Balance de Comprobación de Sumas y Saldos al Primer Mes"
    ws_c['A2'].font = font_subtitle

    headers_comp = ["Cód.", "Cuenta Contable", "Sumas Debe (S/)", "Sumas Haber (S/)", "Saldo Deudor (S/)", "Saldo Acreedor (S/)"]
    for col_idx, h in enumerate(headers_comp, 1):
        c = ws_c.cell(row=4, column=col_idx, value=h)
        c.font = font_header
        c.fill = fill_navy
        c.alignment = align_header
        c.border = box_border

    for row_idx in range(5, 5 + len(cuentas_mayor)):
        m_r = row_idx
        ws_c.cell(row=row_idx, column=1, value=f"=Mayor!A{m_r}").alignment = align_center
        ws_c.cell(row=row_idx, column=2, value=f"=Mayor!B{m_r}").alignment = align_left
        ws_c.cell(row=row_idx, column=3, value=f"=Mayor!D{m_r}").alignment = align_right
        ws_c.cell(row=row_idx, column=4, value=f"=Mayor!E{m_r}").alignment = align_right
        ws_c.cell(row=row_idx, column=5, value=f"=Mayor!F{m_r}").alignment = align_right
        ws_c.cell(row=row_idx, column=6, value=f"=Mayor!G{m_r}").alignment = align_right

        for c_idx in range(1, 7):
            cell = ws_c.cell(row=row_idx, column=c_idx)
            cell.font = font_regular
            cell.border = box_border
            if c_idx >= 3:
                cell.number_format = fmt_currency

    tot_c = len(cuentas_mayor) + 5
    ws_c.cell(row=tot_c, column=2, value="TOTALES BALANCE COMPROBACIÓN:").font = font_bold
    ws_c.cell(row=tot_c, column=2).alignment = align_right

    for c_idx, col_let in [(3, 'C'), (4, 'D'), (5, 'E'), (6, 'F')]:
        cell = ws_c.cell(row=tot_c, column=c_idx, value=f"=SUM({col_let}5:{col_let}{tot_c-1})")
        cell.font = font_bold
        cell.alignment = align_right
        cell.number_format = fmt_currency
        cell.border = total_border

    ctrl_c_row = tot_c + 2
    ws_c.cell(row=ctrl_c_row, column=2, value="CONTROL DE SALDOS (DEUDOR = ACREEDOR):").font = font_bold
    ws_c.cell(row=ctrl_c_row, column=2).alignment = align_right
    c_dif_c = ws_c.cell(row=ctrl_c_row, column=5, value=f"=E{tot_c}-F{tot_c}")
    c_dif_c.font = font_bold
    c_dif_c.alignment = align_right
    c_dif_c.number_format = fmt_currency
    c_st_c = ws_c.cell(row=ctrl_c_row, column=6, value=f'=IF(E{tot_c}=F{tot_c}, "CONFORME (S/ 0.00)", "ERROR")')
    c_st_c.font = font_success
    c_st_c.fill = fill_success
    c_st_c.alignment = align_center

    # =========================================================================
    # 5. HOJA: SITUACIÓN FINANCIERA (Balance General)
    # =========================================================================
    ws_esf = wb.create_sheet(title='Situación financiera')
    ws_esf.views.sheetView[0].showGridLines = True

    ws_esf['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_esf['A1'].font = font_title
    ws_esf['A2'] = "Estado de Situación Financiera (Balance General) al 30 de Noviembre de 2026"
    ws_esf['A2'].font = font_subtitle

    # Headers Activo
    for col_idx, h in [(1, "ACTIVO"), (2, "Importe (S/)")]:
        c = ws_esf.cell(row=4, column=col_idx, value=h)
        c.font = font_header
        c.fill = fill_navy
        c.alignment = align_center
        c.border = box_border

    # Headers Pasivo y Patrimonio
    for col_idx, h in [(4, "PASIVO Y PATRIMONIO"), (5, "Importe (S/)")]:
        c = ws_esf.cell(row=4, column=col_idx, value=h)
        c.font = font_header
        c.fill = fill_navy
        c.alignment = align_center
        c.border = box_border

    # Activo Corriente
    ws_esf.cell(row=5, column=1, value="ACTIVO CORRIENTE").font = font_bold
    ws_esf.cell(row=6, column=1, value="  Efectivo y Equivalentes de Efectivo (Bancos 1041)")
    ws_esf.cell(row=6, column=2, value="=Mayor!F5").number_format = fmt_currency
    ws_esf.cell(row=7, column=1, value="  Cuentas por Cobrar Comerciales - Clientes (1212)")
    ws_esf.cell(row=7, column=2, value="=Mayor!F6").number_format = fmt_currency
    ws_esf.cell(row=8, column=1, value="Total Activo Corriente").font = font_bold
    ws_esf.cell(row=8, column=2, value="=SUM(B6:B7)").font = font_bold
    ws_esf.cell(row=8, column=2).number_format = fmt_currency
    ws_esf.cell(row=8, column=2).border = Border(top=border_thin, bottom=border_thin)

    # Activo No Corriente
    ws_esf.cell(row=10, column=1, value="ACTIVO NO CORRIENTE").font = font_bold
    ws_esf.cell(row=11, column=1, value="  Equipos para Procesamiento de Información (3361)")
    ws_esf.cell(row=11, column=2, value="=Mayor!F7").number_format = fmt_currency
    ws_esf.cell(row=12, column=1, value="Total Activo No Corriente").font = font_bold
    ws_esf.cell(row=12, column=2, value="=B11").font = font_bold
    ws_esf.cell(row=12, column=2).number_format = fmt_currency
    ws_esf.cell(row=12, column=2).border = Border(top=border_thin, bottom=border_thin)

    # Total Activo
    ws_esf.cell(row=14, column=1, value="TOTAL ACTIVO").font = font_title
    ws_esf.cell(row=14, column=2, value="=B8+B12").font = font_title
    ws_esf.cell(row=14, column=2).number_format = fmt_currency
    ws_esf.cell(row=14, column=2).border = total_border

    # Pasivo Corriente
    ws_esf.cell(row=5, column=4, value="PASIVO CORRIENTE").font = font_bold
    ws_esf.cell(row=6, column=4, value="  Cuentas por Pagar Comerciales - Proveedores (4212)")
    ws_esf.cell(row=6, column=5, value="=Mayor!G9").number_format = fmt_currency
    ws_esf.cell(row=7, column=4, value="  Préstamos Bancarios a Corto Plazo (4511)")
    ws_esf.cell(row=7, column=5, value="=Mayor!G10").number_format = fmt_currency
    ws_esf.cell(row=8, column=4, value="  Anticipos de Clientes - Ingresos Diferidos (4699)")
    ws_esf.cell(row=8, column=5, value="=Mayor!G11").number_format = fmt_currency
    ws_esf.cell(row=9, column=4, value="  Remuneraciones por Pagar (4111)")
    ws_esf.cell(row=9, column=5, value="=Mayor!G8").number_format = fmt_currency
    ws_esf.cell(row=10, column=4, value="Total Pasivo Corriente").font = font_bold
    ws_esf.cell(row=10, column=5, value="=SUM(E6:E9)").font = font_bold
    ws_esf.cell(row=10, column=5).number_format = fmt_currency
    ws_esf.cell(row=10, column=5).border = Border(top=border_thin, bottom=border_thin)

    # Patrimonio Neto
    ws_esf.cell(row=12, column=4, value="PATRIMONIO NETO").font = font_bold
    ws_esf.cell(row=13, column=4, value="  Capital Social Aportado (5011)")
    ws_esf.cell(row=13, column=5, value="=Mayor!G12").number_format = fmt_currency
    ws_esf.cell(row=14, column=4, value="  Resultados Acumulados - Utilidad Neta (5911)")
    ws_esf.cell(row=14, column=5, value="=Resultados!B14").number_format = fmt_currency
    ws_esf.cell(row=15, column=4, value="Total Patrimonio Neto").font = font_bold
    ws_esf.cell(row=15, column=5, value="=SUM(E13:E14)").font = font_bold
    ws_esf.cell(row=15, column=5).number_format = fmt_currency
    ws_esf.cell(row=15, column=5).border = Border(top=border_thin, bottom=border_thin)

    # Total Pasivo y Patrimonio
    ws_esf.cell(row=17, column=4, value="TOTAL PASIVO Y PATRIMONIO").font = font_title
    ws_esf.cell(row=17, column=5, value="=E10+E15").font = font_title
    ws_esf.cell(row=17, column=5).number_format = fmt_currency
    ws_esf.cell(row=17, column=5).border = total_border

    # Control Ecuación Contable
    ws_esf.cell(row=19, column=1, value="CONTROL DE ECUACIÓN CONTABLE (ACTIVO = PASIVO + PATRIMONIO):").font = font_bold
    ws_esf.cell(row=19, column=4, value="=B14-E17").font = font_bold
    ws_esf.cell(row=19, column=4).number_format = fmt_currency
    ws_esf.cell(row=19, column=5, value='=IF(B14=E17, "BALANCE EXACTO (CUADRADO)", "DESCUADRE")').font = font_success
    ws_esf.cell(row=19, column=5).fill = fill_success
    ws_esf.cell(row=19, column=5).alignment = align_center

    # =========================================================================
    # 6. HOJA: RESULTADOS (Estado de Resultados por Función)
    # =========================================================================
    ws_r = wb.create_sheet(title='Resultados')
    ws_r.views.sheetView[0].showGridLines = True

    ws_r['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_r['A1'].font = font_title
    ws_r['A2'] = "Estado de Resultados Económico al 30 de Noviembre de 2026"
    ws_r['A2'].font = font_subtitle

    for col_idx, h in [(1, "Concepto"), (2, "Importe (S/)"), (3, "% Sobre Ingresos")]:
        c = ws_r.cell(row=4, column=col_idx, value=h)
        c.font = font_header
        c.fill = fill_navy
        c.alignment = align_center
        c.border = box_border

    r_items = [
        ("Ingresos por Desarrollo de Software (7041)", "=Mayor!G13", "=B5/$B$5", font_bold, False),
        ("Costo del Servicio PANVIZ", "", "", font_sub_header, False),
        ("  (-) Remuneraciones de Desarrollo (6941)", "=Mayor!F14", "=B7/$B$5", font_regular, False),
        ("  (-) Servicios de Infraestructura Nube (6942)", "=Mayor!F15", "=B8/$B$5", font_regular, False),
        ("Total Costo del Servicio", "=B7+B8", "=B9/$B$5", font_bold, True),
        ("UTILIDAD BRUTA", "=B5-B9", "=B10/$B$5", font_bold, True),
        ("Gastos de Operación", "", "", font_sub_header, False),
        ("  (-) Gastos Administrativos Operativos (9411)", "=Mayor!F16", "=B12/$B$5", font_regular, False),
        ("  (-) Gastos Administrativos Sueldos Devengados (9412)", "=Mayor!F17", "=B13/$B$5", font_regular, False),
        ("Total Gastos Administrativos", "=B12+B13", "=B14/$B$5", font_bold, True),
        ("UTILIDAD OPERATIVA (EBIT)", "=B10-B14", "=B15/$B$5", font_bold, True),
        ("Gastos Financieros", "", "", font_sub_header, False),
        ("  (-) Intereses Préstamo Bancario (9711)", "=Mayor!F18", "=B17/$B$5", font_regular, False),
        ("UTILIDAD NETA DEL EJERCICIO", "=B15-B17", "=B18/$B$5", font_title, True)
    ]

    for idx, (label, val_f, pct_f, fnt, is_tot) in enumerate(r_items, 5):
        c1 = ws_r.cell(row=idx, column=1, value=label)
        c1.font = fnt
        c1.border = box_border

        c2 = ws_r.cell(row=idx, column=2, value=val_f if val_f else None)
        c2.font = fnt
        c2.border = box_border
        if val_f:
            c2.alignment = align_right
            c2.number_format = fmt_currency

        c3 = ws_r.cell(row=idx, column=3, value=pct_f if pct_f else None)
        c3.font = fnt
        c3.border = box_border
        if pct_f:
            c3.alignment = align_right
            c3.number_format = fmt_percent

        if is_tot:
            c1.fill = fill_accent
            c2.fill = fill_accent
            c3.fill = fill_accent

    # =========================================================================
    # 7. HOJA: PATRIMONIO (Estado de Cambios en el Patrimonio Neto)
    # =========================================================================
    ws_pat = wb.create_sheet(title='Patrimonio')
    ws_pat.views.sheetView[0].showGridLines = True

    ws_pat['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_pat['A1'].font = font_title
    ws_pat['A2'] = "Estado de Cambios en el Patrimonio Neto al 30 de Noviembre de 2026"
    ws_pat['A2'].font = font_subtitle

    headers_pat = ["Concepto / Movimiento", "Capital Social (S/)", "Resultados Acumulados (S/)", "Total Patrimonio Neto (S/)"]
    for col_idx, h in enumerate(headers_pat, 1):
        c = ws_pat.cell(row=4, column=col_idx, value=h)
        c.font = font_header
        c.fill = fill_navy
        c.alignment = align_center
        c.border = box_border

    pat_rows = [
        ("Saldos Iniciales al 01/11/2026", 0.0, 0.0, "=B5+C5"),
        ("(+) Aportes Dinerarios de Socios (OP01)", "=Mayor!G12", 0.0, "=B6+C6"),
        ("(+) Utilidad Neta del Primer Mes", 0.0, "=Resultados!B18", "=B7+C7"),
        ("SALDOS FINALES AL 30/11/2026", "=SUM(B5:B7)", "=SUM(C5:C7)", "=SUM(D5:D7)")
    ]

    for idx, (label, cap, res, tot) in enumerate(pat_rows, 5):
        ws_pat.cell(row=idx, column=1, value=label).font = font_bold if idx == 8 else font_regular
        ws_pat.cell(row=idx, column=1).border = box_border

        for c_idx, val in [(2, cap), (3, res), (4, tot)]:
            cell = ws_pat.cell(row=idx, column=c_idx, value=val)
            cell.font = font_bold if idx == 8 else font_regular
            cell.alignment = align_right
            cell.number_format = fmt_currency
            cell.border = box_border
            if idx == 8:
                cell.border = total_border
                cell.fill = fill_accent

    # =========================================================================
    # 8. HOJA: FLUJO (Estado de Flujos de Efectivo - Método Directo NIC 7)
    # =========================================================================
    ws_fe = wb.create_sheet(title='Flujo')
    ws_fe.views.sheetView[0].showGridLines = True

    ws_fe['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_fe['A1'].font = font_title
    ws_fe['A2'] = "Estado de Flujos de Efectivo (Método Directo NIC 7) al 30 de Noviembre de 2026"
    ws_fe['A2'].font = font_subtitle

    for col_idx, h in [(1, "Actividades de Flujo de Efectivo"), (2, "Importe Parcial (S/)"), (3, "Flujo Neto (S/)")]:
        c = ws_fe.cell(row=4, column=col_idx, value=h)
        c.font = font_header
        c.fill = fill_navy
        c.alignment = align_center
        c.border = box_border

    fe_data = [
        ("ACTIVIDADES DE OPERACIÓN", "", "", font_bold, False),
        ("  Cobranza por servicios de software (Hito 1 OP08)", 16000.00, "", font_regular, False),
        ("  Cobranza por anticipo de clientes (Hito 2 OP04)", 9000.00, "", font_regular, False),
        ("  (-) Pago de remuneraciones al equipo de desarrollo (OP05)", -15000.00, "", font_regular, False),
        ("  (-) Pago por servicios de nube consumidos (OP06)", -2000.00, "", font_regular, False),
        ("  (-) Pago de gastos administrativos operativos (OP07)", -3000.00, "", font_regular, False),
        ("  (-) Pago de intereses bancarios del préstamo (OP11)", -500.00, "", font_regular, False),
        ("Flujo Neto de Actividades de Operación", "", "=SUM(B6:B11)", font_bold, True),
        ("ACTIVIDADES DE INVERSIÓN", "", "", font_bold, False),
        ("  (-) Pago en efectivo por compra de equipos informáticos (OP02)", -8000.00, "", font_regular, False),
        ("  (-) Pago a proveedor por deuda de adquisición de equipos (OP09)", -2000.00, "", font_regular, False),
        ("Flujo Neto de Actividades de Inversión", "", "=SUM(B14:B15)", font_bold, True),
        ("ACTIVIDADES DE FINANCIACIÓN", "", "", font_bold, False),
        ("  Aporte de capital inicial de los socios (OP01)", 40000.00, "", font_regular, False),
        ("  Desembolso de préstamo bancario recibido (OP03)", 10000.00, "", font_regular, False),
        ("Flujo Neto de Actividades de Financiación", "", "=SUM(B18:B19)", font_bold, True),
        ("AUMENTO NETO DE EFECTIVO Y EQUIVALENTES", "", "=C12+C16+C20", font_title, True),
        ("Saldo Inicial de Efectivo al 01/11/2026", "", 0.00, font_regular, False),
        ("SALDO FINAL DE EFECTIVO Y EQUIVALENTES AL 30/11/2026", "", "=C21+C22", font_title, True)
    ]

    for idx, (label, p_val, n_val, fnt, is_tot) in enumerate(fe_data, 5):
        c1 = ws_fe.cell(row=idx, column=1, value=label)
        c1.font = fnt
        c1.border = box_border

        c2 = ws_fe.cell(row=idx, column=2, value=p_val if p_val != "" else None)
        c2.font = fnt
        c2.border = box_border
        if p_val != "":
            c2.alignment = align_right
            c2.number_format = fmt_currency

        c3 = ws_fe.cell(row=idx, column=3, value=n_val if n_val != "" else None)
        c3.font = fnt
        c3.border = box_border
        if n_val != "":
            c3.alignment = align_right
            c3.number_format = fmt_currency

        if is_tot:
            c1.fill = fill_accent
            c2.fill = fill_accent
            c3.fill = fill_accent

    # Control de Conciliación con Situación Financiera
    ctrl_fe = 25
    ws_fe.cell(row=ctrl_fe, column=1, value="CONTROL DE SALDO FINAL (CONCILIACIÓN CON BANCOS ESF):").font = font_bold
    ws_fe.cell(row=ctrl_fe, column=2, value="='Situación financiera'!B6").font = font_bold
    ws_fe.cell(row=ctrl_fe, column=2).number_format = fmt_currency
    ws_fe.cell(row=ctrl_fe, column=3, value='=IF(C23=\'Situación financiera\'!B6, "CONCILIADO EXACTO", "DIFERENCIA")').font = font_success
    ws_fe.cell(row=ctrl_fe, column=3).fill = fill_success
    ws_fe.cell(row=ctrl_fe, column=3).alignment = align_center

    # =========================================================================
    # 9. HOJA: CAJA 15 DÍAS (Presupuesto de Caja Quincenal e Indicadores)
    # =========================================================================
    ws_cj = wb.create_sheet(title='Caja 15 días')
    ws_cj.views.sheetView[0].showGridLines = True

    ws_cj['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_cj['A1'].font = font_title
    ws_cj['A2'] = "Presupuesto de Caja Quincenal (15 Días) y Evaluación de Estrés a 45 Días"
    ws_cj['A2'].font = font_subtitle

    # Tabla 1: Presupuesto 15 Días
    ws_cj.cell(row=4, column=1, value="Concepto de Tesorería").font = font_header
    ws_cj.cell(row=4, column=1).fill = fill_navy
    ws_cj.cell(row=4, column=2, value="Importe Proyectado (S/)").font = font_header
    ws_cj.cell(row=4, column=2).fill = fill_navy
    ws_cj.cell(row=4, column=3, value="Sustento y Justificación Técnica").font = font_header
    ws_cj.cell(row=4, column=3).fill = fill_navy

    caja_rows = [
        ("SALDO INICIAL DISPONIBLE EN BANCOS (Día 1)", "='Situación financiera'!B6", "Saldo en cuenta corriente certificado al cierre del mes 1."),
        ("(+) INGRESOS Y COBROS PROYECTADOS", 0.00, "Cliente advirtió cobro de S/ 8,000 a 45 días; no se anticipan cobros."),
        ("(-) EGRESOS PROYECTADOS (PRÓXIMOS 15 DÍAS)", "", "Compromisos operacionales ineludibles para la continuidad del servicio."),
        ("  Remuneraciones previstas del equipo", 18000.00, "Nómina técnica quincenal/mensual requerida para desarrollo del Módulo 2."),
        ("  Servicios de nube (Cloud computing)", 2000.00, "Costo de servidores para mantener disponible la ingesta de datos PANVIZ."),
        ("  Deuda restante con proveedor de equipos", 2000.00, "Cancelación de saldo pendiente de compra de hardware (OP02 y OP09)."),
        ("  Remuneraciones administrativas pendientes", 1500.00, "Obligación devengada en OP10 con personal administrativo."),
        ("TOTAL EGRESOS PROYECTADOS (15 DÍAS)", "=SUM(B8:B11)", "Total desembolsos ineludibles de la quincena."),
        ("SALDO FINAL PROYECTADO DE CAJA (Día 15)", "=B5+B6-B12", "Excedente temporal de liquidez al corte del día 15.")
    ]

    for idx, (label, val, just) in enumerate(caja_rows, 5):
        c1 = ws_cj.cell(row=idx, column=1, value=label)
        c2 = ws_cj.cell(row=idx, column=2, value=val if val != "" else None)
        c3 = ws_cj.cell(row=idx, column=3, value=just)

        fnt = font_bold if idx in [5, 12, 13] else font_regular
        c1.font = fnt
        c2.font = fnt
        c3.font = font_regular

        c1.border = box_border
        c2.border = box_border
        c3.border = box_border

        if val != "":
            c2.alignment = align_right
            c2.number_format = fmt_currency
        if idx in [12, 13]:
            c1.fill = fill_accent
            c2.fill = fill_accent
            c3.fill = fill_accent

    # Indicadores Financieros
    ws_cj.cell(row=15, column=1, value="INDICADORES FINANCIEROS Y RATIOS DE LIQUIDEZ").font = font_title
    headers_ind = ["Ratio / Indicador", "Fórmula Contable", "Valor Calculado", "Interpretación y Diagnóstico Gerencial"]
    for col_idx, h in enumerate(headers_ind, 1):
        c = ws_cj.cell(row=17, column=col_idx, value=h)
        c.font = font_header
        c.fill = fill_navy
        c.alignment = align_center
        c.border = box_border

    ind_data = [
        ("Margen Bruto", "Utilidad Bruta / Ingresos", "=Resultados!B10/Resultados!B5", fmt_percent, "29.17% - Eficiencia operativa en costo directo de desarrollo y servidores."),
        ("Margen Neto", "Utilidad Neta / Ingresos", "=Resultados!B18/Resultados!B5", fmt_percent, "8.33% - Rentabilidad económica positiva pero reducida tras gastos operativos."),
        ("Razón Corriente", "Activo Corriente / Pasivo Corriente", "='Situación financiera'!B8/'Situación financiera'!E10", fmt_number, "2.33 - Respaldo contable de corto plazo holgado (S/ 2.33 por cada sol de pasivo)."),
        ("Prueba Ácida", "(Activo Cte. - Inventario) / Pasivo Cte.", "='Situación financiera'!B8/'Situación financiera'!E10", fmt_number, "2.33 - Excelente liquidez teórica (empresa de software sin inventarios físicos)."),
        ("Cobertura Inmediata (15 días)", "Saldo Bancos / Egresos 15 días", "=B5/B12", fmt_number, "1.89 - Caja actual cubre 1.89 veces los compromisos de los primeros 15 días.")
    ]

    for idx, (nom, form, val, fmt, interp) in enumerate(ind_data, 18):
        c1 = ws_cj.cell(row=idx, column=1, value=nom)
        c2 = ws_cj.cell(row=idx, column=2, value=form)
        c3 = ws_cj.cell(row=idx, column=3, value=val)
        c4 = ws_cj.cell(row=idx, column=4, value=interp)

        for col_i, cell in enumerate([c1, c2, c3, c4], 1):
            cell.font = font_bold if col_i in [1, 3] else font_regular
            cell.border = box_border
            if col_i == 3:
                cell.alignment = align_right
                cell.number_format = fmt
            elif col_i == 2:
                cell.alignment = align_center

    # Proyección de Estrés a 45 Días
    ws_cj.cell(row=24, column=1, value="ANÁLISIS DE ESTRÉS DE TESORERÍA A 45 DÍAS (LA TRAMPA DE LIQUIDEZ)").font = font_title
    headers_stress = ["Hito Temporal", "Saldo Inicial (S/)", "Egresos Ciclo (S/)", "Cobros Previstos (S/)", "Saldo Neto (S/)", "Alerta Gerencial / Riesgo Operativo"]
    for col_idx, h in enumerate(headers_stress, 1):
        c = ws_cj.cell(row=26, column=col_idx, value=h)
        c.font = font_header
        c.fill = fill_slate
        c.alignment = align_center
        c.border = box_border

    stress_data = [
        ("Día 1 al Día 15 (Quincena 1)", "=B5", "=B12", 0.00, "=B27-C27+D27", "SUPERÁVIT: Cobertura segura de compromisos iniciales."),
        ("Día 16 al Día 30 (Quincena 2)", "=E27", 18000.00 + 2000.00, 0.00, "=B28-C28+D28", "PRESIÓN: Caja remanente cae a S/ 1,000 por nueva nómina y nube."),
        ("Día 31 al Día 44 (Días críticos)", "=E28", 3500.00, 0.00, "=B29-C29+D29", "DÉFICIT INMINENTE (-S/ 2,500): Suspensión de pagos si no hay financiamiento."),
        ("Día 45 (Cobranza Hito 1)", "=E29", 0.00, 8000.00, "=B30-C30+D30", "RECUPERACIÓN: Ingreso de S/ 8,000 restablece caja a S/ 5,500.")
    ]

    for idx, (periodo, s_ini, egres, cobr, s_net, diag) in enumerate(stress_data, 27):
        c1 = ws_cj.cell(row=idx, column=1, value=periodo)
        c2 = ws_cj.cell(row=idx, column=2, value=s_ini)
        c3 = ws_cj.cell(row=idx, column=3, value=egres)
        c4 = ws_cj.cell(row=idx, column=4, value=cobr)
        c5 = ws_cj.cell(row=idx, column=5, value=s_net)
        c6 = ws_cj.cell(row=idx, column=6, value=diag)

        for col_i, cell in enumerate([c1, c2, c3, c4, c5, c6], 1):
            cell.font = font_bold if col_i in [1, 5] else font_regular
            cell.border = box_border
            if col_i in [2, 3, 4, 5]:
                cell.alignment = align_right
                cell.number_format = fmt_currency
            if idx == 29: # Fila crítica
                cell.fill = fill_gold

    # =========================================================================
    # 10. HOJA: CONCILIACIÓN GNUCASH
    # =========================================================================
    ws_conc = wb.create_sheet(title='Conciliación GnuCash')
    ws_conc.views.sheetView[0].showGridLines = True

    ws_conc['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_conc['A1'].font = font_title
    ws_conc['A2'] = "Matriz de Conciliación Integral: Hoja de Cálculo (Calc/Excel) vs. GnuCash"
    ws_conc['A2'].font = font_subtitle

    headers_conc = ["Cód.", "Cuenta o Indicador Contable", "Saldo Calc / Excel (S/)", "Saldo GnuCash (S/)", "Diferencia Absoluta (S/)", "Estado de Conciliación", "Sustento Técnico y Enlace a Evidencia"]
    for col_idx, h in enumerate(headers_conc, 1):
        c = ws_conc.cell(row=4, column=col_idx, value=h)
        c.font = font_header
        c.fill = fill_navy
        c.alignment = align_header
        c.border = box_border

    conc_data = [
        ("1041", "Cuentas Corrientes Bancarias", "='Situación financiera'!B6", 44500.00, "Criterio directo bancario; ver capturas/captura_3_balance_general_gnucash.png"),
        ("1212", "Cuentas por Cobrar Comerciales - Clientes", "='Situación financiera'!B7", 8000.00, "Registro manual por cobrar comercial; ver balance GnuCash"),
        ("3361", "Equipos para Procesamiento de Información", "='Situación financiera'!B11", 12000.00, "Reconocimiento como PPE a costo histórico (NIC 16)"),
        ("4212", "Cuentas por Pagar Comerciales - Proveedores", "='Situación financiera'!E6", 2000.00, "Pasivo por saldo de compra hardware tras amortización OP09"),
        ("4511", "Préstamos Bancarios a Corto Plazo", "='Situación financiera'!E7", 10000.00, "Deuda financiera principal a 6 meses"),
        ("4699", "Anticipos de Clientes (Ingresos Diferidos)", "='Situación financiera'!E8", 9000.00, "Pasivo corriente por desempeño pendiente de Hito 2 (NIIF 15)"),
        ("4111", "Remuneraciones por Pagar", "='Situación financiera'!E9", 1500.00, "Pasivo devengado administrativo del cierre (OP10)"),
        ("5011", "Capital Social Aportado", "='Situación financiera'!E13", 40000.00, "Aporte dinerario inicial de socios (OP01)"),
        ("5911", "Resultado del Ejercicio (Utilidad Neta)", "=Resultados!B18", 2000.00, "Utilidad neta idéntica en EERR; ver captura_4_estado_resultados_gnucash.png"),
        ("TOT", "TOTAL ACTIVO", "='Situación financiera'!B14", 64500.00, "Total de activos conciliado con diferencia cero"),
        ("TOT", "TOTAL PASIVO Y PATRIMONIO", "='Situación financiera'!E17", 64500.00, "Equilibrio contable perfecto en ambas plataformas")
    ]

    for idx, (code, nom, f_calc, val_gnu, sust) in enumerate(conc_data, 5):
        c1 = ws_conc.cell(row=idx, column=1, value=code).alignment = align_center
        c2 = ws_conc.cell(row=idx, column=2, value=nom)
        c3 = ws_conc.cell(row=idx, column=3, value=f_calc)
        c4 = ws_conc.cell(row=idx, column=4, value=val_gnu)
        c5 = ws_conc.cell(row=idx, column=5, value=f"=C{idx}-D{idx}")
        c6 = ws_conc.cell(row=idx, column=6, value=f'=IF(E{idx}=0, "CONCILIADO EXACTO", "DIFERENCIA")')
        c7 = ws_conc.cell(row=idx, column=7, value=sust)

        for col_i in range(1, 8):
            cell = ws_conc.cell(row=idx, column=col_i)
            cell.font = font_bold if code == "TOT" else font_regular
            cell.border = box_border
            if col_i in [3, 4, 5]:
                cell.alignment = align_right
                cell.number_format = fmt_currency
            elif col_i == 6:
                cell.font = font_success
                cell.fill = fill_success
                cell.alignment = align_center

    # =========================================================================
    # 11. HOJA: PARTICIPACIÓN (Equipo de 4 Integrantes)
    # =========================================================================
    ws_pt = wb.create_sheet(title='Participación')
    ws_pt.views.sheetView[0].showGridLines = True

    ws_pt['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_pt['A1'].font = font_title
    ws_pt['A2'] = "Matriz de Asignación de Responsabilidades y Revisión Cruzada del Equipo (4 Integrantes)"
    ws_pt['A2'].font = font_subtitle

    headers_part = ["#", "Estudiante Integrante", "Rol Asignado", "Responsabilidad Principal", "Hojas Custodiadas / Entregable", "Revisión Cruzada Realizada", "Conformidad"]
    for col_idx, h in enumerate(headers_part, 1):
        c = ws_pt.cell(row=4, column=col_idx, value=h)
        c.font = font_header
        c.fill = fill_navy
        c.alignment = align_header
        c.border = box_border

    equipo_data = [
        ("1", "Chambilla Perca, Ricardo Mauricio", "Especialista Contable y Modelado Operacional", "Diseño del Catálogo de Cuentas, registro de transacciones OP01-OP11 en Diario, Mayorización y Balance de Comprobación.", "Cuentas, Diario, Mayor, Comprobación", "Revisa la Síntesis Crítica y el Control de Lectura 43 de Suclle Suca", "APROBADO (100%)"),
        ("2", "Gutiérrez Ccama, Juan Diego", "Especialista en Reportes Financieros y Conciliación", "Elaboración de Estados Financieros (ESF, EERR, EFE, Patrimonio), conciliación integral Calc vs. GnuCash y validación de balances.", "Situación financiera, Resultados, Patrimonio, Flujo, Conciliación GnuCash", "Revisa los registros contables y comprobación de Chambilla Perca", "APROBADO (100%)"),
        ("3", "Mollo Chuquicaña, Dolly Yadhira", "Analista de Liquidez, Ratios y Tesorería", "Cálculo de Ratios Financieros, proyección de Presupuesto de Caja a 15 y 45 días, detección de brecha de liquidez y decisiones gerenciales.", "Caja 15 días, Modelado de Estrés", "Revisa los Estados Financieros y Conciliación de Gutiérrez Ccama", "APROBADO (100%)"),
        ("4", "Suclle Suca, Michael Benjamin", "Coordinador de Proyecto y Auditoría Gerencial", "Coordinación general, resolución del Control de Lectura 43 (Slide 43), Síntesis Crítica de Guim-Bustos et al. (2023) e integración de decisiones gerenciales.", "Informe MD/PDF, Presentación HTML, Control 43", "Revisa el Presupuesto de Caja y Decisiones Estratégicas de Mollo Chuquicaña", "APROBADO (100%)")
    ]

    for idx, row in enumerate(equipo_data, 5):
        for col_i, val in enumerate(row, 1):
            c = ws_pt.cell(row=idx, column=col_i, value=val)
            c.font = font_regular
            c.border = box_border
            if col_i in [1, 7]:
                c.alignment = align_center
                if col_i == 7:
                    c.font = font_success
                    c.fill = fill_success

    # Ajuste automático del ancho de columnas para todas las hojas
    for sheet in wb.worksheets:
        for col in sheet.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val_str = str(cell.value or '')
                if not val_str.startswith('='):
                    max_len = max(max_len, len(val_str))
                else:
                    max_len = max(max_len, 15)
            sheet.column_dimensions[col_letter].width = max(max_len + 3, 12)

    wb.save(filepath)
    print(f"Libro contable guardado exitosamente en: {filepath}")

if __name__ == "__main__":
    import os
    target = os.path.join(r"C:\Users\micha\Downloads\Borrar entregable 6\GPS-Entregable-6", "PANVIZ_Control_Economico.xlsx")
    build_panviz_excel(target)
