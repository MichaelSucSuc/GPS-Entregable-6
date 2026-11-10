import uuid
import datetime

def make_guid():
    return uuid.uuid4().hex

def generate_gnucash_file(output_path):
    book_id = make_guid()
    root_id = make_guid()
    
    # Account definitions: (name, type, parent_id, code)
    # Types: ROOT, ASSET, BANK, RECEIVABLE, LIABILITY, PAYABLE, EQUITY, INCOME, EXPENSE
    accounts = {}
    
    # Root
    accounts['ROOT'] = {'id': root_id, 'name': 'Root Account', 'type': 'ROOT', 'parent': None, 'code': ''}
    
    # Level 1 Main categories
    for cat, ctype in [('Activos', 'ASSET'), ('Pasivos', 'LIABILITY'), ('Patrimonio', 'EQUITY'), ('Ingresos', 'INCOME'), ('Gastos', 'EXPENSE')]:
        accounts[cat] = {'id': make_guid(), 'name': cat, 'type': ctype, 'parent': root_id, 'code': ''}
        
    # Level 2 & 3
    # Activos
    accounts['Activo Corriente'] = {'id': make_guid(), 'name': 'Activo Corriente', 'type': 'ASSET', 'parent': accounts['Activos']['id'], 'code': '10'}
    accounts['Bancos'] = {'id': make_guid(), 'name': 'Cuenta Corriente Bancaria', 'type': 'BANK', 'parent': accounts['Activo Corriente']['id'], 'code': '1041'}
    accounts['Clientes'] = {'id': make_guid(), 'name': 'Facturas por Cobrar Comerciales', 'type': 'RECEIVABLE', 'parent': accounts['Activo Corriente']['id'], 'code': '1212'}
    accounts['Activo No Corriente'] = {'id': make_guid(), 'name': 'Activo No Corriente', 'type': 'ASSET', 'parent': accounts['Activos']['id'], 'code': '33'}
    accounts['Equipos'] = {'id': make_guid(), 'name': 'Equipos Informáticos y Cómputo', 'type': 'ASSET', 'parent': accounts['Activo No Corriente']['id'], 'code': '3361'}

    # Pasivos
    accounts['Pasivo Corriente'] = {'id': make_guid(), 'name': 'Pasivo Corriente', 'type': 'LIABILITY', 'parent': accounts['Pasivos']['id'], 'code': '40'}
    accounts['Proveedores'] = {'id': make_guid(), 'name': 'Proveedores por Pagar', 'type': 'PAYABLE', 'parent': accounts['Pasivo Corriente']['id'], 'code': '4212'}
    accounts['Prestamos'] = {'id': make_guid(), 'name': 'Préstamos Bancarios Corto Plazo', 'type': 'LIABILITY', 'parent': accounts['Pasivo Corriente']['id'], 'code': '4511'}
    accounts['Anticipos'] = {'id': make_guid(), 'name': 'Anticipos de Clientes (Diferidos)', 'type': 'LIABILITY', 'parent': accounts['Pasivo Corriente']['id'], 'code': '4699'}
    accounts['RemuneracionesPagar'] = {'id': make_guid(), 'name': 'Remuneraciones por Pagar', 'type': 'LIABILITY', 'parent': accounts['Pasivo Corriente']['id'], 'code': '4111'}

    # Patrimonio
    accounts['Capital'] = {'id': make_guid(), 'name': 'Capital Social Aportado', 'type': 'EQUITY', 'parent': accounts['Patrimonio']['id'], 'code': '5011'}
    accounts['ResultadosAcum'] = {'id': make_guid(), 'name': 'Resultados del Ejercicio', 'type': 'EQUITY', 'parent': accounts['Patrimonio']['id'], 'code': '5911'}

    # Ingresos
    accounts['VentasSoftware'] = {'id': make_guid(), 'name': 'Ingresos por Desarrollo de Software', 'type': 'INCOME', 'parent': accounts['Ingresos']['id'], 'code': '7041'}

    # Gastos / Costos
    accounts['CostosServicio'] = {'id': make_guid(), 'name': 'Costo del Servicio PANVIZ', 'type': 'EXPENSE', 'parent': accounts['Gastos']['id'], 'code': '69'}
    accounts['CostoRemun'] = {'id': make_guid(), 'name': 'Remuneraciones de Desarrollo', 'type': 'EXPENSE', 'parent': accounts['CostosServicio']['id'], 'code': '6941'}
    accounts['CostoNube'] = {'id': make_guid(), 'name': 'Servicios de Infraestructura Cloud', 'type': 'EXPENSE', 'parent': accounts['CostosServicio']['id'], 'code': '6942'}
    accounts['GastosAdmin'] = {'id': make_guid(), 'name': 'Gastos Administrativos Generales', 'type': 'EXPENSE', 'parent': accounts['Gastos']['id'], 'code': '9411'}
    accounts['GastosAdminSueldos'] = {'id': make_guid(), 'name': 'Sueldos Administrativos Devengados', 'type': 'EXPENSE', 'parent': accounts['Gastos']['id'], 'code': '9412'}
    accounts['GastosFinanc'] = {'id': make_guid(), 'name': 'Gastos Financieros e Intereses', 'type': 'EXPENSE', 'parent': accounts['Gastos']['id'], 'code': '9711'}

    # Transactions
    # (num, desc, date, [(acc_key, amount)])
    # In GnuCash, debit to Asset/Expense is positive (+), credit is negative (-)
    txs = [
        ("OP01", "Aporte inicial de los socios depositado en bancos", "2026-11-02", [
            ('Bancos', 4000000, 100),       # +40,000.00
            ('Capital', -4000000, 100)      # -40,000.00
        ]),
        ("OP02", "Compra de equipos informáticos (pago parcial y crédito proveedor)", "2026-11-04", [
            ('Equipos', 1200000, 100),      # +12,000.00
            ('Bancos', -800000, 100),       # -8,000.00
            ('Proveedores', -400000, 100)   # -4,000.00
        ]),
        ("OP03", "Desembolso de préstamo bancario recibido a 6 meses", "2026-11-06", [
            ('Bancos', 1000000, 100),       # +10,000.00
            ('Prestamos', -1000000, 100)    # -10,000.00
        ]),
        ("OP04", "Anticipo recibido de entidad de salud por módulo próximo mes", "2026-11-09", [
            ('Bancos', 900000, 100),        # +9,000.00
            ('Anticipos', -900000, 100)     # -9,000.00
        ]),
        ("OP05", "Pago de remuneraciones de desarrollo del mes", "2026-11-13", [
            ('CostoRemun', 1500000, 100),   # +15,000.00
            ('Bancos', -1500000, 100)       # -15,000.00
        ]),
        ("OP06", "Pago de servicios de infraestructura nube del mes", "2026-11-16", [
            ('CostoNube', 200000, 100),     # +2,000.00
            ('Bancos', -200000, 100)        # -2,000.00
        ]),
        ("OP07", "Pago de gastos administrativos operativos del mes", "2026-11-19", [
            ('GastosAdmin', 300000, 100),   # +3,000.00
            ('Bancos', -300000, 100)        # -3,000.00
        ]),
        ("OP08", "Entrega y aceptación hito 1 independiente (cobro 16k, crédito 8k)", "2026-11-23", [
            ('Bancos', 1600000, 100),       # +16,000.00
            ('Clientes', 800000, 100),      # +8,000.00
            ('VentasSoftware', -2400000, 100)# -24,000.00
        ]),
        ("OP09", "Pago parcial de deuda con proveedor de equipos", "2026-11-25", [
            ('Proveedores', 200000, 100),   # +2,000.00 (debit reduces liability)
            ('Bancos', -200000, 100)        # -2,000.00
        ]),
        ("OP10", "Reconocimiento de remuneraciones administrativas devengadas pendientes", "2026-11-28", [
            ('GastosAdminSueldos', 150000, 100), # +1,500.00
            ('RemuneracionesPagar', -150000, 100)# -1,500.00
        ]),
        ("OP11", "Pago de intereses bancarios devengados del préstamo", "2026-11-30", [
            ('GastosFinanc', 50000, 100),   # +500.00
            ('Bancos', -50000, 100)         # -500.00
        ])
    ]

    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    xml_lines = [
        '<?xml version="1.0" encoding="utf-8" ?>',
        '<gnc-v2 xmlns:gnc="http://www.gnucash.org/XML/gnc"',
        '        xmlns:act="http://www.gnucash.org/XML/act"',
        '        xmlns:book="http://www.gnucash.org/XML/book"',
        '        xmlns:cd="http://www.gnucash.org/XML/cd"',
        '        xmlns:cmdty="http://www.gnucash.org/XML/cmdty"',
        '        xmlns:price="http://www.gnucash.org/XML/price"',
        '        xmlns:slot="http://www.gnucash.org/XML/slot"',
        '        xmlns:split="http://www.gnucash.org/XML/split"',
        '        xmlns:sx="http://www.gnucash.org/XML/sx"',
        '        xmlns:trn="http://www.gnucash.org/XML/trn"',
        '        xmlns:ts="http://www.gnucash.org/XML/ts"',
        '        xmlns:fs="http://www.gnucash.org/XML/fs"',
        '        xmlns:bgt="http://www.gnucash.org/XML/bgt"',
        '        xmlns:recurrence="http://www.gnucash.org/XML/recurrence"',
        '        xmlns:lot="http://www.gnucash.org/XML/lot"',
        '        xmlns:cust="http://www.gnucash.org/XML/cust"',
        '        xmlns:job="http://www.gnucash.org/XML/job"',
        '        xmlns:addr="http://www.gnucash.org/XML/addr"',
        '        xmlns:owner="http://www.gnucash.org/XML/owner"',
        '        xmlns:taxtable="http://www.gnucash.org/XML/taxtable"',
        '        xmlns:tte="http://www.gnucash.org/XML/tte"',
        '        xmlns:employee="http://www.gnucash.org/XML/employee"',
        '        xmlns:order="http://www.gnucash.org/XML/order"',
        '        xmlns:billterm="http://www.gnucash.org/XML/billterm"',
        '        xmlns:bt-days="http://www.gnucash.org/XML/bt-days"',
        '        xmlns:bt-prox="http://www.gnucash.org/XML/bt-prox"',
        '        xmlns:invoice="http://www.gnucash.org/XML/invoice"',
        '        xmlns:entry="http://www.gnucash.org/XML/entry"',
        '        xmlns:vendor="http://www.gnucash.org/XML/vendor">',
        '<gnc:count-data cd:type="book">1</gnc:count-data>',
        f'<gnc:book version="2.0.0">',
        f'<book:id type="guid">{book_id}</book:id>',
        '<gnc:count-data cd:type="commodity">1</gnc:count-data>',
        '<gnc:count-data cd:type="account">' + str(len(accounts)) + '</gnc:count-data>',
        '<gnc:count-data cd:type="transaction">' + str(len(txs)) + '</gnc:count-data>',
        '<gnc:commodity version="2.0.0">',
        '  <cmdty:space>CURRENCY</cmdty:space>',
        '  <cmdty:id>PEN</cmdty:id>',
        '  <cmdty:get_quotes/>',
        '  <cmdty:quote_source>currency</cmdty:quote_source>',
        '  <cmdty:quote_tz/>',
        '</gnc:commodity>',
        '<gnc:commodity version="2.0.0">',
        '  <cmdty:space>template</cmdty:space>',
        '  <cmdty:id>template</cmdty:id>',
        '  <cmdty:name>template</cmdty:name>',
        '  <cmdty:xcode>template</cmdty:xcode>',
        '  <cmdty:fraction>1</cmdty:fraction>',
        '</gnc:commodity>'
    ]

    # Accounts
    for key, acc in accounts.items():
        xml_lines.append('<gnc:account version="2.0.0">')
        xml_lines.append(f'  <act:name>{acc["name"]}</act:name>')
        xml_lines.append(f'  <act:id type="guid">{acc["id"]}</act:id>')
        xml_lines.append(f'  <act:type>{acc["type"]}</act:type>')
        if acc['type'] != 'ROOT':
            xml_lines.append('  <act:commodity>')
            xml_lines.append('    <cmdty:space>CURRENCY</cmdty:space>')
            xml_lines.append('    <cmdty:id>PEN</cmdty:id>')
            xml_lines.append('  </act:commodity>')
            xml_lines.append('  <act:commodity-scu>100</act:commodity-scu>')
        if acc['code']:
            xml_lines.append(f'  <act:code>{acc["code"]}</act:code>')
        if acc['parent']:
            xml_lines.append(f'  <act:parent type="guid">{acc["parent"]}</act:parent>')
        xml_lines.append('</gnc:account>')

    # Transactions
    for num, desc, date_str, splits in txs:
        trn_id = make_guid()
        date_iso = f"{date_str} 10:00:00"
        xml_lines.append('<gnc:transaction version="2.0.0">')
        xml_lines.append(f'  <trn:id type="guid">{trn_id}</trn:id>')
        xml_lines.append('  <trn:currency>')
        xml_lines.append('    <cmdty:space>CURRENCY</cmdty:space>')
        xml_lines.append('    <cmdty:id>PEN</cmdty:id>')
        xml_lines.append('  </trn:currency>')
        xml_lines.append(f'  <trn:num>{num}</trn:num>')
        xml_lines.append('  <trn:date-posted>')
        xml_lines.append(f'    <ts:date>{date_iso} +0000</ts:date>')
        xml_lines.append('  </trn:date-posted>')
        xml_lines.append('  <trn:date-entered>')
        xml_lines.append(f'    <ts:date>{now_str} +0000</ts:date>')
        xml_lines.append('  </trn:date-entered>')
        xml_lines.append(f'  <trn:description>{desc}</trn:description>')
        xml_lines.append('  <trn:splits>')
        for acc_k, val, denom in splits:
            sp_id = make_guid()
            acc_id = accounts[acc_k]['id']
            xml_lines.append('    <trn:split>')
            xml_lines.append(f'      <split:id type="guid">{sp_id}</split:id>')
            xml_lines.append('      <split:reconciled-state>n</split:reconciled-state>')
            xml_lines.append(f'      <split:value>{val}/{denom}</split:value>')
            xml_lines.append(f'      <split:quantity>{val}/{denom}</split:quantity>')
            xml_lines.append(f'      <split:account type="guid">{acc_id}</split:account>')
            xml_lines.append('    </trn:split>')
        xml_lines.append('  </trn:splits>')
        xml_lines.append('</gnc:transaction>')

    xml_lines.append('</gnc:book>')
    xml_lines.append('</gnc-v2>')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_lines))
    print(f"Archivo GnuCash generado exitosamente en: {output_path}")

if __name__ == "__main__":
    import os
    target = os.path.join(r"C:\Users\micha\Downloads\Borrar entregable 6\GPS-Entregable-6", "PANVIZ.gnucash")
    generate_gnucash_file(target)
