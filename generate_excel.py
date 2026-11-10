import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build_panviz_excel(filepath):
    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)

    # Styles
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
    # 1. HOJA: CUENTAS
    # =========================================================================
    ws = wb.create_sheet(title='Cuentas')
    ws.views.sheetView[0].showGridLines = True

    ws['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws['A1'].font = font_title
    ws['A2'] = "Catálogo Mínimo de Cuentas y Correspondencia con GnuCash (PCGE / GnuCash Chart)"
    ws['A2'].font = font_subtitle

    headers_cuentas = ["Código PCGE", "Nombre de la Cuenta", "Elemento Contable", "Naturaleza", "Categoría GnuCash", "Cuenta en GnuCash"]
    for col_idx, h in enumerate(headers_cuentas, 1):
        cell = ws.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_header
        cell.border = header_border

    catalogo = [
        ("1041", "Bancos - Cuentas Corrientes", "Activo Corriente", "Deudora", "Asset:Current Assets:Bank", "Activos:Activo Corriente:Bancos:Cuenta Corriente"),
        ("1212", "Cuentas por Cobrar Comerciales", "Activo Corriente", "Deudora", "Asset:Current Assets:Receivable", "Activos:Activo Corriente:Clientes:Facturas por Cobrar"),
        ("3361", "Equipos de Cómputo e Informáticos", "Activo No Corriente", "Deudora", "Asset:Fixed Assets:Equipment", "Activos:Activo Fijo:Equipos Informáticos"),
        ("4111", "Remuneraciones por Pagar", "Pasivo Corriente", "Acreedora", "Liability:Current Liabilities:Payroll", "Pasivos:Pasivo Corriente:Sueldos por Pagar"),
        ("4212", "Cuentas por Pagar Comerciales - Proveedores", "Pasivo Corriente", "Acreedora", "Liability:Current Liabilities:Payable", "Pasivos:Pasivo Corriente:Proveedores:Equipos"),
        ("4511", "Obligaciones Financieras - Préstamo Bancario", "Pasivo Corriente", "Acreedora", "Liability:Current Liabilities:Loan", "Pasivos:Pasivo Corriente:Préstamos Bancarios"),
        ("4699", "Anticipos de Clientes (Ingresos Diferidos)", "Pasivo Corriente", "Acreedora", "Liability:Current Liabilities:Unearned", "Pasivos:Pasivo Corriente:Anticipos de Clientes"),
        ("5011", "Capital Social - Aportes de Socios", "Patrimonio Neto", "Acreedora", "Equity:Paid-in Capital", "Patrimonio:Capital Social:Aportes"),
        ("5911", "Resultado del Ejercicio (Utilidad Neta)", "Patrimonio Neto", "Acreedora", "Equity:Retained Earnings", "Patrimonio:Resultados Acumulados:Resultado del Mes"),
        ("7041", "Ingresos por Servicios de Software", "Ingresos", "Acreedora", "Income:Sales", "Ingresos:Ventas:Desarrollo de Software"),
        ("6941", "Costo de Servicio - Remuneraciones Desarrollo", "Costos", "Deudora", "Expense:Cost of Goods:Labor", "Gastos:Costo del Servicio:Remuneraciones Desarrollo"),
        ("6942", "Costo de Servicio - Alojamiento en la Nube", "Costos", "Deudora", "Expense:Cost of Goods:Hosting", "Gastos:Costo del Servicio:Servicios de Nube"),
        ("9411", "Gastos Administrativos Generales", "Gastos Operativos", "Deudora", "Expense:Administrative:General", "Gastos:Gastos Administrativos:Operativos Generales"),
        ("9412", "Gastos Administrativos - Sueldos Devengados", "Gastos Operativos", "Deudora", "Expense:Administrative:Payroll", "Gastos:Gastos Administrativos:Remuneraciones"),
        ("9711", "Gastos Financieros - Intereses de Préstamo", "Gastos Financieros", "Deudora", "Expense:Financial:Interest", "Gastos:Gastos Financieros:Intereses Bancarios")
    ]

    for row_idx, data in enumerate(catalogo, 5):
        fill = fill_light_blue if row_idx % 2 == 0 else PatternFill(fill_type=None)
        for col_idx, val in enumerate(data, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_regular
            cell.fill = fill
            cell.border = box_border
            if col_idx in [1, 4]:
                cell.alignment = align_center
            else:
                cell.alignment = align_left

    # =========================================================================
    # 2. HOJA: DIARIO
    # =========================================================================
    ws_d = wb.create_sheet(title='Diario')
    ws_d.views.sheetView[0].showGridLines = True

    ws_d['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_d['A1'].font = font_title
    ws_d['A2'] = "Libro Diario General - Mes 1 (Noviembre 2026)"
    ws_d['A2'].font = font_subtitle

    headers_diario = ["Fecha", "N° Op.", "Código", "Cuenta Contable", "Glosa / Explicación de la Operación", "Debe (S/)", "Haber (S/)"]
    for col_idx, h in enumerate(headers_diario, 1):
        cell = ws_d.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_header
        cell.border = header_border

    # Entries: (Fecha, OP, Cod, Cuenta, Glosa, Debe, Haber)
    diario_entries = [
        ("02/11/2026", "OP01", "1041", "Bancos - Cuentas Corrientes", "Aporte inicial de los socios depositado en bancos", 40000.0, 0.0),
        ("02/11/2026", "OP01", "5011", "Capital Social - Aportes de Socios", "Constitución de capital social según minuta", 0.0, 40000.0),
        ("05/11/2026", "OP02", "3361", "Equipos de Cómputo e Informáticos", "Compra de equipos informáticos para el proyecto", 12000.0, 0.0),
        ("05/11/2026", "OP02", "1041", "Bancos - Cuentas Corrientes", "Pago inicial del 66.7% con transferencia bancaria", 0.0, 8000.0),
        ("05/11/2026", "OP02", "4212", "Cuentas por Pagar Comerciales - Proveedores", "Saldo pendiente de pago al proveedor de equipos", 0.0, 4000.0),
        ("07/11/2026", "OP03", "1041", "Bancos - Cuentas Corrientes", "Desembolso de préstamo bancario a 6 meses", 10000.0, 0.0),
        ("07/11/2026", "OP03", "4511", "Obligaciones Financieras - Préstamo Bancario", "Préstamo de capital de trabajo a corto plazo", 0.0, 10000.0),
        ("10/11/2026", "OP04", "1041", "Bancos - Cuentas Corrientes", "Recepción de anticipo por módulo de alertas y reportes", 9000.0, 0.0),
        ("10/11/2026", "OP04", "4699", "Anticipos de Clientes (Ingresos Diferidos)", "Pasivo por servicio futuro no devengado", 0.0, 9000.0),
        ("15/11/2026", "OP05", "6941", "Costo de Servicio - Remuneraciones Desarrollo", "Remuneraciones técnicas devengadas del mes de desarrollo", 15000.0, 0.0),
        ("15/11/2026", "OP05", "1041", "Bancos - Cuentas Corrientes", "Pago de planillas de desarrollo técnico desde bancos", 0.0, 15000.0),
        ("18/11/2026", "OP06", "6942", "Costo de Servicio - Alojamiento en la Nube", "Servicios de nube consumidos en el desarrollo del hito", 2000.0, 0.0),
        ("18/11/2026", "OP06", "1041", "Bancos - Cuentas Corrientes", "Pago de infraestructura cloud del mes desde bancos", 0.0, 2000.0),
        ("20/11/2026", "OP07", "9411", "Gastos Administrativos Generales", "Gastos de gestión operativa y administración del mes", 3000.0, 0.0),
        ("20/11/2026", "OP07", "1041", "Bancos - Cuentas Corrientes", "Cancelación de gastos operativos desde bancos", 0.0, 3000.0),
        ("25/11/2026", "OP08", "1041", "Bancos - Cuentas Corrientes", "Cobro al contado de entrega del primer hito PANVIZ", 16000.0, 0.0),
        ("25/11/2026", "OP08", "1212", "Cuentas por Cobrar Comerciales", "Saldo por cobrar por hito aceptado (a 45 días)", 8000.0, 0.0),
        ("25/11/2026", "OP08", "7041", "Ingresos por Servicios de Software", "Reconocimiento de ingreso devengado por hito 1", 0.0, 24000.0),
        ("27/11/2026", "OP09", "4212", "Cuentas por Pagar Comerciales - Proveedores", "Amortización de deuda con proveedor de hardware", 2000.0, 0.0),
        ("27/11/2026", "OP09", "1041", "Bancos - Cuentas Corrientes", "Pago bancario a proveedor de equipos", 0.0, 2000.0),
        ("30/11/2026", "OP10", "9412", "Gastos Administrativos - Sueldos Devengados", "Sueldos administrativos del mes devengados", 1500.0, 0.0),
        ("30/11/2026", "OP10", "4111", "Remuneraciones por Pagar", "Obligación laboral pendiente de pago al cierre", 0.0, 1500.0),
        ("30/11/2026", "OP11", "9711", "Gastos Financieros - Intereses de Préstamo", "Intereses devengados por préstamo bancario", 500.0, 0.0),
        ("30/11/2026", "OP11", "1041", "Bancos - Cuentas Corrientes", "Pago de intereses financieros desde bancos", 0.0, 500.0)
    ]

    start_row = 5
    for idx, row_data in enumerate(diario_entries):
        curr_row = start_row + idx
        for col_idx, val in enumerate(row_data, 1):
            cell = ws_d.cell(row=curr_row, column=col_idx, value=val)
            cell.font = font_regular
            cell.border = box_border
            if col_idx in [1, 2, 3]:
                cell.alignment = align_center
            elif col_idx in [4, 5]:
                cell.alignment = align_left
            elif col_idx in [6, 7]:
                cell.alignment = align_right
                cell.number_format = fmt_currency

    end_row = start_row + len(diario_entries) - 1
    tot_row = end_row + 1

    ws_d.cell(row=tot_row, column=4, value="SUMAS TOTALES").font = font_bold
    ws_d.cell(row=tot_row, column=4).alignment = align_right
    ws_d.cell(row=tot_row, column=4).border = total_border

    cell_tot_d = ws_d.cell(row=tot_row, column=6, value=f"=SUM(F{start_row}:F{end_row})")
    cell_tot_d.font = font_bold
    cell_tot_d.number_format = fmt_currency
    cell_tot_d.alignment = align_right
    cell_tot_d.border = total_border

    cell_tot_h = ws_d.cell(row=tot_row, column=7, value=f"=SUM(G{start_row}:G{end_row})")
    cell_tot_h.font = font_bold
    cell_tot_h.number_format = fmt_currency
    cell_tot_h.alignment = align_right
    cell_tot_h.border = total_border

    # Control de partida doble
    ctrl_row = tot_row + 2
    ws_d.cell(row=ctrl_row, column=4, value="CONTROL PARTIDA DOBLE (DEBE - HABER = 0):").font = font_bold
    ws_d.cell(row=ctrl_row, column=4).alignment = align_right
    cell_ctrl = ws_d.cell(row=ctrl_row, column=6, value=f"=F{tot_row}-G{tot_row}")
    cell_ctrl.font = font_bold
    cell_ctrl.number_format = fmt_currency
    cell_ctrl.alignment = align_center
    cell_ctrl.fill = fill_success

    cell_status = ws_d.cell(row=ctrl_row, column=7, value=f'=IF(F{tot_row}=G{tot_row}, "BALANCEADO Y CONFORME", "DESCUADRE")')
    cell_status.font = font_success
    cell_status.alignment = align_center
    cell_status.fill = fill_success

    # =========================================================================
    # 3. HOJA: MAYOR
    # =========================================================================
    ws_m = wb.create_sheet(title='Mayor')
    ws_m.views.sheetView[0].showGridLines = True

    ws_m['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_m['A1'].font = font_title
    ws_m['A2'] = "Libro Mayor de Cuentas (Fórmulas dinámicas hacia Diario)"
    ws_m['A2'].font = font_subtitle

    headers_mayor = ["Código", "Cuenta Mayor", "Total Debe (Cargos)", "Total Haber (Abonos)", "Saldo Deudor", "Saldo Acreedor"]
    for col_idx, h in enumerate(headers_mayor, 1):
        cell = ws_m.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_header
        cell.border = header_border

    cuentas_mayor_list = [
        ("1041", "Bancos - Cuentas Corrientes"),
        ("1212", "Cuentas por Cobrar Comerciales"),
        ("3361", "Equipos de Cómputo e Informáticos"),
        ("4111", "Remuneraciones por Pagar"),
        ("4212", "Cuentas por Pagar Comerciales - Proveedores"),
        ("4511", "Obligaciones Financieras - Préstamo Bancario"),
        ("4699", "Anticipos de Clientes (Ingresos Diferidos)"),
        ("5011", "Capital Social - Aportes de Socios"),
        ("7041", "Ingresos por Servicios de Software"),
        ("6941", "Costo de Servicio - Remuneraciones Desarrollo"),
        ("6942", "Costo de Servicio - Alojamiento en la Nube"),
        ("9411", "Gastos Administrativos Generales"),
        ("9412", "Gastos Administrativos - Sueldos Devengados"),
        ("9711", "Gastos Financieros - Intereses de Préstamo")
    ]

    m_start = 5
    for idx, (cod, nom) in enumerate(cuentas_mayor_list):
        r = m_start + idx
        ws_m.cell(row=r, column=1, value=cod).alignment = align_center
        ws_m.cell(row=r, column=2, value=nom).alignment = align_left
        
        # SUMIF Debe
        c_d = ws_m.cell(row=r, column=3, value=f"=SUMIF(Diario!$C$5:$C$28, A{r}, Diario!$F$5:$F$28)")
        c_d.number_format = fmt_currency
        c_d.alignment = align_right
        
        # SUMIF Haber
        c_h = ws_m.cell(row=r, column=4, value=f"=SUMIF(Diario!$C$5:$C$28, A{r}, Diario!$G$5:$G$28)")
        c_h.number_format = fmt_currency
        c_h.alignment = align_right

        # Saldo Deudor
        c_sd = ws_m.cell(row=r, column=5, value=f"=IF(C{r}>=D{r}, C{r}-D{r}, 0)")
        c_sd.number_format = fmt_currency
        c_sd.alignment = align_right

        # Saldo Acreedor
        c_sa = ws_m.cell(row=r, column=6, value=f"=IF(D{r}>C{r}, D{r}-C{r}, 0)")
        c_sa.number_format = fmt_currency
        c_sa.alignment = align_right

        for c_i in range(1, 7):
            cell = ws_m.cell(row=r, column=c_i)
            cell.font = font_regular
            cell.border = box_border

    m_end = m_start + len(cuentas_mayor_list) - 1
    m_tot = m_end + 1

    ws_m.cell(row=m_tot, column=2, value="TOTALES GENERALES").font = font_bold
    ws_m.cell(row=m_tot, column=2).alignment = align_right
    ws_m.cell(row=m_tot, column=2).border = total_border

    for c_i, col_let in enumerate(['C', 'D', 'E', 'F'], 3):
        c = ws_m.cell(row=m_tot, column=c_i, value=f"=SUM({col_let}{m_start}:{col_let}{m_end})")
        c.font = font_bold
        c.number_format = fmt_currency
        c.alignment = align_right
        c.border = total_border

    # =========================================================================
    # 4. HOJA: COMPROBACIÓN
    # =========================================================================
    ws_c = wb.create_sheet(title='Comprobación')
    ws_c.views.sheetView[0].showGridLines = True

    ws_c['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_c['A1'].font = font_title
    ws_c['A2'] = "Balance de Comprobación de Sumas y Saldos"
    ws_c['A2'].font = font_subtitle

    headers_comp = ["Código", "Nombre de la Cuenta", "Sumas Debe", "Sumas Haber", "Saldo Deudor", "Saldo Acreedor"]
    for col_idx, h in enumerate(headers_comp, 1):
        cell = ws_c.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_header
        cell.border = header_border

    c_start = 5
    for idx in range(len(cuentas_mayor_list)):
        r = c_start + idx
        m_r = m_start + idx
        ws_c.cell(row=r, column=1, value=f"=Mayor!A{m_r}").alignment = align_center
        ws_c.cell(row=r, column=2, value=f"=Mayor!B{m_r}").alignment = align_left
        ws_c.cell(row=r, column=3, value=f"=Mayor!C{m_r}").alignment = align_right
        ws_c.cell(row=r, column=4, value=f"=Mayor!D{m_r}").alignment = align_right
        ws_c.cell(row=r, column=5, value=f"=Mayor!E{m_r}").alignment = align_right
        ws_c.cell(row=r, column=6, value=f"=Mayor!F{m_r}").alignment = align_right

        for c_i in range(1, 7):
            cell = ws_c.cell(row=r, column=c_i)
            cell.font = font_regular
            cell.border = box_border
            if c_i >= 3:
                cell.number_format = fmt_currency

    c_end = c_start + len(cuentas_mayor_list) - 1
    c_tot = c_end + 1

    ws_c.cell(row=c_tot, column=2, value="TOTALES BALANCE COMPROBACIÓN").font = font_bold
    ws_c.cell(row=c_tot, column=2).alignment = align_right
    ws_c.cell(row=c_tot, column=2).border = total_border

    for c_i, col_let in enumerate(['C', 'D', 'E', 'F'], 3):
        c = ws_c.cell(row=c_tot, column=c_i, value=f"=SUM({col_let}{c_start}:{col_let}{c_end})")
        c.font = font_bold
        c.number_format = fmt_currency
        c.alignment = align_right
        c.border = total_border

    # Controles de verificación
    ws_c.cell(row=c_tot+2, column=2, value="Control Sumas Debe = Haber:").font = font_bold
    ws_c.cell(row=c_tot+2, column=3, value=f'=IF(C{c_tot}=D{c_tot}, "CUADRADO (DIF = 0)", "DESCUADRADO")').font = font_success
    ws_c.cell(row=c_tot+2, column=3).alignment = align_center
    ws_c.cell(row=c_tot+2, column=3).fill = fill_success

    ws_c.cell(row=c_tot+3, column=2, value="Control Saldos Deudor = Acreedor:").font = font_bold
    ws_c.cell(row=c_tot+3, column=5, value=f'=IF(E{c_tot}=F{c_tot}, "CUADRADO (DIF = 0)", "DESCUADRADO")').font = font_success
    ws_c.cell(row=c_tot+3, column=5).alignment = align_center
    ws_c.cell(row=c_tot+3, column=5).fill = fill_success

    # =========================================================================
    # 5. HOJA: SITUACIÓN FINANCIERA
    # =========================================================================
    ws_sf = wb.create_sheet(title='Situación financiera')
    ws_sf.views.sheetView[0].showGridLines = True

    ws_sf['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_sf['A1'].font = font_title
    ws_sf['A2'] = "Estado de Situación Financiera al 30 de Noviembre de 2026 (En Soles - S/)"
    ws_sf['A2'].font = font_subtitle

    # Estructura de Balance en 2 columnas: Activos a la izquierda (A-C), Pasivos y Patrimonio a la derecha (E-G)
    ws_sf.merge_cells('A4:C4')
    ws_sf['A4'] = "ACTIVO"
    ws_sf['A4'].font = font_header
    ws_sf['A4'].fill = fill_navy
    ws_sf['A4'].alignment = align_center

    ws_sf.merge_cells('E4:G4')
    ws_sf['E4'] = "PASIVO Y PATRIMONIO NETO"
    ws_sf['E4'].font = font_header
    ws_sf['E4'].fill = fill_navy
    ws_sf['E4'].alignment = align_center

    # Columnas detalle
    for col, txt in [('A', 'Código'), ('B', 'Cuenta de Activo'), ('C', 'Importe (S/)'), ('E', 'Código'), ('F', 'Cuenta de Pasivo / Patrimonio'), ('G', 'Importe (S/)')]:
        c = ws_sf[f'{col}5']
        c.value = txt
        c.font = font_sub_header
        c.fill = fill_accent
        c.alignment = align_center
        c.border = box_border

    # Activo Corriente
    ws_sf['B6'] = "ACTIVO CORRIENTE"
    ws_sf['B6'].font = font_bold
    ws_sf['A7'] = "1041"
    ws_sf['B7'] = "Efectivo y Equivalentes de Efectivo (Bancos)"
    ws_sf['C7'] = "=Mayor!E5" # Bancos Saldo Deudor
    ws_sf['A8'] = "1212"
    ws_sf['B8'] = "Cuentas por Cobrar Comerciales (Cliente Salud)"
    ws_sf['C8'] = "=Mayor!E6" # CxC Saldo Deudor
    ws_sf['B9'] = "Total Activo Corriente"
    ws_sf['B9'].font = font_bold
    ws_sf['C9'] = "=SUM(C7:C8)"
    ws_sf['C9'].font = font_bold
    ws_sf['C9'].border = total_border

    # Activo No Corriente
    ws_sf['B11'] = "ACTIVO NO CORRIENTE"
    ws_sf['B11'].font = font_bold
    ws_sf['A12'] = "3361"
    ws_sf['B12'] = "Equipos de Cómputo e Informáticos (Activo Fijo)"
    ws_sf['C12'] = "=Mayor!E7" # Equipos Saldo Deudor
    ws_sf['B13'] = "Total Activo No Corriente"
    ws_sf['B13'].font = font_bold
    ws_sf['C13'] = "=C12"
    ws_sf['C13'].font = font_bold
    ws_sf['C13'].border = total_border

    # Total Activo
    ws_sf['B15'] = "TOTAL ACTIVO"
    ws_sf['B15'].font = Font(name='Segoe UI', size=11, bold=True, color='1E3A8A')
    ws_sf['C15'] = "=C9+C13"
    ws_sf['C15'].font = Font(name='Segoe UI', size=11, bold=True, color='1E3A8A')
    ws_sf['C15'].border = Border(top=border_thin, bottom=border_double)
    ws_sf['C15'].fill = fill_light_blue

    # Pasivo Corriente
    ws_sf['F6'] = "PASIVO CORRIENTE"
    ws_sf['F6'].font = font_bold
    ws_sf['E7'] = "4212"
    ws_sf['F7'] = "Cuentas por Pagar Comerciales - Proveedores"
    ws_sf['G7'] = "=Mayor!F9" # Proveedores Saldo Acreedor
    ws_sf['E8'] = "4511"
    ws_sf['F8'] = "Obligaciones Financieras (Préstamo Bancario 6m)"
    ws_sf['G8'] = "=Mayor!F10" # Préstamo Saldo Acreedor
    ws_sf['E9'] = "4699"
    ws_sf['F9'] = "Anticipos de Clientes (Servicio Futuro)"
    ws_sf['G9'] = "=Mayor!F11" # Anticipo Saldo Acreedor
    ws_sf['E10'] = "4111"
    ws_sf['F10'] = "Remuneraciones y Participaciones por Pagar"
    ws_sf['G10'] = "=Mayor!F8" # Remuneraciones Saldo Acreedor
    ws_sf['F11'] = "Total Pasivo Corriente"
    ws_sf['F11'].font = font_bold
    ws_sf['G11'] = "=SUM(G7:G10)"
    ws_sf['G11'].font = font_bold
    ws_sf['G11'].border = total_border

    # Patrimonio Neto
    ws_sf['F13'] = "PATRIMONIO NETO"
    ws_sf['F13'].font = font_bold
    ws_sf['E14'] = "5011"
    ws_sf['F14'] = "Capital Social (Aportes de los Socios)"
    ws_sf['G14'] = "=Mayor!F12" # Capital Saldo Acreedor
    ws_sf['E15'] = "5911"
    ws_sf['F15'] = "Resultado del Ejercicio (Utilidad Neta del Mes)"
    ws_sf['G15'] = "=Resultados!C17" # Referencia a la Utilidad Neta en Estado de Resultados
    ws_sf['F16'] = "Total Patrimonio Neto"
    ws_sf['F16'].font = font_bold
    ws_sf['G16'] = "=SUM(G14:G15)"
    ws_sf['G16'].font = font_bold
    ws_sf['G16'].border = total_border

    # Total Pasivo + Patrimonio
    ws_sf['F18'] = "TOTAL PASIVO Y PATRIMONIO NETO"
    ws_sf['F18'].font = Font(name='Segoe UI', size=11, bold=True, color='1E3A8A')
    ws_sf['G18'] = "=G11+G16"
    ws_sf['G18'].font = Font(name='Segoe UI', size=11, bold=True, color='1E3A8A')
    ws_sf['G18'].border = Border(top=border_thin, bottom=border_double)
    ws_sf['G18'].fill = fill_light_blue

    # Formatos
    for r in range(6, 20):
        for c in ['C', 'G']:
            cell = ws_sf[f'{c}{r}']
            if cell.value:
                cell.number_format = fmt_currency
                cell.alignment = align_right

    # Ecuación Contable Visible
    ws_sf['B21'] = "CONTROL ECUACIÓN CONTABLE (ACTIVO - PASIVO - PATRIMONIO = 0):"
    ws_sf['B21'].font = font_bold
    ws_sf['B21'].alignment = align_right
    c_eq = ws_sf['C21']
    c_eq.value = "=C15-G18"
    c_eq.font = font_bold
    c_eq.number_format = fmt_currency
    c_eq.alignment = align_center
    c_eq.fill = fill_success

    c_eq_st = ws_sf['F21']
    c_eq_st.value = '=IF(C15=G18, "ECUACIÓN CONTABLE CUMPLE EXACTAMENTE (S/ 64,500.00)", "ERROR")'
    c_eq_st.font = font_success
    c_eq_st.alignment = align_left
    c_eq_st.fill = fill_success

    # =========================================================================
    # 6. HOJA: RESULTADOS
    # =========================================================================
    ws_r = wb.create_sheet(title='Resultados')
    ws_r.views.sheetView[0].showGridLines = True

    ws_r['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_r['A1'].font = font_title
    ws_r['A2'] = "Estado de Resultados del 01 al 30 de Noviembre de 2026 (En Soles - S/)"
    ws_r['A2'].font = font_subtitle

    headers_res = ["Código", "Concepto / Línea del Estado de Resultados", "Importe (S/)", "Análisis Vertical (%)", "Notas Contables"]
    for col_idx, h in enumerate(headers_res, 1):
        cell = ws_r.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_header
        cell.border = header_border

    res_items = [
        ("7041", "Ingresos por Servicios de Software (Hito 1 PANVIZ)", "=Mayor!F13", "=C5/$C$5", "Hito 1 entregado y aceptado (Devengado)"),
        ("6941", "(-) Costo del Servicio - Remuneraciones Desarrollo", "=Mayor!E14", "=C6/$C$5", "Personal técnico directo consumido en el mes"),
        ("6942", "(-) Costo del Servicio - Alojamiento en la Nube", "=Mayor!E15", "=C7/$C$5", "Infraestructura cloud consumida en el hito 1"),
        ("", "TOTAL COSTO DEL SERVICIO", "=SUM(C6:C7)", "=C8/$C$5", "Costos directos vinculados al software"),
        ("", "UTILIDAD BRUTA", "=C5-C8", "=C9/$C$5", "Margen bruto operativo (29.17%)"),
        ("9411", "(-) Gastos Administrativos - Generales Pagados", "=Mayor!E16", "=C10/$C$5", "Gastos de gestión operativa del periodo"),
        ("9412", "(-) Gastos Administrativos - Sueldos Devengados", "=Mayor!E17", "=C11/$C$5", "Sueldos administrativos pendientes de pago"),
        ("", "TOTAL GASTOS ADMINISTRATIVOS", "=SUM(C10:C11)", "=C12/$C$5", "Carga administrativa del periodo"),
        ("", "UTILIDAD OPERATIVA", "=C9-C12", "=C13/$C$5", "Resultado de la actividad del negocio"),
        ("9711", "(-) Gastos Financieros - Intereses de Préstamo", "=Mayor!E18", "=C14/$C$5", "Intereses bancarios pagados en el mes"),
        ("", "RESULTADO ANTES DE IMPUESTOS", "=C13-C14", "=C15/$C$5", "Base imponible operativa"),
        ("", "(-) Impuesto a la Renta (Omitido por bases)", 0.0, "0.00%", "Delimitación del caso de estudio"),
        ("", "UTILIDAD NETA DEL EJERCICIO", "=C15-C16", "=C17/$C$5", "Resultado final que capitaliza el patrimonio")
    ]

    for idx, (cod, nom, val, pct, nota) in enumerate(res_items, 5):
        ws_r.cell(row=idx, column=1, value=cod).alignment = align_center
        ws_r.cell(row=idx, column=2, value=nom).alignment = align_left
        
        c_val = ws_r.cell(row=idx, column=3, value=val)
        c_val.alignment = align_right
        c_val.number_format = fmt_currency

        c_pct = ws_r.cell(row=idx, column=4, value=pct)
        c_pct.alignment = align_right
        c_pct.number_format = fmt_percent

        ws_r.cell(row=idx, column=5, value=nota).alignment = align_left

        is_tot = "TOTAL" in nom or "UTILIDAD" in nom or "RESULTADO" in nom
        for c_i in range(1, 6):
            cell = ws_r.cell(row=idx, column=c_i)
            cell.font = font_bold if is_tot else font_regular
            cell.border = box_border
            if is_tot:
                cell.fill = fill_light_blue
        if nom in ["UTILIDAD BRUTA", "UTILIDAD OPERATIVA", "UTILIDAD NETA DEL EJERCICIO"]:
            ws_r.cell(row=idx, column=3).border = total_border

    # =========================================================================
    # 7. HOJA: PATRIMONIO
    # =========================================================================
    ws_p = wb.create_sheet(title='Patrimonio')
    ws_p.views.sheetView[0].showGridLines = True

    ws_p['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_p['A1'].font = font_title
    ws_p['A2'] = "Estado de Cambios en el Patrimonio Neto (Mes 1 - Noviembre 2026)"
    ws_p['A2'].font = font_subtitle

    headers_pat = ["Concepto Patrimonial", "Capital Social (S/)", "Resultados Acumulados (S/)", "Total Patrimonio Neto (S/)"]
    for col_idx, h in enumerate(headers_pat, 1):
        cell = ws_p.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_header
        cell.border = header_border

    pat_rows = [
        ("Saldo Inicial al 01/11/2026", 0.0, 0.0, "=B5+C5"),
        ("Aportes de Capital de los Socios (OP01)", "=Mayor!F12", 0.0, "=B6+C6"),
        ("Utilidad Neta del Ejercicio (Resultados)", 0.0, "=Resultados!C17", "=B7+C7"),
        ("SALDO FINAL AL 30/11/2026", "=SUM(B5:B7)", "=SUM(C5:C7)", "=B8+C8")
    ]

    for idx, (nom, cap, res, tot) in enumerate(pat_rows, 5):
        ws_p.cell(row=idx, column=1, value=nom).alignment = align_left
        ws_p.cell(row=idx, column=2, value=cap).alignment = align_right
        ws_p.cell(row=idx, column=3, value=res).alignment = align_right
        ws_p.cell(row=idx, column=4, value=tot).alignment = align_right

        is_tot = idx == 8
        for c_i in range(1, 5):
            cell = ws_p.cell(row=idx, column=c_i)
            cell.font = font_bold if is_tot else font_regular
            cell.border = total_border if is_tot else box_border
            if c_i >= 2:
                cell.number_format = fmt_currency
            if is_tot:
                cell.fill = fill_light_blue

    # Control de variación patrimonial
    ws_p['A10'] = "Control: Variación Patrimonial sin Aportes = Resultado del Mes"
    ws_p['A10'].font = font_bold
    ws_p['D10'] = "=D8-B6"
    ws_p['D10'].font = font_bold
    ws_p['D10'].number_format = fmt_currency
    ws_p['D10'].fill = fill_success

    # =========================================================================
    # 8. HOJA: FLUJO
    # =========================================================================
    ws_f = wb.create_sheet(title='Flujo')
    ws_f.views.sheetView[0].showGridLines = True

    ws_f['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_f['A1'].font = font_title
    ws_f['A2'] = "Estado de Flujos de Efectivo - Método Directo (Noviembre 2026)"
    ws_f['A2'].font = font_subtitle

    headers_flujo = ["Actividad / Concepto de Flujo de Efectivo", "Referencia OP", "Entradas / Cobros (S/)", "Salidas / Pagos (S/)", "Flujo Neto (S/)"]
    for col_idx, h in enumerate(headers_flujo, 1):
        cell = ws_f.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_header
        cell.border = header_border

    # Criterio declarado de intereses: Actividades de Operación (NIC 7 párrafo 31)
    flujo_data = [
        ("ACTIVIDADES DE OPERACIÓN", "", "", "", ""),
        ("Cobranza en efectivo por entrega de Hito 1 PANVIZ", "OP08", 16000.0, 0.0, ""),
        ("Anticipo en efectivo recibido de la entidad de salud", "OP04", 9000.0, 0.0, ""),
        ("(-) Pago de remuneraciones de desarrollo de software", "OP05", 0.0, 15000.0, ""),
        ("(-) Pago de servicios de nube e infraestructura", "OP06", 0.0, 2000.0, ""),
        ("(-) Pago de gastos operativos y administrativos", "OP07", 0.0, 3000.0, ""),
        ("(-) Pago de intereses del préstamo bancario (Criterio Operativo)", "OP11", 0.0, 500.0, ""),
        ("FLUJO NETO DE ACTIVIDADES DE OPERACIÓN", "", "=SUM(C6:C11)", "=SUM(D6:D11)", "=C12-D12"),
        ("", "", "", "", ""),
        ("ACTIVIDADES DE INVERSIÓN", "", "", "", ""),
        ("(-) Pago inicial de contado por compra de equipos de cómputo", "OP02", 0.0, 8000.0, ""),
        ("(-) Pago posterior de amortización a proveedor de equipos", "OP09", 0.0, 2000.0, ""),
        ("FLUJO NETO DE ACTIVIDADES DE INVERSIÓN", "", "=SUM(C15:C16)", "=SUM(D15:D16)", "=C17-D17"),
        ("", "", "", "", ""),
        ("ACTIVIDADES DE FINANCIACIÓN", "", "", "", ""),
        ("Aporte de capital inicial de los socios en efectivo", "OP01", 40000.0, 0.0, ""),
        ("Desembolso de préstamo bancario obtenido", "OP03", 10000.0, 0.0, ""),
        ("FLUJO NETO DE ACTIVIDADES DE FINANCIACIÓN", "", "=SUM(C20:C21)", "=SUM(D20:D21)", "=C22-D22"),
        ("", "", "", "", ""),
        ("VARIACIÓN NETA DE EFECTIVO DEL PERIODO", "", "", "", "=E12+E17+E22"),
        ("Saldo Inicial de Efectivo y Equivalentes (01/11/2026)", "", "", "", 0.0),
        ("SALDO FINAL DE EFECTIVO Y EQUIVALENTES AL 30/11/2026", "", "", "", "=E24+E25")
    ]

    for idx, (nom, op, ent, sal, net) in enumerate(flujo_data, 5):
        ws_f.cell(row=idx, column=1, value=nom).alignment = align_left
        ws_f.cell(row=idx, column=2, value=op).alignment = align_center
        ws_f.cell(row=idx, column=3, value=ent).alignment = align_right
        ws_f.cell(row=idx, column=4, value=sal).alignment = align_right
        ws_f.cell(row=idx, column=5, value=net).alignment = align_right

        is_header_sec = nom in ["ACTIVIDADES DE OPERACIÓN", "ACTIVIDADES DE INVERSIÓN", "ACTIVIDADES DE FINANCIACIÓN"]
        is_tot_sec = "FLUJO NETO" in nom or "SALDO FINAL" in nom or "VARIACIÓN NETA" in nom

        for c_i in range(1, 6):
            cell = ws_f.cell(row=idx, column=c_i)
            cell.border = box_border
            if is_header_sec:
                cell.font = font_sub_header
                cell.fill = fill_accent
            elif is_tot_sec:
                cell.font = font_bold
                cell.fill = fill_light_blue
                if "SALDO FINAL" in nom:
                    cell.border = Border(top=border_thin, bottom=border_double)
            else:
                cell.font = font_regular

            if c_i in [3, 4, 5] and cell.value != "":
                cell.number_format = fmt_currency

    # Control con Saldo en Bancos
    ws_f['A28'] = "CONTROL CONCILIACIÓN: SALDO FINAL FLUJO = SALDO EN BANCOS (SITUACIÓN FINANCIERA)"
    ws_f['A28'].font = font_bold
    ws_f['C28'] = "=E26-Mayor!E5"
    ws_f['C28'].font = font_bold
    ws_f['C28'].number_format = fmt_currency
    ws_f['C28'].fill = fill_success

    ws_f['E28'] = '=IF(E26=Mayor!E5, "CONCILIADO EXACTO (DIFERENCIA = S/ 0.00)", "ERROR")'
    ws_f['E28'].font = font_success
    ws_f['E28'].fill = fill_success

    # =========================================================================
    # 9. HOJA: CAJA 15 DÍAS
    # =========================================================================
    ws_cj = wb.create_sheet(title='Caja 15 días')
    ws_cj.views.sheetView[0].showGridLines = True

    ws_cj['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_cj['A1'].font = font_title
    ws_cj['A2'] = "Presupuesto de Caja a 15 Días, Proyección de Estrés a 45 Días e Indicadores Financieros"
    ws_cj['A2'].font = font_subtitle

    # Indicadores Financieros
    ws_cj['A4'] = "EVALUACIÓN DEL CONTROL ECONÓMICO E INDICADORES CLAVE"
    ws_cj['A4'].font = font_header
    ws_cj.merge_cells('A4:E4')
    ws_cj['A4'].fill = fill_navy

    indicadores = [
        ("Margen Neto", "=Resultados!C17/Resultados!C5", fmt_percent, "Resultado del Mes / Ingresos Totales", "8.33% - Rentabilidad contable sobre ingresos facturados"),
        ("Razón Corriente", "='Situación financiera'!C9/'Situación financiera'!G11", fmt_number, "Activo Corriente / Pasivo Corriente", "2.33 - Aparente solvencia a corto plazo (distorsionada)"),
        ("Cobertura Inmediata", "=Mayor!E5/D17", fmt_number, "Saldo en Bancos / Pagos Previstos en 15 días", "1.89 - Capacidad de pago para la primera quincena")
    ]

    for idx, (ind, form, f_type, formula_txt, interp) in enumerate(indicadores, 5):
        ws_cj.cell(row=idx, column=1, value=ind).font = font_bold
        c_val = ws_cj.cell(row=idx, column=2, value=form)
        c_val.font = font_bold
        c_val.number_format = f_type
        c_val.alignment = align_center
        c_val.fill = fill_light_blue
        ws_cj.cell(row=idx, column=3, value=formula_txt).font = font_regular
        ws_cj.cell(row=idx, column=4, value=interp).font = font_regular

        for c_i in range(1, 5):
            ws_cj.cell(row=idx, column=c_i).border = box_border

    # Presupuesto de Tesorería a 15 días
    ws_cj['A10'] = "PRESUPUESTO DE CAJA - PRIMEROS 15 DÍAS (01/12 AL 15/12)"
    ws_cj['A10'].font = font_header
    ws_cj.merge_cells('A10:D10')
    ws_cj['A10'].fill = fill_slate

    caja_15_rows = [
        ("Saldo Inicial en Bancos (Disponible al cierre del mes)", "=Mayor!E5", "Efectivo real en cuenta corriente"),
        ("(+) Cobros proyectados de clientes en 15 días", 0.0, "Cliente advirtió que S/ 8,000 se cobran en 45 días"),
        ("TOTAL EFECTIVO DISPONIBLE QUINCENA", "=B11+B12", "Fondos para hacer frente a obligaciones"),
        ("(-) Pagos de remuneraciones técnicas y desarrollo", 18000.0, "Personal técnico para módulo de alertas"),
        ("(-) Pagos de servicios de nube e infraestructura", 2000.0, "Consumo continuo de servidores cloud"),
        ("(-) Pago deuda restante proveedor de equipos informáticos", 2000.0, "Saldo pendiente de compra de hardware"),
        ("(-) Pago de remuneraciones administrativas pendientes", 1500.0, "Pasivo devengado en OP10"),
        ("TOTAL EGRESOS PREVISTOS EN 15 DÍAS", "=SUM(B14:B17)", "Salidas de efectivo comprometidas"),
        ("SALDO FINAL ESTIMADO AL DÍA 15 (EXCEDENTE)", "=B13-B18", "Excedente de caja transitorio al día 15")
    ]

    for idx, (nom, val, desc) in enumerate(caja_15_rows, 11):
        ws_cj.cell(row=idx, column=1, value=nom).alignment = align_left
        c_val = ws_cj.cell(row=idx, column=2, value=val)
        c_val.alignment = align_right
        c_val.number_format = fmt_currency
        ws_cj.cell(row=idx, column=3, value=desc).alignment = align_left

        is_tot = "TOTAL" in nom or "SALDO FINAL" in nom
        for c_i in range(1, 4):
            cell = ws_cj.cell(row=idx, column=c_i)
            cell.font = font_bold if is_tot else font_regular
            cell.border = total_border if is_tot else box_border
            if is_tot:
                cell.fill = fill_light_blue

    # Análisis de Estrés Financiero a 45 Días
    ws_cj['A21'] = "PROYECCIÓN DE LIQUIDEZ Y ESTRÉS FINANCIERO A 45 DÍAS (DÍA 16 AL 45)"
    ws_cj['A21'].font = font_header
    ws_cj.merge_cells('A21:D21')
    ws_cj['A21'].fill = PatternFill(start_color='991B1B', end_color='991B1B', fill_type='solid') # Red Header

    estres_rows = [
        ("Saldo al inicio del periodo de estrés (Día 16)", "=B19", "Efectivo remanente de la primera quincena"),
        ("(+) Cobranzas proyectadas del Día 16 al Día 44", 0.0, "No hay nuevos cobros programados"),
        ("(-) Egresos operativos estimados del Día 16 al Día 44 (Nómina + Nube + Gastos)", 23500.0, "Obligaciones mensuales recurrentes para sostener PANVIZ"),
        ("DÉFICIT PROYECTADO ANTES DE COBRANZA EN DÍA 45", "=B22+B23-B24", "QUIEBRA TÉCNICA DE CAJA SIN GESTIÓN DE LIQUIDEZ"),
        ("(+) Cobranza pendiente de la entidad de salud en Día 45", "=Mayor!E6", "Ingreso de S/ 8,000 en el día 45"),
        ("SALDO PROYECTADO TRAS COBRANZA DÍA 45", "=B25+B26", "Situación de caja severamente debilitada")
    ]

    for idx, (nom, val, desc) in enumerate(estres_rows, 22):
        ws_cj.cell(row=idx, column=1, value=nom).alignment = align_left
        c_val = ws_cj.cell(row=idx, column=2, value=val)
        c_val.alignment = align_right
        c_val.number_format = fmt_currency
        ws_cj.cell(row=idx, column=3, value=desc).alignment = align_left

        is_tot = "DÉFICIT" in nom or "SALDO PROYECTADO" in nom
        for c_i in range(1, 4):
            cell = ws_cj.cell(row=idx, column=c_i)
            cell.font = font_bold if is_tot else font_regular
            cell.border = total_border if is_tot else box_border
            if "DÉFICIT" in nom:
                cell.fill = fill_gold
                cell.font = Font(name='Segoe UI', size=10, bold=True, color='991B1B')

    # =========================================================================
    # 10. HOJA: CONCILIACIÓN GNUCASH
    # =========================================================================
    ws_cg = wb.create_sheet(title='Conciliación GnuCash')
    ws_cg.views.sheetView[0].showGridLines = True

    ws_cg['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_cg['A1'].font = font_title
    ws_cg['A2'] = "Tabla de Conciliación Integral entre Calc / Excel y GnuCash (Corte 30/11/2026)"
    ws_cg['A2'].font = font_subtitle

    headers_concil = ["Código", "Cuenta o Indicador Financiero", "Saldo Calc (S/)", "Saldo GnuCash (S/)", "Diferencia (S/)", "Estado de Conciliación", "Evidencia en GnuCash"]
    for col_idx, h in enumerate(headers_concil, 1):
        cell = ws_cg.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_header
        cell.border = header_border

    concil_data = [
        ("1041", "Bancos - Cuenta Corriente", "=Mayor!E5", 44500.0, "Cuenta Corriente en GnuCash"),
        ("1212", "Cuentas por Cobrar (Clientes)", "=Mayor!E6", 8000.0, "Activos:Clientes:Facturas por Cobrar"),
        ("3361", "Equipos Informáticos", "=Mayor!E7", 12000.0, "Activos:Equipos Informáticos"),
        ("4212", "Cuentas por Pagar Proveedores", "=Mayor!F9", 2000.0, "Pasivos:Proveedores:Equipos"),
        ("4511", "Obligaciones Financieras (Préstamo)", "=Mayor!F10", 10000.0, "Pasivos:Préstamos Bancarios"),
        ("4699", "Anticipos de Clientes", "=Mayor!F11", 9000.0, "Pasivos:Anticipos de Clientes"),
        ("4111", "Remuneraciones por Pagar", "=Mayor!F8", 1500.0, "Pasivos:Sueldos por Pagar"),
        ("5011", "Capital Social (Aportes)", "=Mayor!F12", 40000.0, "Patrimonio:Capital Social"),
        ("7041", "Ingresos por Servicios de Software", "=Mayor!F13", 24000.0, "Ingresos:Desarrollo de Software"),
        ("6941", "Costo Servicio - Remuneraciones", "=Mayor!E14", 15000.0, "Gastos:Costo:Remuneraciones"),
        ("6942", "Costo Servicio - Nube", "=Mayor!E15", 2000.0, "Gastos:Costo:Servicios de Nube"),
        ("9411", "Gastos Administrativos Generales", "=Mayor!E16", 3000.0, "Gastos:Administrativos:Generales"),
        ("9412", "Gastos Adm. - Sueldos Devengados", "=Mayor!E17", 1500.0, "Gastos:Administrativos:Sueldos"),
        ("9711", "Gastos Financieros - Intereses", "=Mayor!E18", 500.0, "Gastos:Financieros:Intereses"),
        ("5911", "Resultado del Ejercicio (Utilidad Neta)", "=Resultados!C17", 2000.0, "Pérdidas y Ganancias GnuCash"),
        ("PAT", "Patrimonio Neto Total", "='Situación financiera'!G16", 42000.0, "Balance General GnuCash: Total Patrimonio")
    ]

    for idx, (cod, nom, form_calc, val_gnu, evid) in enumerate(concil_data, 5):
        ws_cg.cell(row=idx, column=1, value=cod).alignment = align_center
        ws_cg.cell(row=idx, column=2, value=nom).alignment = align_left
        
        c_calc = ws_cg.cell(row=idx, column=3, value=form_calc)
        c_calc.number_format = fmt_currency
        c_calc.alignment = align_right

        c_gnu = ws_cg.cell(row=idx, column=4, value=val_gnu)
        c_gnu.number_format = fmt_currency
        c_gnu.alignment = align_right

        c_dif = ws_cg.cell(row=idx, column=5, value=f"=C{idx}-D{idx}")
        c_dif.number_format = fmt_currency
        c_dif.alignment = align_right

        c_st = ws_cg.cell(row=idx, column=6, value=f'=IF(E{idx}=0, "CONCILIADO EXACTO", "DISCREPANCIA")')
        c_st.alignment = align_center
        c_st.font = font_success
        c_st.fill = fill_success

        ws_cg.cell(row=idx, column=7, value=evid).alignment = align_left

        for c_i in range(1, 8):
            cell = ws_cg.cell(row=idx, column=c_i)
            cell.font = font_bold if cod in ["5911", "PAT"] else font_regular
            cell.border = box_border

    tot_concil_r = len(concil_data) + 5
    ws_cg.cell(row=tot_concil_r, column=2, value="SUMATORIA DE DIFERENCIAS").font = font_bold
    ws_cg.cell(row=tot_concil_r, column=2).alignment = align_right
    c_tot_dif = ws_cg.cell(row=tot_concil_r, column=5, value=f"=SUM(E5:E{tot_concil_r-1})")
    c_tot_dif.font = font_bold
    c_tot_dif.number_format = fmt_currency
    c_tot_dif.alignment = align_right
    c_tot_dif.border = total_border
    c_tot_dif.fill = fill_success

    ws_cg.cell(row=tot_concil_r, column=6, value=f'=IF(E{tot_concil_r}=0, "DIFERENCIA CERO (100% CONCILIADO)", "ERROR")').font = font_success
    ws_cg.cell(row=tot_concil_r, column=6).alignment = align_center
    ws_cg.cell(row=tot_concil_r, column=6).fill = fill_success

    # =========================================================================
    # 11. HOJA: PARTICIPACIÓN
    # =========================================================================
    ws_pt = wb.create_sheet(title='Participación')
    ws_pt.views.sheetView[0].showGridLines = True

    ws_pt['A1'] = "ANDES SOFTWARE - PROYECTO PANVIZ"
    ws_pt['A1'].font = font_title
    ws_pt['A2'] = "Matriz de Distribución de Responsabilidades y Revisión Cruzada (Peer Review)"
    ws_pt['A2'].font = font_subtitle

    headers_part = ["#", "Estudiante Integrante", "CUI", "Correo Institucional", "Responsabilidad Principal", "Entregable / Hoja Custodiada", "Revisión Cruzada Realizada", "Conformidad"]
    for col_idx, h in enumerate(headers_part, 1):
        cell = ws_pt.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_header
        cell.border = header_border

    integrantes_info = [
        ("1", "Suclle Suca, Michael Benjamin", "20210678", "msuclles@unsa.edu.pe", "Coordinación general, síntesis crítica de lectura e integración", "Informe PDF/MD y Sección 1, 2", "Revisa decisiones y sustento del integrante 5", "APROBADO (100%)"),
        ("2", "Fernandez Huarca, Rodrigo Alexander", "20210672", "rfernandezh@unsa.edu.pe", "Catálogo y registros completos en GnuCash", "Archivo PANVIZ_equipo06.gnucash y reportes", "Revisa síntesis e informe del integrante 1", "APROBADO (100%)"),
        ("3", "Meza Vizcarra, Cielo Cristal", "20210685", "cmezav@unsa.edu.pe", "Hoja de cálculo: Cuentas, Diario, Mayor y Comprobación", "Hojas Cuentas, Diario, Mayor, Comprobación", "Revisa libro GnuCash del integrante 2", "APROBADO (100%)"),
        ("4", "Borda Espinoza, Gabriela Nayely", "20210665", "gbordae@unsa.edu.pe", "Estados financieros y tabla integral de conciliación", "Hojas Situación Fin., Resultados, Flujo, Patrimonio", "Revisa mayorización y balance del integrante 3", "APROBADO (100%)"),
        ("5", "Ccoscco Alvis, Italo Frankdux", "20210669", "iccosccoa@unsa.edu.pe", "Indicadores, presupuesto de caja y decisiones", "Hoja Caja 15 días y Sección 5, 6 de decisiones", "Revisa estados financieros del integrante 4", "APROBADO (100%)")
    ]

    for idx, row_vals in enumerate(integrantes_info, 5):
        for c_i, v in enumerate(row_vals, 1):
            cell = ws_pt.cell(row=idx, column=c_i, value=v)
            cell.font = font_regular
            cell.border = box_border
            if c_i in [1, 3, 8]:
                cell.alignment = align_center
            else:
                cell.alignment = align_left
            if c_i == 8:
                cell.font = font_success
                cell.fill = fill_success

    # Ajustar ancho de columnas automáticamente en todas las hojas
    for sheet in wb.worksheets:
        for col in sheet.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                # Omitir títulos combinados en fila 1 y 2 para ancho
                if cell.row in [1, 2]:
                    continue
                val_str = str(cell.value or '')
                if len(val_str) > max_len:
                    max_len = len(val_str)
            sheet.column_dimensions[col_letter].width = max(max_len + 3, 12)

    wb.save(filepath)
    print(f"Libro Excel generado exitosamente en: {filepath}")

if __name__ == '__main__':
    out_path = r"C:\Users\micha\Downloads\Borrar entregable 6\GPS-Entregable-6\PANVIZ_Control_Economico_Equipo06.xlsx"
    build_panviz_excel(out_path)
