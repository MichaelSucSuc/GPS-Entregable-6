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
    # For Liability/Equity/Income, credit is positive (+) in amount/value relative to its account, but standard GnuCash stores splits as signed relative to standard convention:
    # Debits are positive, credits are negative!
    txs = [
        ("OP01", "Aporte inicial de los socios depositado en bancos", "2026-11-02", [
            ('Bancos', 4000000, 100),       # +40,000.00
            ('Capital', -4000000, 100)      # -40,000.00
        ]),
        ("OP02", "Compra de equipos informáticos (pago parcial y deuda)", "2026-11-05", [
            ('Equipos', 1200000, 100),      # +12,000.00
            ('Bancos', -800000, 100),       # -8,000.00
            ('Proveedores', -400000, 100)   # -4,000.00
        ]),
        ("OP03", "Desembolso de préstamo bancario a 6 meses", "2026-11-07", [
            ('Bancos', 1000000, 100),       # +10,000.00
            ('Prestamos', -1000000, 100)    # -10,000.00
        ]),
        ("OP04", "Anticipo recibido de entidad de salud por módulo futuro", "2026-11-10", [
            ('Bancos', 900000, 100),        # +9,000.00
            ('Anticipos', -900000, 100)     # -9,000.00
        ]),
        ("OP05", "Pago de remuneraciones de desarrollo del mes", "2026-11-15", [
            ('CostoRemun', 1500000, 100),   # +15,000.00
            ('Bancos', -1500000, 100)       # -15,000.00
        ]),
        ("OP06", "Pago de servicios de nube consumidos en el mes", "2026-11-18", [
            ('CostoNube', 200000, 100),     # +2,000.00
            ('Bancos', -200000, 100)        # -2,000.00
        ]),
        ("OP07", "Pago de gastos administrativos generales del mes", "2026-11-20", [
            ('GastosAdmin', 300000, 100),   # +3,000.00
            ('Bancos', -300000, 100)        # -3,000.00
        ]),
        ("OP08", "Entrega y aceptación Hito 1 PANVIZ (cobro parcial y saldo)", "2026-11-25", [
            ('Bancos', 1600000, 100),       # +16,000.00
            ('Clientes', 800000, 100),      # +8,000.00
            ('VentasSoftware', -2400000, 100) # -24,000.00
        ]),
        ("OP09", "Amortización de deuda con proveedor de equipos", "2026-11-27", [
            ('Proveedores', 200000, 100),   # +2,000.00 (debit reduces liability)
            ('Bancos', -200000, 100)        # -2,000.00
        ]),
        ("OP10", "Devengo de remuneraciones administrativas pendientes", "2026-11-30", [
            ('GastosAdminSueldos', 150000, 100), # +1,500.00
            ('RemuneracionesPagar', -150000, 100) # -1,500.00
        ]),
        ("OP11", "Pago de intereses del préstamo bancario desde bancos", "2026-11-30", [
            ('GastosFinanc', 50000, 100),   # +500.00
            ('Bancos', -50000, 100)         # -500.00
        ])
    ]

    xml = []
    xml.append('<?xml version="1.0" encoding="utf-8" ?>')
    xml.append('<gnc-v2 xmlns:gnc="http://www.gnucash.org/XML/gnc"')
    xml.append('        xmlns:act="http://www.gnucash.org/XML/act"')
    xml.append('        xmlns:book="http://www.gnucash.org/XML/book"')
    xml.append('        xmlns:cd="http://www.gnucash.org/XML/cd"')
    xml.append('        xmlns:cmdty="http://www.gnucash.org/XML/cmdty"')
    xml.append('        xmlns:price="http://www.gnucash.org/XML/price"')
    xml.append('        xmlns:slot="http://www.gnucash.org/XML/slot"')
    xml.append('        xmlns:split="http://www.gnucash.org/XML/split"')
    xml.append('        xmlns:trn="http://www.gnucash.org/XML/trn"')
    xml.append('        xmlns:ts="http://www.gnucash.org/XML/ts">')
    xml.append('<gnc:count-data cd:type="book">1</gnc:count-data>')
    xml.append(f'<gnc:book version="2.0.0">')
    xml.append(f'  <book:id type="guid">{book_id}</book:id>')
    xml.append('  <book:slots>')
    xml.append('    <slot>')
    xml.append('      <slot:key>default-currency</slot:key>')
    xml.append('      <slot:value type="string">PEN</slot:value>')
    xml.append('    </slot>')
    xml.append('  </book:slots>')

    # Commodity
    xml.append('  <gnc:count-data cd:type="commodity">1</gnc:count-data>')
    xml.append('  <gnc:commodity version="2.0.0">')
    xml.append('    <cmdty:space>ISO4217</cmdty:space>')
    xml.append('    <cmdty:id>PEN</cmdty:id>')
    xml.append('    <cmdty:name>Sol peruano</cmdty:name>')
    xml.append('    <cmdty:xcode>604</cmdty:xcode>')
    xml.append('    <cmdty:fraction>100</cmdty:fraction>')
    xml.append('  </gnc:commodity>')

    # Accounts
    xml.append(f'  <gnc:count-data cd:type="account">{len(accounts)}</gnc:count-data>')
    for acc_key, acc_val in accounts.items():
        xml.append('  <gnc:account version="2.0.0">')
        xml.append(f'    <act:name>{acc_val["name"]}</act:name>')
        xml.append(f'    <act:id type="guid">{acc_val["id"]}</act:id>')
        xml.append(f'    <act:type>{acc_val["type"]}</act:type>')
        if acc_val['code']:
            xml.append(f'    <act:code>{acc_val["code"]}</act:code>')
        if acc_val['type'] != 'ROOT':
            xml.append('    <act:commodity>')
            xml.append('      <cmdty:space>ISO4217</cmdty:space>')
            xml.append('      <cmdty:id>PEN</cmdty:id>')
            xml.append('    </act:commodity>')
            xml.append('    <act:commodity-scu>100</act:commodity-scu>')
        if acc_val['parent']:
            xml.append(f'    <act:parent type="guid">{acc_val["parent"]}</act:parent>')
        xml.append('  </gnc:account>')

    # Transactions
    xml.append(f'  <gnc:count-data cd:type="transaction">{len(txs)}</gnc:count-data>')
    for op_num, op_desc, op_date, splits in txs:
        trn_id = make_guid()
        date_str = f"{op_date} 12:00:00 +0000"
        xml.append('  <gnc:transaction version="2.0.0">')
        xml.append(f'    <trn:id type="guid">{trn_id}</trn:id>')
        xml.append('    <trn:currency>')
        xml.append('      <cmdty:space>ISO4217</cmdty:space>')
        xml.append('      <cmdty:id>PEN</cmdty:id>')
        xml.append('    </trn:currency>')
        xml.append(f'    <trn:num>{op_num}</trn:num>')
        xml.append('    <trn:date-posted>')
        xml.append(f'      <ts:date>{date_str}</ts:date>')
        xml.append('    </trn:date-posted>')
        xml.append('    <trn:date-entered>')
        xml.append(f'      <ts:date>{date_str}</ts:date>')
        xml.append('    </trn:date-entered>')
        xml.append(f'    <trn:description>{op_desc}</trn:description>')
        xml.append('    <trn:splits>')
        for acc_k, num, denom in splits:
            split_id = make_guid()
            acc_id = accounts[acc_k]['id']
            val_str = f"{num}/{denom}"
            xml.append('      <trn:split>')
            xml.append(f'        <split:id type="guid">{split_id}</split:id>')
            xml.append('        <split:reconciled-state>n</split:reconciled-state>')
            xml.append(f'        <split:value>{val_str}</split:value>')
            xml.append(f'        <split:quantity>{val_str}</split:quantity>')
            xml.append(f'        <split:account type="guid">{acc_id}</split:account>')
            xml.append('      </trn:split>')
        xml.append('    </trn:splits>')
        xml.append('  </gnc:transaction>')

    xml.append('</gnc:book>')
    xml.append('</gnc-v2>')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml))
    print(f"Archivo GnuCash generado exitosamente en: {output_path}")

if __name__ == '__main__':
    out_gnucash = r"C:\Users\micha\Downloads\Borrar entregable 6\GPS-Entregable-6\PANVIZ_equipo06.gnucash"
    generate_gnucash_file(out_gnucash)
